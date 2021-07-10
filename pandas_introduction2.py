import pandas as pd
import seaborn as sns
tips = sns.load_dataset("tips")
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.dtypes)


