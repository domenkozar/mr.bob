# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages

install_requires = [
    'setuptools',
    'argparse',
    'jinja2',
    'six',
]

try:
    import importlib  # NOQA
except ImportError:
    install_requires.append('importlib')

try:
    from collections import OrderedDict  # NOQA
except ImportError:
    install_requires.append('ordereddict')


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name='mr.bob',
      version='0.1a6.dev0',
      description='Bob renders directory structure templates',
      long_description=read('README.rst') + "\n" + read('HISTORY.rst'),
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.2",
      ],
      author='Domen Kozar, Tom Lazar',
      author_email='',
      url='https://github.com/iElectric/mr.bob.git',
      license='BSD',
      packages=find_packages(),
      install_requires=install_requires,
      extras_require={
          'test': [
              'pytest',
              'pytest-cov',
              'flake8',
              'pytest',
              'mock',
          ],
          'development': [
              'zest.releaser',
              'Sphinx',
          ],
      },
      entry_points="""
      [console_scripts]
      mrbob = mrbob.cli:main
      """,
      include_package_data=True,
      zip_safe=False,
      )
