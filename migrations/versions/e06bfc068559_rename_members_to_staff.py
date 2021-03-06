"""Rename members to staff

Revision ID: e06bfc068559
Revises: 15811884a1cb
Create Date: 2021-04-04 17:17:10.300824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e06bfc068559'
down_revision = '15811884a1cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('alias', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('avatar_override', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('member')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('full_name', sa.VARCHAR(), nullable=True),
    sa.Column('alias', sa.VARCHAR(), nullable=True),
    sa.Column('role', sa.VARCHAR(), nullable=True),
    sa.Column('avatar_override', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('staff')
    # ### end Alembic commands ###
