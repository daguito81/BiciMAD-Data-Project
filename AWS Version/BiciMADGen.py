# Import libraries to use
import json
import requests
import pandas as pd
import datetime
from sqlalchemy import create_engine
import psycopg2

psycopg2.Date # This is just to get rid of the error message for not using psycopg2
# credentials = json.loads(open("credentials.json").read()) # Credentials are stored in a separate file
# psqlcred = json.loads(open("psqlpass.json").read()) # Credentials are stored in a separate file

# The next part creates the complete URL to get the data as it's URL/id/Pass
url = 'https://rbdata.emtmadrid.es:8443/BiciMad/get_stations' #URL to get stations for all data
a = "/" + "API USERNAME"
b = "/" + "API KEY HERE"

response = requests.get(url + a + b) # Here we make the data requests to get the state of all stations.

data = response.json()['data'] # This parses it as a json but then it has only 1 main key which is 'data'
test1 = json.loads(data) # Here we tried to grab only the data under 'data' and parse it as a dict

mydict = {}
for i, result in enumerate(test1['stations']):
    mydict[i + 1] = result

df = pd.DataFrame.from_dict(mydict, orient='index') # We create the data frame with the orient='index'

df['timestamp'] = datetime.datetime.now()
df['year'] = datetime.datetime.now().year
df['month'] = datetime.datetime.now().month
df['day'] = datetime.datetime.now().day
df['hour'] = datetime.datetime.now().hour
df['minute'] = datetime.datetime.now().minute

# Now we send the data to the database
engine = create_engine('postgresql://username:password@awspsqladdress:5432/bicimaddb')
df.to_sql('bicimaddata', engine, if_exists='append') # Data is now in Database

print("Data is in Database: " + str(datetime.datetime.now()))
