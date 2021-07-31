"""added correction in the table

Revision ID: ef8cc4cbfa7c
Revises: 
Create Date: 2021-07-31 15:26:43.695813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef8cc4cbfa7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toy',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toy')
    op.drop_table('owner')
    op.drop_table('puppy')
    # ### end Alembic commands ###