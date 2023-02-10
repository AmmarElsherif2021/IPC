# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:37:59 2023

@author: ammar
"""
import multiprocessing
import time
import random
import string
import queue
# output result in global scope
result=['']*10
q=queue.Queue()
#Generate random char every 1 sec
def Alpha(q):
    
    i=0
    while i<5:
        time.sleep(1)
        q.put(random.choice(string.ascii_letters))
        i=i+1
   
    
    
#Generate integer every 1 sec
def Counter(q):
    
    i=1
    while i<6:
        time.sleep(1)
        q.put(i)
        i=i+1
    

#Restart function
def Restart(q,x):
    time.sleep(x)
    q.put('Restart')
    

#print queue
def print_q(q):
    queue=list()
    while not q.empty():
        queue.append(q.get())
    return queue
#main
if __name__ == "__main__":
    
    print('Main process starts')
    q = multiprocessing.Queue()
    # creating new processes
    p1 = multiprocessing.Process(target=Alpha, args=(q,))
    p2 = multiprocessing.Process(target=Counter, args=(q,))
    p3 = multiprocessing.Process(target=Restart, args=(q,10))
    
    # starting process
    p1.start()
    p2.start()
    p3.start()
    # wait until process is finished
    p1.join()
    p2.join()
    p3.join()
    #finish
    print("Result(in main program): {}".format(print_q(q)[:]))