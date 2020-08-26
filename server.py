from merch_check import *
from os import environ
from flask import Flask
import threading

app = Flask(__name__)

port = int(environ.get('PORT', 3000))

if __name__ == "__main__":
    print("Starting server")

    checking_merch_thread = threading.Thread(target=checking_merch)
    checking_merch_thread.start()

    app.run(host='0.0.0.0', port=port)

