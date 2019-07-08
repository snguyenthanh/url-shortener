"""Migrating...

Revision ID: 31219109e3c9
Revises: d57ffa1ea737
Create Date: 2019-07-06 15:46:11.006091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "31219109e3c9"
down_revision = "d57ffa1ea737"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("urls", sa.Column("actual_url", sa.String(), nullable=True))
    op.add_column("urls", sa.Column("url_hash", sa.String(), nullable=True))
    op.create_index("idx_url_hash", "urls", ["url_hash"], unique=True)
    op.drop_index("idx_shortened_url", table_name="urls")
    op.drop_column("urls", "shortened_url")
    op.drop_column("urls", "full_url")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "urls", sa.Column("full_url", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "urls",
        sa.Column("shortened_url", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.create_index("idx_shortened_url", "urls", ["shortened_url"], unique=True)
    op.drop_index("idx_url_hash", table_name="urls")
    op.drop_column("urls", "url_hash")
    op.drop_column("urls", "actual_url")
    # ### end Alembic commands ###
