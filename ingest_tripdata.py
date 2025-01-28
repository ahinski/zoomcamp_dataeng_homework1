import pandas as pd
from sqlalchemy import create_engine
import argparse

def main(args):
    user = args.user
    password = args.password
    host = args.host
    db = args.db
    table_name = args.table_name
    csv_path = args.csv_path

    # parse_dates for pickup and dropoff dates. better to use some kind of config for that in the future
    data = pd.read_csv(csv_path, parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'])
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}/{db}')
    
    data.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    data.to_sql(name=table_name, con=engine, if_exists='append', chunksize=10000)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--csv_path', required=True, help='path for the csv file')

    args = parser.parse_args()

    main(args)

