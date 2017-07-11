#!/usr/bin/env python
import numpy as np
import pytablewriter

# Abstract
print '# Abstract'
print '> Recently, the problem of imbalanced data is the focus of intense research of machine learning community. Following work tries to utilize an approach of transforming the data space into another where classification task may become easier. Paper contains a proposition of a tool, based on a photographic metaphor to build a classifier ensemble, combined with a random subspace approach. It is a naturally naive parallel, insensitive to a sample size, robust to dimension increase, which allows a regularization of feature space, to reduce the impact of biased classes. The proposed approach was evaluated on the basis of the computer experiments carried out on the benchmark datasets.\n'

datasets = ['syntetic5f', 'syntetic10f', 'syntetic20f']

tables = ['csv/experiment_1_syntetic5f.csv', 'csv/experiment_1_syntetic10f.csv']

for dataset in datasets:
    csvArray = np.genfromtxt('csv/experiment_1_%s.csv' % dataset, delimiter=',')
    print '# `%s`\n' % dataset

    writer = pytablewriter.MarkdownTableWriter()
    writer.header_list = csvArray[0,:].tolist()
    writer.value_matrix = csvArray[1:,:].tolist()
    writer.header_list[0] = "."

    writer.write_table()
