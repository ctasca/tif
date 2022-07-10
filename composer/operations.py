import pty
import string
from fabric.connection import Connection
from tif.fabric.CommandPrefix import CommandPrefix

def install(c : Connection, install_dir : string, command_prefix=""):
    with c.cd(install_dir):
        command = "composer install"
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
