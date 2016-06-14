from setuptools import setup

setup(name='markov',
      version='0.1',
      description='Markov Process example in Python',
      url='http://github.com/finiteautomata/markov',
      author='Juan Manuel Perez',
      author_email='jmperez.85@gmail.com',
      license='MIT',
      install_requires=[
          'numpy',
      ],
      test_suite="tests",
      packages=['markov'],
      zip_safe=False)