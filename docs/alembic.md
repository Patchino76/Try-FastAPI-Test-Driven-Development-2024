alembic inint alembic -n migrations

1. make a folder migrations

2. init alembic:
   run: alembic init migrations

3. Create migration
   run: alembic revision --autogenerate -m "initial"

in our case [alembic] is empty, cause we are using [devdb] engine
to run the [devdb] engine
run: alembic -n devdb revision --autogenerate -m "initial"

but in env.py the meatdata should be also set before:
from app import models
target_metadata = models.Base.metadata

4.  run: ``alembic -n devdb upgrade head``
    Remember (-n devdb) specifies alembic to use the [devdb] engine

docker-compose:
run: docker-compose up -d

5. pytest alembic:
run: pip install pytest-alembic


for scpecific alembic db configurations like dev-db:
run: alembic -n devdb revision --autogenerate -m "initial"       