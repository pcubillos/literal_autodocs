# Literal Autodocs
API documentation generator keeping literal docstrings

[![Build Status](https://travis-ci.com/pcubillos/literal_autodocs.svg?branch=master)](https://travis-ci.com/pcubillos/literal_autodocs)
[![PyPI](https://img.shields.io/pypi/v/literal_autodocs.svg)](https://pypi.org/project/literal_autodocs)
[![GitHub](https://img.shields.io/github/license/pcubillos/literal_autodocs.svg?color=blue)](https://github.com/pcubillos/literal_autodocs/blob/master/LICENSE)


`autodocs` requires that '*the docstrings must **of course** be written in correct reStructuredText'*.  
I don't like that constrain, I prefer to write my docstrings in my own format.
This package creates automated rest API documentation keeping the docstrings as literal text, using the Python-console-session lexer.

Here's an example:
https://bibmanager.readthedocs.io/en/latest/api.html

### Install
``literal_autodocs`` has been [tested](https://travis-ci.com/pcubillos/literal_autodocs) to work on Python 3.6 and 3.7; and runs (at least) in both Linux and OSX.  You can install ``literal_autodocs`` from the terminal with pip:

```shell
pip install literal_autodocs
```

Alternative (for conda users or for developers), you can directly
dowload the source code and install to your local machine with the
following terminal commands:

```shell
git clone https://github.com/pcubillos/literal_autodocs
cd literal_autodocs
python setup.py install
```
