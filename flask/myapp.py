from crypt import methods
from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import json

def apiScrape():
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
        monitorList.update({int(line['id']): line['name']})

    # Grab status from the api
    idList = []
    r = requests.get('http://ut.ls.byu.edu/api/status-page/heartbeat/scrape')
    jsonLine = json.loads(r.content)

    # Create a list of the ids
    for line in jsonLine['heartbeatList']:
        idList.append(int(line))

    statusList = {}
    for line in idList:
        statusList.update({int(line): jsonLine['heartbeatList'][str(line)][9]['status']})

    returnList = []
    for line in statusList:
        templist = [str(monitorList[line]), str(statusList[line])]
        returnList.append(templist)
    
    return returnList

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    monitorList = apiScrape()
    upnum = 0
    downnum = 0
    for line in monitorList:
        if line[1] == '1':
            upnum += 1
        else:
            downnum += 1

    return render_template('index.html', monitorList=monitorList, upnum=upnum, downnum=downnum)

# return the favicon
@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico', mimetype='image/ico')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)