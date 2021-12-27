
# task3 nearest integrated transport network
import json
from rtree import index
idx = index.Index()
# read the ITN file
with open('Material/Material/itn/solent_itn.json', 'r') as f:
    itn = json.load(f)
# print(itn)
