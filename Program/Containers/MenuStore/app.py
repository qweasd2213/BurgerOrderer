from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db' # Specifies what database to use
db = SQLAlchemy(app)

Base = declarative_base() # Creates a base class for setting up the Object Relational Mapping

class BurgerOrder(Base): 
    __tablename__ = "BurgerOrders"
    burger_id = Column("burger_id", Integer, primary_key = True, autoincrement=True) # Sets column as primary key and uses autoincrementation
    burger_name = Column("burger_name", String)

    def __init__(self, name): # Making a constructor so that making each row is easier and faster
        self.burger_name = name

    def __repr__(self): # Makes printing simpler
        return f"({self.burger_id}),{self.burger_name}"
    
# class Option(Base):
#     __tablename__ = "options"


    
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True) # Engine interact with SQLite database

Base.metadata.create_all(bind=engine) #Bascily runs SQL "CREATE TABLE" commands
Session = sessionmaker(bind=engine)
session = Session()

session.query(BurgerOrder).delete() #Delets all data in BurgerOrder since otherwise it just adds on and on.
session.commit()

b1 = BurgerOrder("ChickenBurger") 
session.add(b1)
session.commit()

results = session.query(BurgerOrder).all() #Queries everything in BurgerOrder and stores in results
print("RESULTS: ")
print(results) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)