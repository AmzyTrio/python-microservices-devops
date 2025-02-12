# python-microservices-devops

[![Python application test with Github Actions](https://github.com/AmzyTrio/python-microservices-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/AmzyTrio/python-microservices-devops/actions/workflows/devops.yml)

#Scaffold
Code repo will have following structure:
Makefile
requirements.txt 
source code
Test
Dockerfile
IAC


Steps:
1) Create virtual python environment so as to have all python dependencies in one place
virtualenv ~/.venv
1.5) Add to bash to source this environment
vim ~/.bashrc
At the end , add "source ~/.venv/bin/activate"
Open new terminal, and you will see that it has the new env
2) Create empty files (through GUI or below commands)
touch requirements.txt
touch Dockerfile
touch Makefile
mkdir mylib
touch mylib/__init__.py
touch mylib/logic.py
touch main.py
touch test_logic.py
touch cli-fire.py
3) Populate Makefile (to articulate all the different things we need to do for our project)
    Populated all the dependecies in the requirements.txt file. Then within the make file within install wrote the below to install the dependencies.
    pip install -r requirements.txt
    make install (run this command to install)
    To freeze the dependency version numbers, use command 'pip freeze' to see the current versions and then update the requirements.txt file.
4) Setup continuous integration with auto installing dependencies, lint checks, formats, running tests etc.
5) Setup command line tool using python fire library. use ./cli-fire.py --help