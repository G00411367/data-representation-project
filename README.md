# Data Representation Project

Author: Ioan Domsa  
Student: G00411367  

This repository contains the project folder for a Flask server API project for the module Data Representation, Winter 2023/2024.

***

### Objective
Create a server application on Flask that has a RESTful API. The application links to database tables and throuh web pages performs CRUD operations on the data.

***

### The Repository

The GitHub repository contains the following files and folders:

1. A README file    
2. server.py        Flask server
3. productDAO.py    Data Access Object file that interacts with MySQL database
4. dbconfig.py      Config template for connecting with MySQL
5. productDB.sql    Script to create a database and tables
6. staticpages      Folder containg the HTML home page and images
7. requirements.txt Packages required to run the application

***

### Clonning the repository on a local machine

- open your terminal 
- navigate to location where you want to clone the repository
- clone the repository using git clone command on the command line:

git clone https://github.com/G00411367/data-representation-project.git

- navigate through the cloned directory

- create a virtual environment by typing :

python -m venv venv

- install required packages in the same directory unig pip install command :

pip install -r requirements.txt

***

### Initialize the database

- on MySQL workbench open productDB.sql from the clonned repository
- execute the script

***

### Running the application

on the command line type :

python server.py 

The web browser will open on the local host http://127.0.0.1:8080 




