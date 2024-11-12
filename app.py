from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.environ.get('USER', 'Unknown User')  # Use environment variable for username
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.check_output("top -bn1", shell=True).decode('utf-8')

    return f"""
    <h1>/htop Endpoint</h1>
    <p>Name: Preetham lk</p>
    <p>Username: 1234shadowtech</p>
    <p>Server Time in IST: {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
