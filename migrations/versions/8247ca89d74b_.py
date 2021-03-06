"""empty message

Revision ID: 8247ca89d74b
Revises: 860a0431689a
Create Date: 2021-10-29 21:21:50.580688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8247ca89d74b'
down_revision = '860a0431689a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Show', 'Show', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'venue_id')
    # ### end Alembic commands ###
