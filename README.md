# pyqt5ac (PyQt5 Auto Compiler)
Automatically compile UI and RC files in PyQt5 to Python files

.. image:: https://img.shields.io/pypi/pyversions/polarTransform.svg
    :target: https://img.shields.io/pypi/pyversions/polarTransform.svg
    :alt: Python version

.. image:: https://badge.fury.io/py/polarTransform.svg
    :target: https://badge.fury.io/py/polarTransform
    :alt: PyPi version

|

Introduction
=================
pyqt5ac is a Python package for automatically compiling Qt's UI and QRC files into Python files.

[Qt](https://www.qt.io/) Designer is an application apart of Qt's suite of tools that allows one to create a GUI using a drag-and-drop interface. The user interface for a window/widget/dialog is stored in a *.ui* file and any resources such as images or icons are stored in a *.qrc* file.

These two filetypes must be compiled into Python files before they can be used in your Python program using PyQt5. There are a few ways to go about this currently:
1. Manually compile the files using the command line and pyuic5 for *.ui* files and pyrcc for *.qrc* files.
2. Compile the files each time the application is started up by calling pyuic5 and pyrcc5 within your Python script

The downside to the first method is that it can be a tedious endeavor to compile the files, especially when one is faced with a larger project with many of these files that need to be compiled.

Although the second method eliminates the tediousness of compilation, these files are compiled **every** time you run your script, regardless of if anything has been changed. This can cause a hit in performance and take longer to startup your script.

Enter *pyqt5ac*! This command-line interface (CLI) given a set of parameters will search through your files and automatically compile any *.ui* or *.qrc* files. In addition, pyqt5ac can be called from your Python script. In both instances, **ui and resource files are only compiled if they have been updated**.

Installing
=================
Installing pyqt5ac
-------------------------
pyqt5ac is currently available on `PyPi <https://pypi.python.org/pypi/pyqt5ac/>`_. The simplest way to
install alone is using ``pip`` at a command line::

  pip install pyqt5ac

which installs the latest release.  To install the latest code from the repository (usually stable, but may have
undocumented changes or bugs)::

  pip install git+https://github.com/addisonElliott/pyqt5ac.git

For developers, you can clone the pyqt5ac repository and run the ``setup.py`` file. Use the following commands to get
a copy from GitHub and install all dependencies::

  git clone pip install git+https://github.com/addisonElliott/pyqt5ac.git
  cd pyqt5ac
  pip install .

or, for the last line, instead use::

  pip install -e .

to install in 'develop' or 'editable' mode, where changes can be made to the local working code and Python will use
the updated polarTransform code.

Running from Command Line
=================
XXX

Running from Python Script
=================
XXX

Example Configuration Files
=================
YAML
-----------------
```YAML
ioPaths:
  -
    - "D:/Users/addis/Documents/PythonProjects/PATS/gui/*.ui"
    - "%%DIRNAME%%/../generated/%%FILENAME%%_ui.py"
  -
    - "D:/Users/addis/Documents/PythonProjects/PATS/resources/*.qrc"
    - "D:/Users/addis/Documents/PythonProjects/PATS/generated/%%FILENAME_%%EXT%%.py"

rcc: pyrcc5
uic: pyuic5
uic_options: --from-imports
force: True
```

JSON
-----------------
```JSON
{
  "ioPaths": [
    ["D:/Users/addis/Documents/PythonProjects/PATS/gui/*.ui", "%%DIRNAME%%/../generated4/%%FILENAME%%_ui.py"]
  ],
  "rcc": "pyrcc5",
  "rcc_options": "",
  "uic": "pyuic5",
  "uic_options": "--from-imports",
  "force": true
}
```

License
=================
pyqt5ac has an MIT-based `license <https://github.com/addisonElliott/pyqt5ac/blob/master/LICENSE>`_.
