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
Flask

```
Installing flask
pip install -r E:/machine_learning_project_/requirements.txt

```
creating app.py file
writing code :
from crypt import methods
from flask import Flask

app= Flask(__name__)

@app.route("/", methods=['GET','POST']) 
def index():
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)

```
app deployoment
python app.py
```

