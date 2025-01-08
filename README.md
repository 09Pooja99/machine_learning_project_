# machine_learning_project_
This is first machine learning project

### software and account requirement.

1.[git cli](https://git-scm.com/downloads)

2.[github account](https://github.com/)

3.[cloud account](https://aws.amazon.com/events/apj/aws-lift/?gclid=CjwKCAiA1eO7BhATEiwAm0Ee-E3diNUBsJatGLKscks4IWHoAzu3M5P-DJHktAdHnpguW7NhwQeySBoClyIQAvD_BwE&trk=fb8718a7-d9f7-4e07-9fc5-b85de26b4178&sc_channel=ps&ef_id=CjwKCAiA1eO7BhATEiwAm0Ee-E3diNUBsJatGLKscks4IWHoAzu3M5P-DJHktAdHnpguW7NhwQeySBoClyIQAvD_BwE:G:s&s_kwcid=AL!4422!3!476942607298!e!!g!!aws%20cloud!11542865500!116152063887)

4.[vs code account](https://code.visualstudio.com/download)

5.[terminal](https://learn.microsoft.com/en-us/windows/terminal/install)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate E:/machine_learning_project_/venv
```
creating requirements.txt file
1. Flask


Installing requirements : flask
```
pip install -r E:/machine_learning_project_/requirements.txt

```
creating app.py file
code to create app :
```
from crypt import methods
from flask import Flask

app= Flask(__name__)

@app.route("/", methods=['GET','POST']) 
def index():
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)

```

```
python app.py
```

To add files to git 
```
git add .
```
or 
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
 To check all version maintained by git
 ```
git log
```
To create version/commit all changes by git
```
git commit -m "messege"

```
To send version/changes to github
```
git push origin main

```
To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = poojaapaandey9@gmail.com
2. HEROKU_API_KEY = HRKU-0197c56d-3222-4875-8417-83f9da674fb3
3. HEROKU_APP_NAME =

Adding gunicorn in requirements.txt 

Creating Dockerfile 
```
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
```

 Creating .dockerignore file (venv/,  .git, .gitignore)

BUID DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

>Note: Image name for docker must be lowercase, (tagename=latest)

To build docker image 
```
latest .
```

To list docker image
```
docker images
```

To run docker image 
docker run <port_number> -e <env_number> <image_id>
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
To check running container in docker
```
docker ps
```
To stop the docker container

```
docker stop <container_id>
```
