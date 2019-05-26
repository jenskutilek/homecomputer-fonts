from __future__ import division

glyphs = ["hyphen"]


def getPaths(glyph_name):
    layer = Glyphs.font.glyphs[glyph_name].layers[2]

    result = "%s = [" % glyph_name

    for path in layer.paths:
        result += "["
        for node in path.nodes:
            result += "((%i, %i), %r), " % (node.x, node.y, node.type)
        result += "], "
    result += "]"
    return result


layer_values = [
    (0, 0),
    (-2, 20),
    (-60, 250), # 122
    (-90, 20),
    (-122, 250),
]


def drawPathsInGlyph(glyph):
    ref_paths = glyph.layers[0].paths
    for i in range(len(glyph.layers) - 2):
        layer = glyph.layers[i + 1]
        layer.paths = []
        for ref_path in ref_paths:
            n0 = ref_path.segments[0][0]
            n1 = ref_path.segments[0][1]
            cor, exp = layer_values[i + 1]
            drawPathsInLayer(layer, n0.x, n0.y, n1.x, n1.y, cor, exp)


offcurve_ratio_x = 39/122
offcurve_ratio_y = 50/122
line_ratio_x = 73/122


def drawPathsInLayer(layer, x0, y0, x1, y1, correction, expansion, clear=True):
    c = correction
    e = expansion
    half = e / 2
    offcurve_ratio_x = 39/122
    offcurve_ratio_y = 50/122
    line_ratio_x = 73/122

    # Correct for short segments
    if abs(x1 - x0) < expansion:
        line_ratio_x = 0.5
        offcurve_ratio_x = 0.288
    p = GSPath()
    for node in [
            ((x0 + c + e * offcurve_ratio_x, y0 - half), "offcurve"),
            ((x0 + c, y0 - half * offcurve_ratio_y), "offcurve"),
            ((x0 + c, y0 + half * offcurve_ratio_y), "offcurve"),
            ((x0 + c + e * offcurve_ratio_x, y0 + half), "offcurve"),
            ((x0 + c + e * line_ratio_x, y0 + half), "qcurve"),
            ((x1 - c - e * line_ratio_x, y0 + half), "line"),

            ((x1 - c - e * offcurve_ratio_x, y0 + half), "offcurve"),
            ((x1 - c, y0 + half * offcurve_ratio_y), "offcurve"),
            ((x1 - c, y0 - half * offcurve_ratio_y), "offcurve"),
            ((x1 - c - e * offcurve_ratio_x, y0 - half), "offcurve"),
            ((x1 - c - e * line_ratio_x, y0 - half), "qcurve"),
            ((x0 + c + e * line_ratio_x, y0 - half), "line"),
    ]:
        pt, typ = node
        x, y = pt
        n = GSNode((int(round(x)), int(round(y))), typ)
        if typ in ("line", "qcurve"):
            n.smooth = True
        p.nodes.append(n)
    p.closed = True
    layer.paths.append(p)

# for glyph_name in glyphs:
#     print getPaths(glyph_name)


for l in Glyphs.font.selectedLayers:
    drawPathsInGlyph(l.parent)
