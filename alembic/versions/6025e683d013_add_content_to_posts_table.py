"""add content to posts table

Revision ID: 6025e683d013
Revises: 2c6eab5f8474
Create Date: 2024-05-27 20:04:42.589810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6025e683d013'
down_revision: Union[str, None] = '2c6eab5f8474'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
