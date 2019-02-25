# packaging_tutorial

This is an example package using tutorial provided by [PyPA >> Python Packageing User Guide >> Tutorials](https://packaging.python.org/tutorials/packaging-projects/).

Further reading recommended: [PyPA >> Python Packageing User Guide >> An Overview of Packaging for Python](https://packaging.python.org/overview/).

## Generating distribution archives

Make sure you have the latest versions of `setuptools` and `wheel` installed:

```Bash
$ sudo pip install --upgrade pip
$ python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where `setup.py` is located:

```Bash
$ python3 setup.py sdist bdist_wheel
```

This command should output a lot of text and once completed should generate two files in the dist directory:

```Bash
dist/
	Hanmei_Tang-example-package-name-to-be-distributed-2019.2.24.tar.gz
	Hanmei_Tang_example_package_name_to_be_distributed-2019.2.24-py3-none-any.whl
```

## Uploading the distribution archives

Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:
```
$ python3 -m pip install --user --upgrade twine
$ cd ~/repos/packaging_tutorial
$ python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Take a look at [the vieable package on TestPyPI](https://test.pypi.org/project/Hanmei_Tang-example-package-name-to-be-distributed)


## Installing your newly uploaded package

```
$ python3 -m pip install --index-url https://test.pypi.org/simple/ Hanmei_Tang-example-package-name-to-be-distributed
Looking in indexes: https://test.pypi.org/simple/
Requirement already satisfied: Hanmei_Tang-example-package-name-to-be-distributed in /Users/hanmeiTang/repos/packaging_tutorial (2019.2.24)
```

Test in iPython
```
$ ipython
iPython 3.6.7 |Anaconda, Inc.| (default, Oct 23 2018, 14:01:38)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import example_pkg

In [2]: example_pkg.name
Out[2]: 'example_pkg'
```
