from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='FDIC',
      version='1.0',
      description='collection of frequent functions',
      author='RyanMcStylin',
      author_email='ryanmcstylin@gmail.com',
      license='RyanMcStylin Inc',
      packages=['FDIC'],
      #zip_safe=False,
      #install_requires=['datetime',
      #                  'pandas',
      #                  'dateutil',
      #                  'numpy',
      #                  'pyqtgraph',
      #                  'pymysql',
      #                  'selenium'],
      test_suite='nose.collector',
      test_require=['nose']
      )
