import sys
import pdb

# num is a string 
def convert_to_dec(num,b):
    d = dict(zip(map(str,range(10)),range(10))+zip('abcdef',[10+n for n in range(6)]))
    a = list(enumerate([d[x] for x in num[::-1]])) # enumerated list
    return sum([i[1]*b**i[0] for i in a])

def main(filename):
    f = open(filename).read().splitlines()
    for line in f:
        hexa, bina = map(lambda x:x.split(), line.split('|'))
        virus = [convert_to_dec(x,16) for x in hexa]
        antivirus = [convert_to_dec(x,2) for x in bina]
        print(sum(virus)<=sum(antivirus))

if __name__=='__main__':
    main(sys.argv[1])


