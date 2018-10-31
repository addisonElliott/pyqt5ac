import os

from setuptools import setup

from pyqt5ac import __version__

currentPath = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(currentPath, 'README.md'), 'r') as f:
    longDescription = f.read()

longDescription = '\n' + longDescription

setup(name='pyqt5ac',
      version=__version__,
      description='Python module to automatically compile UI and RC files in PyQt5 to Python files',
      long_description=longDescription,
      long_description_content_type='text/markdown',
      author='Addison Elliott',
      author_email='addison.elliott@gmail.com',
      url='https://github.com/addisonElliott/pyqt5ac',
      license='MIT License',
      install_requires=['click', 'pyyaml'],
      python_requires='>=3',
      py_modules=['pyqt5ac'],
      entry_points={
          'console_scripts': ['pyqt5ac = pyqt5ac:main']
      },
      keywords='pyqt pyqt5 qt qt5 qt auto compile generate ui rc pyuic5 pyrcc5 resource designer creator automatic',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      project_urls={
          'Source': 'https://github.com/addisonElliott/pyqt5ac',
          'Tracker': 'https://github.com/addisonElliott/pyqt5ac/issues',
      }
      )
