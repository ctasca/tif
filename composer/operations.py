import string
from turtle import write_docstringdict
from fabric.connection import Connection
from tif.fabric import cli

def install(c : Connection, install_dir : string):
    with c.cd(install_dir):
        c.run("composer install",  pty=True)
