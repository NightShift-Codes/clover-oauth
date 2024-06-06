from flask import Flask, redirect
from util import get_merchant_info_clover
from oauth_callback import clover_oauth_callback
from flask import request
from config import AUTHORIZE_URL, CLIENT_ID
import os
from html_templates import BEGIN_TEMPLATE, END_TEMPLATE
import time

app = Flask(__file__)

OAUTH_ARGS = [
    "merchant_id",
    "client_id",
    "employee_id",
    "code"
]

@app.get("/")
def main_page():
    # detect if this is the redirect after logging into Clover
    if all(map(lambda x: x in request.args, OAUTH_ARGS)):
        time.sleep(3)  # give it some time to think if we just connected the app
        try:
            clover_oauth_callback(query_data=request.args)
        except:
            # the initial redirect doesn't work at first... so just redirect again.
            return redirect(f"{AUTHORIZE_URL}?client_id={CLIENT_ID}")
    
    if all(map(os.path.isfile, ("merchant_id", "access_token"))):
        return END_TEMPLATE.format(AUTHORIZE_URL=AUTHORIZE_URL, CLIENT_ID=CLIENT_ID)
    else:
        return BEGIN_TEMPLATE.format(AUTHORIZE_URL=AUTHORIZE_URL, CLIENT_ID=CLIENT_ID)

@app.get("/merchant")
def get_merchant_info() -> dict:
    try:
        with open("access_token", "r") as f:
            access_token = f.read()
        with open("merchant_id", "r") as f:
            merchant_id = f.read()
    except OSError:
        print("Unable to read access token or merchant ID. Access the /oauth endpoint first!")

    # interact with the Clover API
    merchant_info = get_merchant_info_clover(merchant_id, access_token)

    return merchant_info


if __name__ == "__main__":
    print("Access localhost:5000/oauth in a browser to initiate the oauth flow")
    print("Then go to localhost:5000/merchant to see your merchant info")
    app.run(host="localhost", port=5000, debug=True)

