# Preliminary Analysis

# Project Title
NYC Vehicle Collision Data Science Project

### Group Members
- Kazi Siam
- Ming Hin Cheung

### Repository Structure
- `./../Dataset`
  - `Motor_Vehicle_Collisions_-_Crashes.cvs`: Raw NYC collisions data from the NYC Open data.
  - `cleaned_data.csv`: Cleaned dataset for modeling.

- `Jupyter Notebook` 
  - `data_cleaning.ipynb`: Includes code for data cleaning and pre-processing. It also contains the data dictionary. 
  - `EDA.ipynb`: Includes code for exploratory data analysis on our data with different statistical descriptions and graph interpretations.
  - `logistic_regression.ipynb`: Includes the code for our model and its classification report.

- `Scripts`
  - `data_cleaning.py`: Script for data cleaning and pre-processing.
  - `EDA.py`: Script for exploratory data analysis, including descriptive statistics and charts.
  - `logistic_regression.py`: Script for our model and its classification report.

### Exploratory Analysis
- We use Matplotlib and Seaborn to analyze our data and see trends in our data. We see which year has the most collisions, which borough has more collisions overall, how many people get killed each year. There are several features that we don’t need in our predictive model such as COLLISION ID, ZIP CODE, etc. that we have dropped in our “./Jupyter Notebook/logistic_regression.ipynb” and “./Jupyter Notebook/data_cleaning.ipynb” notebook. After analyzing and choosing the required features, we will use the Logistic Regression model for predicting borough. This model tends to work well with large datasets.

### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

- The major challenges in this problem include dealing with a lot of missing values and choosing the right features. Fortunately, the dataset is huge so we will use the technique of dropping the null values in our target variable and filling the rest of the missing values in other columns with mean since there are no outliers detected.

### Future Work
Describe what work you are planning to complete for the final analysis.

- For future work, we will build a model for each of our problems such as:
  - Which borough would have more accidents in a given month?
  - Which borough would have more accidents in a given year?

### Contributions
Describe the contributions that each group member made.

- We worked as a team. We have done everything together via Zoom. Therefore, it was a 50/50 contribution.
