SHELL := /bin/bash

env-setup:
	rm -rf venv
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt


run-local:
	source venv/bin/activate; \
	export CONFIG_PATH=common/configs/local.cfg; \
	pip install -r requirements.txt; \
	python manage.py makemigrations; \
	python manage.py migrate; \
	python manage.py runserver 8000


run-local1:
	source venv/bin/activate; \
	pip install -r requirements.txt; \
	python manage.py makemigrations; \
	python manage.py migrate; \
	python manage.py runserver 8000
