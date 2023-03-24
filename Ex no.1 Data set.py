import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
print(df)
df.head(10)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.describe()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.info()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.tail()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.shape

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.columns

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df.isnull().sum()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
~df.duplicated()
df=df[~df.duplicated()]

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df=df.dropna()
print(df)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df=df.fillna(0)
print(df)

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("Data_set (2).csv")
df["original_network"]=df["original_network"].fillna(df["original_network"].mode()[0])
df["current_overall_rank"]=df["current_overall_rank"].fillna(df["current_overall_rank"].median)
df["rating"]=df["rating"].fillna(df["rating"].median)
df["lifetime_popularity_rank"]=df["lifetime_popularity_rank"].fillna(df["lifetime_popularity_rank"].mean)
df["watchers"]=df["watchers"].fillna(df["watchers"].median)
print(df)
