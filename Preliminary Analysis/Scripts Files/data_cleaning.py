# Import library

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def data_cleaning():
    #importing our dataset
    df = pd.read_csv("./../../Dataset/Motor_Vehicle_Collisions_-_Crashes.csv")
    
    #Taking 50,000 random samples from our data.
    df = df.sample(n=50000)
    
    #Keeping only the required features
    columns = ["CRASH DATE", "CRASH TIME", "BOROUGH", "LATITUDE", "LONGITUDE", "NUMBER OF PERSONS INJURED",\
          "NUMBER OF PERSONS KILLED","NUMBER OF PEDESTRIANS INJURED", "NUMBER OF PEDESTRIANS KILLED",\
          "NUMBER OF CYCLIST INJURED", "NUMBER OF CYCLIST KILLED", "NUMBER OF MOTORIST INJURED",\
          "NUMBER OF MOTORIST KILLED"]
    
    #Keeping only the required features in our dataset
    df = df[columns]

    #Filling missing values
    df["LATITUDE"].fillna(df["LATITUDE"].mean(), inplace=True)
    df["LONGITUDE"].fillna(df["LONGITUDE"].mean(), inplace=True)
    df.dropna(inplace=True)

    #Fixing the datatype
    df["LATITUDE"] = df["LATITUDE"].astype("float64")
    df["LONGITUDE"] = df["LONGITUDE"].astype("float64")

    #Saving our cleaned data in a csv file
    df.to_csv("./../../Dataset/cleaned_data.csv")
data_cleaning()
