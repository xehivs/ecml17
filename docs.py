#!/usr/bin/env python
import numpy as np
import pytablewriter

csvArray = np.genfromtxt('csv/experiment_1_syntetic5f.csv', delimiter=',')
print '# Hello!\n'

writer = pytablewriter.MarkdownTableWriter()
#writer.table_name = "example_table"
writer.header_list = csvArray[0,:].tolist()
writer.value_matrix = csvArray[1:,:].tolist()
writer.header_list[0] = "."

writer.write_table()
