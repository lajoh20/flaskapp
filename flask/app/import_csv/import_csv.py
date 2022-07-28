import pandas as pd
def import_csv():
    df = pd.read_csv('flask/app/import_csv/Brand Dataset.csv')

    return(df.to_string()) 

