FONTMAKE_OPTIONS=-o variable --keep-overlaps --keep-direction

all: sixtyfour workbench fix-fonts

update-designspace:
	# Export a designspace + UFOs from the Glyphs file
	fontmake -g production/SixtyfourC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Sixtyfour.designspace --output-path temp_out/Sixtyfour.ttf
	fontmake -g production/WorkbenchC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Workbench.designspace --output-path temp_out/Workbench.ttf
	rm -f temp_out/Sixtyfour.ttf
	rm -f temp_out/Workbench.ttf

sixtyfour:
	fontmake -m master_ufo/Sixtyfour.designspace $(FONTMAKE_OPTIONS) --output-path temp_out/Sixtyfour-VF.ttf

workbench:
	fontmake -m master_ufo/Workbench.designspace $(FONTMAKE_OPTIONS) --output-path temp_out/Workbench-VF.ttf

fix-fonts:
	python3 scripts/fix_varfont.py

clean:
	rm -f temp_out/*.ttf
