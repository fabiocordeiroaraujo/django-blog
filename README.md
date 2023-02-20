# Project

Personal blog written with Python/Django

# Steps for run

01) mkvirtualenv blog-portfolio
02) pip3 install --upgrade pip
03) pip install --upgrade pip
04) pip3 install django 
05) pip3 install Markdown
06) pip3 install Pillow
07) pip3 install python-decouple
08) python manage.py makemigrations
09) python manage.py migrate
10) python manage.py collectstatic
11) python manage.py createsuperuser
    - user: admin
    - email: [your_email]
    - password: admin123456
12) sudo apt install gettext
13) python manage.py makemessages --locale=pt_br
14) python manage.py compilemessages
15) python manage.py runserver or python manage.py runserver 0.0.0.0:8000