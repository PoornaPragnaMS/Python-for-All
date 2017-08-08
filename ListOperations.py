# In this program we are going to see, how to perform any suggested operation from end user on a List

L = []
ip = input("Kindly Enter the operation to be performed on a string").split()
cmd = ip[0]
args = ip[1:]
if cmd != 'print':
    cmd += '('+','.join(args)+')'
    eval ('L.'+cmd)
else:
    print(L)
    
    
# Sample Input

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print 
#remove 6
#append 9
#append 1
#sort 
#print
#pop
#reverse
#print
