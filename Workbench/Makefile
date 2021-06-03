.PHONY: all
all: workbench

.PHONY: workbench
workbench: config.yaml production/Workbench.glyphs fonts/variable/Workbench[BLED,SCAN].ttf

fonts/variable/Workbench[BLED,SCAN].ttf:
	gftools builder config.yaml
