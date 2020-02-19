from setuptools import setup
from pathlib import Path

readme = str(Path(Path(__file__).parent.absolute(), 'README.md'))
long_description = open(readme, encoding='utf-8').read()

setup(
    name='eucalyptus-protos',
    description='Protobuf files for Senseye\'s Eucalyptus API.',
    author='Senseye Inc',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'eucalyptus_protos',
    ],
    package_dir={
        'eucalyptus_protos': 'eucalyptus_protos/python_protos',
    },
    install_requires=[
        'grpcio-tools',
    ],
)
