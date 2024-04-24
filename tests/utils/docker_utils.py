import docker
import docker.errors
import time
import os


def is_the_container_ready(container): #this function checks if the container is ready.... or if it is not stopped somehow
    
    container.reload() #fetching the latest info about the container
    return container.status == "running"

def wait_for_stable_status(container, stable_duration_seconds = 11, interval=1):
    counter = 0
    while container.status == "running" and counter < stable_duration_seconds:
        time.sleep(interval)
        counter+=interval  
        print(counter)
        print(container.status)
    if is_the_container_ready(container)  and counter == stable_duration_seconds:
        print(f"Container {container.name} is ready.")
        return True
    else:
        return False  
def start_db_container():
    client = docker.from_env()
    container_name = "test-db" 
    scripts_dir = os.path.abspath("./scripts/test-db-setup.sh")
    
    try:
        existing_container = client.containers.get(container_name)

        print(f"Stopping and removing existing container {container_name}")
        existing_container.stop()
        existing_container.remove()
        print(f"Existing container {container_name} stopped.")
        
    except docker.errors.NotFound:
        print(f"Container {container_name} not found")

    container = client.containers.run("postgres", ports={"5432/tcp": 5433}, detach=True, name=container_name,
                                      environment={"POSTGRES_USER": "sve", "POSTGRES_PASSWORD": "123", "POSTGRES_DB": "inventory"},
                                       volumes={scripts_dir: {"bind": "/docker-entrypoint-initdb.d/test-db-setup.sh", "mode": "rw"}},
                                      network_mode="fastapi-development_dev_net")
    
    while not is_the_container_ready(container):
        time.sleep(2) #wait for the container to be ready (2 sec)
        
    if not wait_for_stable_status(container): #FIX THE PROBLEM HERE!
        raise Exception(f"Container {container_name} is not ready to run.")
    
            
