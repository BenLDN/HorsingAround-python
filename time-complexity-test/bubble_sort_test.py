import time
import random

def random_list(size):
    out_list=[]
    for i in range(0,size):
        out_list.append(random.randint(1,999))
    return out_list
        

def bubble_sort_it(in_list):
    start_time=time.time()
    list_sorted=False
    length=len(in_list)
    while list_sorted==False:
        no_change=True
        for i in range(0,length-1):
           if in_list[i]>in_list[i+1]:
               no_change=False
               temp=in_list[i+1]
               in_list[i+1]=in_list[i]
               in_list[i]=temp
        if no_change==True:
            list_sorted=True
    stop_time=time.time()
    time_elapsed=stop_time-start_time
    return in_list, time_elapsed

def try_sort(sizes):
    results={}
    for size in sizes:
        try_list=random_list(size)
        sorted_list, try_time = bubble_sort_it(try_list)
        results[size]=try_time
    return results

try_array_sizes=[1000,2000,3000,4000,5000,6000]

times=try_sort(try_array_sizes)

for key in times:
    print(times[key])
