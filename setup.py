import os

from setuptools import setup, find_packages


def file_content(filename):
    '''Load file content'''
    with open(filename) as ifile:
        return ifile.read()


def pip(filename):
    """Return path to pip requirements file"""
    return file_content(os.path.join('requirements', filename))


long_description = '\n'.join((
    file_content('README.md'),
    file_content('CHANGELOG.md'),
    ''
))


install_requires = pip('install.pip')
tests_require = pip('test.pip')


setup(
    name='udata-transport',
    version=__import__('udata_transport').__version__,
    description=__import__('udata_transport').__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/opendatateam/udata-transport',
    author='Opendata Team',
    author_email='opendatateam@data.gouv.fr',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        'udata.views': [
            'transport = udata_transport.views',
        ],
        'udata.tasks': [
            'transport = udata_transport.tasks',
        ],
    },
    license='GNU AGPLv3+',
    keywords='udata transport',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ('License :: OSI Approved :: GNU Affero General Public License v3'
         ' or later (AGPLv3+)'),
    ],
)
