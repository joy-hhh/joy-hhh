import pandas as pd
df = pd.DataFrame({'a':[10,20,30], 'b':[20,30,40]})
print(df)

def my_sq(x):
	return x ** 2

print(df['a'] ** 2)
print(df['a'].apply(my_sq))

import seaborn as sns
titanic = sns.load_dataset("titanic")
# print(titanic)
# print(titanic)
# print(titanic.info())

print(titanic.head())
print(titanic.columns)
print(titanic.shape)

import numpy as np

def count_missing(vec):
	null_vec = pd.isnull(vec)
	null_count = np.sum(null_vec)
	return null_count

cmis_col = titanic.apply(count_missing)
# print(cmis_col)

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num/dem

pmis_col = titanic.apply(prop_missing)
print(pmis_col)

def prop_complete(vec):
	return 1 - prop_missing(vec)

cmis_row = titanic.apply(count_missing, axis = 1)
pmis_row = titanic.apply(prop_missing, axis = 1)
pcom_row = titanic.apply(prop_complete, axis = 1)

print(cmis_row.head())
print(pmis_row.head())
print(pcom_row.head())
