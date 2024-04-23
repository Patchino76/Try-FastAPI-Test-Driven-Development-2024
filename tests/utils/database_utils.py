import alembic.config
from alembic import command


def migrate_to_db(script_location="migrations", alembic_ini_path = "alembic.ini", connection=None, revision="head"):
    config = alembic.config.Config(alembic_ini_path)
    
    if connection is not None:
        print(connection)
        config.config_ini_section = "testdb"
        command.upgrade(config, revision)
        
    