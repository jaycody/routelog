from distutils.core import setup
from glob import glob

setup(
    name='routelog',
    version='0.1',
    author='Matthew Story',
    author_email='matt.story@axial.net',
    scripts=['bin/routelog'],
    data_files=[('share/man/man1', [ 'man/man1/routelog.1', ], ),
                ('share/man/man5', [ 'man/man5/routelog.5', ], ), ],
    url='https://github.com/axialmarket/routelog',
    license='3-BSD',
    description='A Flexible DSL For Processing Logs',
    long_description=open('README.md').read()
)

