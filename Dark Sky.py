# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#lodaing necessary functions
from forecastiopy import *

#API key to access data from Black Sky
api_key = '04c3089921e925fc01edd9c7c4ee2386'

#Creating list for latitudes and longitudes of each city
loc = [\
        ["\'Anchorage, Alaska'", 61.2181, -149.9003],\
        ["\'Buenos Aires, Argentina'", -34.6037, -58.3816],\
        ["\'São José dos Campos, Brazil'", -23.2237, -45.9009],\
        ["\'San José, Costa Rica'", 9.9281, -84.0907],\
        ["\'Nanaimo, Canada'", 49.1659, -123.9401],\
        ["\'Ningbo, China'", 29.8683, 121.5440],\
        ["\'Giza, Egypt'", 30.0131, 31.2089],\
        ["\'Mannheim, Germany'", 49.4875, 8.4660],\
        ["\'Hyderabad, India'", 17.3850, 78.4867],\
        ["\'Tehran, Iran'", 35.6892, 51.3890],\
        ["\'Bishkek, Kyrgyzstan'", 42.8746, 74.5698],\
        ["\'Riga, Latvia'", 56.9496, 24.1052],\
        ["\'Quetta, Pakistan'", 30.1798, 66.9750],\
        ["\'Warsaw, Poland'", 52.2297, 21.0122],\
        ["\'Dhahran, Saudia Arabia'", 26.2361, 50.0393],\
        ["\'Madrid, Spain'", 40.4168, -3.7038],\
        ["\'Oldham, United Kingdom'", 53.5409, -2.1114] 
        ]

# Get a five-day min and max temperature forecast
# fc stands for forecast
fc = []
for i in loc:
    fc.append(i[0])
    TotalMin = 0
    TotalMax = 0
    weather = ForecastIO.ForecastIO( api_key, latitude=i[1], longitude=i[2], units = "si")
    daily = FIODaily.FIODaily( weather )
    for day in range( 2, 7 ):
        val = daily.get( day )
        fc.append( str( val[ 'temperatureMin' ] ) )
        fc.append( str( val[ 'temperatureMax' ] ) )
        TotalMin = TotalMin + val[ 'temperatureMin' ]
        TotalMax = TotalMax + val[ 'temperatureMax' ]
        MinAvg = str(round((TotalMin/5), 2))
        MaxAvg = str(round((TotalMax/5), 2))
    fc.append(MinAvg)
    fc.append(MaxAvg)   

#separating my list of forecasts into a list of lists
n = 13 
finalfc = [fc[i * n:(i + 1) * n] for i in range((len(fc) + n - 1) // n )]  
#print (finalfc) 

#City,Min 1,Max 1, ... Min 5,Max 5,Min Avg,Max Avg
#print each list using a for loop into the csv
import csv
with open("temp.csv", 'w') as tempcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(tempcsv, delimiter=',')
    writer.writerow(['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2', 'Min 3', 'Max 3', 
                          'Min4', 'Max 4', 'Min 5', 'Max 5', 'Min Avg', 'Max Avg'])
    for item in finalfc:
        #Write item to outcsv
        writer.writerow(item)
        

