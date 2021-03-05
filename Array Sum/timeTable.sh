for threadNum in 1 2 4 8
do
echo $threadNum
    for i in '10k' '100k' '1m' '10m'
    do 
        OMP_NUM_THREADS=$threadNum ./arraySum $i'.txt'
    done
done