#!/bin/bash

# Utility functions and setup for scripts that need to generate credentials and (optionally)
# run the Cloud SQL proxy
# Expected environment variables: $ACCOUNT, $PROJECT, $CREDS_ACCOUNT

set -e
gcloud auth login $ACCOUNT
gcloud config set project $PROJECT

SERVICE_ACCOUNT="circle-deploy@all-of-us-rdr-staging.iam.gserviceaccount.com"
if [ "${PROJECT}" != "pmi-drc-api-test" ] && [ "${PROJECT}" != "all-of-us-rdr-staging" ]
then
  SERVICE_ACCOUNT="configurator@${PROJECT}.iam.gserviceaccount.com"
fi

source tools/setup_vars.sh
CREDS_FILE=/tmp/creds.json
DB_INFO_FILE=/tmp/db_info.json
PORT=3308
INSTANCE=https://${PROJECT}.appspot.com
CLOUD_PROXY_PID=
PRIVATE_KEY=

function cleanup {
  if [ "$CLOUD_PROXY_PID" ];
  then
    kill $CLOUD_PROXY_PID
  fi
  if [ "$PRIVATE_KEY" ];
  then
    gcloud iam service-accounts keys delete $PRIVATE_KEY -q --iam-account=$SERVICE_ACCOUNT --account=$CREDS_ACCOUNT
  fi
  rm -f ${CREDS_FILE}
  rm -f ${DB_INFO_FILE}
}

trap cleanup EXIT

gcloud iam service-accounts keys create $CREDS_FILE --iam-account=$SERVICE_ACCOUNT --account=$CREDS_ACCOUNT
PRIVATE_KEY=`grep private_key_id $CREDS_FILE | cut -d\" -f4`

function get_instance_connection_name {
  echo "Getting database info..."
  tools/install_config.sh --key db_config --instance $INSTANCE --creds_file ${CREDS_FILE} > $DB_INFO_FILE
  INSTANCE_CONNECTION_NAME=`grep db_connection_name $DB_INFO_FILE | cut -d\" -f4`
}

function get_db_password {
  echo "Getting database password..."
  tools/install_config.sh --key db_config --instance $INSTANCE --creds_file ${CREDS_FILE} > $DB_INFO_FILE
  PASSWORD=`grep db_password $DB_INFO_FILE | cut -d\" -f4`
}

function run_cloud_sql_proxy {
  if [ -z "$INSTANCE_CONNECTION_NAME" ]
  then
    get_instance_connection_name
  fi

  echo "Running cloud proxy..."
  bin/cloud_sql_proxy -instances=${INSTANCE_CONNECTION_NAME}=tcp:${PORT} -credential_file=${CREDS_FILE} &
  sleep 3
  CLOUD_PROXY_PID=%1
}

function set_db_connection_string {
  PASSWORD=`grep db_password $DB_INFO_FILE | cut -d\" -f4`
  function finish {
    cleanup
    export DB_CONNECTION_STRING=
  }
  trap finish EXIT
  export DB_CONNECTION_STRING="mysql+mysqldb://${DB_USER}:${PASSWORD}@127.0.0.1:${PORT}/${DB_NAME}?charset=utf8"
}