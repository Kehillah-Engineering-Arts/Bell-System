import sys
import time
import datetime as dt
from flask import Flask, render_template

from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run()