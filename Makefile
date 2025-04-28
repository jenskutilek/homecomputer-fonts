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

.PHONY: .init.stamp
.init.stamp:
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


venv: venv/touchfile

venv-test: venv-test/touchfile


venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt
	test -d venv-test || python3 -m venv venv-test
	. venv-test/bin/activate; pip install -Ur requirements-test.txt
	touch venv-test/touchfile


update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	venv-test/bin/pip install --upgrade pip-tools
	venv-test/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	venv-test/bin/pip-sync requirements-test.txt

	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push