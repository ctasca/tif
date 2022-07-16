import string
from tif.fabric import cli

class Options:
    def __init__(self, **options) -> None:
        self.options = options

    def print(self) -> string:
        for key in self.options.keys():
            print (cli.puts_hide(">>> {}".format(key)), '--', self.options[key])

    def get_option(self, option):
        if (option.strip() not in self.options.keys()):
                cli.puts("!!! Not a valid option")
        elif (self.options[option].lower() == 'exit'):
            cli.puts("** Aborted task")
            exit()
        else:
            return self.options[option]