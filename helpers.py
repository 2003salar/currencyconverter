from flask import redirect, render_template, session
from functools import wraps
import requests


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def currency_rate(currency):
    myKey = ''
    try:
        url = f"https://v6.exchangerate-api.com/v6/{myKey}/latest/{currency}"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        if str(e) == "result: error" or str(e) == "error-type: unsupported-type":
            return None


def convert_currency(amount, source_currency, target_currency):
    rates = currency_rate(source_currency)
    if rates is None or 'conversion_rates' not in rates or target_currency not in rates["conversion_rates"]:
        return None
    rate = rates["conversion_rates"][target_currency]
    return amount * rate
