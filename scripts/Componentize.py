def replace_in_layer(layer, components):
    # print(layer.parent.name)
    new = []
    delete_paths = []
    for i, path in enumerate(layer.paths):
        b = path.bounds
        # print(i, path, b)
        for c in components:
            if c.bounds.size == b.size:
                delete_paths.append(i)
                new.append((
                    c.parent.name,
                    (
                        b.origin.x - c.bounds.origin.x,
                        b.origin.y - c.bounds.origin.y
                    )
                ))
    delete_paths.sort(reverse=True)
    for i in delete_paths:
        del layer.paths[i]
    for cn, pos in new:
        layer.components.append(GSComponent(cn, pos))


components = [
    Font.glyphs[name].layers[Font.selectedFontMaster.id]
    for name in [
        "pixel.1",
        "pixel.2",
        "pixel.3",
        "pixel.4",
        "pixel.5",
        "pixel.6",
        "pixel.7",
        "pixel.8",
    ]
]

for layer in Font.selectedLayers:
    replace_in_layer(layer, components)
