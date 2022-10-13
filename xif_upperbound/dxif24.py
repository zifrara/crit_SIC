from newdim import *
import csv
from csv import reader
from time import time

for vertices in range(24,26):
    mini=1000
    with open('vtc'+str(vertices)+'tB','r') as read_obj:
        csv_reader = reader(read_obj,delimiter='\t')
        # header = next(csv_reader)
        l=0
        # Check file as empty
        # if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader: 
            # row variable is a list that represents a row in csv
            l=l+1
            lin=[row[0]]
            for s in row[1:]:
                n=eval(s)
                lin=lin+[n]
            # print(lin)
            d=int(vertices/lin[3])
            #print(d)
            if d<=2:
                d=d+1
            res = dimQ(row[0],d,10)
            while (res != 'True' and lin[1]*d < vertices):
                d=d+1
                res = dimQ(row[0],d,10)
            eta=2*lin[1]/(lin[1]+(vertices/d))
            if eta <= mini:
            	mini=min(mini,eta)
            print(l,' ',eta,' ',d)
            if eta < 1:
                print(l,' ',lin,' ',eta,' ',d)
            #if eta < 1:
             #   print(l,' ',lin,' ',eta,' ',d)
    if mini > 1:
        mini=1
    print(vertices,'\t',mini,'\t',l)
