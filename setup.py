from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-intro_text',
    version=version,
    description="ckan custom intro text plugin",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Janos Farkas',
    author_email='farkas@microcomp.sk',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.intro_text'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'babel.extractors': [
            'ckan = ckan.lib.extract:extract_ckan',
        ],
        'ckan.plugins' : [
            'intro_text_plugin=ckanext.intro_text.plugin:IntroTextPlugin',
        ]
    }
        

)
