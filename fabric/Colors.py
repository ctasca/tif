import re

def _wrap_with(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner

red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')

class Colors:
        def __init__(self):
            pass
        def get(self, text):
            if re.match(r'^\>\>\>', text):
                return cyan(text)
            if re.match(r'^\*\*\s', text):
                return white(text)
            if re.match(r'^\*\*\*', text):
                return yellow(text)
            if re.match(r'^\[\d{1,}\]', text):
                return yellow(text)
            if re.match(r'^\!\!\!', text):
                return red(text)
            if re.match(r'^\!\!\s', text):
                return blue(text)
            if re.match(r'^\.:\~', text):
                return green(text)