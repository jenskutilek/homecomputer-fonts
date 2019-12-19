FONTMAKE_OPTIONS=-o variable --keep-overlaps --keep-direction

all: sixtyfour workbench

designspace:
	fontmake -g production/SixtyfourC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Sixtyfour.designspace --output-path temp_out/Sixtyfour.ttf
	fontmake -g production/WorkbenchC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Workbench.designspace --output-path temp_out/Workbench.ttf

sixtyfour: designspace
	fontmake -m master_ufo/Sixtyfour.designspace $(FONTMAKE_OPTIONS)
# 	python3 scripts/fix_varfont.py

workbench: designspace
	fontmake -m master_ufo/Workbench.designspace $(FONTMAKE_OPTIONS)
# 	python3 scripts/fix_varfont.py

fix-fonts:
	python3 scripts/fix_varfont.py
