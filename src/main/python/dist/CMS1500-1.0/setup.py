#from distutils.core import setup
from setuptools import setup, find_packages


setup( name="CMS1500",
       version="1.0",
       description="CMS 1500 test data preparation too",
       author="Venkatesh",
       #packages=['py.cms.dao.TestData','py.cms.dao.DbConnector','py.cms.model.Entities','py.cms.properties.appProperties'],
       #packages=['pyth.cms.dao','pyth.cms.model','pyth.cms.properties','pyth.cms.resources'],
       packages=find_packages()
       #include_package_data=True,
       #install_requires=['mysql.connector'],
      # url='',
       #author_email="venkatesh.sanklapur@gmail.com",
    )