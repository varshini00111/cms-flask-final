# Article CMS (Flask + Azure)

This project is a simple Content Management System (CMS) built using Flask and deployed on Microsoft Azure. It allows users to create articles with a title, author, body, and an optional image.

The application is connected to:

* Azure SQL Database (for storing article data)
* Azure Blob Storage (for storing images)
* Azure App Service (for hosting the web app)

## Live Application

 https://cmsproject123-cjahawhmg6erbzcc.australiaeast-01.azurewebsites.net/

Create Article Page:
https://cmsproject123-cjahawhmg6erbzcc.australiaeast-01.azurewebsites.net/create

## Features

* Create articles (Title, Author, Content)
* Upload images for articles
* Store data in Azure SQL Database
* Store images in Azure Blob Storage
* Deployed using Azure App Service
* Secure configuration using environment variables

## Architecture

* Frontend: HTML (Flask templates)
* Backend: Flask (Python)
* Database: Azure SQL Database
* Storage: Azure Blob Storage
* Hosting: Azure App Service

## Technologies Used

* Python 3.10
* Flask
* pyodbc
* Azure Blob Storage SDK
* Gunicorn (for deployment)

## Project Structure

project/
│
├── app.py
├── requirements.txt
├── README.md
├── WRITEUP.md
├── startup.txt
└── templates/
    └── create.html

## Environment Variables (Azure Configuration)

The application uses environment variables configured in Azure App Service:

* SQL_SERVER
* SQL_DATABASE
* SQL_USER_NAME
* SQL_PASSWORD
* BLOB_CONNECTION_STRING
* BLOB_CONTAINER
* BLOB_ACCOUNT
* BLOB_STORAGE_KEY
* SECRET_KEY
* CLIENT_ID
* CLIENT_SECRET

## Database Structure

Table: 'articles'

| Column    | Type              |
| --------- | ----------------- |
| id        | INT (Primary Key) |
| title     | NVARCHAR(100)     |
| author    | NVARCHAR(100)     |
| body      | NVARCHAR(MAX)     |
| image_url | NVARCHAR(MAX)     |


## Azure Resources Used

* Azure Resource Group
* Azure SQL Server
* Azure SQL Database
* Azure Storage Account
* Azure App Service

## Screenshots (Submission Proof)

Add the following screenshots in your repository (recommended folder: `screenshots/`):

1. Resource Group (all resources visible)
2. SQL Database (articles table with data)
3. Storage Account (blob container and endpoint)
4. Application running in browser (with URL visible)
5. Create Article success screen

## Note
The application is successfully deployed on Azure and works as expected. It connects to Azure SQL Database and Blob Storage for storing data and images.

However, during testing, there were occasional connection timeout issues when accessing the database from the deployed web app. This is mainly due to Azure network and firewall settings, not because of any issue in the application code.

The database itself is working correctly, and all operations were verified using the Azure Query Editor.

Overall, the application logic and integration are functioning properly.
## 🎯 Conclusion

This project demonstrates how to build and deploy a full-stack web application using Flask and Azure services, including database integration, cloud storage, and web hosting.

Varshini
B.Tech AIML Student
