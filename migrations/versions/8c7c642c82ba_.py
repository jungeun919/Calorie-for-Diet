"""empty message

Revision ID: 8c7c642c82ba
Revises: 3b9947e5ae05
Create Date: 2021-10-16 22:12:12.337856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c7c642c82ba'
down_revision = '3b9947e5ae05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'image')
    # ### end Alembic commands ###