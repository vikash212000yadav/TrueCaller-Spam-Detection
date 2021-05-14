# TrueCaller REST API
<hr>
A REST API which is somewhat similar to TrueCaller with spam detection.

### Steps to install and run in local system:-
<hr>

- Create a virtual environment ```python3 -m venv <env_name>```
- Activate virtual environment ```source <env_name>/bin/activate```
- Install requirements in venv ```pip install -r requirements.txt```
- Make migrations ```python manage.py makemigrations truecallerapi```
- Apply migrations ```python manage.py migrate```
- Createsuperuser ```python manage.py createsuperuser```
- Run the server ```python manage.py runserver```

## Login Credentials:
<hr>

- Username: ```admin```
- Password: ```root```