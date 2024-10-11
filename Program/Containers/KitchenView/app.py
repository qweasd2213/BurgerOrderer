from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/buy/<burgerName>', methods=['get'])
def buy(burgerName):
    quantity = request.args.get('quantity', '1')
    options = request.args.getlist('options')

    print(f"Order received: {quantity} {burgerName}")
    if options:
        print("options:")
        for option in options:
            print(f' - {option}')
    else:
        print("No options...")
    
    return "Order recived"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
