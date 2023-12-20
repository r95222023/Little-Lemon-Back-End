# Little Lemon Restaurant Back End

This marks the culmination of the Meta Back-End Developer Course on Coursera, showcasing a Django web application
tailored for the Little Lemon restaurant. For Front-End counter part, check out [Little Lemon Front-End](https://github.com/r95222023/Little-Lemon-Front-End)

## Framework
This project was initialized using Django and incorporates djangorestframework with Simple-JWT for authentication.

## Features

- Utilizes the Django framework to deliver static HTML content
- JWT (JSON Web Token) authentication is implemented
- Establishes a connection between the backend and a MySQL database
- Incorporates APIs for both menu functionality and table reservations
- Configured with user registration and authentication features
- Includes a suite of unit tests
- The API is testable using the Insomnia REST client

## Packages Used

- django
- mysqlclient
- django-cors-headers
- djangorestframework-simplejwt

## Setup

To use this application, follow these steps:

1. Clone the repository from GitHub.

    ```bash
    git clone https://github.com/r95222023/Little-Lemon-Back-End.git
    ```
   <br>
2. Install the necessary dependencies within the virtual environment and then activate the virtual environment.
    ```bash
    pipenv install
    ```
    ```bash
    pipenv shell
    ```
   <br>
3. Establish a MySQL database and configure the application to utilize it.
   In the settings.py file, modify the default database settings to:

   ```jsx
   DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'littlelemon',
            'HOST': 'localhost',
            'PORT': '3306',
            'USER': '[your username]',
            'PASSWORD': '[your password]',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        },
   }
   ```
   Important: 
   - Use the username and password of the MySql superuser as your credentials in the **settings.py** file.
   - The 'django.db.backends.mysql' engine is incompatible with ARM-based machines. Please install
   mysql-connector-python using either pip or pipenv. Alternatively, if you are utilizing the mysqlclient connector,
   uncomment the **'django.db.backends.mysql'** line in the **settings.py** file, and comment out the line below it to
   successfully establish a database connection.  

   <br>
4. Apply the migrations.
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```

## Usage

1. To initiate the server, use the following command:
   ```bash
   python manage.py runserver
   ```
2. For code testing, execute the following command:
   

## Testing

For code testing, execute the following command:
```bash
   python manage.py test
```
The API can also be tested using the Insomnia REST client or other tools.

## API endpoints


| Description           | Method | Path                    | Example                                                                                  | Form/JSON payload                                                        |
|-----------------------|--------|-------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Load static home page | GET    | ```/```                 |                                                                                          |                                                                          |
| View menu items       | GET    | ```/menu/```            |                                                                                          |                                                                          |
| View single menu item | GET    | ```/menu/<id>```        |                                                                                          |                                                                          |
| Obtain authtoken      | POST   | ```/api/token/``` |                                                                                          | {    "username": "mario",    "password": "mariospassword"}                      |
| View table bookings   | GET    | ```/booking/tables```   |                                                                                          |


