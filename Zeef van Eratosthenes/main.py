from mpi4py import MPI
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import math
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# print(comm.Get_size())
# print(comm.Get_rank())

def sieve_master(data):
    markers, k, stop = data[0], data[1], data[2]
    # if markers[k]:
    for i in range(k*2, stop+1, k):
        markers[i] = False


def sieve_worker(data):
    markers, k, start, i = data[0], data[1], data[2], data[3]
    if (start + k + i) % k == 0:
        markers[i] = False


def sieve_mpi_multiprocessing(N:int):
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

        data = [(markers,x,stop) for x in range(k, int(math.sqrt(stop)))]
        with Pool() as p:
            p.map(sieve_master, data)
            
    else:
        markers = np.ones(chunkSize, dtype=bool)

        while k**2 <= stop:
            if k < start or markers[k]:

                data = [(markers,k,start,x) for x in range(k, chunkSize)]
                with Pool() as p:
                    p.map(sieve_worker, data)

            k+=1

    n = len(np.where(markers == True)[0])
    n = comm.reduce(n, MPI.SUM, 0)
    if rank == 0:
        print(f'N found:{n}, took {time.time() - startTime} seconds.')


def sieve_mpi_multithreading(N:int):
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

        data = [(markers,x,stop) for x in range(k, 1+int(math.sqrt(stop)))]
        with ThreadPoolExecutor() as executor:
            executor.map(sieve_master, data)
            
    else:
        markers = np.ones(chunkSize, dtype=bool)

        while k**2 <= stop:
            if k < start or markers[k]:

                data = [(markers,k,start,x) for x in range(chunkSize)]
                with ThreadPoolExecutor() as executor:
                    executor.map(sieve_worker, data)

            k+=1
    
    n = len(np.where(markers == True)[0])
    n = comm.reduce(n, MPI.SUM, 0)
    if rank == 0:
        print(f'N found:{n}, took {time.time() - startTime} seconds.')


def sieve_mpi(N:int):
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
                    if (start + k + i) % k == 0:
                        markers[i] = False

            k+=1
        

    print(f'ID:{comm.Get_rank()}, len:{len(markers)}, Start:{start}, Stop:{stop}')

    n = len(np.where(markers == True)[0])
    n = comm.reduce(n, MPI.SUM, 0)
    if rank == 0:
        print(f'N found:{n}, took {time.time() - startTime} seconds.')




# markers of prime numbers goes from 0 to n!
# n = sieve(1000000)
# sieve_mpi_multiprocessing(1000) # Werkt niet samen met MPI
# sieve_mpi_multithreading(100000)

# sieve_mpi(1000)
# sieve_mpi(10000)
# sieve_mpi(100000)
sieve_mpi(1000000) # Deze is gebruikt vanwege zijn snelheid
