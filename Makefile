# FONTMAKE_OPTIONS=-o variable --keep-overlaps --keep-direction

.PHONY: all
all: 64 wb fix-fonts

# .PHONY: update-designspace
# update-designspace:
# 	# Export a designspace + UFOs from the Glyphs file
# 	fontmake -g production/SixtyfourC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Sixtyfour.designspace --output-path temp_out/Sixtyfour.ttf
# 	fontmake -g production/WorkbenchC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Workbench.designspace --output-path temp_out/Workbench.ttf
# 	rm -f temp_out/Sixtyfour.ttf
# 	rm -f temp_out/Workbench.ttf

64:
	$(MAKE) -C Sixtyfour

wb:
	$(MAKE) -C Workbench

fix-fonts:
	python3 scripts/fix_varfont.py

clean:
	rm -f temp_out/*.ttf
