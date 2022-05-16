"""Three

Revision ID: bded8fd39448
Revises: d8009d188870
Create Date: 2022-05-15 15:26:15.528407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bded8fd39448'
down_revision = 'd8009d188870'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('author', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index('ix_author_id', table_name='author')
    op.add_column('blog_posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_index('ix_blog_posts_id', table_name='blog_posts')
    op.drop_constraint('blog_posts_author_fkey', 'blog_posts', type_='foreignkey')
    op.create_foreign_key(None, 'blog_posts', 'author', ['author_id'], ['id'])
    op.drop_column('blog_posts', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blog_posts', type_='foreignkey')
    op.create_foreign_key('blog_posts_author_fkey', 'blog_posts', 'author', ['author'], ['id'])
    op.create_index('ix_blog_posts_id', 'blog_posts', ['id'], unique=False)
    op.drop_column('blog_posts', 'author_id')
    op.create_index('ix_author_id', 'author', ['id'], unique=False)
    op.alter_column('author', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('author', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###