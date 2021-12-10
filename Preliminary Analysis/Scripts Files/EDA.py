import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

def EDA():
    df = pd.read_csv("./../../Dataset/cleaned_data.csv", index_col=0)
    #Checking categorical features in our dataset.

    print(df.head())
    print(df.shape)
    print(df.columns)
    print(df.isnull().sum())
    #Statistical Summary of our data
    print(df.describe())
    #Checking categorical features in our dataset.
    categorical_features = df.select_dtypes(include=[np.object])
    print(categorical_features.columns)

    #Heatmap of our data
    fig, ax = plt.subplots(figsize=(12,6))
    sns.heatmap(df.corr(), annot=True, cmap="Reds" )
    print(df.max())
    print(df.min())
    #Checking skewness
    print(df.skew())
    #Checking kurtosis
    print(df.kurt())
    #Boroughs with their collision numbers
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(x=df['BOROUGH'], data=df, ax=ax)
    plt.show()
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
    plt.show()
    #Checking for number of collisions by month
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(x=df['month'], data=df, ax=ax)
    plt.show()
    #Boroughs with most number of deaths
    killed_by_borough = df.groupby("BOROUGH")[["NUMBER OF PERSONS KILLED", "NUMBER OF PEDESTRIANS KILLED",\
                                               "NUMBER OF CYCLIST KILLED"]].sum()
    print(killed_by_borough)
    killed_by_borough.plot.bar(figsize=(12,6))
    persons_killed_by_year = df.groupby("year")["NUMBER OF PERSONS KILLED"].sum()
    print(persons_killed_by_year)
    #Pie chart for persons killed by year
    fig, ax  = plt.subplots(figsize=(16, 8))
    fig.suptitle('Persons killed by year', size = 14, color = "black")
    ax = plt.pie(persons_killed_by_year, labels=persons_killed_by_year.index,
           autopct='%1.0f%%',
           pctdistance=0.9)
    print(ax)
EDA()
