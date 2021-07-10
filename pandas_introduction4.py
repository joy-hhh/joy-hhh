#-*-coding:utf-8-*-

import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")

import numpy as np

def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)

def prop_missing(vec):
    num = count_missing(vec)
    dem =vec.size
    return num /dem

pmis_col = titanic.apply(prop_missing)
print(pmis_col)

