# Makefile for linting

.PHONY: linting setup unit-test

setup:
	sudo apt-get update
	sudo apt-get install -y python3-pip python3-venv
	python3 -m venv /opt/venv
	. /opt/venv/bin/activate && pip install -r requirements.txt

linting:
	. /opt/venv/bin/activate && \
	isort --check-only app.py test_app.py && \
	black --check app.py test_app.py && \
	flake8 app.py test_app.py && \
	pylint app.py test_app.py

unit-test:
	. /opt/venv/bin/activate && \
	python -m unittest test_app.py
