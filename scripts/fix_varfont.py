# import struct
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import ROUND_XY_TO_GRID, USE_MY_METRICS
# from fontTools.ttLib.tables.DefaultTable import DefaultTable


def fix_font(path, outpath):
    f = TTFont(path)
    glyf_table = f["glyf"]

    # Fix glyf table

    for name, glyph in glyf_table.glyphs.items():
        glyph.expand(glyf_table)
        found_metrics = False
        _lsb, width = f["hmtx"][name]
        if glyph.isComposite() and hasattr(glyph, "components"):
            for c in glyph.components:

                # Unset the component rounding flag
                c.flags &= ~ROUND_XY_TO_GRID

                # Set the use my metrics flag if appropriate
                c.flags &= ~USE_MY_METRICS
                if not found_metrics and f["hmtx"][c.glyphName][1] == width:
                    c.flags |= USE_MY_METRICS
                    found_metrics = True

    # Merge STAT, gasp and name tables

    patch = TTFont()
    patch.importXML("patch/patch.ttx")

    # Copy gasp and prep tables
    f["gasp"] = patch["gasp"]
    f["prep"] = patch["prep"]

    # The HVAR patch is not needed for building with fontmake
    # hvar = DefaultTable("HVAR")
    # glyphs = len(f.getGlyphOrder())
    # hvar.data = struct.pack(
    #     ">HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
    #     0x0001, 0x0000, 0x0000, 0x0014, 0x0000, 0x0000, 0x0000, 0x0000,
    #     0x0000, 0x0000, 0x0001, 0x0000, 0x000c, 0x0001, 0x0000, 0x0034,
    #     0x0002, 0x0003, 0x0000, 0x4000, 0x4000, 0x0000, 0x0000, 0x0000,
    #     0x0000, 0x0000, 0x0000, 0x0000, 0x4000, 0x4000, 0x0000, 0x4000,
    #     0x4000, 0x0000, 0x4000, 0x4000, glyphs, 0x0000, 0x0000
    # )
    # f["HVAR"] = hvar

    # Glyphs does not set the weight class of the default master
    # f["OS/2"].usWeightClass = 200

    f.save(outpath)
    f.close()
    f = TTFont(outpath)
    f.saveXML(outpath + ".ttx")


fix_font(
    "Sixtyfour/fonts/variable/Sixtyfour[BLED,SCAN].ttf",
    "fonts/variable/Sixtyfour[BLED,SCAN].ttf",
)

fix_font(
    "Workbench/fonts/variable/Workbench[BLED,SCAN].ttf",
    "fonts/variable/Workbench[BLED,SCAN].ttf",
)
