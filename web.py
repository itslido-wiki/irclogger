from flask import Flask
import os

app = Flask(__name__)

LOG_DIR = "logs"

@app.route("/")
def index():

    files = os.listdir(LOG_DIR)

    html = "<h1>IRC Logs</h1>"

    for f in files:
        html += f'<p><a href="/logs/{f}">{f}</a></p>'

    return html


@app.route("/logs/<name>")
def show_log(name):

    path = os.path.join(LOG_DIR, name)

    if not os.path.exists(path):
        return "Not found"

    with open(path) as f:
        content = f.read()

    return f"<pre>{content}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
