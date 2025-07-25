install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=app --cov=utils tests/test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C *.py utils/*.py tests/*.py

#container-lint:
#	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

deploy:
	echo "deploy not implemented"

build:
	pyinstaller --name App --onefile --windowed --icon=assets/logo.ico app.py

all: install lint test format