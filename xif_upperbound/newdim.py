from scipy.linalg import eigh, eigvalsh
from scipy.sparse import coo_matrix
import numpy as np
import networkx,math,sys
import time
from scipy.stats import unitary_group, ortho_group
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)

def psdrF(mat,r,d=None):
    if d is None:
        d = len(mat)
    vas,ves = eigh(mat)
    vas[vas<0]=0
    pvas=np.diag(vas*np.array([0]*(d-r)+[1]*r))
    ves = np.matrix(ves)
    return np.matmul(np.matmul(ves,pvas),ves.H)

def normF(mat,adj,d=None):
    if d is None:
        d = len(mat)
    return np.multiply(mat,adj) + 1*np.identity(d)

def ranH(d):
    Mr = np.random.rand(d,d)
    Mi = np.random.rand(d,d)
    M = (Mr+Mr.T)/2 + 1j*(Mi-Mi.T)/2
    return np.matrix(M)

def dimQ(ghf,r,t): # k is the rank of the projectors; r is the rank of the matrix, i.e., the dimension of the vectors; t is the number of steps in the see-saw method in each monitored period
    if isinstance(ghf,str):gh = networkx.from_graph6_bytes(ghf.encode())
    elif isinstance(ghf,list) or isinstance(ghf,np.matrix):gh = networkx.Graph(ghf)
    else:return('Accepted types:str of graph6 format,list of edges, np.matrix of adjacency matrix')
    d = len(gh)
    adjc = 1-np.matrix(networkx.adjacency_matrix(gh).A)-np.identity(d)
    iterM = ranH(d)
    tmp0 = d
    tmp1 = 2*d
    start0 = time.time()
    start = start0
    while abs(tmp1-tmp0)>1e-9 and start-start0<30:
        newtime = time.time()
        if newtime-start>3:
            iterM = iterM + ranH(d)/100
            start = newtime
        for i in range(t): # t is the number of steps in the see-saw method in each monitored period
            iterM = psdrF(iterM,r,d)
            iterM = normF(iterM,adjc,d)
        vas = eigvalsh(iterM,eigvals=(0,d-r-1))
        tmp0 = tmp1
        tmp1 = sum(abs(vas))
    #return [abs(tmp1-tmp0)<1e-9,tmp1<1e-9]
    if tmp1<1e-9:
        return 'True'
    else:
        return 'Undetermied'

def dimQM(ghf,r,lt): # lt is the number of rounds
    res = []
    for i in range(lt):
        tmp = dimQ(ghf,r,20)
        if tmp[0]:res.append(tmp[1])
        if tmp[1]<1e-6:return [len(res),tmp]
        if len(res)>=5:return [len(res),min(res)]
    return [len(res),min(res+[1000])]

