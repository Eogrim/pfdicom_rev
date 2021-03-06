import sys

# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'pfdicom_rev',
      version          =   '2.4.4',
      description      =   'Process DICOM trees and create JSON summares for the ReV viewer.',
      long_description =   readme(),
      author           =   'FNNDSC',
      author_email     =   'dev@babymri.org',
      url              =   'https://github.com/FNNDSC/pfdicom_rev',
      packages         =   ['pfdicom_rev'],
      install_requires =   ['pfdicom'],
      #test_suite       =   'nose.collector',
      #tests_require    =   ['nose'],
      scripts          =   ['bin/pfdicom_rev'],
      license          =   'MIT',
      zip_safe         =   False
)
