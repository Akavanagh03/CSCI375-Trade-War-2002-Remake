TEST = python -m pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = pytest
ASSIGNMENT = assignments
SCRIPT = ship_classes.py
SCRIPT_TEST = test_ships.py
SCRIPT_NAME = $(basename $(SCRIPT))
DOC_DIR = ./docs
HTML_FILE = $(DOC_DIR)/$(SCRIPT_NAME)_doc.html

.PHONY: all
all: fix-style check-type run-test-coverage clean
	@echo "All checks passed"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) $(SCRIPT)

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .


.PHONY: check-style
check-style:
	$(STYLE_CHECK) $(SCRIPT)

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) $(SCRIPT)
.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=html:htmlcov --cov-report=term --cov=$(SCRIPT) $(SCRIPT_TEST)

html: $(HTML_FILE)

$(HTML_FILE): $(SCRIPT)
	pdoc $(SCRIPT) -o $(DOC_DIR)
	@echo "HTML documentation generated as $(HTML_FILE)"

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 