SRC_PATH=./src
TEST_PATH=./test
APP_PATH=./src/

ensure-pip:
	pip install --user --upgrade pipenv pip
	pip --version
	pipenv --version

install:
	pipenv --python 3.7.1 install --dev

clean:
	pipenv --rm

lint:
	pipenv run pycodestyle --show-source --show-pep8 ./

precommit: lint test

start:
	$(source ./env.sh) 
	cd src
	pipenv run gunicorn app:app --reload

verify:
	pipenv run pytest test/test*.py