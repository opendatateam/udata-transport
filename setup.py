import io
import os
import re

from setuptools import setup, find_packages

RE_REQUIREMENT = re.compile(r'^\s*-r\s*(?P<filename>.*)$')
RE_BADGE = re.compile(r'^\[\!\[(?P<text>[^\]]+)\]\[(?P<badge>[^\]]+)\]\]\[(?P<target>[^\]]+)\]$', re.M)

BADGES_TO_KEEP = []


def md(filename):
    '''
    Load .md (markdown) file and sanitize it for PyPI.
    Remove unsupported github tags:
     - code-block directive
     - travis ci build badges
    '''
    content = io.open(filename).read()

    for match in RE_BADGE.finditer(content):
        if match.group('badge') not in BADGES_TO_KEEP:
            content = content.replace(match.group(0), '')
    return content


def pip(filename):
    '''Parse pip reqs file and transform it to setuptools requirements.'''
    requirements = []
    for line in open(os.path.join('requirements', filename)):
        line = line.strip()
        if not line or '://' in line or line.startswith('#'):
            continue
        requirements.append(line)
    return requirements


long_description = '\n'.join((
    md('README.md'),
    md('CHANGELOG.md'),
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
    author_email='contact@opendata.team',
    packages=find_packages(),
    package_data={'udata_transport': ['schema.json']},
    python_requires='>=3.7',
    include_package_data=True,
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
    license='LGPL',
    zip_safe=False,
    keywords='udata transport',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)
