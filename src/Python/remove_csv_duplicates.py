#!/usr/bin/env python

import csv

with open('models_edit.csv', 'r') as inp, open('models.csv', 'w') as out:
    writer = csv.writer(out)
    i = 0
    for row in csv.reader(inp):
        if(row[0] != '%time'):
            mismatch = False
            for i in range(1, len(row)):
                if(row[i] != prev_row[i]):
                    # there is mismatch
                    mismatch = True
                    break
            if mismatch:
                writer.writerow(row)
                prev_row = row
        else:
            # first column
            prev_row = [i * 0 for i in range(len(row))]
            writer.writerow(row)
        

        