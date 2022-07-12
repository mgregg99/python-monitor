import requests
from bs4 import BeautifulSoup
import json

# Get the data from UK and make the Beautiful soup object
r = requests.get('http://ut.ls.byu.edu/status/scrape')
soup = BeautifulSoup(r.content, 'html.parser')

# Get the line from the soup object
messyLine = ""
for line in soup.find_all('script'):
    if str(line).find('window.preloadData') != -1:
        messyLine = str(line)

# Clean the line
messyLine = messyLine.replace('window.preloadData = ', '')
messyLine = messyLine.replace('</script>', '')
messyLine = messyLine.replace('<script>', '')

# conver the string to a json object
jsonLine = json.loads(messyLine)

# get the data from the json object
monitorList = {}
for line in jsonLine['publicGroupList'][0]['monitorList']:
    monitorList.update({line['id']: line['name']})

# Grab status from the api
idList = []
r = requests.get('http://ut.ls.byu.edu/api/status-page/heartbeat/scrape')
jsonLine = json.loads(r.content)

# Create a list of the ids
for line in jsonLine['heartbeatList']:
    idList.append(line)

for line in idList:
    print(type(jsonLine['heartbeatList'][line]))












    

    