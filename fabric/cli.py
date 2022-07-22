import string
from . import Colors

c = Colors.Colors()

def confirm(question):
    return input(c.get(question))

def prompt(text):
    return input(c.get(text))

def puts(text):
    print(c.get(text))

def puts_hide(text) -> string:
    return c.get(text)

def cli_confirm(message):
    value = confirm("*** {} Y/n ".format(message))
    while value not in ["Y", "n"]:
        value = confirm("*** {} Y/n ".format(message))
    return value.lower()  
