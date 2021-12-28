
# task3 nearest integrated transport network
import json
from rtree import index
idx = index.Index()
# read the ITN file
with open('Material/Material/itn/solent_itn.json', 'r') as f:
    itn = json.load(f)
# print(itn)
# print(itn.keys())
road_node = itn['roadnodes']
# print(road_node)
# print(road_node.values())
for i in road_node.values():
    roadnodes = i['coords']

for n, point in enumerate(roadnodes):
    idx.insert(n, point, str(n))

# define a query for user:
q_user = (qu_x, qu_y)
# identify the nearest itn node to the user
index.nearest(q_user, num_results=1, objects=True)

# define a query for highest point
q_highest = (qh_x, qh_y)
# identify the nearest itn node to the highest
index.nearest(q_highest, num_results=1, objects=True)
