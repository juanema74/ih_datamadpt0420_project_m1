import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
#from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Specify path and url...')
    parser.add_argument("-p", "--path", type=str, help="Specify path...", required=True)
    parser.add_argument("-u", "--url",type=str, help="Specify url...", required=True)
    args = parser.parse_args()
    return args

def main(arguments):
     data_base = mac.proyect_data(arguments.path)
     countries = mwr.get_info(arguments.url)
     juanito = mwr.data_merged(data_base, countries)


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)