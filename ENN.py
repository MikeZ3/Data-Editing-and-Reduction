import numpy as np
import pandas as pd
from collections import Counter
from scipy.spatial.distance import pdist, squareform

#validation
while True:
    file_name = input('Enter the csv file name with Normalized Values: ')
    if file_name[-3:] == 'csv':
        break
    print ('Please enter a valid csv file name')
print('This is the ENN algorithm')
while True:
    k_input = input('Enter the k parameter: ')
    k_input = int(k_input)
    if k_input>=0:
        break
    print ('Please enter a valid k parameter')

file = pd.read_csv(file_name)
# Test Set
test_set = (file.iloc[:,:-1]).to_numpy()
# Edited Set
edited_set = file

classes=[]
distances=[]
index=[]
positions=[]
# time:~12sec and ~6 GB RAM
distances = squareform(pdist(test_set))
# find the k smallest distances (k+1 is because np.argpartition() includes distance from itself)
minsPositions=np.argpartition(distances,k_input+1)[:,:k_input+1]
# clear memory
distances = None
del distances
# More Memory efficient ways (about 0.1 GB RAM)- but way too slow:
# for i in range (nrows):
#     distances.clear()
#     for j in range (nrows):
#         if not(i==j):
# time:~17mins
            # distances.append(np.linalg.norm(test_set[i]-test_set[j]))
# time:~35mins
            # distances.append(sum((p1-p2)**2 for p1,p2 in zip(test_set[i],test_set[j])))
#time:~35mins
            # distances.append(np.einsum('i,i->',test_set[i]-test_set[j],test_set[i]-test_set[j],optimize='greedy'))
# time:~12mins
            # distances.append(np.dot(test_set[i]-test_set[j],test_set[i]-test_set[j]))
for i in range (len(minsPositions)):
    classes.clear()
    for j in range (k_input+1):
        # if it's not the distance of itself
        if(i!=minsPositions[i][j]):
            classes.append(file.iloc[minsPositions[i][j],-1])
    counter = Counter(classes)
    most_common_class = counter.most_common(1)[0][0]
    if not(most_common_class.__eq__(file.iloc[i,-1])):
        index.append(i)
edited_set=edited_set.drop(index)
edited_set_filename=file_name[:-4]+'ENN.csv'
edited_set.to_csv(edited_set_filename)
print("Success!")
