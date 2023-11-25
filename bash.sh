#!/bin/bash


pip install django==4.2.6
pip show django
pip install spleeter
git clone https://github.com/chaitragurjar/SoftwareLabProject.git
cd SoftwareLabProject/src
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
