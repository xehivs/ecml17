#!/usr/bin/env python
import numpy as np
import pytablewriter
import yaml
import json
import csv

classifiers = ['knn', 'gnb', 'dtc', 'mlp', 'svc']
colors = ['#e53935', '#ba68c8', '#64b5f6', '#dce775', '#81c784', '#ffb74d']
datasets = ['syntetic5f', 'syntetic10f', 'syntetic20f', 'syntetic50f', 'syntetic100f', 'syntetic200f',
    'syntetic500f','balance', 'yeast3', 'wisconsin', 'ionosphere']



def chartjsdata(classifiers, datasets):
    results = []
    data = []
    for dataset in datasets:
        csv_data = np.genfromtxt('csv/experiment_1_%s.csv' % dataset, delimiter=',')
        data.append('%.3f' % float(np.max(csv_data[1:,1:])))

    results.append({
        'label': 'ECE',
        'data': data,
        'backgroundColor': [colors[0]] * (len(datasets))
    })
    for idx, classifier in enumerate(classifiers):
        data = []
        for dataset in datasets:
            key = '%sbac%s' % (classifier, dataset)
            data.append('%.3f' % float(reference_dictionary[key]))

        results.append({
            'label': classifier.upper(),
            'data': data,
            'backgroundColor': [colors[idx+1]] * (len(datasets))
        })
    return {'labels': datasets, 'datasets': results}

def barplot(data, label='not'):
    options = {
        'scales': {
            'yAxes': [{
                'display': True,
                'stacked': False,
                'ticks': {
                    'min': 0,
                    'max': 1
                }
            }]
        }
    }
    print '<canvas id="%s" height="40em" width="100%%"></canvas>' % label
    print '<script>\nvar ctx_benchmark = document.getElementById("%s").getContext(\'2d\');' % label
    print 'var myChart = new Chart(ctx_benchmark, { type: \'bar\', data: %s, options: %s });' % (json.dumps(data), json.dumps(options))
    print '</script>'

datasets_dictionary = {}
with open('data/datasets.csv', 'rb') as csvfile:
    reference_reader = csv.reader(csvfile, delimiter=',')
    headers = reference_reader.next()
    for row in reference_reader:
        for idx, cell in enumerate(row):
            datasets_dictionary.update(
                {'%s%s' % (headers[idx], row[0]): cell})

def datasets_table(datasets):
    datasets_table = []
    for dataset in datasets:
        datasets_table.append([dataset,
            datasets_dictionary['features%s' % dataset],
            datasets_dictionary['classes%s' % dataset],
            datasets_dictionary['samples%s' % dataset],
            datasets_dictionary['ratio%s' % dataset],
            datasets_dictionary['tags%s' % dataset]])

    writer = pytablewriter.MarkdownTableWriter()
    writer.header_list = ['dataset', 'features', 'classes', 'samples', 'ratio', 'tags']
    writer.value_matrix = datasets_table

    writer.write_table()
    print '\n\n'

def result_table(dataset):
    csvArray = np.genfromtxt('csv/experiment_1_%s.csv' %
                             dataset, delimiter=',')
    print '# `%s`\n' % dataset

    writer = pytablewriter.MarkdownTableWriter()
    writer.header_list = csvArray[0,:].tolist()
    writer.value_matrix = csvArray[1:,:].tolist()
    writer.header_list[0] = "."

    writer.write_table()


reference_dictionary = {}
with open('data/reference.csv', 'rb') as csvfile:
    reference_reader = csv.reader(csvfile, delimiter=',')
    headers = reference_reader.next()
    for row in reference_reader:
        for idx, cell in enumerate(row):
            reference_dictionary.update(
                {'%s%s' % (headers[idx], row[0]): cell})

# Frontmatter
print '---\nlayout: default\n---\n'

# Congig yaml
config = yaml.load(open("_config.yml", "r"))

# Abstract
print '# Abstract'
print '> %s\n' % config['abstract']



# Benchmark
print '# Benchmark data\n'
benchmark_datasets = datasets[7:]
barplot(chartjsdata(
    classifiers = classifiers,
    datasets = benchmark_datasets
), label='benchmark')
datasets_table(benchmark_datasets)

for dataset in benchmark_datasets:
    result_table(dataset)

# Synthetic
print '# Synthetic data\n'
synthetic_datasets = ['syntetic5f', 'syntetic10f', 'syntetic20f', 'syntetic50f', 'syntetic100f', 'syntetic200f', 'syntetic500f']

barplot(chartjsdata(
    classifiers = classifiers,
    datasets = synthetic_datasets[:4]
), label='synthetic')
datasets_table(synthetic_datasets[:4])
print '\n---\n'

barplot(chartjsdata(
    classifiers = classifiers,
    datasets = synthetic_datasets[4:]
), label='synthetic2')
datasets_table(synthetic_datasets[4:])

for dataset in synthetic_datasets:
    result_table(dataset)
