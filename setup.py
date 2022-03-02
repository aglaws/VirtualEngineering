from setuptools import setup

setup(name = 'Virtual Engineering Toolbox',
    version = '0.0',
    packages = ['vebio'],
    zip_safe = False,
    package_dir={'vebio': 'vebio/'},
    package_data={'libptreat': ['pretreatment/test/libptreat.so']},)
