import string
from fabric.connection import Connection
from tif.fabric.CommandPrefix import CommandPrefix
from tif.fabric.logger import Logger

def install(c : Connection, install_dir : string, command_prefix=""):
    with c.cd(install_dir):
        command = "composer install"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
