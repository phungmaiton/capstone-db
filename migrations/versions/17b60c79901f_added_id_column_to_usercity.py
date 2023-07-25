"""added id column to usercity

Revision ID: 17b60c79901f
Revises: 9f7d5feb01bd
Create Date: 2023-07-25 13:08:26.134713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b60c79901f'
down_revision = '9f7d5feb01bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usercities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usercities', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###
