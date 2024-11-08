install:
	Cf. https://python-poetry.org/docs/#installation

build:
    poetry version prerelease
    poetry version patch
	poetry build

deploy-test:
    poetry publish -r test-pypi
	twine upload --repository testpypi dist/*

deploy-pypi:
    poetry publish
	twine upload --repository pypi dist/*
