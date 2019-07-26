# Project-Shush

## 1. Before setup

1. Install python3 on your operating system
2. `git clone git@github.com:Plech12/Project-Shush.git /home/$USER/projects/shush`

## 2. One-time commands for setting up python environment

1. `mkdir /home/$USER/python_env`
2. `cd /home/$USER/python_env`
3. `python3 -m venv shush_env`

## 3. Commands to run every time before starting work

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`

## 4. Commands to run project

1. `python src/shush.py`

## 5. Installing python libs

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`
3. `pip install lib_name`
4. `pip freeze > requirements.txt`

## 6. Updating python environment with newly installed libs

1. `source /home/$USER/python_env/shush_env/bin/activate`
2. `cd /home/$USER/projects/shush`
3. `pip install -r requirements.txt`
