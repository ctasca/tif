import emoji
from tif.fabric import cli

class Logger:
    def __init__(self) -> None:
        pass

    def log(self, message):
        """
        Outputs white message to console with :bell: emoji
        """
        cli.puts("** {} {}".format(emoji.emojize(':bell:'), message))

    def info(self, message):
        """
        Outputs white message to console with :information: emoji
        """
        cli.puts("** {} {}".format(emoji.emojize(':information:') + " ", message))
    
    def error(self, message):
        """
        Outputs red message to console with :red_exclamation_mark: emoji
        """
        cli.puts("error: {} {}".format(emoji.emojize(':red_exclamation_mark:'), message))

    def success(self, message):
        """
        Outputs green message to console
        """
        cli.puts(".:~ {}".format(message))