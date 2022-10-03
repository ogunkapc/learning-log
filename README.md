# learning Log

A leaning log written in Python's Django web framework.

***just a minor project to learn django***

<!-- GETTING STARTED -->
## Getting Started

The steps below consist of instructions to get this project up and running on your local system

### Prerequisites

This is a list of things you need to run the program and how to install them.

* pip

  ```sh
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

  ```sh
  python get-pip.py
  ```
  
* virtualenv

  ```sh
  pip install virtualenv
  ```

### Installation

Now you would want to install all the projects dependencies

1. Create and activate a virtual environment

    ```sh
    python3 -m virtualenv “your environment name”
    ```

    ```sh
    source <path to virtual environment folder just created>/bin/activate
    ```

    <p align="center">OR</p>

    ```sh
    <path to virtual environment folder just created>\Scripts\activate
    ```

2. Clone the repo

     ```sh
     git clone https://github.com/ogunkapc/learning-log.git
     ```

3. Install dependencies

     ```sh
     pip install -r requirements.txt
     ```

4. Generate Django secret key
    * Start up a python shell from the terminal using the code

       ```sh
       python3 manage.py shell
       ```

    * Inside the shell that opens in the terminal type the following:

       ```py
       from django.core.management.utils import get_random_secret_key
       print(get_random_secret_key())
       ```

    * Copy the generated output
5. Define your django secret key using the environment variable SECRET_KEY in a  .env file at the root of the project.

    ```py
    SECRET_KEY='generated secret'
    ```

6. Run the command `python3 manage.py migrate` to start up your database

7. Run the command `python3 manage.py runserver` to startup your server
