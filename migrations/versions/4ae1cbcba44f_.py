"""empty message

Revision ID: 4ae1cbcba44f
Revises: 
Create Date: 2021-06-03 12:25:03.177310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae1cbcba44f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=201), nullable=True),
    sa.Column('surname', sa.String(length=201), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('clas', sa.String(length=201), nullable=True),
    sa.Column('science', sa.String(length=201), nullable=True),
    sa.Column('history', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('school', sa.String(length=201), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=201), nullable=True),
    sa.Column('surname', sa.String(length=201), nullable=True),
    sa.Column('clas', sa.String(length=201), nullable=True),
    sa.Column('science', sa.String(length=201), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    op.drop_table('student')
    # ### end Alembic commands ###