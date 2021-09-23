
@echo off

del /q dist\*

rem pure python wheel
python setup.py sdist bdist_wheel