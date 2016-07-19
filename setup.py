from os import path, chdir, pardir
from setuptools import setup, find_packages

VERSION = '0.1'
PROJECT_NAME = 'django-xcache'
DESCRIPTION = 'Keeps backups of expired cached values.'
AUTHOR = 'Chad G. Hansen'
EMAIL = 'chadgh@gmail.com'
URL = 'https://github.com/chadgh/django-xcache'
PYTHON_SUPPORTED_VERSIONS = [
    '2.7',
    '3.4',
    '3.5',
]
DJANGO_SUPPORTED_VERSIONS = [
    '1.8',
    '1.9',
]

with open(path.join(path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
chdir(path.normpath(path.join(path.abspath(__file__), pardir)))

# req_path = path.join(path.dirname(__file__), 'src', 'requirements.txt')
# with open(req_path) as req_file:
#     REQUIREMENTS = req_file.read().split()

classifiers = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
]

for version in PYTHON_SUPPORTED_VERSIONS:
    classifiers.append('Programming Language :: Python :: {}'.format(version))

for version in DJANGO_SUPPORTED_VERSIONS:
    classifiers.append('Framework :: Django :: {}'.format(version))

setup(
    name=PROJECT_NAME,
    version=VERSION,
    packages=find_packages('src', exclude=['tests']),
    package_dir={
        "": "src",
    },
    include_package_data=True,
    description=DESCRIPTION,
    long_description=README,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    # install_requires=REQUIREMENTS,
    classifiers=classifiers,
)
