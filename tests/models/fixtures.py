import pytest
from sqlalchemy import inspect #inspects sql database metadata

@pytest.fixture(scope="function")
def db_inspector(db_session):
    return inspect(db_session().bind)
