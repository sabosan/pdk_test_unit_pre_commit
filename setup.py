#!/usr/bin/env python3

from setuptools import setup, find_packages
setup(name='pdk_test_unit_pre_commit',
      version='0.1',
      description='pre-commit to check to execute `pdk test unit`',
      packages=['pdk_test_unit_pre_commit'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'pdk_test_unit_pre_commit=pdk_test_unit_pre_commit.pdk_test_unit_pre_commit:main'
          ]
      },
      )
