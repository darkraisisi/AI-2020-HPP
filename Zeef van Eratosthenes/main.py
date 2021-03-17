from mpi4py import MPI
import numpy as np
import math
import time

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
print(comm.Get_size())
print(comm.Get_rank())

def sieve(N:int):
    chunkSize = math.ceil(N/comm.Get_size())
    start = comm.Get_rank() * chunkSize
    stop = start + chunkSize

    print(f'ID:{comm.Get_rank()}, Start:{start},Stop:{stop}')

    k = start + 2

    markers = np.ones(N+1, dtype=bool)
    markers[0] = False
    markers[1] = False

    while k**2 <= N and k < stop:
        if markers[k]:
            print('K:',k)
            for i in range(k*2, N+1, k):
                markers[i] = False
                # Or add local counter.

        k+=1
    # Or dont count when one process is finished.
    return len(np.where(markers[start:stop] == True)[0])
    
# markers of prime numbers goes from 0 to n!
startTime = time.time()
# n = sieve(1000000000)
n = sieve(1000)
print(f'N found:{n}, took {time.time() - startTime} seconds.')