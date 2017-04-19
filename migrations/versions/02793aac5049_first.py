"""first

Revision ID: 02793aac5049
Revises: None
Create Date: 2017-04-19 17:22:39.233550

"""

# revision identifiers, used by Alembic.
revision = '02793aac5049'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('budgets', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('transactions', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    # ### end Alembic commands ###