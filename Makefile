all:
	./experiment.sh experiment_1.py
	./docs.py > README.md

init:
	cd data; ./analyze.py; ./reference.py
