# -*- coding: utf-8 -*-
import sys
import weles
import hssa
import json
import bson
import pymongo as pm
import numpy as np
import itertools
from scipy import stats
import hashlib
import os
from operator import itemgetter
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd

PBORDER = 0.15

# You need to define connection to MongoDB to store results
MONGO_URI = os.environ['RESULTS_URI']
MONGO_DB = os.environ['RESULTS_DB']
MONGO_TABLE = os.environ['RESULTS_TABLE']

class Experiment(object):
    '''
    # Initializer
    '''
    def __init__(self, subject = 'NONE', revision = '', datasets = [], fixed = {}, parameters = {}, sortInstancesBy = None):
        # Initialize DB
        self.database = pm.MongoClient(MONGO_URI)[MONGO_DB][MONGO_TABLE]

        # Establish parameters
        self.prefix = str(sys.argv[0]).split('.')[0]
        self.subject = subject
        self.revision = revision
        self.datasets = datasets
        self.fixed = fixed
        self.parameters = parameters

        # Counter
        self.entries = []
        self.reses = []  # for statistical tests
        self.complementary = []
        self.currentDataset = None
        self.sortInstancesBy = sortInstancesBy

        # Colour palette
        self.materialized = LinearSegmentedColormap.from_list(
            'materialized', ['#fafafa', '#f44336', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5', '#2196f3', '#03a9f4', '#00bcd4', '#009688', '#4caf50', '#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff9800', '#ff5722', '#000000'])

        # Prepare instances
        self.instances = [
            dict(zip(parameters.keys(), values), **self.fixed)
            for values in list(itertools.product(*parameters.values()))
        ]

        # Sort instances for time optimisation
        if sortInstancesBy:
            self.instances = sorted(self.instances, key=itemgetter(sortInstancesBy))

        # Say hello
        self.hello()

    def references(self, classifiers, dataset, measure):
        reftable = pd.read_csv('data/reference.csv', delimiter=',')
        classifiers = [c.name().lower() for c in classifiers]
        datasets = reftable['dataset']
        did = datasets[datasets == dataset]

        #print 'C = %s' % classifiers
        #print 'D = %s' % did
        #print 'M = %s' % measure

        reference = {}
        for classifier in classifiers:
            column = reftable[classifier + measure]
            result = column[did.index[0]]
            reference.update({classifier.upper(): result})

        return reference

    def start(self, dataset):
        self.entries = []
        self.independenceEntries = []  # for statistical tests
        self.independence = None
        self.complements = []
        self.warn('Dataset %s (%i/%i)' % (
            dataset,
            self.datasets.index(dataset),
            len(self.datasets)
        ))
        self.currentDataset = dataset

    def end(self):
        self.glorify('Processing on %s dataset done' % self.currentDataset)
        # Independence test
        if len(self.independenceEntries):
            self.warn('Making an statistical independence tests')
            meanValues = [np.mean(x) if x is not None else 0 for x in self.independenceEntries]
            bestValue = max(meanValues)
            bestIdx = meanValues.index(bestValue)

            self.independence = [self.areIndependent(x, self.independenceEntries[bestIdx]) for x in self.independenceEntries]
            self.glorify('%i values are marked as best, with mean %.3f' %
                (sum(self.independence), bestValue), 1)
        # Complementary check
        if len(self.complements):
            self.warn('Preparing complements')
            divider = len(self.instances) / len(self.parameters[self.sortInstancesBy])
            self.complements = self.complements[0::divider]
            self.glorify('Complements are %s' % self.complements, 1)

    def table(self, xx, xl, xf, yy, yl, yf, vf, refrow = None, valignment = 'r', reflead = '---', bestRow = None):
        self.warn('Making a table (%s to %s)' % (xl, yl))
        it = 0
        table = ''
        table += '\\begin{tabular}{@{}n%s@{}}\n' % (valignment * len(yy))
        table += '\t\\toprule\n'

        table += '\t\\multicolumn{1}{@{}N}{%s} & \\multicolumn{%i}{V{5em}@{}}{%s}\\\\\n' % (xl, len(yy), yl)
        table += '\t\\cmidrule(l){2-%i}\n\t' % (len(yy) + 1)

        for y in yy:
            table += ' & ' + xf % y

        table += '\\\\\n\t\\cmidrule(r){1-1} '
        for i, y in enumerate(yy):
            if i == len(yy) - 1:
                break
            table += '\\cmidrule(lr){%i-%i} ' % (i+2, i+2)
        table += '\\cmidrule(l){%i-%i}\n\t\t' % (len(yy) + 1, len(yy) + 1)

        # Wiersze i wartości
        vid = -1
        for i1, x in enumerate(xx):
            table += yf % x
            for i2, y in enumerate(yy):
                vid += 1
                table += ' & '
                if self.independence:
                    if self.independence[vid]:
                        table += '\\color{red!75!black} '
                val = self.entries[it]
                if val == 'nan':
                    table += '\\tiny NaN'
                else:
                    table += '' + vf % val
                it += 1
            table += ' \\\\\n\t\t'

        if refrow:
            table += '\\color{black!50} %s' % reflead
            for item in refrow:
                val = '%.3f' % refrow[item]
                if val == 'nan':
                    table += ' & \\tiny NaN'
                else:
                    table += ' & \\color{black!50}' + vf % val

            table += '\\\\\n\t\t'

        table += '\\bottomrule\n'

        if bestRow:
            content = ''
            #print 'BESTROW'
            #print bestRow
            bestValue = max(bestRow.values())
            worstValue = min(bestRow.values())

            difference = (float(max(self.entries)) - bestValue)

            for key in bestRow:
                if bestRow[key] == bestValue:
                    #print 'Best %s %.3f' % (key, bestRow[key])
                    content += 'best \\oldstylenums{%.3f} (\\textsc{%s}), worst \\oldstylenums{%.3f}' % (
                        bestRow[key],
                        key.lower(),
                        worstValue
                    )

            for key in bestRow:
                if bestRow[key] == worstValue:
                    #print 'Best %s %.3f' % (key, bestRow[key])
                    content += ' (\\textsc{%s})' % (
                        key.lower(),
                    )
            '''
            for key in bestRow:
                if bestRow[key] != bestValue:
                    print 'Other %s %.3f' % (key, bestRow[key])
                    content += '\\textsc{%s}:\\oldstylenums{%.3f} ' % (
                        key.lower(),
                        bestRow[key]
                    )
            '''

            #print 'Content of a row = %s' % content
            table += '\t\\multicolumn{%i}{@{}r@{}}{\\footnotesize \\color{black!50} {%s\\oldstylenums{%.1f}\\smallpercent}, %s}\\\\\n' % (
                len(yy) + 1,
                '+' if difference > 0 else '\\color{red!75!black}-',
                np.abs(100 * difference),
                content
            )

        table += '\\end{tabular}\n'

        filename = self.filename('%s.tex' % self.currentDataset, 'tables')
        self.saveStringToFile(
            table,
            filename
        )
        self.glorify('Table saved in %s' % filename, 1)

    def areIndependent(self, a, b, border = PBORDER):
        if a is None or b is None:
            return False
        test = stats.ttest_ind(a, b)
        return test.pvalue > border

    def addEntry(self, entry):
        self.glorify('Added entry %s' % entry, 1)
        self.entries.append(entry)

    def addIndependenceEntry(self, entry):
        self.independenceEntries.append(entry)

    def addComplement(self, entry):
        self.complements.append(entry)

    # Returns HS image according to the dataset name
    def hsi(self, dataset):
        path = '%s%s' % (HSIDIR, '%s.json' % dataset)
        print path
        with open(path) as f:
            hsi = hssa.HS(json.load(f))
        self.glorify('Dataset loaded (%s)' % hsi)
        return hsi

    def saveStringToFile(self, string, filename):
        text_file = open(filename, "w")
        text_file.write(string)
        text_file.close()

    # Returns Weles dataset
    def ds(self, dataset, pureLabels = False):
        ds = weles.Dataset('data/datasets/%s.csv' % dataset, pureLabels = pureLabels)
        self.glorify('Dataset loaded (%s)' % ds)
        return ds

    # Returns Weles dataset from filename
    def dsFromFilename(self, filename, pureLabels = False):
        ds = weles.Dataset(filename, pureLabels = pureLabels)
        self.glorify('Dataset loaded (%s)' % ds)
        return ds

    # Returns the result of classification
    def clfResult(self, clf):
        clfRes = {'acc': float('nan'), 'bac': float('nan'), 'wacc': None, 'wbac': None}
        ds = clf.dataset
        if (clf.name() == 'KNN' and len(ds.train) < 5) or len(ds.train) == 0 or (clf.name() == 'SVC' and len(np.unique(ds.y)) < 2):
            self.warn('To small training set', 1)
        else:
            clfRes = clf.quickLoop()
        self.glorify('Classifier returned %.3f:%.3f' % (clfRes['acc'], clfRes['bac']), 1)
        return clfRes

    def clfResultWithoutInjection(self, clf):
        clfRes = {'acc': float('nan'), 'bac': float('nan'), 'wacc': None, 'wbac': None}
        ds = clf.dataset
        print ds
        clfRes = clf.quickLoop()
        self.glorify('Classifier returned %.3f:%.3f' % (clfRes['acc'], clfRes['bac']), 1)
        return clfRes

    def showInstance(self, instance):
        didx = self.datasets.index(self.currentDataset)
        iidx = self.instances.index(instance)
        lins = len(self.instances)
        ldat = len(self.datasets)

        prc = float(iidx + lins * didx) / (lins * ldat)
        self.warn('Instance %i at dataset %i (%.2f%%) [EXP %s]' % (
            iidx, didx, 100 * prc, self.prefix
        ))
        for parameter in instance:
            self.notpam(parameter, instance[parameter], 1)

    def toProcess(self, cfgTag):
        count = self.database.find({"configHash": self.md5(cfgTag)}).count()
        return False if count else True

    def insertResults(self, results):
        identifier = self.database.insert_one(results).inserted_id
        self.glorify('Results passed to database [%s]' % identifier, 1)

    def getResults(self, configTag, toShow = []):
        results = self.database.find_one({"configHash": self.md5(configTag)})
        if results is not None:
            self.glorify('Results get from database [%s]' % configTag, 1)
            for parameter in results:
                if parameter in toShow:
                    self.notres(parameter, str(results[parameter]), 1)
        else:
            self.warn('There are no results for %s in database' % configTag, 1)
        return results

    def md5(self, value):
        return hashlib.md5(value).hexdigest()

    def hello(self):
        print bcolors.HEADER
        print '#' * 50
        print '# Experiment %s' % self.prefix
        print '# Subject: %s' % self.subject
        print '# Fixed parameters:'
        for parameter in self.fixed:
            print '#   %s = %s' % (parameter, self.fixed[parameter])
        print '# Testing parameters:'
        for parameter in self.parameters:
            print '#   %s (%i) %s -- %s' % (
                parameter,
                len(self.parameters[parameter]),
                self.parameters[parameter][0],
                self.parameters[parameter][-1])
        print '# Test will consist of %i instances' % len(self.instances)
        print '#' * 50
        print bcolors.ENDC

    def notify(self, what, depth=0):
        print '%s- %s' % (
            '  ' * depth,
            what
        )

    def warn(self, what, depth=0):
        print '%s%s- %s%s' % (
            bcolors.WARNING,
            '  ' * depth,
            what,
            bcolors.ENDC
        )

    def fileFromBson(self, filename, fileContent):
        with open(filename, mode='wb') as file:
            file.write(fileContent)

    def bsonFromFile(self, filename):
        with open(filename, mode='rb') as file:
            fileContent = file.read()
        return bson.Binary(fileContent)

    def glorify(self, what, depth=0):
        print '%s%s- %s%s' % (
            bcolors.OKGREEN,
            '  ' * depth,
            what,
            bcolors.ENDC
        )

    def notpam(self, name, value, depth=0):
        print '%s- %s = %s%s%s' % (
            '  ' * depth,
            name,
            bcolors.OKBLUE,
            value,
            bcolors.ENDC
        )

    def notres(self, name, value, depth=0):
        print '%s- %s = %s%s%s' % (
            '  ' * depth,
            name,
            bcolors.OKGREEN,
            value,
            bcolors.ENDC
        )

    def filename(self, name, path=''):
        return "%s/%s_%s" % (
            path,
            self.prefix,
            name
        )

    @classmethod
    def referenceClassifiers(cls):
        return [
            weles.sklKNN,
            weles.sklGNB,
            weles.sklDTC,
            weles.sklMLP,
            weles.sklSVC
        ]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
