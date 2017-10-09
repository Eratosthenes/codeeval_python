import sys
import pdb

# a is an array
def stupid_sort(a):
  i = 0
  while i<len(a)-1:
    if a[i]>a[i+1]:
      a[i],a[i+1] = a[i+1],a[i]
      i = 0
      yield a
    else:
      i += 1
  yield a

def main(filename):
  pdb.set_trace()
  f = open(filename).read().splitlines()
  split_by_pipe = map(lambda x: x.split('|'), f) # data split by pipes
  data = map(lambda x: map(int,x[0].split()), split_by_pipe) # list of int lists
  iterations = map(int,zip(*split_by_pipe)[1]) # corresponding iterations

  for data,iterations in zip(data,iterations):
    gen = stupid_sort(data)
    for i in range(iterations):
      a = gen.next()
    print(' '.join(map(str,a)))

if __name__=='__main__':
  main(sys.argv[1])
