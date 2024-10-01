from flask import Flask
from flask import request
import os
import requests

app = Flask(__name__)

staticBurgers= [{"name":"Chiken burger"},
                {"name":"Halloumi burger"},
                {"name":"Hamburger"}
                {"name":"Deluxe burger"}
                {"name":"Vegan burger"}]

def getBurgers():
    return staticBurgers


def renderFrontpage():
    pg = "<h1>Welcome to BurgerOrderer</h1>"
    pg += "<P><UL>"
    
    for b in getBurgers():
        pg += "<LI>" + b["name"]

    pg += "</UL>"
    return pg

def renderOrderingPage(burgerName, args):
    return 'ordered ' + burgerName
    
@app.route('/')
def frontpage():
    return renderFrontpage()

baseURL='http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5000')

def makeURL(burgerName):
    return baseURL + '/buy/' + burgerName

def addOptions(url, args):
    if 0!=len(args):
        url += '?'
        for arg in args:
            url += arg + '&'
    return url

def sendToKitchen(burgerName, args):
    requrl = makeURL(burgerName)
    requrl = addOptions(requrl, args)

    print('Using KitchenView URL: ' + requrl)
    requests.get(requrl)
    return

@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    print('Placing an order on ' + burgerName)
    sendToKitchen(burgerName, request.args)
    return renderOrderingPage(burgerName, request.args)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)


