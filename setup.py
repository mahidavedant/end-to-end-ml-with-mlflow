from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = '0.0.0'
REPO = 'end-to-end-ml-with-mlflow'
SRC_REPO = 'mlProject'
AUTHOR_USERNAME = 'mahidavedant'
AUTHOR_EMAIL = 'vedantsinh13@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USERNAME}/{REPO}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USERNAME}/{REPO}/issues'
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)
