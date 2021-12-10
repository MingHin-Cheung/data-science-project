import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, plot_confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

def model():
    df = pd.read_csv("./../../Dataset/cleaned_data.csv", index_col=0)
    
    #Adding a new column for years
    df["CRASH DATE"] = pd.to_datetime(df["CRASH DATE"])
    df["year"] = df["CRASH DATE"].dt.year
    df["year"].unique()

    #Adding a month column for months
    df["month"] = df["CRASH DATE"].dt.month
    df["month"].unique()

    # Setting our training and target variables
    X = df.drop(["CRASH DATE", "CRASH TIME", "BOROUGH", "year", "month"], axis=1)
    y = df["BOROUGH"]

    #Splitting our dataset for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    #Model instantiation
    logreg = LogisticRegression()

    #Model fitting
    logreg.fit(X_train, y_train)

    #Model Prediction
    pred = logreg.predict(X_test)

    # Confusion Matrix
    cm = confusion_matrix(y_test, pred)

    #Classification report of our model
    print(classification_report(y_test, pred))

model()
