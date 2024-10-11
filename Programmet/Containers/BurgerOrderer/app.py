from flask import Flask, request
import os
import requests

app = Flask(__name__)

staticBurgers = [
    {"name": "Chicken burger"},
    {"name": "Halloumi burger"},
    {"name": "Hamburger"},
    {"name": "Deluxe burger"},
    {"name": "Vegan burger"}
]

options_list = ["3xcheese", "Onions", "Secret sauce", "Tomato", "Pickles"]

def getBurgers():
    return staticBurgers

def renderFrontpage():
    pg = "<h1>Welcome to BurgerOrderer</h1>"
    pg += "<UL>"
    for b in getBurgers():
        pg += f"<LI><a href='/order/{b['name']}'>{b['name']}</a></LI>"
    pg += "</UL>"
    return pg

def renderOrderingPage(burgerName):
    pg = f"<h2>Order {burgerName}</h2>"
    pg += "<form action='/buy' method='get'>"
    pg += f"<input type='hidden' name='burger' value='{burgerName}'>"

    pg += "<label for='quantity'>Quantity of burger: </label>"
    pg += "<input type='number' name='quantity' min='1' value='1'><br><br>"
    
    pg += "<h3>Choose options for burger:</h3>"
    for option in options_list:
        pg += f"<input type='checkbox' name='options' value='{option}'> {option}<br>"
    
    pg += "<input type='submit' value='Order'>"
    pg += "</form>"
    return pg

@app.route('/')
def frontpage():
    return renderFrontpage()

baseURL='http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5000')

def makeURL(burgerName):
    return baseURL + '/buy/' + burgerName

def addOptions(url, args):
    if len(args):
        url += "?"
        list_of_options = []
        
        for key, value in args.items():
            if isinstance(value, list):
                for i in value:
                    list_of_options.append(f"{key}={i}")
            else:
                list_of_options.append(f"{key}={value}")

        url += "&".join(list_of_options)
    return url

def sendToKitchen(burgerName, args):
    requrl = makeURL(burgerName)
    requrl = addOptions(requrl, args)

    print('Using KitchenView URL: ' + requrl)
    requests.get(requrl)
    return

@app.route('/order/<burgerName>', methods=['get'])
def order(burgerName):
    return renderOrderingPage(burgerName)

@app.route('/buy', methods=['get'])
def buy():
    burgerName = request.args.get('burger')
    quantity = request.args.get('quantity')
    options = request.args.getlist('options')

    sendToKitchen(burgerName, request.args)
    return f"Ordered {quantity} {burgerName} with options: {', '.join(options)}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
