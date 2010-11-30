from setuptools import setup, find_packages
import os

version = '1.0'

tests_require = []

setup(name='dolmen.emailer',
      version=version,
      description="",
      long_description=open(os.path.join("docs", "README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dolmen'],
      include_package_data=True,
      zip_safe=False,
      package_dir={'': 'src'},
      packages=find_packages('src'),
      extras_require = {'test': tests_require},
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
