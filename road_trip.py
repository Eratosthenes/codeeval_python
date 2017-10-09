# import pdb
def get_ints(line):
  return map(int, [x[1] for x in map(lambda x:x.split(','),line.split(';'))[:-1]])

def nearest_cities(ints):
  return [y-x for x,y in zip(ints, ints[1:])]

content = open('road_trip.txt').read().splitlines()
ints = map(get_ints,content) # array of ints
sorted_ints = map(lambda x:sorted(x),ints) # sorted ints
nearest_cities = map(lambda x: nearest_cities(x), sorted_ints)
first_cities = [x[0] for x in sorted_ints]
r = [[x]+y for x,y in zip(first_cities,nearest_cities)]
output = map(lambda x:','.join(map(str,x)), r)
for line in output:
  print line 
# pdb.set_trace()
