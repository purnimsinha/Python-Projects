# Introduction
this project is based on python flask frame work which is used to manage the events organised on school and colleges
Follow the given steps to run this application

# How to run ?
Step 1: Backend Hosting : https://remotemysql.com/ (Free public mysql hosting) or you can also install local mysql
Create the tables using .sql file inside the github Repo and Note Down the credentials given in the database<br />

Step 2: First Install the dependencies using pip install -r requirements.txt<br>
Run it : python app.py

Note : Dont forget to change the connection string to app.py<br/>
<h2>Heroku Part</h2>
Create a Procfile and add the gurnicorn run command (web: gunicorn app:app) make sure ( pip install gunicorn ) should be present in the local requirements.txt file<br/>
Push the Repo to github and login with heroku <br>
Create one app with Unique Name and Select Github and connect a particular respository with it that you want to deploy<br>

<h4>Easy Way </h4>
Click on the deploy to heroku button below and fill the details. Deployement process will start.<br>


# Deploy
<a href="https://heroku.com/deploy?template=https://github.com/purnimsinha/event-managemnt-sytem-flask-python.git">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
<br><p>HAPPY CODING</p>
