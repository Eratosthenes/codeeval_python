import sys
import pdb

def stupid_sort(a):
  i = 0
  while i < len(a)-1:
    if a[i] > a[i+1]:
      a[i],a[i+1] = a[i+1],a[i]
      i = 0
      yield a
    else:
      i += 1
  yield a

def split(line):
    data, iterations = line.split(' | ')
    return [int(i) for i in data.split()], int(iterations)

def main(filename):
  f = open(filename).read().splitlines()
  for data,iterations in map(split,f):
    gen = stupid_sort(data)
    for i in range(iterations):
      a = gen.next()
    print(' '.join(map(str,a)))

if __name__=='__main__':
  main(sys.argv[1])
