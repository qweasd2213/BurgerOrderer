import app
"""
Imports the functions inside of app.py
"""

def test_make_url_Halloumi_burger():
    assert app.makeURL("Halloumi burger") == "http://localhost:5000/buy/Halloumi burger"

def test_make_url_Hamburger():
    assert app.makeURL("Hamburger") == "http://localhost:5000/buy/Hamburger"

def test_make_url_Deluxe_burger():
    assert app.makeURL("Deluxe burger") == "http://localhost:5000/buy/Deluxe burger"

def test_make_url_Vegan_burger():
    assert app.makeURL("Vegan burger") == "http://localhost:5000/buy/Vegan burger"