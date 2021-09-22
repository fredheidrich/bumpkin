
@echo off

if exist update_requirements.bat (
 echo ERROR: please run this from the project root
 exit /b 1
)

pip-compile --output-file=requirements.txt dev/requirements.in
pip-compile --output-file=dev/requirements-dev.txt dev/requirements-dev.in
