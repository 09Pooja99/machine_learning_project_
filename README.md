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
send changes to github

```
git add .
git commit -m "sending docker files to github"
git push origin main

```
FINAL DEPLOYMENT

Creating a folder : .github
creating a folder inside .github folder : workflows
creating a file inside workflows : main.yaml

```
# Your workflow name.
name: Deploy to heroku.

# Run workflow on every push to main branch.
on:
  push:
    branches: [main]

# Your workflows jobs.
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Check-out your repository.
      - name: Checkout
        uses: actions/checkout@v2


### ⬇ IMPORTANT PART ⬇ ###

      - name: Build, Push and Release a Docker container to Heroku. # Your custom step name
        uses: gonuit/heroku-docker-deploy@v1.3.3 # GitHub action name (leave it as it is).
        with:
          # Below you must provide variables for your Heroku app.

          # The email address associated with your Heroku account.
          # If you don't want to use repository secrets (which is recommended) you can do:
          # email: my.email@example.com
          email: ${{ secrets.HEROKU_EMAIL }}
          
          # Heroku API key associated with provided user's email.
          # Api Key is available under your Heroku account settings.
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          
          # Name of the heroku application to which the build is to be sent.
          heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}

          # (Optional, default: "./")
          # Dockerfile directory.
          # For example, if you have a Dockerfile in the root of your project, leave it as follows:
          dockerfile_directory: ./

          # (Optional, default: "Dockerfile")
          # Dockerfile name.
          dockerfile_name: Dockerfile

          # (Optional, default: "")
          # Additional options of docker build command.
          docker_options: "--no-cache"

          # (Optional, default: "web")
          # Select the process type for which you want the docker container to be uploaded.
          # By default, this argument is set to "web".
          # For more information look at https://devcenter.heroku.com/articles/process-model
          process_type: web
          
   
          
### ⬆ IMPORTANT PART ⬆ ###
```

DEPLOYMENT WITH GITHUB
from github action build 
once completed deployment started ,after , open app from heroku
deployment done: app  on internet




CREATE STRUCTURE FOR ML PROJECT

creating folder : housing

creating file inside housing : __init__.py file

creating file : setup.py

```
from setuptools import setup
from typing import List

#Declarig variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Pooja Pandey"
DESCRIPTION="This is a first FSDS Machine Leaning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"




def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in 
    requirements.txt file

    return this function is going to return a list which contain name of libraries
    mentioned in the requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = [req.strip() for req in requirement_file.readlines() if req.strip() and req.strip() != "-e ."]
        return requirements




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())
```

adding more libraries to requirements.txt file:
```
numpy
Flask
gunicorn
scikit-learn
pandas
-e .
```
>note : -e . : if run pip install -r requirements.txt,
along with all other libraries it will also going to search for all the packages (housing) created in the current directory


To check the code running from setup.py file 

```
python setup.py install
```
or 
```
pip install -r requirements.txt
```
CREATE DIRECTORY STRUCTURE OF ML PROJECT

Inside housing package create following package(serialwise)
housing 
       __init__.py
       logger               
               __init__.py
       exception
               __init__.py
       pipeline
               __init__.py
       component
               __init__.py
       config
               __init__.py
       entity
               __init__.py

>note : by creating special file  __init__.py file in any directory , it indicate that directory should be treated as package.

write code for logger __init__.py file

```
import logging
from datetime import datetime
import os

LOG_DIR="housing_logs"

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH =os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig (
filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)
```

Validating logger code : app.py

```
from crypt import methods
from flask import Flask
**from housing.logger import logging**

app= Flask(__name__)

@app.route("/", methods=['GET','POST']) 
def index():
   ** logging.info("We are testing logging module")**
    return "Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)
```
write code for Exception __init__.py file

