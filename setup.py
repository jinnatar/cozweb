from setuptools import setup

import sys
import cozify

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='cozweb',
    version=cozify.__version__,
    python_requires='>=3.4',
    author='artanicus',
    author_email='cozweb@nocturnal.fi',
    url='https://github.com/Artanicus/cozweb',
    description='Simple web client written in Python utilizing the python-cozify library.',
    long_description=long_description,
    license='MIT',
    packages=['cozweb'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=['cozify', 'absl-py'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ])  # yapf: disable
