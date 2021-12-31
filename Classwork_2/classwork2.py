import csv
import json
import pickle
import os

with open(os.path.join('ClassWork', 'classwork19_10.csv'), 'r') as csv_r,\
        open(os.path.join('ClassWork', 'file.json'), 'w') as json_w,\
        open(os.path.join('ClassWork', 'file.pickle'), 'wb') as pickle_wb:
    reader = csv.DictReader(csv_r)
    rows = list(reader)
    json.dump(rows, json_w)
    pickle.dump(rows, pickle_wb)
