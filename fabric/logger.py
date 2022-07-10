from tif.fabric import cli

class Logger:
    def __init__(self) -> None:
        pass

    def log(self, message):
        """
        Outputs white message to console
        """
        cli.puts("** {}".format(message))