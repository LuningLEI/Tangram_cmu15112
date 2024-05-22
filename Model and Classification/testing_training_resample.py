import pandas as pd
import os
os.getcwd()
os.name
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

thyroid_default_data = pd.read_csv("Thyroid_Diff.csv")
data = thyroid_default_data.rename(columns={"Physical Examination":"Physical_Examination","Thyroid Function":"Thyroid_Function","Hx Radiothreapy":"Hx_Radiothreapy","Hx Smoking":"Hx_Smoking"})
Recurred = data.Recurred.replace("No",0)
data["Recurred"] = Recurred
Recurred = data.Recurred.replace("Yes",1)
data["Recurred"] = Recurred
shuffled_df = data.sample(frac=1, random_state=42).reset_index(drop=True)
# Select the first 100 rows
testing = shuffled_df.iloc[:100]
testing.to_csv("testing.csv",index = False)
training = shuffled_df.iloc[100:]
testing.to_csv("traning.csv",index = False)
