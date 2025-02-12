install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
lint:
	#pylint or flake8
test:
	#test
deploy:
	#deploy
all: install format lint test deploy