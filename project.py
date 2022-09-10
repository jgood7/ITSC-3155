from queue import Empty
import pandas as pd
import re

stateList = pd.read_excel (r'C:\Users\joshg\OneDrive\Desktop\itsc-3155\projOneData.xls',usecols='B')
stateList.dropna(axis=0)
#print(stateList.type)
#print(stateList)
newList = {}
for rowNum in range(4,56):
    newList[rowNum-4] = ((stateList.iloc[rowNum][0]))
print(newList)
fullList = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
fullList = fullList.drop(columns=list('AB'))
print(fullList)
for each in newList:
    stateVals= pd.read_excel(r'C:\Users\joshg\OneDrive\Desktop\itsc-3155\projOneData.xls',sheet_name=each,skiprows=lambda x: x in [0,7])
    print(each)
    print(stateVals)
    if each==0:
        stateVals.iloc[0:0]
    else:
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.head(stateVals.shape[0] -1)
        stateVals = stateVals.iloc[6: , :]

        #stateVals = stateVals[stateVals.iloc[:, 0].str.contains('..*')]

        stateVals = stateVals[stateVals.iloc[:, 0].str.find('..')!=-1]
        stateVals['State'] = newList[each]
        print('~~~~~~~~~~~~~')
        #print(stateVals.iloc[0].str.contains('..Spanish'))
        print(stateVals)
        print('~~~~~~~~~~~~~~~~~')
#        print(newList[each])
        print('************')
        print(';;;;;;;;;;;;;;')
        
        fullList = pd.concat([fullList,stateVals],ignore_index=True)
fullList.to_csv('C:/Users/joshg/OneDrive/Desktop/itsc-3155/projOneDataOutput.csv')
print('---------------')
print('---------------')
print(fullList)
#print(fullList)