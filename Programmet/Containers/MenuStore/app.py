from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost:5432/your_database_name'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
