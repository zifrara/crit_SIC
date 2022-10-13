from newdim import *

gh = [[0,1],[1,2],[2,3],[3,4],[0,4]] #edge format
gh = 'Dhc' #graph6 format
res = dimQ(gh,3,10) # graph, orthogonal rank to check, length of iteration in each small step (the larger the more accurate, then more time)
# The result 'Ture' means that we have a orthogonal representation with such a rank, 'Undetermined' means that it cannot be decided by this routine. We can always increase the targeted orthogonal rank to obtain the result 'True'.
print(res)
