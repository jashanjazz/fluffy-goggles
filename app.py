"""
Flask app to display the time remaining to the next New Year's Eve.
"""
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def time_to_nye():
    """
    Endpoint to display the time remaining until the next New Year's Eve.
    
    Returns:
        str: Description of the time remaining to NYE.
    """

    current_date = datetime.now()
    nye_this_year = datetime(current_date.year, 12, 31, 23, 59, 59)

    if current_date > nye_this_year:
        nye_next_year = datetime(current_date.year + 1, 12, 31, 23, 59, 59)
        time_difference = nye_next_year   - current_date
    else:
        time_difference = nye_this_year - current_date

    return f"Time remaining to the next NYE: {time_difference}"

if __name__ == '__main__':
    app.run()
