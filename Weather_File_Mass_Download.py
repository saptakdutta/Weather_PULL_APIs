# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:48:56 2019

@author: sapta
"""
#%% Import the needed libraries
import requests
import numpy as np

#%% 
base_url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html'
# Create the API header function
def make_header(stn_id, year, month):
    api_headers = {
        'format': 'csv',
        'stationID': stn_id,
        'Year': year,
        'Month': month,
        'Day': 1,
        'timeframe': 1,
        'submit': 'Download+Data'
    }
    return api_headers
    
#%% Put in the scraping details
stn_id = 71628 #This is the WMO ID field
years = np.arange(2009,2016,1) #Create a numpy array range for years
months = np.arange(1,13,1) #Same thing for months

#%% Run the scraping in a loop
folder = 'Ottawa_Intl'
for year in years:
    for month in months:
        header = make_header(stn_id, year, month)
        response = requests.get(base_url, header)
        if response.status_code == 200:
            data = response.content.decode('UTF-8')
            data = data.replace(u'\ufeff', '')
            file = open("c:\\users\\sapta\\Downloads\\Weather_Files\\%s%s_%s.csv"%(folder , str(year), str(month)), 'w+')
            file.write(data)
            file.close()
            
#%% 