"""empty message

Revision ID: fb06dd3cc09d
Revises: fc30dfe62fe2
Create Date: 2021-10-28 21:50:17.118902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb06dd3cc09d'
down_revision = 'fc30dfe62fe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Genre', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Genre', type_='unique')
    # ### end Alembic commands ###
