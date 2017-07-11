# -*- coding: utf-8 -*-
from Experiment import *
import ece

''' Experiment configuration '''
e = Experiment(
    subject = 'A subject of experiment.',
    revision = 'b',
    datasets = ['syntetic5f', 'syntetic10f', 'syntetic20f', 'syntetic50f', 'syntetic100f', 'syntetic200f', 'syntetic500f', 'balance', 'ionosphere', 'wisconsin', 'yeast3'],
    fixed = {
        'resample': 250,
        'votingMethod': 1,
        'approach': 2,
        'limit': 60
    },
    parameters = {
        'radius': [.1,.2,.3,.4,.5],
        'grain': [4,8,16,32],
    },
    sortInstancesBy = 'radius'
)

# Those two are for passing processing when we only change clf between instances
alg = None
modelCfgTag = None

# Looping through datasets
for dataset in e.datasets:
    # Load your dataset(s)
    e.start(dataset)
    #hsi = e.hsi(dataset)
    ds = e.ds(dataset)
    #ds = e.ds(dataset, pureLabels = True)

    # Looping through instances
    for instance in e.instances:
        e.showInstance(instance)

        # Get the current parameters as variables
        locals().update(instance)

        # Configuration tag for model
        newModelCfgTag = ece.ECE.cfgTag(
            ds = ds,
            radius = radius,
            grain = grain,
            votingMethod = votingMethod,
            approach = approach,
            resample = resample,
            limit = limit
        )

        # First, establish the cfgTag
        cfgTag = newModelCfgTag + e.revision

        # Prepare a name for eventual illustration
        '''
        illustrationFilename = e.filename('%s_l%i.png' % (
            dataset,
            limit), 'figures')
        '''

        # Process if there is a need to
        if e.toProcess(cfgTag):
            e.warn(('Processing %s' % cfgTag), 1)

            # Do your things with the model if it's changed
            if modelCfgTag == newModelCfgTag:
                e.glorify('Model is the same as in previous task', 1)
            else:
                alg = ece.ECE(
                    dataset = ds,
                    radius = radius,
                    grain = grain,
                    resample = resample,
                    votingMethod = votingMethod,
                    approach = approach,
                    limit = limit
                )
                e.glorify('New model established', 1)
            modelCfgTag = newModelCfgTag

            # Do your things, which need to be done at each loop

            # Get the result of classification if needed an make them variables
            #clfRes = e.clfResultWithoutInjection(clf(ds))
            clfRes = alg.quickLoop()
            locals().update(clfRes)

            # Make an illustration if necessary
            '''
            alg.png(illustrationFilename, False)
            illustration = e.bsonFromFile(illustrationFilename)
            '''

            # Prepare results and put them in database
            e.insertResults({
                'configHash': e.md5(cfgTag),
                'cfgTag': cfgTag,
                'wacc': wacc,
                'wbac': wbac,
                'accuracy': acc,
                'bac': bac,
                'combinations': alg.combinations,
                'combinationsNo': len(alg.combinations),
                'thetas': [list(ex.thetas) for ex in alg.exposers]
            })

        # Get the results from database and make them variables
        results = e.getResults(cfgTag, [
            'accuracy', 'bac'
        ])
        locals().update(results)

        # Save figure if exists
        if results is not None and 'figure' in results.keys():
            e.fileFromBson(illustrationFilename, figure)

        # Add entry. String, when you'll making a table
        e.addEntry('%.3f' % bac)

        # Add data to statistical independence test if necessary
        e.addIndependenceEntry(wbac)

        # Add complementary data if necessary
        #e.addComplement(trainingSamples)

    # Make an independence test and complements
    e.end()

    # Prepare a table
    ## Row indicators
    xl = 'Radius'
    xx = e.parameters['radius']
    yf = '\\multicolumn{1}{@{}l}{\\oldstylenums{%s}}'

    ## Column indicators
    yl = 'Grain'
    yy = e.parameters['grain']
    ##yy = ['\\textsc{%s}' % clf.name().lower() for clf in yy]
    xf = '\\multicolumn{1}{V{2em}}{%s}'

    ## Value format
    vf = '\\oldstylenums{%s}'

    ## Extra row
    reference = e.references(
        classifiers = Experiment.referenceClassifiers(),
        dataset = dataset,
        measure = 'bac'
    )
    refrow = None
    bestRow = reference

    # And save a table
    e.table(xx = xx, xl = xl, xf = xf, yy = yy, yl = yl, yf = yf, vf = vf,
        refrow = refrow, bestRow = bestRow)

    e.csv(bestRow = bestRow, xx = e.parameters['radius'], yy = e.parameters['grain'])
