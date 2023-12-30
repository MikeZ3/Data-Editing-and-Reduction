import numpy as np
import pandas as pd

#validation
while True:
    file_name = input('Enter the csv file name with Normalized Values: ')
    if file_name[-3:] == 'csv':
        break
    print ('Please enter a valid csv file name')
print('This is the IB2 algorithm')

file = pd.read_csv(file_name)
test_set = (file.iloc[:,:]).to_numpy()
condensed_set = np.array([file.iloc[0]])
test_set=np.delete(test_set,0,0)
indexes=[]
distances=[]
for index,testItem in enumerate(test_set,start=1):
    distances.clear()
    # item without the class
    tsItem=testItem[:-1]
    for condesedItem in condensed_set:
        # item without the class 
        csItem=condesedItem[:-1]
        distances.append(np.dot(tsItem-csItem,tsItem-csItem))
    # index of min distance
    minPosition=np.argmin(distances,axis=0)
    # if items don't belong to the same class, add item to CS
    if testItem[-1]!=condensed_set[minPosition][-1]:
        condensed_set=np.vstack((condensed_set,testItem))
    else:
        # append the indexes that won't be contained in CS
        indexes.append(index)
    test_set=np.delete(test_set,0,0)
condensed_set_filename=file_name[:-4]+'IB2.csv'
condensed_set=file.drop(indexes)
condensed_set.to_csv(condensed_set_filename)
print("Success!")
