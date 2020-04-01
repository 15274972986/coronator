#!/usr/bin/python3
#Filename: modCIGAR.py

import re

def Split(cigar):
    #Split CIGAR by pattern and remove '' in list, eg:100M50S to ['100','50'] .
    SplCigarLen=re.split(r'[SHMDI]',cigar)
    SplCigarLen=list(filter(None, SplCigarLen))
#   print(SplCigarLen)
#   FloatSplCigarLen=list(map(float,SplCigarLen))
#Convert string into integer as they indicate pattren length.
    IntSplCigarLen=list(map(int,SplCigarLen))
    #Split CIGAR to make a list of patterns and remove '', eg:100M50S to ['M','S']
    SplCigarPat=re.split(r'[0123456789]*',cigar)
    SplCigarPat=list(filter(None, SplCigarPat))
#   print(SplCigarPat)
    #Calculate length of the reads.
    s=0
    for PatLen in SplCigarLen:
        s+=int(PatLen)
#   print(SplCigarPat)
#   s=IntModcigarLen[0]
#   e=IntModcigarLen[len(Modcigar)]
    #Acoording to patterns at both ends, predict possible breakpoint.
    RelativeBpSite=0
    if SplCigarPat[0] == "M" and SplCigarPat[len(SplCigarPat)-1] == "M":
        RelativeBpSite=0
    elif SplCigarPat[0] != "M" and SplCigarPat[len(SplCigarPat)-1] == "M":
        RelativeBpSite=-1
    elif SplCigarPat[0] == "M" and SplCigarPat[len(SplCigarPat)-1] != "M":
        RelativeBpSite=s-IntSplCigarLen[len(SplCigarLen)-1]
    elif SplCigarPat[0] != "M" and SplCigarPat[len(SplCigarPat)-1] != "M" and IntSplCigarLen[0] < IntSplCigarLen[len(SplCigarLen)-1]:
        RelativeBpSite=s-IntSplCigarLen[0]-IntSplCigarLen[len(SplCigarLen)-1]
    elif SplCigarPat[0] != "M" and SplCigarPat[len(SplCigarPat)-1] != "M" and IntSplCigarLen[0] > IntSplCigarLen[len(SplCigarLen)-1]:
        RelativeBpSite=-1
    else:
        RelativeBpSite=0
#   String=str(IntSplCigarLen[0]) + SplCigarPat[0] + str(IntSplCigarLen[len(SplCigarLen)-1]) + SplCigarPat[len(SplCigarPat)-1]
    return RelativeBpSite
