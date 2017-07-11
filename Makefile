all: init
	./experiment.sh experiment_1.py

init:
	cd data; ./analyze.py; ./reference.py
