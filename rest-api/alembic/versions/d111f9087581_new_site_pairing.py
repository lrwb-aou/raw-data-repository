"""new_site_pairing

Revision ID: d111f9087581
Revises: f81a8b941a77
Create Date: 2018-01-23 10:51:33.522289

"""
from alembic import op
import sqlalchemy as sa
import model.utils


from participant_enums import PhysicalMeasurementsStatus, QuestionnaireStatus, OrderStatus
from participant_enums import WithdrawalStatus, SuspensionStatus
from participant_enums import EnrollmentStatus, Race, SampleStatus, OrganizationType
from participant_enums import MetricSetType, MetricsKey
from model.site_enums import SiteStatus
from model.code import CodeType

# revision identifiers, used by Alembic.
revision = 'd111f9087581'
down_revision = 'f81a8b941a77'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()



def upgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('participant', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.add_column('participant', sa.Column('site_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'participant', 'site', ['site_id'], ['site_id'])
    op.create_foreign_key(None, 'participant', 'organization', ['organization_id'], ['organization_id'])
    op.add_column('participant_history', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.add_column('participant_history', sa.Column('site_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'participant_history', 'site', ['site_id'], ['site_id'])
    op.create_foreign_key(None, 'participant_history', 'organization', ['organization_id'], ['organization_id'])
    op.add_column('participant_summary', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.add_column('participant_summary', sa.Column('site_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'participant_summary', 'organization', ['organization_id'], ['organization_id'])
    op.create_foreign_key(None, 'participant_summary', 'site', ['site_id'], ['site_id'])
    # ### end Alembic commands ###


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'participant_summary', type_='foreignkey')
    op.drop_constraint(None, 'participant_summary', type_='foreignkey')
    op.drop_column('participant_summary', 'site_id')
    op.drop_column('participant_summary', 'organization_id')
    op.drop_constraint(None, 'participant_history', type_='foreignkey')
    op.drop_constraint(None, 'participant_history', type_='foreignkey')
    op.drop_column('participant_history', 'site_id')
    op.drop_column('participant_history', 'organization_id')
    op.drop_constraint(None, 'participant', type_='foreignkey')
    op.drop_constraint(None, 'participant', type_='foreignkey')
    op.drop_column('participant', 'site_id')
    op.drop_column('participant', 'organization_id')
    # ### end Alembic commands ###


def upgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
