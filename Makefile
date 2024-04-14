# Makefile for linting and unit-test

SHELL := /bin/bash

.PHONY: linting setup unit-test

setup:
	apt-get update && apt-get install -y --no-install-recommends gcc
	#apt-get install -y python3-pip python3-venv
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

linting:
	. venv/bin/activate && \
	isort --check-only app.py test_app.py && \
	black --check app.py test_app.py && \
	flake8 app.py test_app.py && \
	pylint app.py test_app.py

unit-test:
	source /opt/venv/bin/activate && \
	python3 -m unittest test_app.py
