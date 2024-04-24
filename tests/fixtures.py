from  sqlalchemy import create_engine
import pytest
import os
from utils.docker_utils import start_db_container
from utils.database_utils import migrate_to_db
from sqlalchemy.orm import sessionmaker



@pytest.fixture(scope="session", autouse=True) # the fixture will be used for the scope of the test session
def db_session():
    container = start_db_container()
    
    engine = create_engine(os.environ.get("TEST_DATABASE_URL"))
    print(engine)
    
    with engine.begin() as connection:
        # print(connection)
        migrate_to_db(connection=connection)
        
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal
    
    # container.stop()
    # container.remove()
    engine.dispose()
        