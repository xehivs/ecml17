all: init experiment docs

experiment:
	./experiment.sh experiment_1.py

init:
	cd data; ./analyze.py; ./reference.py

docs:
	./docs.py > index.md
