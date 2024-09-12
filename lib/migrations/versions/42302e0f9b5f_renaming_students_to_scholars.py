"""Renaming students to scholars

Revision ID: 42302e0f9b5f
Revises: 791279dd0760
Create Date: 2024-09-12 09:56:33.581004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42302e0f9b5f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
