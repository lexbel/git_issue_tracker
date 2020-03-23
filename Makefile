PYPI_REPO=https://test.pypi.org/legacy/

VERSION=$(shell git describe --tags)
VERSION_FILE=VERSION

all: build push clean

build:
	echo $(VERSION) >> ${VERSION_FILE}
	python setup.py sdist bdist_wheel
	rm $(VERSION_FILE)

push-test:
	python -m twine upload --repository-url $(PYPI_REPO) dist/*

clean:
	rm -rf build/ issue_fix_version_tracker_lexbel.egg-info dist/ __pycache__/