```
import os
import sys

class HousingException(Exception):
    def __init__(self, error_messege: Exception, error_detail: sys):
        super().__init__(error_messege)
        self.error_messege = HousingException.get_detailed_error_messege(
            error_messege=error_messege,
            error_detail=error_detail,  # Consistent naming
        )

    @staticmethod
    def get_detailed_error_messege(error_messege: Exception, error_detail: sys) -> str:
        _, _, exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_lineno  # Get the line number where the exception occurred
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_messege = (
            f"Error occurred in script: [{file_name}] at line number: [{line_number}] "
            f"error message: [{error_messege}]"
        )
        return error_messege

    def __str__(self):
        return self.error_messege

    def __repr__(self) -> str:
        return f"{HousingException.__name__}({self.error_messege})"

```
Testing exception handling : app.py(flask)

```
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app= Flask(__name__)

@app.route("/", methods=['GET','POST']) 
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        raise HousingException(e,sys)
        logging.info(housing.error_messege)
        logging.info("We are testing logging module")
    return "Machine Learning Project"

if __name__== "__main__":
    app.run(debug=False)
```
Run Debugging while staying on the app.py page and add the breakpoint at the line number where it was detected in the exception log

Create pipeline component: .py files
1. Data Ingestion 
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation
6. Model Pusher

create pipeline.py file in pipeline directory

now, in entity component folder, create config_entity.py file

Create folder : notebook, to keep ipynb file
create eample.ipynb file inside this 

activate current environment 
```
conda activate E:\machine_learning_project_\venv
```
Install ipynb

```
pip install ipykernel
```

Configuration info must use namedtuple as it cannot be alterable as configurtion should not be altered

write config_entity.py in entity directory
```
from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig =namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig= namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                 "transformed_train_dir",
                                                                 "transformed_test_dir",
                                                                 "preprocessed_object_file_path"])

ModelTrainerConfig= namedtuple("ModelTrainerConfig", ["trained_model_file_path", "base_ccuracy"])

ModelEvaluationConfig= namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

ModelPusherConfig= namedtuple("ModelPusherConfig", ["export_dir_path"])

```

create  folder in machine_learning_project  named as config, inside it create config.yaml file

```
training_pipeline_config:
  pipeline_name: housing
  artifact_dir: artifact

data_ingestion_config:
  dataset_download_url: https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz
  raw_data_dir: raw_data
  tgz_download_dir: tgz_data
  ingested_dir: ingested_data
  ingested_train_dir: train
  ingested_test_dir: test 




data_validation_config:
  schema_dir: config
  schema_file_name: schema.yaml
  report_file_name: report.json
  report_page_file_name: report.html

data_transformation_config:
  add_bedroom_per_room: true
  transformed_dir: transformed_data
  transformed_train_dir: train
  transformed_test_dir: test
  preprocessing_dir: preprocessed
  preprocessed_object_file_name: preprocessed.pkl
  
model_trainer_config:
  trained_model_dir: trained_model
  model_file_name: model.pkl
  base_accuracy: 0.6
  model_config_dir: config
  model_config_file_name: model.yaml


model_evaluation_config:
  model_evaluation_file_name: model_evaluation.yaml
  

model_pusher_config:
  model_export_dir: saved_models
```





WRITE in housing\config\configuration.py file to connect config.yaml and config_entity.py file to read info and send configurations to the pipeline 

```
from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig

from housing.util.util import read_yaml_file

from housing.constant import *



class Configuration:
    def __init__(self)-> None:
        pass

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        pass

    def get_data_validation_config(self)-> DataValidationConfig:
        pass

    def get_data_transformation_config(self)-> DataTransformationConfig:
        pass

    def get_model_trainer_config(self)-> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)-> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)-> TrainingPipelineConfig:
        pass
```

install python supported yaml file 
```
pip install PyYAML

```

create a folder util inside housing folder , and create util.py and __ini__.py file inside util 

write code to read yaml file in util.py file
```
import yaml
from housing.exception import HousingException
import os, sys


def read_yaml_file(file_path:str)->dict:
    """read a yaml file and returns the contents as dictionary.
    file_path:str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e
```

create folder inside housing : constant
and create __init__.py file inside and write code to define a path for yaml file to read and connect it with configuration.py file by calling ROOT_DIR there.

```
import os
from datetime import datetime

#to get current working directory
ROOT_DIR =os.getcwd() 
CONFIG_DIR= "config"
CONFIG_FILE_NAME ="config.yaml"

CONFIG_FILE_PATH =os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP =f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

```