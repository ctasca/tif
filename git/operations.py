import string
from fabric.connection import Connection
from tif.fabric import cli
from tif.fabric.CommandPrefix import CommandPrefix

def clone_repo(c : Connection, clone_dir: string, repo: string, command_prefix = ""):
    with c.cd(clone_dir):
        command = "git clone {0} .".format(repo)
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)

def switch_branch(c: Connection, repo_dir: string, command_prefix = ""):
    with c.cd(repo_dir):
        branch(c, repo_dir)
        sbranch = cli.prompt(">>> Enter branch to switch to: ")
        if (sbranch):
            command = "git checkout {0}".format(sbranch)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def new_branch(c: Connection, repo_dir: string, command_prefix = ""):
    with c.cd(repo_dir):
        new_branch = cli.prompt(">>> Enter new branch name: ")
        if (new_branch):
            command = "git checkout -b {0}".format(new_branch)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")
 
def branch(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        c.run(CommandPrefix("git branch", command_prefix).prefix_command())

def current_branch(c : Connection, repo_dir : string, command_prefix = "") -> string :
    with c.cd(repo_dir):
        c.run(CommandPrefix("git rev-parse --abbrev-ref HEAD", command_prefix).prefix_command(), hide=True)
        return branch.stdout

def pull(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        branch = current_branch(c, repo_dir, command_prefix)
        confirm = cli.cli_confirm("You are about to pull the remote branch {0}. Are you sure?".format(branch))
        if (confirm == "y"):
            command = "git pull origin {0}".format(branch)
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
        else:
            cli.puts("!!! Aborted")

def pull_branch(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        branch = current_branch(c, repo_dir, command_prefix)
        origin_branch = cli.prompt(">>> Enter branch to pull from origin: ")
        confirm = cli.cli_confirm("You are about to pull the remote branch {0} into {1}. Are you sure?".format(origin_branch, branch))
        if (confirm == "y"):
            command = "git pull origin {0}".format(origin_branch)
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
        else:
            cli.puts("!!! Aborted")

def origin_merge(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        cli.puts("** Fetching origin...")
        fetch(c, repo_dir, command_prefix)
        branch(c, repo_dir, command_prefix)
        local_branch = current_branch(c, repo_dir, command_prefix)
        origin_branch = cli.prompt(">>> Enter origin branch to merge: ")
        if (local_branch and origin_branch):
            confirm = cli.cli_confirm("You are about to merge the origin branch {0} into local branch {1}. Are you sure?".format(origin_branch, local_branch))
            if (confirm == "y"):
                command = "git merge origin/{0}".format(origin_branch)
                c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
            else:
                cli.puts("!!! Aborted")
        else:
            cli.puts("!!! Aborted")

def push(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        branch = current_branch(c, repo_dir, command_prefix)
        confirm = cli.cli_confirm("You are about to push to origin branch {0}. Are you sure?".format(branch))
        if (confirm == "y"):
            command = "git push origin {0}".format(branch)
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
        else:
            cli.puts("!!! Aborted")

def fetch(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git fetch"
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)

def status(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git status"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def diff(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        file = cli.prompt(">>> Enter file to diff: ")
        command = "git diff {0}".format(file)
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def file_checkout(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        status(c, repo_dir)
        file = cli.prompt(">>> Enter file to checkout: ")
        if(file):
            command = "git checkout -- {0}".format(file)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def add_iteractive(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git add -i"
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)

def commit(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git commit"
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)

def stash(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git stash"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def stash_list(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git stash list"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def stash_drop(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git stash drop"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def stash_pop(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git stash pop"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def reset_head(c : Connection, repo_dir : string, command_prefix = ""):
    with c.cd(repo_dir):
        command = "git reset --hard HEAD"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def remove(c : Connection, repo_dir : string, command_prefix = ""):
     with c.cd(repo_dir):
        file = cli.prompt(">>> Enter file to remove. Type 'exit' to finish the operation: ")
        while file not in ["exit"]:
            command = "git rm {0}".format(file)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            status(c, repo_dir, command_prefix)
            file = cli.prompt(">>> Enter file to remove. Type 'exit' to finish the operation: ")
        status(c, repo_dir, command_prefix)

def log(c : Connection, repo_dir : string, logs = "-5", command_prefix = ""):
    with c.cd(repo_dir):
        command = "git log -p {0}".format(logs)
        c.run(CommandPrefix(command, command_prefix).prefix_command())