from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():

    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    return f"""
    <h1>DevOps End to End Project</h1>
    <p>Hostname: {hostname}</p>
    <p>Time: {current_time}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)