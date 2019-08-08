import pandas as pd
import os
import time
    
def wait1(s):
    for i in range(int(s/0.4)):
        print('/',end='\r')
        time.sleep(0.1)
        print('-',end='\r')
        time.sleep(0.1)
        print('\\',end='\r')
        time.sleep(0.1)
        print('|',end='\r')
        time.sleep(0.1)

def wait2(s):
    for i in range(s):
        print('>'*i + '-'*(s-i), end = '\r')
        time.sleep(1)
    print('>'*60, end = '\r')
        
def wait3(s):
    for i in range(int(s/2)):
        for j in range(5):
            print('■■'*j + '  '*(5-j), end = '\r')
            time.sleep(1/5)
        
wait1(60)