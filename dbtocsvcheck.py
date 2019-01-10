# Import libraries to use

import pandas as pd
import datetime
from sqlalchemy import create_engine
import psycopg2


def get_Data():

    psycopg2.Date
    engine = create_engine('postgresql://user:password@awspsqladdress:5432/bicimaddb')
    newdf = pd.read_sql_table('bicimaddata', con=engine)
    timelapsed = newdf['timestamp'].value_counts().sort_index().index[-1] - newdf['timestamp'].value_counts().sort_index().index[0]

    # print(newdf.tail(3))
    print("-------------------------------------------------")
    print(newdf.info())
    print("-------------------------------------------------")
    print(len(newdf['timestamp'].value_counts().sort_index()), " minutes in DB")

    print("-------------------------------------------------")
    print("Time running: ")
    print(timelapsed.days, " Days")
    print(round(timelapsed.seconds / 60 / 60, 2), " Hours")
    print(round(timelapsed.seconds / 60, 2), " Minutes")
    print("-------------------------------------------------")
    print("Start: ", newdf['timestamp'].value_counts().sort_index().index[0])
    print("End: ", newdf['timestamp'].value_counts().sort_index().index[-1])
    print("Rows: ", str(len(newdf['timestamp'])))

    newdf.to_csv('./Data/' + str(datetime.datetime.now().date()) + '-' + 'newdf.csv', index=False)
    newdf.to_csv('./Data/updated-newdf.csv', index=False)


if __name__ == '__main__':
    get_Data()
