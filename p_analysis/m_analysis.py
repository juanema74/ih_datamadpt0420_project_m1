import pandas as pd

#analysis functions

def analyze(df_data):
    grouped = df_data.groupby(['Country', 'Job_title', 'Rural'], as_index=False).count()
    grouped['Percentage'] = grouped['Quantity'].apply(lambda qtty: str((qtty * 100 / grouped['Quantity'].sum()).round(2))+ '%')
    grouped.to_csv('/Users/juandediegosuanzes/desktop/ih_datamadpt0420_project_m1/data/raw/data_grouped.csv', index=False)
    return grouped


