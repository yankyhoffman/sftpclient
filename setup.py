from os import path
from setuptools import find_packages, setup


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='sftpclient',
    version='1.0.0',
    author='Yanky Hoffman',
    author_email='developer.yankyhoffman@gmail.com',
    url='https://github.com/yankyhoffman/sftpclient.git',
    description='Username/Password SFTP Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pysftp',
    ],
)
