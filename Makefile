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

.PHONY: clean
clean:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@

.PHONY: dist-clean
dist-clean:
	$(MAKE) -C Sixtyfour $@
	$(MAKE) -C Workbench $@