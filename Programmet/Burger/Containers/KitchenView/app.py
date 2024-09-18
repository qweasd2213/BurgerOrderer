from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def frontpage():
    return 'Please specify a burger to buy'

@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    print('One ' + burgerName + ' ordered with the following options:')
    for arg in request.args:
        print(' - ' + arg)
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


