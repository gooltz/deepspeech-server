import os, sys
try:
    from setuptools import setup, find_packages
    use_setuptools = True
except ImportError:
    from distutils.core import setup
    use_setuptools = False

try:
    with open('readme.md', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''

install_requires = [
]

setup(
    name="mozilla deepspeech server",
    version='0.1.0',
    url='git@gitlabinternal.softathome.com:sah_datalab/deepspeech-server-py.git',
    license='SAH',
    description="deepspeech server",
    long_description=description,
    author='Romain Picard',
    author_email='romain.picard@softathome.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: SAH',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    scripts=['script/deepspeech-server'],
)