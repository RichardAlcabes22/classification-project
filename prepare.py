import matplotlib.pyplot as plt
import seaborn as sns
import acquire as acq
from env import uname, pwd, host
import pandas as pd
import os
from sklearn.model_selection import train_test_split


def prep_telco(df):
    '''
    Accepts a telco df and drops unneeded columns and encodes required features
    '''
    
    #drop out unneeded or bad columns
    df = df.drop(columns=['total_charges','customer_id'])

    # encode categorical values:
    df = pd.concat(
        [df, pd.get_dummies(df[['gender','partner','dependents','phone_service','paperless_billing','churn',]],
                            drop_first=True)], axis=1)
    return df

def split_data(df, target):
    '''
    split_data will split data into train,val,test based on 
    the values present in a cleaned version of df.  Target parameter is intended to 
    take an argument that specifies the target variable and stratisfies the splits by the target.  
    However, data can be stratified by any column other than the target label if desired.
    
    '''
    train_val, test = train_test_split(df,train_size=0.8,random_state=2013,
                                   stratify=df[target])
    train, validate = train_test_split(train_val,train_size=0.7,random_state=2013,
                                   stratify=train_val[target])
    return train, validate, test


def cat_num_cols(df):
    cat_cols, num_cols = [], []
    for col in df.columns.to_list():
        if df[col].dtype == 'O':
            cat_cols.append(col)
        else:
            if df[col].nunique() < 6:
                cat_cols.append(col)
            else:
                num_cols.append(col)
    return cat_cols, num_cols
#------------------------------------------

def remind_data_prep():
    '''
    A quick function call to print out all possible data prep steps to inspect and execute should
    they be required
    '''
    print(f'-SUMMARIZE with head(),describe().T,info(),isnull(), isnull.sum().isnull.mean(),\n\
          value_counts(), .shape\n\
-PLOT with plt.hist(),plt.boxplot,plt.barchart(),plt.scatter\n\
-DOCUMENT takeaways and outline further cleaning steps to take\n\
-MISSINGNESS...OUTLIERS...DATA ERRORS...TEXT NORMALIZATION (caps vs.lowercase)\n\
-TIDYDATA...CALCULATED COLUMNS...RENAME COLUMNS...DROP COLUMNS\n\
-DATATYPES...SCALE NUMERIC DATA')
    




def ex_cat_cols(cat_cols,train_df):
    for col in cat_cols:
        print(f'Univariate assessment of feature {col}:')
        sns.countplot(data=train_df, x=col)
        plt.show()
        print(
        pd.concat([train_df[col].value_counts(),
        train_df[col].value_counts(normalize=True)],
                axis=1))