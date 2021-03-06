"""Add avatar_url

Revision ID: b48d07c691aa
Revises: ed135e10c794
Create Date: 2021-03-31 23:50:38.220487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48d07c691aa'
down_revision = 'ed135e10c794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar_url')
    # ### end Alembic commands ###
