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