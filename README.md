# Ex-01_DS_Data_Cleansing
# AIM
To read the given data and perform data cleaning and save the cleaned data to a file.

# Explanation
Data cleaning is the process of preparing data for analysis by removing or modifying data that is incorrect ,incompleted , irrelevant , duplicated or improperly formatted. Data cleaning is not simply about erasing data ,but rather finding a way to maximize datasets accuracy without necessarily deleting the information.

# ALGORITHM
## STEP-1
Read the given Data

## STEP-2
Get the information about the data

## STEP-3
Remove the null values from the data

## STEP-4
Save the Clean data to the file

# CODE:
## DATA SET:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("Data_set (2).csv")

print(df)

df.head(10)

df.describe()

df.info()

df.tail()

df.shape

df.columns

df.isnull().sum()

~df.duplicated()

df=df[~df.duplicated()]

df=df.dropna()

df=df.fillna(0)

df["original_network"]=df["original_network"].fillna(df["original_network"].mode()[0])

df["current_overall_rank"]=df["current_overall_rank"].fillna(df["current_overall_rank"].median)

df["rating"]=df["rating"].fillna(df["rating"].median)

df["lifetime_popularity_rank"]=df["lifetime_popularity_rank"].fillna(df["lifetime_popularity_rank"].mean)

df["watchers"]=df["watchers"].fillna(df["watchers"].median)

print(df)

## LOAN DATA SET:
import pandas as pd

import numpy as np

import seaborn as sns

from google.colab import files

uploaded = files.upload()

df = pd.read_csv("Loan_data (2).csv")

print(df)

df.head(10)

df.info()

df.tail()

df.shape

df.columns

df.isnull().sum()

~df.duplicated()
df=df[~df.duplicated()]

df=df.dropna()

df=df.fillna(0)

df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0]) 

df["Loan_ID"]=df["Loan_ID"].fillna(df["Loan_ID"].mean)

df["ApplicantIncome"]=df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean)

df["CoapplicantIncome"]=df["CoapplicantIncome"].fillna(df["CoapplicantIncome"].median)

df["LoanAmount"]=df["LoanAmount"].fillna(df["LoanAmount"].median)

df["Married"]=df["Married"].fillna(df["Married"].mode()[0])

df["Education"]=df["Education"].fillna(df["Education"].mode()[0])

df["Dependents"]=df["Dependents"].fillna(df["Dependents"].mean)

df["Loan_Amount_Term"]=df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median)

df["Credit_History"]=df["Credit_History"].fillna(df["Credit_History"].median)

df["Self_Employed"]=df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

df["Property_Area"]=df["Property_Area"].fillna(df["Property_Area"].mode()[0])

print(df)

# OUTPUT:
## DATA SET:
![Screenshot (76)](https://user-images.githubusercontent.com/127846109/232232480-1b9c7c1f-7428-454f-9b86-aca32c958ae1.png)



![Screenshot (77)](https://user-images.githubusercontent.com/127846109/232232496-2acfeadc-847a-4a23-9118-89e1972073e2.png)



![Screenshot (78)](https://user-images.githubusercontent.com/127846109/232232505-d170bf30-3975-40d0-9da8-0cbb748de1a3.png)



![Screenshot (79)](https://user-images.githubusercontent.com/127846109/232232517-330a6432-a673-4c83-852d-2ddd595fe444.png)



![Screenshot (80)](https://user-images.githubusercontent.com/127846109/232232528-8a1a3cdd-9ac5-42e8-aeea-b2907264baf2.png)



![Screenshot (81)](https://user-images.githubusercontent.com/127846109/232232549-7d3ff9a0-ca0d-4c0c-8e81-066afa4f32e2.png)



![Screenshot (82)](https://user-images.githubusercontent.com/127846109/232232563-ae4eb243-9292-4a68-b1e2-7106bf3431fe.png)



![Screenshot (83)](https://user-images.githubusercontent.com/127846109/232232590-a95e2ad0-3618-4876-9cf4-0e8a62690e83.png)



![Screenshot (84)](https://user-images.githubusercontent.com/127846109/232232610-3d6adc52-3112-4847-a562-f418067baf3e.png)



![Screenshot (85)](https://user-images.githubusercontent.com/127846109/232232620-775773e5-5d7d-4759-bab5-5f95af2aece5.png)



![Screenshot (86)](https://user-images.githubusercontent.com/127846109/232232632-3c2486d2-2191-4c73-bc36-e576a078d15d.png)

## LOAN DATA SET:
![Screenshot (87)](https://user-images.githubusercontent.com/127846109/232232954-2eb12c12-7c76-435b-9491-4cb9d4de1016.png)



![Screenshot (88)](https://user-images.githubusercontent.com/127846109/232232961-c3316abe-6775-479e-b553-43749923b075.png)



![Screenshot (89)](https://user-images.githubusercontent.com/127846109/232232971-7ba76794-912e-4cdf-8611-57c98ea06d16.png)



![Screenshot (90)](https://user-images.githubusercontent.com/127846109/232232982-35e97c91-ecfc-4c66-9eec-8b0a8f44f4e4.png)



![Screenshot (91)](https://user-images.githubusercontent.com/127846109/232232986-a1f29000-eccf-4da2-853e-df560b7459a7.png)



![Screenshot (92)](https://user-images.githubusercontent.com/127846109/232232993-32aff3c1-c62b-46e5-bfdd-415af70f67a9.png)



![Screenshot (93)](https://user-images.githubusercontent.com/127846109/232233001-4be67e97-1b75-481c-a8cb-70f6acae793b.png)



![Screenshot (94)](https://user-images.githubusercontent.com/127846109/232233013-aabfb761-37ac-4389-98f1-b069a218998c.png)



![Screenshot (95)](https://user-images.githubusercontent.com/127846109/232233021-c115b2b9-c6d6-4c29-9534-d0e6a4e7dd65.png)



![Screenshot (96)](https://user-images.githubusercontent.com/127846109/232233026-ca72a718-7e1c-4757-9276-43890a3b56b0.png)



# RESULT:
Thus the data cleaning for the given data set is executed and output was verified successfully.
