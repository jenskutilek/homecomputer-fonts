from c64.colors import colors, godots
from c64.fonts import pchr

from rhino import rhino_chars, rhino_colors


def do64():
    save()
    rect(0, 0, w, h)
    translate(19, h-45)
    scale(4, 4)
    t = FormattedString(
        "",
        font="/Users/kuti/Documents/Schriften/Homecomputer/Sixtyfour/fonts/variable/Sixtyfour[BLED,SCAN].ttf",
        fontSize=8,
        fill=(1)
    )
    for scan in range(-53, 100, 8):
        for bled in range(0, 100, 5):
            color = choice(colors)
            while color == (0, 0, 0):
                color = choice(colors)
            t.append(pchr(randint(0, 255)), fontVariations={"BLED": bled, "SCAN": scan}, fill=color)
        t.append("\n")

    text(t, (0, 0))
    restore()


def doWB():
    newPage()
    save()
    rect(0, 0, w, h)
    translate(2, h-27)
    scale(4, 4)

    c = "a"

    t = FormattedString("", font="/Users/kuti/Documents/Schriften/Homecomputer/Workbench/fonts/variable/Workbench[BLED,SCAN].ttf", fontSize=8, fill=(1))
    for scan in range(-53, 100, 7):
        for bled in range(0, 100, 2):
            t.append(c, fontVariations={"BLED": bled, "SCAN": scan}, fill=(random(), random(), random()))
        t.append("\n")
    text(t, (0, 0))
    restore()


def doRhino():
    newPage()
    save()
    fill(1)
    rect(0, 0, w, h)
    translate(2, h-27)
    scale(3, 3)

    t = FormattedString(
        "",
        font="/Users/kuti/Documents/Schriften/Homecomputer/Sixtyfour/fonts/variable/Sixtyfour[BLED,SCAN].ttf",
        fontSize=8,
        fill=(0)
    )
    lc = 0
    cc = 0
    num_lines = len(rhino_chars)
    for scan in range(num_lines):
        rhino_line = rhino_chars[lc]
        color_line = rhino_colors[lc]
        num_cols = len(rhino_line)
        for bled in range(num_cols):
            r, g, b = godots[color_line[cc]]
            t.append(pchr(rhino_line[cc]), fontVariations={"BLED": calcBleed(bled, num_cols, 0, 0), "SCAN": calcScan(scan, num_lines, -53, 20)}, fill=(r/255, g/255, b/255))
            cc += 1
        t.append("\n")
        lc += 1
        cc = 0
    text(t, (0, 0))
    restore()


def calcBleed(step, max_value, start=0, stop=100):
    return round(start + (stop - start) * step / max_value)


def calcScan(step, max_value, start=-53, stop=100):
    return round(start + (stop - start) * step / max_value)


w = 1200
h = 675
size(w, h)

do64()
doWB()
doRhino()