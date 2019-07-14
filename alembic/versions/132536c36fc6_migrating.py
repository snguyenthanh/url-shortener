"""Migrating...

Revision ID: 132536c36fc6
Revises: aa5cffbc8a52
Create Date: 2019-07-08 23:44:45.862957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "132536c36fc6"
down_revision = "aa5cffbc8a52"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("api_key", sa.String(), nullable=True))
    op.add_column("users", sa.Column("password", sa.String(), nullable=True))
    op.create_index("idx_api_key", "users", ["api_key"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("idx_api_key", table_name="users")
    op.drop_column("users", "password")
    op.drop_column("users", "api_key")
    # ### end Alembic commands ###