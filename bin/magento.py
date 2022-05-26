import string
from fabric.connection import Connection
from tif.fabric import cli

def list_commands(c : Connection, magento_root: string):
    with c.cd(magento_root):
        c.run("bin/magento list")

def run(c : Connection, magento_root: string):
    with c.cd(magento_root):
        command = cli.prompt(">>> Enter bin/magento command to run: ")
        c.run("bin/magento {0}".format(command))

def install(c : Connection, install_dir : string):
    with c.cd(install_dir):
        c.run("bin/magento setup:install")

def delete_generated(c : Connection, magento_root : string):
    with c.cd(magento_root):
        confirm = cli.cli_confirm("You are about to delete the generated directory, Are you sure?")
        if (confirm == "y"):
            c.run("rm -rf generated/*")
            cli.puts(".:~ Done")
        else:
            cli.puts("!!! Aborted")

def di_compile(c : Connection, magento_root : string):
    with c.cd(magento_root):
        c.run("bin/magento setup:di:compile")

def module_enable(c : Connection, magento_root : string):
    with c.cd(magento_root):
        module = cli.prompt(">>> Enter module to enable: ")
        if (module):
            c.run("bin/magento module:enable {0}".format(module))
        else:
            cli.puts("!!! Aborted")

def setup_upgrade(c : Connection, magento_root : string):
    with c.cd(magento_root):
        c.run("bin/magento setup:upgrade")

def cache_clean(c : Connection, magento_root : string):
    with c.cd(magento_root):
        c.run("bin/magento cache:clean")

def cache_flush(c : Connection, magento_root : string):
    with c.cd(magento_root):
        c.run("bin/magento cache:flush")

def template_hints(c : Connection, magento_root : string):
    with c.cd(magento_root):
        status = cli.prompt(">>> Enter disable or enable for template hints: ")
        if (status == "enable" or status == "disable"):
            c.run("bin/magento dev:template-hints:{0}".format(status))
        else:
            cli.puts("!!! Aborted")

def generate_whitelist(c : Connection, magento_root : string):
    with c.cd(magento_root):
        module_name = cli.prompt(">>> Enter module name to generate whitelist json: ")
        c.run("bin/magento setup:db-declaration:generate-whitelist --module-name={0}".format(module_name))

def run_cron_group(c : Connection, magento_root : string):
        with c.cd(magento_root):
            group = cli.prompt(">>> Specify cron group to run: ")
            c.run("bin/magento cron:run --group {0}".format(group))

def cron_install(c : Connection, magento_root : string):
        with c.cd(magento_root):
            c.run("bin/magento cron:install")

def run_cron(c : Connection, magento_root : string):
        with c.cd(magento_root):
            c.run("bin/magento cron:run")

def cat_log(c : Connection, magento_root : string):
        with c.cd(magento_root + "/var/log"):
            c.run("ls", pty=True)
            log = cli.prompt(">>> Specify log to cat: ")
            c.run("cat {0}".format(log), pty=True)