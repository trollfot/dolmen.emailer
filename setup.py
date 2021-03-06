from setuptools import setup, find_packages
import os

version = '1.0'

tests_require = []

setup(name='dolmen.emailer',
      version=version,
      description="",
      long_description=open(os.path.join("docs", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      include_package_data=True,
      zip_safe=False,
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['dolmen'],
      extras_require = {'test': tests_require},
      install_requires=[
          'grokcore.component',
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.security',
          'zope.sendmail',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
