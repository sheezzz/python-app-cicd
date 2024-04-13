# Makefile for linting

.PHONY: lint setup

setup:
	sudo apt-get update
	sudo apt-get install -y python3-pip python3-venv
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

linting:
	. venv/bin/activate && \
	isort --check-only app.py test_app.py && \
	black --check app.py test_app.py && \
	flake8 app.py test_app.py && \
	pylint app.py test_app.py

unit-test:
	. venv/bin/activate && \
	python3 -m unittest test_app.py
