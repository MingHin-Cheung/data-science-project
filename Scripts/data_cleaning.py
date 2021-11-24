import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes.csv")
df = df.sample(n=50000)

columns = ["CRASH DATE", "CRASH TIME", "BOROUGH", "LATITUDE", "LONGITUDE", "NUMBER OF PERSONS INJURED",\
          "NUMBER OF PERSONS KILLED","NUMBER OF PEDESTRIANS INJURED", "NUMBER OF PEDESTRIANS KILLED",\
          "NUMBER OF CYCLIST INJURED", "NUMBER OF CYCLIST KILLED", "NUMBER OF MOTORIST INJURED",\
          "NUMBER OF MOTORIST KILLED"]

df = df[columns]
df.dropna(subset=["BOROUGH"], inplace=True)
df["LATITUDE"].fillna(df["LATITUDE"].mean(), inplace=True)
df["LONGITUDE"].fillna(df["LONGITUDE"].mean(), inplace=True)
df.dropna(inplace=True)
df["LATITUDE"] = df["LATITUDE"].astype("float64")
df["LONGITUDE"] = df["LONGITUDE"].astype("float64")
df.to_csv("cleaned_data.csv")