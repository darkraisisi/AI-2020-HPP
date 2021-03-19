from mpi4py import MPI
import multiprocessing as mp
import numpy as np
import math
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# print(comm.Get_size())
# print(comm.Get_rank())

def sieve(N:int):
    startTime = time.time()
    chunkSize = N // comm.Get_size()
    start = comm.Get_rank() * chunkSize
    stop = start + chunkSize
    totalSum = 0

    k = 2

    if rank == 0:
        markers = np.ones(chunkSize+1, dtype=bool)
        markers[0] = False
        markers[1] = False

        while k**2 <= stop:
            if markers[k]:
                for i in range(k*2, stop+1, k):
                    markers[i] = False
            k+=1
    else:
        markers = np.ones(chunkSize, dtype=bool)

        while k**2 <= stop:
            if k < start or markers[k]:
                for i in range(chunkSize):
                    # print((start + k + i) % k, start, k, i)
                    if (start + k + i) % k == 0:
                        markers[i] = False

            k+=1
        

    print(f'ID:{comm.Get_rank()}, len:{len(markers)}, Start:{start}, Stop:{stop}')
    # for i in range(len(markers)):
    #     if markers[i]:
    #         print(i + (chunkSize * rank))

    n = len(np.where(markers == True)[0])
    n = comm.reduce(n, MPI.SUM, 0)
    if rank == 0:
        print(f'N found:{n}, took {time.time() - startTime} seconds.')




# markers of prime numbers goes from 0 to n!
# n = sieve(1000000)
sieve(1000)