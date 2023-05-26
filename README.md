# Chitter Project Starter

This is a starter project for you to use to start this project.


## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:tiagocollot/chitter_project.git chitter_project

# Or, if you don't have SSH keys set up
; git clone https://github.com/tiagocollot/chitter_project.git chitter_project
# Enter the directory
; cd chitter_project

# Install dependencies and set up the virtual environment
; pipenv install
; pipenv install pytest
; pipenv install playwright
; pipenv install flask
; pipenv install psycopg


# Activate the virtual environment
; pipenv shell

# Create the database
; createdb chitter_project

# Open lib/database_connection.py and change the database name to chitter_project
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py
```

<details>
  <summary>:confused: I see an error about `python_full_version`?</summary>

  <!-- OMITTED -->

  ---

  Your `pipenv` may be outdated and subject to a bug with newer `Pipfile`s.

  ```shell
  ; pipenv --version
  2022.9.24 # If you see something in September 2022, try this
  ; pip3 install "pipenv>=2022.11.5" -U
  # pip3 will update pipenv for you

  # Then try running `pipenv install` again
  ; pipenv install
  ```


