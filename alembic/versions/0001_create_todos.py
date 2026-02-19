"""create todos table

Revision ID: 0001_create_todos
Revises:
Create Date: 2026-02-16 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = "0001_create_todos"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("is_done", sa.Boolean, nullable=False, server_default=sa.text("false")),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    op.create_index("ix_todos_id", "todos", ["id"], unique=False)


def downgrade():
    op.drop_index("ix_todos_id", table_name="todos")
    op.drop_table("todos")

