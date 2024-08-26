from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easy-kit",
    author='flegac',
    description='Python toolkit',

    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['easy_kit'],
    # install_requires=[line for line in open('requirements.txt')],
    python_requires=">=3.7",
    include_package_data=True
)
