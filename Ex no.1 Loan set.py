import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
print(df)
df.head(10)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df.info()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df.tail()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df.shape

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df.columns

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df.isnull().sum()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
~df.duplicated()
df=df[~df.duplicated()]

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df=df.dropna()
print(df)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
df=df.fillna(0)
print(df)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Loan_data (2).csv")
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
