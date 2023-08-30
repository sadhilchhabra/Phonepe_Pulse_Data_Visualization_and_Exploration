# Phonepe_Pulse_Data_Visualization_and_Exploration

In this streamlit app users will be able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. The dashboard will provide valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making.

### Link : <a href="https://www.linkedin.com/posts/activity-7102573994251345922-Ycdn?utm_source=share&utm_medium=member_desktop">LinkedIn Post / Working Model Video</a>
<br/>

## Prerequisites
1. **Python** -- Programming Language
2. **plotly** -- Python Module that is used for data visualization and supports various graphs
3. **pandas** -- Python Library for Data Visualization
4. **streamlit** -- Python framework to rapidly build and share beautiful machine learning and data science web apps
5. **git.repo.base** -- Python Module that helps to clone the github Repository and the store the data locally
6. **mysql.connector** -- Python Library that enables Python programs to access MySQL databases
7. **json** -- Python Library that helps parse JSON into a Python dictionary/list, in short open JSON files using Python
8. **os** -- Python Module that provides functions for interacting with the operating system

<br/>
   
## Project Workflow
### Step 1 -- Installing and Importing the required Libraries
Firstly install all the required extensions/libraries/modules given above, if not installed
   
   > pip install (name of the library/module)

After installing the required libraries one need to import them in the program before one can use them.

   ```
   import streamlit as st
   import mysql.connector as sql
   from streamlit_option_menu import option_menu
   import pandas as pd
   import plotly.express as px
   import os
   import json
   ```
<br/>

### Step 2 -- Data Extraction - Cloning the GitHub Repository
Now one need to clone the GitHub Repository to fetch the data from the Phonepe pulse GitHub repository.

   ```
   from git.repo.base import Repo
   Repo.clone_from("Github Repository URL that need to be cloned", "Local URL where one need to clone there data")
   ```
<br/>

### Step 3 -- Data Tranformation - JSON to Pandas DataFrame
#### *Note : This step is performed in the .ipynb Python notebook that is in a Jupyter Notebook, because it is comparitively easy to visualize and tranform data in a .ipynb Python notebook as comapared to .py Python file. You can check the .ipynb notebook attached above for the code implementation of the process below.*

After the Data Extraction part is completed one need to transform the data. The data that was extracted from the Phonepe Pulse Repository is in form of .json file, now we need to transform that data into Pandas DataFrame, so that we can visualize the data more efficiently in the form of table and if there are any null values we can do Data cleaning to handle those null values. One more advantage of tranforming the data into Pandas DataFrame is that we can further visualize the data in the form of graphs using the Plotly module in Python.

Here, we go through each JSON file in each folder using a for loop to convert them into a DataFrame that the rest of the program can read and understand. Iteratively accessing each folder's json files, extracting the necessary key and value pairs, and then combining them into a dataframe. For this procedure, I relied on the os, json, and pandas packages. And then I saved the dataframe as a CSV file on my hard disk.

<br/>

### Step 4 -- Data Insertion - Inserting the Data into MySQL Database
#### *Note : You can check the .ipynb notebook attched above for the code implementation of the below process.*
After that one need to create a MySQL Database in there local system. Now below is the Python code to connect to that SQL Database.

  ```
  hostname = "your host name goes here"
  database = "your database name goes here"
  username = "your username goes here"
  pwd = "your password goes here"
  
  mydb = sql.connect(host=hostname, user=username, password=pwd, database=database)
                       
  cursor1 = mydb.cursor(buffered=True)
  ```
    
After the connection is successfully established one need to write the code to create the required tables with the required columns and insert the data that we have transformed in step-3 to the MySQL database. 

<br/>

### Step 5 -- To create a Streamlit Application 
#### *Note : You can check the .py file attched above for the code implementation of this streamlit Application.*
The result of this project is a live geo visualization streamlit dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. 

The data is stored in a MySQL database for efficient retrieval and the dashboard is dynamically updated to reflect the latest data. Users are able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. 

The dashboard provides valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making. 

Overall, the result of this project is a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository. 

The user-friendly interface is made with Streamlit, and the data is visualized using Plotly's in-built functionalities.

To Run the Application one can run the command mentioned below.

  > streamlit run main.py
