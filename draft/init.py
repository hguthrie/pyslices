__author__ = 'hguthrie'

file = open('data.txt')
input = open('data.txt','r')
output = open('data.txt','a')

# read line by line
for line in file:
    print(line, end ='')

#for line in input:
 #   print(line, file = output,)