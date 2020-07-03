import pandas as pd
from sqlalchemy import create_engine
from functools import reduce

#acquisition functions -- this will contain the info of the fist tables on the same table (proyect_data)
def proyect_data(path):
    print('collecting database...')
    sqlitepath = path
    engine = create_engine(f'sqlite:///{sqlitepath}')
    tables = pd.read_sql_query("""SELECT name FROM sqlite_master WHERE type = 'table'""", engine)
    tables_list = tables['name'].to_list()
    x = [pd.read_sql_query(f'SELECT * FROM {i}', engine) for i in tables_list]
    df_data = reduce(lambda left, right: pd.merge(left, right, on='uuid'), x)
    df_data.to_csv('/Users/juandediegosuanzes/desktop/ih_datamadpt0420_project_m1/data/raw/df_data.csv')

    return df_data


