from flask import Flask, request, render_template
from datetime import datetime
import requests
import os

BACKEND_URL = os.environ.get('BACKEND_URL','http://localhost:8500')

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data, verify=False)
    return 'Data submitted'

@app.route('/data')
def data():
    response = requests.get(BACKEND_URL + '/data', verify=False)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)