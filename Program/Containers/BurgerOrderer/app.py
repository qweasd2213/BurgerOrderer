import os
from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

Base = declarative_base()

class BurgerOrder(Base):
    __tablename__ = "BurgerOrders"
    burger_id = Column("burger_id", Integer, primary_key=True, autoincrement=True)
    burger_name = Column("burger_name", String)

    def __init__(self, name):
        self.burger_name = name

    def __repr__(self):
        return f"({self.burger_id}), {self.burger_name}"

class Option(Base):
    __tablename__ = "Options"
    option_id = Column("option_id", Integer, primary_key=True, autoincrement=True)
    a_option = Column("a_option", String)

    def __init__(self, option):
        self.a_option = option

    def __repr__(self):
        return f"({self.option_id}), {self.a_option}"

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

staticBurgers = []
options_list = []

def initialize_data(): # Function is used to run code. Without function the code won't run properly
    global staticBurgers, options_list
    staticBurgers = [{"name": burger.burger_name} for burger in session.query(BurgerOrder).all()]

    options_list = [option.a_option for option in session.query(Option).all()]

initialize_data()

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

baseURL = 'http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5000')

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
