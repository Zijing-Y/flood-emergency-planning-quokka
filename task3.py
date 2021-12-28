
# task3 nearest integrated transport network
# reference:
# https://rtree.readthedocs.io/en/latest/class.html
# http://www.manongjc.com/detail/7-bmdxrklxbxfzgon.html

from rtree import index
idx = index.Index()

# read the ITN file
with open('Material/Material/itn/solent_itn.json', 'r') as f:
    itn = json.load(f)
road_node = itn['roadnodes']

# create roadnodes sequence:
road_nodes = []
for i in road_node.values():
    road_nodes.append(tuple(i['coords']))

# add roadnodes and rectangles to the spatial index:
for n, point in enumerate(road_nodes):
    idx.insert(n, point, str(n))

# define a query for user:
q_user = (point_user.x, point_user.y)

# identify the nearest itn node to the user
# objects=False turn to id
# objects=True turn to item
hits_1 = list(idx.nearest(q_user, num_results=1, objects=False))
for i in hits_1:
    print('the nearest ITN node to the user', point_user, 'is:', road_nodes[i])

# define a query for highest point:
q_highest = (a[0], a[1])

# identify the nearest itn node to the highest:
hits_2 = list(idx.nearest(q_highest, num_results=1, objects=False))
for i in hits_2:
    print('the nearest ITN node to the highest point', a, 'is:', road_nodes[i])
