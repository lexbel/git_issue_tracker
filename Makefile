PYPI_REPO=https://test.pypi.org/legacy/

VERSION=$(shell git describe --tags)
VERSION_FILE=VERSION

all: build push clean

test-deploy: build push-test clean

build:
	echo $(VERSION) >> ${VERSION_FILE}
	python setup.py sdist bdist_wheel

push-test:
	twine upload --repository-url $(PYPI_REPO) dist/*

push:
	twine upload dist/*

clean:
	rm -rf build/ git_issue_tracker.egg-info dist/ __pycache__/ $(VERSION_FILE)
