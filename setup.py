# setup.py
from setuptools import setup, find_packages

version = '0.0.1'

setup(name='meals',
      version=version,
      description='Meal Planner',
      install_requires=['cherrypy', 'routes', 'sqlalchemy', 'mysql-python', 'python-dateutil', 'beautifulsoup4', 'lxml',
                        'requests', 'nltk', 'numpy', 'pyparsing'],
      packages=find_packages(),
      py_modules=['meals',],
      include_package_data=True,
      zip_safe=False,
)
