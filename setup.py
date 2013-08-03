from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='ep.cdpolicy',
      version=version,
      description="Policies for the corporate design manual of the europython",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Zope Plone',
      author='Veit Schiele',
      author_email='kontakt@veit-schiele.de',
      url='https://github.com/veit/ep.cdpolicy',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['ep', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.documentviewer',
          'wildcard.foldercontents',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
