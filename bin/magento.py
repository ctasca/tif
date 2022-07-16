import string
from fabric.connection import Connection
from tif.fabric import cli
from tif.fabric.logger import Logger
from tif.fabric.CommandPrefix import CommandPrefix

def list_commands(c : Connection, magento_root: string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento list"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def run(c : Connection, magento_root: string, command_prefix=""):
    with c.cd(magento_root):
        list_commands(c, magento_root, command_prefix)
        command = cli.prompt(">>> Enter bin/magento command to run: ")
        command = "bin/magento {0}".format(command)
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def install(c : Connection, install_dir : string, command_prefix=""):
    with c.cd(install_dir):
        command = "bin/magento setup:install"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def mode_show(c : Connection, install_dir : string, command_prefix=""):
    with c.cd(install_dir):
        command = "bin/magento deploy:mode:show"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def delete_generated(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the generated directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf generated/*"
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def delete_static(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the static directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf pub/static/*"
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def delete_logs(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to empty the var/log directory, Are you sure?")
        if (confirm == "y"):
            command = "rm -rf var/log/*"
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def di_compile(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento setup:di:compile"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def module_enable(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        module = cli.prompt(">>> Enter module to enable: ")
        if (module):
            command = "bin/magento module:enable {0}".format(module)
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def setup_upgrade(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento setup:upgrade"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def cache_clean(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento cache:clean"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def cache_flush(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento cache:flush"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def template_hints(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        status = cli.prompt(">>> Enter disable or enable for template hints: ")
        if (status == "enable" or status == "disable"):
            command = "bin/magento dev:template-hints:{0}".format(status)
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())
        else:
            cli.puts("!!! Aborted")

def generate_whitelist(c : Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        module_name = cli.prompt(">>> Enter module name to generate whitelist json: ")
        command = "bin/magento setup:db-declaration:generate-whitelist --module-name={0}".format(module_name)
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command())

def run_cron_group(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            group = cli.prompt(">>> Specify cron group to run: ")
            command = "bin/magento cron:run --group {0}".format(group)
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def cron_install(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            command = "bin/magento cron:install"
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def run_cron(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root):
            command = "bin/magento cron:run"
            Logger().log("Running {}", command)
            c.run(CommandPrefix(command, command_prefix).prefix_command())

def cat_log(c : Connection, magento_root : string, command_prefix=""):
        with c.cd(magento_root + "/var/log"):
            command = "ls"
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)
            log = cli.prompt(">>> Specify log to cat: ")
            command = "cat {0}".format(log)
            Logger().log("Running command '{}'".format(command))
            c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)

def admin_user_create(c: Connection, magento_root : string, command_prefix=""):
    with c.cd(magento_root):
        command = "bin/magento admin:user:create"
        Logger().log("Running command '{}'".format(command))
        c.run(CommandPrefix(command, command_prefix).prefix_command(), pty=True)