"""Added accounts table

Revision ID: 1852e4859683
Revises: bbc10f992358
Create Date: 2024-10-06 16:57:55.233161

"""
from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1852e4859683"
down_revision: str | None = "bbc10f992358"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("account",
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.Column("type", sa.Enum("PERSONAL", "BUSINESS", name="accounttype"), nullable=False),
    sa.Column("balance", sa.Integer(), nullable=False),
    sa.Column("branch", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column("number", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("account")
    # ### end Alembic commands ###
