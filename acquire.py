# inside acquire.py script:
from env import uname, pwd, host
import pandas as pd
import os

######### USE THIS FOR THE NEW TELCO DATASET!!!!
def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df.
    '''
    filename = "telco_new.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename,index_col=False)
    else:
        sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
        # Read in DataFrame from Codeup db.
        df = pd.read_sql(sql_query, get_sql_url('telco_churn'))
        df.to_csv(filename,index=False)
        return df


#----------------------------------------------------
    