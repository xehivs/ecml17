#!/usr/bin/env python
# This script calculates effectiveness of all reference algorithms wrapped from
# skl and saves them to reference.csv.

from weles import *  # to analyze with ksskml
from ece import *
import numpy as np
import os  # to list files
import re  # to use regex
import csv  # to save some output
from scipy import stats

PBORDER = 0.15
def areIndependent(a, b, border = PBORDER):
    if a is None or b is None:
        return False
    test = stats.ttest_ind(a, b)
    return test.pvalue > border

# Gather all the datafiles
directory = 'datasets/'
files = [(directory + x, x[:-4]) for \
    x in os.listdir(directory) \
    if re.match('^([a-zA-Z0-9])+\.csv$', x)]

# Iterate datafiles
with open('reference.csv', 'wb') as csvfile:
    with open('hreference.csv', 'wb') as hcsvfile:
        writer = csv.writer(csvfile, delimiter=',')
        hwriter = csv.writer(hcsvfile, delimiter=',')
        # write header
        header = ['dataset', 'knnacc', 'knnbac', 'gnbacc', 'gnbbac', 'dtcacc', 'dtcbac', 'mlpacc', 'mlpbac', 'svcacc', 'svcbac']
        writer.writerow(header)
        hwriter.writerow(header)
        for file in files:
            # load dataset
            dataset = Dataset(file[0])
            print dataset

            # initialize classifiers
            classifiers = [
                sklKNN,
                sklGNB,
                sklDTC,
                sklMLP,
                sklSVC
            ]

            # and save output
            row = [dataset.db_name]
            hrow = [dataset.db_name]

            # independence
            independenceEntries = []
            resultEntries = []
            for classifier in classifiers:
                results = classifier(dataset).quickLoop()
                print '\t - %s - acc = %.3f, bac = %.3f' % (
                    classifier.name(), results['acc'], results['bac']
                )
                independenceEntries.append(results['wbac'])
                resultEntries.append((results['acc'], results['bac']))
                row.extend([results['acc'], results['bac']])

            # analysis
            meanValues = [np.mean(x) if x is not None else 0 for x in independenceEntries]
            bestValue = max(meanValues)
            bestIdx = meanValues.index(bestValue)

            independence = [areIndependent(x, independenceEntries[bestIdx]) for x in independenceEntries]
            print '%i values are marked as best, with mean %.3f' % (sum(independence), bestValue)
            for i, isIndependent in enumerate(independence):
                result = resultEntries[i]
                hrow.extend(['%s \\oldstylenums{%.3f}' % ('\\color{red!75!black}' if isIndependent else '', result[0])])
                if np.isnan(result[1]):
                    hrow.append('\\tiny NaN')
                else:
                    hrow.extend(['%s \\oldstylenums{%.3f}' % ('\\color{red!75!black}' if isIndependent else '', result[1])])

            writer.writerow(row)
            hwriter.writerow(hrow)
