all: init experiment docs

experiment:
	./experiment.sh experiment_1.py

init:
	pip install -r requirements.txt
	cd data; ./analyze.py; ./reference.py

docs:
	./docs.py > index.md
