# Birthday Tracker

Birthday Tracker is a Flask-based web application that allows users to keep track of birthdays. It provides features for user registration, login, and managing birthday records.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3
- Flask
- Flask_SQLAlchemy
- Flask_WTF
- Flask_Bcrypt
- Flask_Login
- WTForms

## Installation

1. Clone the repository:

  > git clone <repository-url>

  
2. Navigate to the project directory:

  >cd BirthdayTracker

  
3. Install the required dependencies:

  >pip install -r requirements.txt
 

## Configuration

1. Open the `__init__.py` file.

2. Set the `SECRET_KEY` to a secure random string.

3. Set the `SQLALCHEMY_DATABASE_URI` to the desired database connection URL.

## Usage

1. Run the following command to start the application:

  >python app.py
 
  
2. Open your web browser and navigate to `http://localhost:5000`.

3. Register a new account or log in with your existing credentials.

4. Add, view, and manage birthday records using the provided forms and interface.

## Files

The project consists of the following files:

- `app.py`: The main entry point of the application. It initializes the Flask app and runs it on the specified host and port.

- `__init__.py`: Initializes the Flask app and configures the necessary extensions, such as SQLAlchemy, Bcrypt, and LoginManager.

- `forms.py`: Contains the FlaskForm classes for the registration, login, and new entry forms. These forms define the fields, validators, and submit buttons for user input.

- `models.py`: Defines the database models for the User and Data tables using SQLAlchemy. It also includes the user loader function required by Flask-Login.

- `routes.py`: Contains the route definitions and view functions for handling requests. It includes routes for home, index, adding and deleting birthdays, registration, login, and logout.

## Contributing

Contributions to the Birthday Tracker project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.



  
