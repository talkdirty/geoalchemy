from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='GeoAlchemy',
      version=version,
      description="Using SQLAlchemy with Spatial Databases",
      long_description="""\
""",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Plugins",
          "Intended Audience :: Information Technology",
          "License :: OSI Approved :: MIT License",
          "Topic :: Scientific/Engineering :: GIS"
      ],
      keywords='geo gis sqlalchemy orm',
      author='Sanjiv Singh',
      author_email='singhsanjivk@gmail.com',
      url='http://geoalchemy.org/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', "doc"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'SQLAlchemy>=0.5',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
