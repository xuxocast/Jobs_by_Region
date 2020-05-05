## This program show the most demanded jobs per location (independent of date)
######################################################################################################


# OutPut example with 10M lines analyzed :
#
# Top five locations hiring engeneers & Softw dev with number of openings:
#{'Redmond': 11326, 'San Francisco': 12579.0, 'Bengaluru': 19665, 'Santa Clara Valley': 24985, 'Seattle': 25229}


######################################################################################################

import os
from csv import reader
import statistics as st
import collections 
from scipy.stats.stats import pearsonr

os.getcwd()

file = "temp_datalab_records_job_listings.csv" #1/7 Job Postings data from Thinknum

N = 10000000  # For now only first 10M lines 


def num(a):
	 if a == '':
	 	return 1
	 else:
	 	return float(a)

def Read(FILE,I): 
	i=0 
	L=[] 
	with open(FILE) as FF: 
	    while i < I: 
	        line = FF.readline()
	        a = [line]
	        for l in reader(a):
    	             L.append(l) 
	        i+=1 
	return L

data = Read(file,N)

for i in range(1,N):  
	   dl = len(data[0]) - len(data[i])
	   while dl > 0:
	     	  data[i].append(0)                     #Fill with zeros to match lenght
	     	  dl = dl - 1



############################################################################

# 4  title job
# 8 locality a
# 11 number_of_openings

match_eng = ["Engineer","Web","Software","Android","iOS"]

def RegionCount(match):
    JJ=[]
    for i in range(1,N):
	    if isinstance(data[i][4], str) and any(x in data[i][4] for x in match) and data[i][8] != '':   #ignore data without location 
             nn = num(data[i][11])
             JJ.append( {data[i][8]:nn} )
    count_jj = collections.Counter()
    for d in JJ: 
         count_jj.update(d)
    d_jj = dict(count_jj) 
    d_jj = dict(sorted(d_jj.items(), key=lambda t: t[1]))
    return d_jj

d_eng = RegionCount(match_eng)
nn = len(d_eng)

print("Top five locations hiring engeneers & Softw dev with number of openings")
print(dict(list(d_eng.items())[nn-5:nn]))
print()
del d_eng, data

######################################################################################################


