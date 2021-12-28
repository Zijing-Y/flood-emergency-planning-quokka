
# task3 nearest integrated transport network
import json
from rtree import index
idx = index.Index()

# read the ITN file
with open('Material/Material/itn/solent_itn.json', 'r') as f:
    itn = json.load(f)
road_node = itn['roadnodes']

# create roadnodes sequence:
roadnodes = []
for i in road_node.values():
    roadnodes.append(i['coords'])
# print(roadnodes)

# add roadnodes and rectangles to the spatial index:
for n, point in enumerate(roadnodes):
    idx.insert(n, point, str(n))
# print(idx)

# define a query for user:
q_user = (qu_x, qu_y)
# identify the nearest itn node to the user
idx.nearest(q_user, num_results=1, objects=True)

# define a query for highest point
q_highest = (qh_x, qh_y)
# identify the nearest itn node to the highest
idx.nearest(q_highest, num_results=1, objects=True)
