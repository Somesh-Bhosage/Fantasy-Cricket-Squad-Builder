from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now().strftime('%d %b')
    matches = [
        {'id': 1, 'team1': 'IND', 'team2': 'AUS', 'time': '7:30 PM', 'day': 'TODAY', 'date': today}
    ]
    return render_template('index.html', matches=matches)

@app.route('/builder/<int:match_id>')
def builder(match_id):
    players = [
        {'id': 1, 'name': 'Rohit Sharma', 'role': 'BAT', 'credits': 10.5, 'team': 'IND'},
        {'id': 2, 'name': 'Virat Kohli', 'role': 'BAT', 'credits': 10.5, 'team': 'IND'},
        {'id': 3, 'name': 'Rishabh Pant', 'role': 'WK', 'credits': 9.5, 'team': 'IND'},
        {'id': 4, 'name': 'Hardik Pandya', 'role': 'AR', 'credits': 9.5, 'team': 'IND'},
        {'id': 5, 'name': 'S. Gill', 'role': 'BAT', 'credits': 9.0, 'team': 'IND'},
        {'id': 6, 'name': 'R. Jadeja', 'role': 'AR', 'credits': 9.0, 'team': 'IND'},
        {'id': 7, 'name': 'J. Bumrah', 'role': 'BOWL', 'credits': 10.0, 'team': 'IND'},
        {'id': 8, 'name': 'M. Siraj', 'role': 'BOWL', 'credits': 8.5, 'team': 'IND'},
        {'id': 9, 'name': 'K. Yadav', 'role': 'BOWL', 'credits': 9.0, 'team': 'IND'},
        {'id': 10, 'name': 'A. Patel', 'role': 'AR', 'credits': 8.5, 'team': 'IND'},
        {'id': 11, 'name': 'A. Singh', 'role': 'BOWL', 'credits': 8.5, 'team': 'IND'},
        {'id': 12, 'name': 'Y. Jaiswal', 'role': 'BAT', 'credits': 8.0, 'team': 'IND'},
        {'id': 13, 'name': 'Travis Head', 'role': 'BAT', 'credits': 9.5, 'team': 'AUS'},
        {'id': 14, 'name': 'G. Maxwell', 'role': 'AR', 'credits': 9.5, 'team': 'AUS'},
        {'id': 15, 'name': 'D. Warner', 'role': 'BAT', 'credits': 9.5, 'team': 'AUS'},
        {'id': 16, 'name': 'P. Cummins', 'role': 'BOWL', 'credits': 9.5, 'team': 'AUS'},
        {'id': 17, 'name': 'M. Starc', 'role': 'BOWL', 'credits': 9.0, 'team': 'AUS'},
        {'id': 18, 'name': 'J. Inglis', 'role': 'WK', 'credits': 8.5, 'team': 'AUS'},
        {'id': 19, 'name': 'M. Marsh', 'role': 'AR', 'credits': 9.0, 'team': 'AUS'},
        {'id': 20, 'name': 'A. Zampa', 'role': 'BOWL', 'credits': 9.0, 'team': 'AUS'},
        {'id': 21, 'name': 'J. Hazlewood', 'role': 'BOWL', 'credits': 9.0, 'team': 'AUS'},
        {'id': 22, 'name': 'M. Stoinis', 'role': 'AR', 'credits': 8.5, 'team': 'AUS'},
        {'id': 23, 'name': 'T. David', 'role': 'BAT', 'credits': 8.0, 'team': 'AUS'},
        {'id': 24, 'name': 'C. Green', 'role': 'AR', 'credits': 8.5, 'team': 'AUS'}
    ]
    return render_template('team_builder.html', players=players)

@app.route('/captain-selection')
def captain_selection():
    return render_template('captain_selection.html')

if __name__ == '__main__':
    app.run(debug=True)
