# standard_deviation

Author: James Henry

Date: December 17, 2016

[![Build Status](https://travis-ci.org/jghenry/standard_deviation.svg?branch=master)](https://travis-ci.org/jghenry/standard_deviation)

## What does it do?

This package calculates standard deviation and standard error in Python

## Where to find it?

The source code is hosted on GitHub at: https://github.ubc.ca/jghenry/standard_deviation

To install this package use the following command:

```
pip install git+ssh://git@github.ubc.ca/jghenry/standard_deviation.git
```

To run the standard_deviation function use the following commands:

```
from sd_py import sd
sd.standard_deviation([0,1,2])
```
OR

```
from sd_py.sd import *
standard_deviation([0,1,2])
```

The same syntax applies for the standard_error function 

## Release

Latest release 0.1dev

## Dependencies

None

## License

MIT

## Tests
1. clone repo
2. install pytest (`pip install -U pytest`)
3. navigate to root directory of `standard_deviation` (this is the repo you just cloned) and run `pytest`
