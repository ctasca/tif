import string
from tif.fabric import cli

class Options:
    def __init__(self, **options) -> None:
        self.options = options

    def render(self, input_text= None) -> string:
        self._print()
        if (input_text):
            option = input(input_text)
        else:
            option = input("Choose an option: ")
        return self._get_option(option.strip())

    def _print(self) -> string:
        for key in self.options.keys():
            print (cli.puts_hide(">>> {}".format(key)), '--', self.options[key])

    def _get_option(self, option):
        if (option.strip() not in self.options.keys()):
                cli.puts("!!! Not a valid choice")
        elif (self.options[option].lower() == 'exit'):
            exit()
        else:
            choise = cli.cli_confirm("You have chosen '{}'. Continue?".format(self.options[option]))
            if (choise == 'y'):
                return self.options[option]
            exit()