# This Script Makes SQL quires to the database then outputs the info in a JSON format
# This Script is run by a cron job on the host.


import sqlite3
import json
from unicodedata import name
import datetime
import requests

totry = 0
final = 0
between = 0

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('/var/lib/docker/volumes/uptime-kuma/_data/kuma.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
  
    # Finds the number of monitors that we are using
    query = "SELECT COUNT(id) FROM monitor"
    cursor.execute(query)
  
    # Fetch result
    result = cursor.fetchall()
    totry = result.pop()[0]
    
    # Finds the most recent heartbeat
    query = "SELECT id FROM heartbeat ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
  
    # Fetch result
    result = cursor.fetchall()
    final = result.pop()[0]

    between = final - (totry + 20)


    # Finds Selects the monitor name and the status
    query = "SELECT monitor.name, status FROM heartbeat INNER JOIN monitor ON monitor.id = heartbeat.monitor_id WHERE heartbeat.id BETWEEN " + str(between) + " AND " + str(final)
    cursor.execute(query)
  
    # Fetch and output result
    result = cursor.fetchall()
    heartbeat = result

    # Finds the id and name of each monitor
    query = "SELECT name, id FROM monitor"
    cursor.execute(query)
  
    # Fetch and output result
    result = cursor.fetchall()
    nameList = result
  
    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print('Error occured - ', error)
    f = open("errorfile.txt", "w")
    f.write('Error occured - ', error)
    f.close()


finally:
    
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')


beatdict = {}
for item in heartbeat:
    if beatdict.get(item[0]) == None:
        beatdict.update({item[0]: item[1]})

namedict = {}
for line in nameList:
    namedict.update({line[0]: line[1]})

jsonob = "let incoming = '" + str(json.dumps(beatdict)) + "\'"
nameob = "let nameList = '" + str(json.dumps(namedict)) + "\'"
now = datetime.datetime.now()
time = '// ' + now.strftime("%Y-%m-%d %H:%M:%S")

r = requests.post('http://localhost:5000/update', data={'status': jsonob, 'mid': nameob, 'time': time})