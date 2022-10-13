import numpy as np
import networkx
import picos, string#, sympy
from scipy import sparse

def lovasz(ghf): # k is the rank of the projectors; r is the rank of the matrix, i.e., the dimension of the vectors; t is the number of steps in the see-saw method in each monitored period
    if isinstance(ghf,str):gh = networkx.from_graph6_bytes(ghf.encode())
    elif isinstance(ghf,list) or isinstance(ghf,np.matrix):gh = networkx.Graph(ghf)
    else:return('Accepted types:str of graph6 format,list of edges, np.matrix of adjacency matrix')
    nv = len(gh)
    edges = [it for it in gh.edges(data=False)]
    adjm = sparse.coo_matrix(([1.]*(2*len(edges)), ([it[0] for it in edges]+[it[1] for it in edges], [it[1] for it in edges]+[it[0] for it in edges])), shape=(1+nv, 1+nv)).toarray()
    prob = picos.Problem()
    weights = picos.diag([1]*nv+[0])
    X = picos.HermitianVariable('X',(1+nv,1+nv))
    prob.add_list_of_constraints([X[i,nv]==X[i,i] for i in range(nv)])
    prob.add_constraint(X[nv,nv] == 1)
    prob.add_constraint(X^adjm == 0)
    prob.add_constraint(X >> 0)
    prob.set_objective('max', (weights|X))
    sol = prob.solve(verbosity=0,solver='mosek')
    return sol.value.real

#gh = '~?@@~~~~|~n}~|~|~}~nn||~Vv}nnynn|Vv|T|~inn}i}~|T|~|T|~]i}~vinn}|T|~ZtVv}vinnyvinnxZtVv{U|T|~AvinnwJ]i}~_U|T|~_U|T|~OJ]i}~sAvinn}_U|T|~Y@ZtVv}sAvinn}sAvinn~Y@ZtVv~u_U|T|~]sAvinn|zOJ]i}~ju_U|T|~ju_U|T|~TzOJ]i}#~t]sAvinnyju_U|T|~inY@ZtVv~T]sAvinn~T]sAvinn~inY@ZtVv~yju_U|T|~^T]sAvinn||TzOJ]i}~zyju_U|T|~zyju_U|T|~||TzOJ]i}~~^T]sAvinn~zyju_U|T|~~ninY@ZtVv{'
#res = lovasz(gh)
#print(res)

gh='~?@@????A?O@?A?A?@?OOAA?gG@OODOOAgGAiA?TOO@T@?AiA?AiA?`T@?GTOO@AiA?cIgG@GTOODGTOOEcIgGBhAiA?|GTOOFs`T@?^hAiA?^hAiA?ns`T@?J|GTOO@^hAiA?d}cIgG@J|GTOO@J|GTOO?d}cIgG?H^hAiA?`J|GTOOACns`T@?SH^hAiA?SH^hAiA?iCns`T@?I`J|GTOODSH^hAiA?TOd}cIgG?i`J|GTOO?i`J|GTOO?TOd}cIgG?DSH^hAiA?_i`J|GTOOAAiCns`T@?CDSH^hAiA?CDSH^hAiA?AAiCns`T@??_i`J|GTOO?CDSH^hAiA??OTOd}cIgG?'
res = lovasz(gh)
print(res)
