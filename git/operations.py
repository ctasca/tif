import string
from fabric.connection import Connection
from tif.fabric import cli

def clone_repo(c : Connection, clone_dir: string, repo: string):
    with c.cd(clone_dir):
        c.run("git clone {0} .".format(repo), pty=True)

def switch_branch(c: Connection, repo_dir: string):
    with c.cd(repo_dir):
        branch(c, repo_dir)
        sbranch = cli.prompt(">>> Enter branch to switch to: ")
        if (sbranch):
            c.run("git checkout {0}".format(sbranch))
        else:
            cli.puts("!!! Aborted")

def new_branch(c: Connection, repo_dir: string):
    with c.cd(repo_dir):
        new_branch = cli.prompt(">>> Enter new branch name: ")
        if (new_branch):
            c.run("git checkout -b {0}".format(new_branch))
        else:
            cli.puts("!!! Aborted")
 
def branch(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git branch")

def current_branch(c : Connection, repo_dir : string) -> string :
    with c.cd(repo_dir):
        branch = c.run("git rev-parse --abbrev-ref HEAD", hide=True)
        return branch.stdout

def pull(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        branch = current_branch(c, repo_dir)
        confirm = cli.cli_confirm("You are about to pull the remote branch {0}. Are you sure?".format(branch))
        if (confirm == "y"):
            c.run("git pull origin {0}".format(branch), pty=True)
        else:
            cli.puts("!!! Aborted")

def push(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        branch = current_branch(c, repo_dir)
        confirm = cli.cli_confirm("You are about to push to origin branch {0}. Are you sure?".format(branch))
        if (confirm == "y"):
            c.run("git push origin {0}".format(branch), pty=True)
        else:
            cli.puts("!!! Aborted")

def fetch(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git fetch", pty=True)

def status(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git status")

def diff(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        file = cli.prompt(">>> Enter file to diff: ")
        c.run("git diff {0}".format(file))

def file_checkout(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        status(c, repo_dir)
        file = cli.prompt(">>> Enter file to checkout: ")
        if(file):
            c.run("git checkout -- {0}".format(file))
        else:
            cli.puts("!!! Aborted")

def add_iteractive(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git add -i", pty=True)

def commit(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git commit", pty=True)

def stash(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git stash")

def stash_drop(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git stash drop")

def reset_head(c : Connection, repo_dir : string):
    with c.cd(repo_dir):
        c.run("git reset --hard HEAD")
