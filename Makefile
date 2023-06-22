help:
	@echo "###"
	@echo "# Build targets for the Homecomputer fonts"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

.PHONY: build
build:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: test
test:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: proof
proof:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: images
images:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: clean
clean:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: dist-clean
dist-clean:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@
