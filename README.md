# Project-Shush

## 1. One-time commands for setting up python environment

1. Install python3 on your operating system
2. `git clone git@github.com:Plech12/Project-Shush.git /home/$USER/projects/shush`
3. `mkdir /home/$USER/python_env`
4. `cd /home/$USER/python_env`
5. `python3 -m venv shush_env`
6. `source /home/$USER/python_env/shush_env/bin/activate`
7. `cd /home/$USER/projects/shush`
8. `pip install --upgrade pip`
9. `pip install -r requirements.txt`

## 2. Commands to run every time before starting work

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`
3. `code .` -- to open Visual Studio Code

## 3. Commands to run project

1. `python src/shush.py`

## 4. Installing python libs

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`
3. `pip install lib_name`
4. `pip freeze > requirements.txt`

## 5. Updating python environment with newly installed libs

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`
3. `pip install -r requirements.txt`
