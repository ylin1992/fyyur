"""empty message

Revision ID: 388b36ae960d
Revises: 4585432e4a99
Create Date: 2021-10-28 20:46:38.170649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388b36ae960d'
down_revision = '4585432e4a99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###