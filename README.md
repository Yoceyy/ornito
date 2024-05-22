
# Installation de Python sur LINUX :

Command : 

sudo apt update

sudo apt install python 3.12

python3 --version

# Installation d'environement sur LINUX :
- Pour creer votre dossier d'environement avec le bin etc....

python3 -m venv testhumoov  

- Pour acceder a votre dossier

cd testhumoov/   

 - Pour activer votre environement 

source bin/activate  

- Installation de Django

pip install django  

# Creation du projet src 

django-startproject nomduprojet


# Migrate 

- python3 manage.py migrate

# Creation coté admin 

- python3 manage.py creatsuperuser


# Demmarage de l'environement

- python3 manage.py runserver


