# djanjo-initiate
Automate creating of .gitignore and local_settings when creating a new django project

## Usage
The script takes an argument which is the name of the django project. It has to be executed from inside the same directory as 
manage.py. You can also just copy the script that directory and run without any arguments. It will still run fine.
* if script is located in some folder and executing from django project folder *
`python /path/to/file/generate.py <django-project-name>` 

* if script is located in the django project folder *
`python generate.py ` 
