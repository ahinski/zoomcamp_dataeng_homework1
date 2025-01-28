import wget
import os
import argparse
import pandas as pd

def main(args):
    url = args.url
    csv_name = args.csv_name
    path = args.path

    filename = wget.download(url)

    data = pd.read_csv(filename)
    data.to_csv(path+csv_name+'.csv')
    
    os.remove(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download data and save as csv')
    parser.add_argument('--url', required=True, help='url of the csv file')
    parser.add_argument('--csv_name', required=True, help='name of the output csv file')
    parser.add_argument('--path', nargs='?', const='', help='path for the output csv file')

    args = parser.parse_args()

    main(args)

