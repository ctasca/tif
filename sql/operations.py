import string
from fabric.connection import Connection
from tif.fabric import cli

def import_db(c : Connection, dump_location : string):
    with c.cd(dump_location):
        c.run("ls")
        user = cli.prompt(">>> Enter DB user: ")
        db = cli.prompt(">>> Enter DB name: ")
        dump = cli.prompt(">>> Enter dump filename: ")
        if (user and db and dump):
            c.run("mysql -u{0} -p {1} < {2}".format(user, db, dump), pty=True)
            cli.puts(".:~ Import finished: {0}".format(dump))
        else:
            cli.puts("!!! Aborted")