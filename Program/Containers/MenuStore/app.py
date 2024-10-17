from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    
class Option(Base):
    __tablename__ = "Options"
    option_id = Column("option_id", Integer, primary_key = True, autoincrement=True)
    a_option =  Column("a_option", String)

    def __init__(self, option):
        self.a_option = option

    def __repr__(self):
        return f"({self.option_id}),{self.a_option}"


    
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True) # Engine interact with SQLite database

Base.metadata.create_all(bind=engine) #Bascily runs SQL "CREATE TABLE" commands
Session = sessionmaker(bind=engine)
session = Session()

session.query(BurgerOrder).delete() #Delets all data in BurgerOrder since otherwise it just adds on and on.
session.query(Option).delete()
session.commit()

b1 = BurgerOrder("Chicken burger")
b2 = BurgerOrder("Halloumi burger")
b3 = BurgerOrder("Hamburger")
b4 = BurgerOrder("Deluxe burger")
b5 = BurgerOrder("Vegan burger")

op1 = Option("3xcheese")
op2 = Option("Onions")
op3 = Option("Secret sauce")
op4 = Option("Tomato")
op5 = Option("Pickels")

session.add(b1)
session.add(b2)
session.add(b3)
session.add(b4)
session.add(b5)

session.add(op1)
session.add(op2)
session.add(op3)
session.add(op4)
session.add(op5)

session.commit()

burgers = session.query(BurgerOrder).all() #Queries everything in BurgerOrder and stores in results
options = session.query(Option).all()

print(burgers)
print(options)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)