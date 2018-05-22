#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as f:
	ldescrip = f.read()

if __name__ == "__main__":
    setup(name='BasicMath',
          version='1.0',
          description='Command line adder and multiplier',
          author='Viresh Gupta',
          url='https://github.com/virresh/python-packaging',
          platforms='any',
          packages=find_packages(),
          license='MIT',
          long_description=ldescrip,
          long_description_content_type="text/markdown",
          entry_points={
              "console_scripts": [
                  "adder = adder._cmdline:main",
                  "multiplier = multiplier._cmdline:main",
              ]
          },
          # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          classifiers=[
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Operating System :: OS Independent',
          ],
     )
