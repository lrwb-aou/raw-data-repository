# Tools for the RDR API

## Scripts to run directly

### connect_to_database.sh

Starts the Cloud SQL proxy and runs mysql so that you can issue SQL commands directly against
a Cloud SQL instance.

### generate_schema.sh

Generates an Alembic schema migration in alembic/versions after altering the
SQLAlchemy schema in model/.

To regenerate an initial schema:

```
# Remove the existing schema definition.
rm alembic/versions/*.py
# Clear the database. (The setup script clears the db, creates an empty one,
# and then fails everything else leaving it empty.)
tools/setup_local_database.sh
# Optionally add any new imports to the Alembic bootstrap.
$EDITOR alembic/script.py.mako
# Regenerate the schema.
tools/generate_schema.sh 'Initial schema with manual edits for HPO IDs.'
# Re-add the HPO IDs.
$EDITOR alembic/versions/*.py
# Start a dev appserver and set up the db according to the new schema (and
# import the codebook).
dev_appserver.py test.yaml --require_indexes &
tools/setup_local_database.sh
```

### import_codebook.sh

Imports a codebook into the database.

### install_config.sh

Populates configuration JSON in Datastore, for use by the AppEngine app.

### setup_database.sh

Sets up a Cloud SQL database instance, sets the root password, creates an rdr database in
it, and populates database configuration in Datastore.

### setup_env.sh

Sets up your workspace after checking out the code, or when something changes in
requirements.txt.

### setup_local_database.sh

Sets up an rdr database on your local MySQL instance, for use when running a local
server.

### upgrade_database.sh

Upgrades a database (either local or in Cloud SQL) to the latest or a specified Alembic revision,
applying schema migrations. (If the schema is already up to date, this is a no-op.)

### remove_trailing_whitespace.sh

Trim trailing whitespace form all files and optionally commit changes.

## check_uncommitted.sh

Returns nonzero if there are uncommitted changes, for use as a pre-push hook.

## Included scripts (use with "source &lt;script name&gt;")

### auth_setup.sh

Creates credentials in a temp file, exports run_cloud_sql_proxy function used to run Cloud SQL.

### set_path.sh

Sets PYTHONPATH to include everything in libs and the AppEngine SDK. For use when running python
scripts that rely on these libraries.


