# B2U Backend
This is the backend of B2U.
## Requirements
 - Python 3.9

## Installation and Setup
To set up this Django backend project locally, follow these steps:

1. Clone the repository
    ```sh
    git clone https://github.com/wubeshetA/b2u-backend
    ```

2. Change into the project directory
    ```sh
    cd b2u-backend
    ```
3. Install pipenv dependecy management tool with the following command. This project
uses pipenv to create isolated virtual environement and manage third party packages.
    ```sh
    pip install pipenv
    ```
4. Activate the virtual environment:
    ```sh
    pipenv shell
    ```
5. Install the required dependencies (This depencendencies are listed in the Pipfile):
    ```sh
    pipenv install
    ```
6. Update the development settings at [./b2u/settings/dev.py](./b2u/settings/dev.py) file based on your local development configuration cessary database

7. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```
8. Start the development server:
    ```sh
    python manage.py runserver
    ```
    You can now access the Django backend at http://localhost:8000/
9. If you want to seed the database with some sample data, run the following command:
    ```sh
    python manage.py seed_db
    ```
10. Optional for VSCode user - If you are using VSCode as your IDE, you can select the virtual environment
    you just created as your python interpreter. This will enable you to use the virtual
    environment in your IDE. To do this, open the command palette (Ctrl+Shift+P) and type
    "Python: Select Interpreter" and select the virtual environment you just created.
    To see the path to the virtual environment, run the following command in the terminal and have a look at the path displayed.
    ```sh
    pipenv --venv
    ```


## Deployment

This project is deployed on Digital Ocean. You can access it at [https://b2u-backend.vercel.app/](https://b2u-backend.vercel.app/)

## Author

👤 [**Wubeshet Yimam**](https://github.com/wubeshetA)