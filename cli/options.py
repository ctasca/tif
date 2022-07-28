import string
import re
import os
from tif.fabric import cli
from tif.fabric.CommandPrefix import CommandPrefix
from fabric.connection import Connection

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

    def file_chooser(self, c : Connection, dir = None, absolute_path = False, input_text = None, list_all = False):
        options = []
        dir = dir or c.cwd
        dir_list = c.sftp().listdir(dir)
        if not list_all:
            filtered_dir_list = [file for file in dir_list if (not file.startswith(".") and not re.search(r"\.([\w\d]){1,}$", file))]
        else:
            filtered_dir_list = dir_list
        for file in filtered_dir_list:
            print (cli.puts_hide(">>> {}".format(filtered_dir_list.index(file) + 1)), '--', file)
        if (input_text):
            option = input(input_text)
        else:
            option = input("Choose an option: ")
        while(option is not None):
            if (re.search(r"\.([\w\d]){1,}$", filtered_dir_list[int(option) - 1])):
                if not absolute_path:
                    return os.sep.join(options) + os.sep + filtered_dir_list[int(option) - 1]
                else:
                    return dir + os.sep + os.sep.join(options) + os.sep + filtered_dir_list[int(option) - 1]
            options.append(filtered_dir_list[int(option) - 1])
            c.sftp().chdir(dir + os.sep + os.sep.join(options))
            dir_list = c.sftp().listdir(dir + os.sep + os.sep.join(options))
            if not list_all:
                filtered_dir_list = [file for file in dir_list if (not file.startswith("."))]
            else:
                filtered_dir_list = dir_list
            for file in filtered_dir_list:
                print (cli.puts_hide(">>> {}".format(filtered_dir_list.index(file) + 1)), '--', file)
            if (input_text):
                option = input(input_text)
            else:
                option = input("Choose an option: ")

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