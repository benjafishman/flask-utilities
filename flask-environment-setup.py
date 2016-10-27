#!/usr/local/bin/python3

########
#
# A Script to aid in setting up an environemnt for a flask project
# 1. create root directory of project (shoudl be the project name)
# 2. setup a new virtualenv for the project
# 3. create a local git repo and .gitignore for project

import subprocess
import os

def run_cmd(cmd):
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	process.wait()
	print(process.returncode)

# create root directory for project
root_dir_name = input("What is the project name (root directory): ")

if not os.path.exists(root_dir_name):
    os.makedirs(root_dir_name)

# cd into project directory
dname = os.path.dirname(os.path.realpath(__file__)) + '/' + root_dir_name
os.chdir(dname)

# setup virtualenwrapper for project
venv_name = input("What is the virtual environment name: ")

export_venv_cmd = 'export WORKON_HOME=~/Envs'
run_cmd(export_venv_cmd)

# create the virtual env
venv_cmd = 'source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv ' + venv_name
run_cmd(venv_cmd)

# setup version control with git
git_cmd = 'git init'
run_cmd(git_cmd)

# create git ignore file
file = open(".gitignore", "w")
file.writelines(['*.pyc\n', 'instance/\n'])
file.close()
