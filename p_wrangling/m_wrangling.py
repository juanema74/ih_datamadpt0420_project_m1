import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#Cleaning functions
def rural_column(df_data):
    print('Cleaning rural columns...')
    df_data['rural'] = df_data['rural'].str.lower()
    df_data['rural'] = df_data['rural'].str.replace('city', 'urban').replace('non-rural', 'urban').replace('countryside', 'rural').replace('country', 'rural')
    print('Rural column cleaned...')
    return df_data


def job_id(df_normalized_job_codes):
    jobs_id = list(df_normalized_job_codes['normalized_job_code'].unique())
    print('importing api info...')
    return jobs_id

#Function to have the info of the api (jobs)
def get_jobs (jobs_id):
    print('calling api...')
    jobs_api = []
    for job in jobs_id:
        if job == None:
            pass
        else:
            response = requests.get(f'http://api.dataatwork.org/v1/jobs/{job}')
            jobs_json = response.json()
            jobs_api.append(jobs_json)
    df_jobs = pd.DataFrame(jobs_api)
    df_jobs = pd.DataFrame((jobs_api), columns=['uuid', 'title', 'normalized_job_title'])
    df_jobs = df_jobs.rename(columns={'uuid': 'normalized_job_code'})
    return df_jobs

#Function to have the info of web scraping (countries)
def get_info(countries):
    print('getting web scraping info...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table')

    dirty_list = []
    rows = table.find_all('tr')
    for tr in rows:
        element_row = tr.find_all('td')
        for td in element_row:
            dirty_list.append(td.text)

    clean_list = []
    for i in dirty_list:
        f = i.replace('\n', '').replace('(','').replace(')','')
        clean_list.append(f)

    row_split = 2
    rows_refactored = [clean_list[x:x+row_split] for x in range(0, len(clean_list), row_split)]
    df_countries = pd.DataFrame(rows_refactored, columns={'country_name', 'country_code'})
    #df_countries['country_code'].replace({'EL': 'GR'}, inplace=True)
    return df_countries

#Function to merge the 3 data sources/tables
def merged_info(df_data, df_countries, df_jobs):
    print('Merging 3 data sources info...')
    merged_table1 = df_data.merge(df_countries, how='left', on='country_code')
    merged_table2 = merged_table1.merge(df_jobs, how='left', on='normalized_job_code')
    merged_table2.rename(columns={'country_name': 'Country', 'title': 'Job_title', 'rural': 'Rural', 'uuid': 'Quantity'}, inplace=True)
    merged_table2['Job_title'].fillna('Unemployed', inplace=True)
    final_table = merged_table2[['Country', 'Job_title','Rural', 'Quantity']]
    final_table.to_csv('/Users/juandediegosuanzes/desktop/ih_datamadpt0420_project_m1/data/raw/data_merged.csv', index=False)
    return final_table


#Function to filter the info by country
def filter_country(grouped, country):
    filter = country
    if filter in list(grouped['Country']):
        df_country = (grouped[grouped['Country'] == filter].groupby(
            ['Country', 'Job_title', 'Rural', 'Percentage']).agg({'Quantity': 'sum'}).reset_index())
        print(df_country)
    else:
        df_country = (
            grouped.groupby(['Country', 'Job_title', 'Rural', 'Percentage']).agg({'Quantity': 'sum'}).reset_index())
        print(df_country)
    df_country.to_csv(f'data/raw/{country}_filtered.csv', index=True)
    return df_country



