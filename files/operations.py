import string
from fabric.connection import Connection
from fabric.transfer import Transfer
from tif.fabric import cli

def gunzip(c : Connection , dir : string, listFiles = True):
    with c.cd(dir):
        if (listFiles):
            c.run("ls")
        zip = cli.prompt(">>> Enter file to gunzip: ")
        if (zip):
            c.run("gunzip {0}".format(zip))
        else:
            cli.puts("!!! Aborted")

def ls(c : Connection, dir : string):
    with c.cd(dir):
        c.run("ls")

def rm(c : Connection, dir : string):
    with c.cd(dir):
        c.run("ls")
        to_delete = cli.prompt(">>> Enter directory/file to delete: ")
        if c.run('test -d {0}'.format(to_delete), warn=True):
            confirm = cli.cli_confirm("You are about to delete the directory {0}. Are you sure?".format(to_delete))
            if (confirm == "y"):
                c.run("rm -rf {0}".format(to_delete))
            else:
                cli.puts("!!! Aborted")
        elif c.run('test -f {0}'.format(to_delete), warn=True):
            confirm = cli.cli_confirm("You are about to delete the file {0}. Are you sure?".format(to_delete))
            if (confirm == "y"):
                c.run("rm {0}".format(to_delete))
            else:
                cli.puts("!!! Aborted")
        else:
            cli.puts("!!! Aborted operation. {0} not found.".format(to_delete))


def ls_dir(c : Connection, dir : string):
    ls_dir = cli.prompt(">>> Enter directory to list: ")
    with c.cd(dir + "/" + ls_dir):
        c.run("ls")

def ls_la(c : Connection, dir : string):
    with c.cd(dir):
        c.run("ls -la")

def get(c : Connection):
    t = Transfer(c)
    remote_file = cli.prompt(">>> Enter remote file path to download (relative to home directory): ")
    local_file = cli.prompt(">>> Enter local file path to download to (relative to fabfile location): ")
    t.get(remote_file, local_file)