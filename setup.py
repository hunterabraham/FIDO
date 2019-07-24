from setuptools import setup


def readme():
    with open('README') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as req:
        return req.read()


setup(name='FIDOControl',
      version='0.0.1',
      description='Controls FIDO\'s motion',
      long_description=readme(),
      url='None',
      author='Hunter Abraham',
      author_email='hjabraham@wisc.edu',
      license='MIT',
      packages=['FIDOControl'],
      install_requires=[],
      zip_safe=False,
      )
