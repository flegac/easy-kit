
Cf. https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org

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