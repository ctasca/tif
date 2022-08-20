import string
import docker
import re

class Service:
    def __init__(self, docker_dir : string) -> None:
        self.docker_dir = docker_dir

    def container_name_search(self, search : string) -> string:
        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            if re.search(search, container.name):
                return container.name
        raise Exception("No {} container match".format(search))

    def command(self, container : string, command : string):
        """
        Runs command on a docker container
        """
        return "cd {} & docker exec -it {} bash -c \"{}\"".format(self.docker_dir, container, command)