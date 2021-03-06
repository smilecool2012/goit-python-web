"""add users table

Revision ID: fcb8225c21ac
Revises: eef203c5cfc8
Create Date: 2022-05-23 20:07:42.551813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcb8225c21ac'
down_revision = 'eef203c5cfc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('epl_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('epl_match', sa.String(), nullable=False),
    sa.Column('score', sa.String(), nullable=True),
    sa.Column('match_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_epl_results_id'), 'epl_results', ['id'], unique=False)
    op.create_table('nhl_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nhl_match', sa.String(), nullable=False),
    sa.Column('score', sa.String(), nullable=True),
    sa.Column('match_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_nhl_results_id'), 'nhl_results', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nhl_results_id'), table_name='nhl_results')
    op.drop_table('nhl_results')
    op.drop_index(op.f('ix_epl_results_id'), table_name='epl_results')
    op.drop_table('epl_results')
    # ### end Alembic commands ###
