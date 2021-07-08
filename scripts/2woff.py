from sys import argv
from os.path import basename, join
from fontTools.ttLib import TTFont

for arg in argv[1:]:
    f = TTFont(arg)
    f.flavor = "woff2"
    base, suffix = basename(arg).rsplit(".", 1)
    f.save(join("fonts", "webfonts", f"{base}.woff2"))
