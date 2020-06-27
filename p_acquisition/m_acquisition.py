import pandas as pd
from sqlalchemy import create_engine

#acquisition functions -- aqui es donde pondre las funciones de las tres primeras tablas unidas (proyect_data)
def data_connect(path):
    sqlitepath = '/Users/juandediegosuanzes/Desktop/ih_datamadpt0420_project_m1/data/raw/raw_data_project_m1.db'
    engine_connection = create_engine(f'sqlite:///./{sqlitepath}')
    proyect_data = pd.read_sql_query(query, engine)
    return proyect_data