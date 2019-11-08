from flask import Flask
from threading import Thread
import os
from dotenv import load_dotenv

load_dotenv("vars.env")

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))

def keep_alive():
    server = Thread(target=run)
    server.start()