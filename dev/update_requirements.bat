
@echo

rem todo/fred: check if we run this from the root of the repo, otherwise error out

pip-compile --output-file=requirements.txt dev/requirements.in
pip-compile --output-file=dev/requirements-dev.txt dev/requirements-dev.in
