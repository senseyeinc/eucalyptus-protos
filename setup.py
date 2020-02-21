from setuptools import setup
from pathlib import Path

readme = str(Path(Path(__file__).parent.absolute(), 'README.md'))
long_description = open(readme, encoding='utf-8').read()

setup(
    name='senseye-api-protos',
    description='Protobuf files for Senseye\'s Eucalyptus API.',
    author='Senseye Inc',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'senseye_api_protos',
    ],
    package_dir={
        'senseye_api_protos': 'senseye_api_protos/python',
    },
    install_requires=[
        'protobuf',
        'grpcio-tools',
    ],
)
