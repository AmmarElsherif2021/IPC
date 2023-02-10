# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:50:10 2023

@author: ammar
"""
import time
import random
import multiprocessing
import string 

result=[None]*10
def Alpha(result):
    """
    function to generate random chars
    """
    i=0
    while i<5:
        time.sleep(1)
        result[i]=random.choice(string.ascii_letters)
        i=i+1
   
    print("Result(in process p1): {}".format(result[:]))

#Generate integer every 1 sec
def Counter(result):
    #global result
    i=1
    while i<6:
        time.sleep(1)
        result[i]=i
        i=i+1
    print("Result(in process p2): {}".format(result[:]))
    
  
if __name__ == "__main__":
    
  
    # creating Array of int data type with space for 10 places
    result = multiprocessing.Array('i', 10)
  
    # creating Value of int data type
    some_value = multiprocessing.Value('i')
  
    # creating new process
    p1 = multiprocessing.Process(target=Alpha , args=(result,))
    p2 = multiprocessing.Process(target=Counter  , args=(result,))
    # starting process
    p1.start()
    p2.start()
    # wait until the process is finished
    p1.join()
    p2.join()
    # print result array
    print("Result(in main program): {}".format(result[:]))
  
    