"""empty message

Revision ID: 06fa96289999
Revises: 
Create Date: 2023-01-26 17:08:16.116616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06fa96289999'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imagen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_path', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('resource_path')
    )
    op.create_table('token_blocked_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    with op.batch_alter_table('token_blocked_list', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_token_blocked_list_email'), ['email'], unique=False)

    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('type_music', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('artist_picture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_picture_id'], ['imagen.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('firstname', sa.String(length=40), nullable=True),
    sa.Column('lastname', sa.String(length=120), nullable=True),
    sa.Column('telnumber', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('country', sa.String(length=120), nullable=True),
    sa.Column('age', sa.String(length=120), nullable=True),
    sa.Column('profile_picture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_picture_id'], ['imagen.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('make', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('style', sa.String(length=120), nullable=False),
    sa.Column('fuel', sa.String(length=120), nullable=False),
    sa.Column('transmission', sa.String(length=120), nullable=False),
    sa.Column('financing', sa.Boolean(), nullable=False),
    sa.Column('doors', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Fav_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Fav_posts')
    op.drop_table('posts')
    op.drop_table('user')
    op.drop_table('artist')
    with op.batch_alter_table('token_blocked_list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_blocked_list_email'))

    op.drop_table('token_blocked_list')
    op.drop_table('imagen')
    # ### end Alembic commands ###