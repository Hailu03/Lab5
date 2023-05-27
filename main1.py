from scipy.io import arff
import pandas as pd
from scipy.io import arff
import apyori
from apyori import apriori

# Load the data set.
data = arff.loadarff("supermarket.arff")
df = pd.DataFrame(data[0])

# drop the total column
df = df.drop(['total'],axis=1)

# convert the data to a list of attributes
attributes = list(df.columns)

# transform the data into strings and into a numpy matrix for easier handling
sales = df.to_numpy().astype(str)

transactions = [ [] for _ in range(df.shape[0]) ]  #Empty lists to be filled with the specific products purchased.

#We iterate over every element in the sales matrix and, if a product belongs to a transaction, we save it.
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if sales[i,j] == "t":
            transactions[i].append(attributes[j])
    

mins = [0.1,0.2,0.3] # minimum support
minc = 0.9 # minimum confidence

for m in mins:
    # We use the apriori algorithm to find the association rules.
    results = list(apriori(transactions,min_support=m,min_confidence=minc))
    if len(results) > 10:
        for i in range(0,10):
            print(list(results[i][2][0][0]),'->',list(results[i][2][0][1]))
    else:
        for i in range(0,len(results)):
            print(list(results[i][2][0][0]),'->',list(results[i][2][0][1]))
    
    print('There are '+str(len(results))+' rules with a minimum support of '+str(m)+
          ', a minimum confidence of ' +str(minc))
    print('')

mins = 0.1 # minimum support
minc = [0.9,0.8,0.7] # minimum confidence

for m in minc:
    # We use the apriori algorithm to find the association rules.
    results = list(apriori(transactions,min_support=mins,min_confidence=m))
    if len(results) > 10:
        for i in range(0,10):
            print(list(results[i][2][0][0]),'->',list(results[i][2][0][1]))
    else:
        for i in range(0,len(results)):
            print(list(results[i][2][0][0]),'->',list(results[i][2][0][1]))
    
    print('There are '+str(len(results))+' rules with a minimum support of '+str(mins)+
          ', a minimum confidence of ' +str(m))
    print('')

