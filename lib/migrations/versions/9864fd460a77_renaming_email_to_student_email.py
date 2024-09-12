"""Renaming email to student_email

Revision ID: 9864fd460a77
Revises: 42302e0f9b5f
Create Date: 2024-09-12 10:03:37.557201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9864fd460a77'
down_revision = '42302e0f9b5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('email', 'student_email')


def downgrade() -> None:
    op.alter_column('student_email', 'email')
