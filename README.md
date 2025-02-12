# python-microservices-devops

Scaffold
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
3) Populate Makefile ( to articulate all the different things we need to do for our project)