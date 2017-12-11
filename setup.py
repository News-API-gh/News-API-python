from setuptools import setup

setup(name='newsapi',
      version='0.0.1',
      description='News - API Python SDK ',
      url='https://github.com/Gabrock94/News-API-python',
      author='Giulio Gabrieli',
      author_email='gack94@gmail.com',
      license='MIT',
      packages=['newsapi'],      
      install_requires=[
            'os',
            'datetime',
            'requests'
      ],
      zip_safe=False)

