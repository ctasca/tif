import string
from fabric.connection import Connection
from tif.fabric import cli
from tif.fabric.CommandPrefix import CommandPrefix

def list_commands(c : Connection, magento_root: string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento list"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def run(c : Connection, magento_root: string, command_prefix=""):
    with c.cd(magento_root):
        command = cli.prompt(">>> Enter bin/magento command to run: ")
        command = "bin/magento {0}".format(command)
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def install(c : Connection, install_dir : string, command_prefix=""):
    with c.cd(install_dir):
        command = "bin/magento setup:install"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def delete_generated(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the generated directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf generated/*"
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def delete_static(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the static directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf pub/static/*"
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def delete_logs(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the var/log directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf var/log/*"
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def di_compile(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        c.run("bin/magento setup:di:compile")

def module_enable(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        module = cli.prompt(">>> Enter module to enable: ")
        if (module):
            command = "bin/magento module:enable {0}".format(module)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def setup_upgrade(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        c.run("bin/magento setup:upgrade")

def cache_clean(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento cache:clean"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def cache_flush(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento cache:flush"
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def template_hints(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        status = cli.prompt(">>> Enter disable or enable for template hints: ")
        if (status == "enable" or status == "disable"):
            command = "bin/magento dev:template-hints:{0}".format(status)
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def generate_whitelist(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        module_name = cli.prompt(">>> Enter module name to generate whitelist json: ")
        command = "bin/magento setup:db-declaration:generate-whitelist --module-name={0}".format(module_name)
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def run_cron_group(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            group = cli.prompt(">>> Specify cron group to run: ")
            command = "bin/magento cron:run --group {0}".format(group)
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def cron_install(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            command = "bin/magento cron:install"
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def run_cron(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            command = "bin/magento cron:run"
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def cat_log(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root + "/var/log"):
            command = "ls"
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
            log = cli.prompt(">>> Specify log to cat: ")
            command = "cat {0}".format(log)
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)