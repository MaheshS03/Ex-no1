Ex-01_DS_Data_Cleansing
AIM
To read the given data and perform data cleaning and save the cleaned data to a file.

Explanation
Data cleaning is the process of preparing data for analysis by removing or modifying data that is incorrect ,incompleted , irrelevant , duplicated or improperly formatted. Data cleaning is not simply about erasing data ,but rather finding a way to maximize datasets accuracy without necessarily deleting the information.

ALGORITHM
STEP-1
Read the given Data

STEP-2
Get the information about the data

STEP-3
Remove the null values from the data

STEP-4
Save the Clean data to the file

CODE:
DATA SET:
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

LOAN DATA SET:
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

~df.duplicated() df=df[~df.duplicated()]

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

OUTPUT:
DATA SET:
Screenshot (76)

Screenshot (77)

Screenshot (78)

Screenshot (79)

Screenshot (80)

Screenshot (81)

Screenshot (82)

Screenshot (83)

Screenshot (84)

Screenshot (85)

Screenshot (86)

LOAN DATA SET:
Screenshot (87)

Screenshot (88)

Screenshot (89)

Screenshot (90)

Screenshot (91)

Screenshot (92)

Screenshot (93)

Screenshot (94)

Screenshot (95)

Screenshot (96)

RESULT:
Thus the data cleaning for the given data set is executed and output was verified successfully.
