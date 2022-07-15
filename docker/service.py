import string

class Service:
    def __init__(self, docker_dir:string, container: string) -> None:
        self.docker_dir = docker_dir
        self.container = container
    
    def command(self, command):
        """
        Runs command on a docker container
        """
        return "cd {} & docker exec -it {} bash -c \"{}\"".format(self.docker_dir, self.container, command)