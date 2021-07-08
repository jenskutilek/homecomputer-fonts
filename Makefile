help:
	@echo "###"
	@echo "# Build targets for the Homecomputer fonts"
	@echo "###"
	@echo
	@echo "  make build: Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:  Tests the fonts with fontbakery"
	@echo "  make proof: Creates HTML proof documents in the proof/ directory"
	@echo

build: build.stamp Sixtyfour/sources/config.yaml Sixtyfour/sources/Sixtyfour.glyphs Workbench/sources/config.yaml Workbench/sources/Workbench.glyphs

venv: venv/touchfile

build.stamp: venv
	. venv/bin/activate; gftools builder Sixtyfour/sources/config.yaml && touch build.stamp
	. venv/bin/activate; gftools builder Workbench/sources/config.yaml && touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: venv build.stamp
	. venv/bin/activate; fontbakery check-googlefonts --html fontbakery-report.html --ghmarkdown fontbakery-report.md $(shell find fonts -type f)

proof: venv build.stamp
	. venv/bin/activate; gftools gen-html proof $(shell find fonts/ttf -type f) -o proof

.PHONY: clean
clean:
	rm -f temp_out/*.ttf

.PHONY: dist-clean
dist-clean:
	rm -rf venv
	find -iname "*.pyc" -delete

# .PHONY: update-designspace
# update-designspace:
# 	# Export a designspace + UFOs from the Glyphs file
# 	fontmake -g production/SixtyfourC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Sixtyfour.designspace --output-path temp_out/Sixtyfour.ttf
# 	fontmake -g production/WorkbenchC.glyphs $(FONTMAKE_OPTIONS) --designspace-path master_ufo/Workbench.designspace --output-path temp_out/Workbench.ttf
# 	rm -f temp_out/Sixtyfour.ttf
# 	rm -f temp_out/Workbench.ttf

.PHONY: 64
64:
	$(MAKE) -C Sixtyfour

.PHONY: wb
wb:
	$(MAKE) -C Workbench

fix-fonts:
	python3 scripts/fix_varfont.py
