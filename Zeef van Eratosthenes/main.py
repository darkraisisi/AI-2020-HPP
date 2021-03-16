from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

"""
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print(rank,data)
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print(rank,data)
else:
    print(rank)
"""

N = 100
k = 2

markers = np.ones(N+1, dtype=bool)
markers[0] = False
markers[1] = False

while k**2 <= N:
    if markers[k]:
        print('K:',k)
        for i in range(k*2, N+1, k):
            markers[i] = False

        print(markers,len(markers))
        print(np.where(markers == True))
    k+=1
    
# markers of prime numbers goes from 0 to n!