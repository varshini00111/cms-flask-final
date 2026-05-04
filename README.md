# Article CMS (Flask + Azure)

This project is a simple Content Management System (CMS) built using Flask and deployed on Microsoft Azure. It allows users to create articles with a title, author, body, and an optional image.

---

## Azure Services Used

* Azure SQL Database (stores article data)
* Azure Blob Storage (stores images)
* Azure App Service (hosts the web application)

----

## Live Application

**Home Page:**
https://cmsproject123-cjahawhmg6erbzcc.australiaeast-01.azurewebsites.net/

**Login Page:**
https://cmsproject123-cjahawhmg6erbzcc.australiaeast-01.azurewebsites.net/login

**Create Article Page:**
https://cmsproject123-cjahawhmg6erbzcc.australiaeast-01.azurewebsites.net/create

## Features

* Create articles (Title, Author, Content)
* Upload images for articles
* Store data in Azure SQL Database
* Store images in Azure Blob Storage
* Deployed using Azure App Service
* Secure configuration using environment variables
* Login system with logging

## Authentication & Logging

This application includes a simple login system for demonstration and logging purposes.

### Login Credentials:

* Username: `admin`
* Password: `pass`

### Logging:

The application logs:

* Successful login attempts
* Failed login attempts

Logs can be viewed in **Azure App Service → Log Stream**.

### Example Log Output:

```
Invalid login attempt
admin logged in successfully
```

Screenshots showing both successful and failed login attempts are included in this repository.


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
* Gunicorn


## Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── README.md
├── WRITEUP.md
├── startup.txt
└── templates/
    └── create.html
```

## Environment Variables

Configured in Azure App Service:

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

Table: `articles`

| Column    | Type              |
| --------- | ----------------- |
| id        | INT (Primary Key) |
| title     | NVARCHAR(100)     |
| author    | NVARCHAR(100)     |
| body      | NVARCHAR(MAX)     |
| image_url | NVARCHAR(MAX)     |


## Screenshots (Submission Proof)

Screenshots are available in the `screenshots/` folder:

1. Resource Group – All Azure resources
2. SQL Database – Articles table with data
3. Blob Storage – Container and uploaded images
4. App Running – Application URL in browser
5. Create Article – Successful article creation
6. Login Logs – Successful and failed login attempts


## Note

The application is successfully deployed on Azure and works as expected. It connects to Azure SQL Database and Blob Storage for storing data and images.

During testing, occasional database connection timeouts were observed due to Azure network/firewall configuration, not due to application logic.

All database operations were verified using Azure Query Editor.


## Conclusion

This project demonstrates how to build and deploy a full-stack web application using Flask and Azure services, including database integration, cloud storage, authentication logging, and web hosting.
