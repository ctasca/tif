import string
from fabric.connection import Connection
from fabric.transfer import Transfer
from tif.fabric import cli
from tif.fabric.CommandPrefix import CommandPrefix

def gunzip(c : Connection , dir : string, listFiles = True, command_prefix = ""):
    with c.cd(dir):
        if (listFiles):
            command = "ls"
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        zip = cli.prompt(">>> Enter file to gunzip: ")
        if (zip):
            command = "gunzip {0}".format(zip)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def ls(c : Connection, dir : string, command_prefix = ""):
    with c.cd(dir):
        command = "ls"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def rm(c : Connection, dir : string, command_prefix = ""):
    with c.cd(dir):
        c.run("ls")
        to_delete = cli.prompt(">>> Enter directory/file to delete: ")
        if c.run(CommandPrefix('test -d {0}'.format(to_delete), command_prefix).prefix_command(), warn=True):
            confirm = cli.cli_confirm("You are about to delete the directory {0}. Are you sure?".format(to_delete))
            if (confirm == "y"):
                command = "rm -rf {0}".format(to_delete)
                c.run(CommandPrefix(command, command_prefix).prefix_command())
            else:
                cli.puts("!!! Aborted")
        elif c.run(CommandPrefix('test -f {0}'.format(to_delete), command_prefix).prefix_command(), warn=True):
            confirm = cli.cli_confirm("You are about to delete the file {0}. Are you sure?".format(to_delete))
            if (confirm == "y"):
                command = "rm {0}".format(to_delete)
                c.run(CommandPrefix(command, command_prefix).prefix_command())
            else:
                cli.puts("!!! Aborted")
        else:
            cli.puts("!!! Aborted operation. {0} not found.".format(to_delete))


def ls_dir(c : Connection, dir : string, command_prefix = ""):
    ls_dir = cli.prompt(">>> Enter directory to list: ")
    with c.cd(dir + "/" + ls_dir):
        c.run(CommandPrefix("ls", command_prefix).prefix_command())

def ls_la(c : Connection, dir : string, command_prefix = ""):
    with c.cd(dir):
        c.run(CommandPrefix("ls -la", command_prefix).prefix_command())

def get(c : Connection):
    t = Transfer(c)
    remote_file = cli.prompt(">>> Enter remote file path to download (relative to home directory): ")
    local_file = cli.prompt(">>> Enter local file path to download to (relative to fabfile location): ")
    t.get(remote_file, local_file)