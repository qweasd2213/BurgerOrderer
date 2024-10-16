from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

Base = declarative_base()

class BurgerOrder(Base):
    __tablename__ = "BurgerOrders"
    burger_id = Column("burger_id", Integer, primary_key = True, autoincrement=True)
    burger_name = Column("burger_name", String)

    def __init__(self, name):
        self.burger_name = name

    def __repr__(self):
        return f"({self.burger_id}),{self.burger_name}"
    
# class Option(Base):
#     __tablename__ = "options"


    
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

session.query(BurgerOrder).delete()
session.commit()

b1 = BurgerOrder("ChickenBurger")
session.add(b1)
session.commit()

results = session.query(BurgerOrder).all()
print("!!!HELLO THERE!!!")
print(results)
print("!!!BYE BYE!!!")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)