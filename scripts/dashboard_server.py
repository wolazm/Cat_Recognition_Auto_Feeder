from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Ensure the logs directory exists
os.makedirs('../logs', exist_ok=True)

@app.route('/')
def index():
    log_file = '../logs/feeding_logs.csv'
    if os.path.exists(log_file):
        logs = pd.read_csv(log_file)
    else:
        logs = pd.DataFrame(columns=['timestamp', 'cat_detected'])
    return render_template('index.html', logs=logs.to_dict('records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)