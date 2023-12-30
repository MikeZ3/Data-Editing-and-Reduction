import pandas as pd
import numpy as np
import csv

while True:
    file_name = input('Enter the csv file name: ')
    if file_name[-3:] == 'csv':
        break
    print ('Please enter a valid csv file name')
pd_file2 = pd.read_csv(file_name)
pd_file = pd_file2.iloc[:,:-1]
names = pd_file2.columns
ncol = len(pd_file.columns)
ncol2 = len(pd_file2.columns)
nrows = pd_file.shape[0]
b=[]
species=[]
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
species.append(np.array(pd_file2[names[ncol]]))
for i in range(ncol):
    b.append(np.array(NormalizeData(np.array(pd_file[names[i]]))))
newFileName = "normalized_"+file_name
with open(newFileName, 'w', newline='') as file:
    write=csv.writer(file)
    write.writerow(names)
    for j in range (nrows):
        for i in range (ncol):
            file.write(str(b[i][j]))
            file.write(",")
        file.write("".join(species[0][j]))
        file.write("\n")
    
print("Success!")