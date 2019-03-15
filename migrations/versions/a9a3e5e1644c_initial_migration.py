"""Initial Migration

Revision ID: a9a3e5e1644c
Revises: 845e9e79ae03
Create Date: 2019-03-15 15:43:45.201103

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a9a3e5e1644c'
down_revision = '845e9e79ae03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_index('ix_posts_timestamp', table_name='posts')
    op.drop_constraint('posts_author_id_fkey', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    op.drop_column('posts', 'timestamp')
    op.drop_column('posts', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_author_id_fkey', 'posts', 'users', ['author_id'], ['id'])
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
