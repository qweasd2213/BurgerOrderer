from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost:5432/your_database_name'

db = SQLAlchemy(app)

connection = psycopg2.connect(host='0.0.0.0', database='asdf', user='adsf', password='adsf')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)