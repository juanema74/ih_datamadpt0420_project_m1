import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Specify path and url...')
    parser.add_argument('-p', "--path", type=str, help="Specify path...", required=True)
    parser.add_argument('-u', "--url", type=str, help="Specify url...")
    parser.add_argument('-c', "--country", type=str, dest="country", help='specify country to analyze...')
    args = parser.parse_args()
    return args

def main(args):
    data_base = mac.proyect_data(args.path)
    jobs = mwr.job_id(data_base)
    data_jobs = mwr.get_jobs(jobs)
    df_countries = mwr.get_info(args.url)
    rural_clean = mwr.rural_column(data_base)
    merged_data = mwr.merged_info(data_base, df_countries, data_jobs)
    grouped_rural = man.analyze(merged_data)
    filter_data = mwr.filter_country(grouped_rural, args.country)
    #filter_data = mwr.filter_country(grouped_rural, args.country)

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)

