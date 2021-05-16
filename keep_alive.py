#!/usr/bin/env python

from threading import Thread

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello. I am alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    thread = Thread(target=run)
    thread.start()
