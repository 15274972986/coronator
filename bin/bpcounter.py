#!/usr/bin/python3

import pandas as pd
import numpy as np
import modCIGAR
#from pandas import Series

#input filename
FileName='../inputdir/MapsWithBreakPointSite'

#read the file
BpList=pd.read_csv(FileName,sep='\t',header=None)
BpList.index=range(len(BpList))
BpList.columns=['Read','Site','CIGAR']
BpList['RelaBpSite']=''

#take a look at the input file
#print(BpList.head(10))

r=0
while r < len(BpList):
     CIGAR=BpList['CIGAR'][r]
     Site=BpList['Site'][r]
     #Acoording to CIGAR pattern, calculate relative breakpoint sites
     chCIGAR=modCIGAR.Split(CIGAR)
     print("Match_start: " + str(Site) + " CIGAR: " + CIGAR + ", expected relative breaksite: " + str(chCIGAR))
     BpList['RelaBpSite'][r]=chCIGAR
     r+=1
#take a look at the newly generated column
#print(BpList.head(10))
BpList.to_csv('../outputdir/DataforR',sep='\t',header=True)
