import app

def test_make_url():
    assert app.makeURL("Chicken burger") == "http://localhost:5000/buy/Chicken burger"
