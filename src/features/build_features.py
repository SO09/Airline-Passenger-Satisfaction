import pandas as pd

def process_data(df):
    
    """Process data by encoding categorical variables and handling missing values."""
    df = df.drop(['Unnamed: 0', 'id'], axis=1)
    df['Gender'] = df['Gender'].replace({'Female': 1, 'Male': 0})
    df['Customer Type'] = df['Customer Type'].replace({'Loyal Customer': 1, 'disloyal Customer': 0})
    df['Type of Travel'] = df['Type of Travel'].replace({'Business travel': 1, 'Personal Travel': 0})
    df['Class'] = df['Class'].replace({'Business': 2, 'Eco Plus': 1, 'Eco': 0})
    df['satisfaction'] = df['satisfaction'].replace({'satisfied': 1, 'neutral or dissatisfied': 0})
    df['Arrival Delay in Minutes'].fillna(df['Arrival Delay in Minutes'].median(), inplace=True)
    
    return df
