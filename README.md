#   Python + MongoDB
This project shows how to connect to a MongoDB using Python
The idea is use CRUD and the other artifacts provided
The **init.py** file shows how to connect to DB using the Mongo Server

## Setup

1. Install **pymongo** using the following CLI command

        pip install pymongo

2. Go to your MongoDB **Project Overview** and look for **Data Explorer**.

    2.1. in the cluster looks for **Connect via..** option. 

    2.2. Click in **Drivers and Client libraries** 

    2.3. Language: Python, Client Library: PyMongo (Sync)

    2.4. Connection_String: copy the uri (some like this)

    mongodb+srv://**<db_username>**:**<db_password>**@cluster0.klll7qw.mongodb.net/
3. Go to your MongoDB **Project Overview** and look for **Security Quickstart**/ Username and Password.

    3.1. Write a Username and Password (or update)

    3.2. Click on **Create Uswer** buttom