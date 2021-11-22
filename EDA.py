import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("cleaned_data.csv", index_col=0)
categorical_features = df.select_dtypes(include=[np.object])

#Heatmap of our data
fig, ax = plt.subplots(figsize=(12,6))
sns.heatmap(df.corr(), annot=True, cmap="Reds" )
fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(x=df['BOROUGH'], data=df, ax=ax)
#Adding a new column for years
df["CRASH DATE"] = pd.to_datetime(df["CRASH DATE"])
df["year"] = df["CRASH DATE"].dt.year
df["year"].unique()
#Adding a month column for months
df["month"] = df["CRASH DATE"].dt.month
df["month"].unique()
#Checking for number of collisions by year
fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(x=df['year'], data=df, ax=ax)
#Checking for number of collisions by month
fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(x=df['month'], data=df, ax=ax)
persons_killed_by_year = df.groupby("year")["NUMBER OF PERSONS KILLED"].sum()
