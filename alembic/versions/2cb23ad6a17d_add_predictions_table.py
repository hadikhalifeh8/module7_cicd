"""add predictions table

Revision ID: 2cb23ad6a17d
Revises:
Create Date: 2025-10-24 17:34:07.096810
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2cb23ad6a17d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'predictions',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('sentiment', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('predictions')