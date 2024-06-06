import requests
from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN_URL
)


def clover_oauth_callback(query_data: dict):
    """The user is redirected back to this endpoint by Clover after logging into Clover.

    Args:
        query_data (dict): contains OAuth params merchant_id, employee_id, client_id, code
    """
    merchant_id = query_data["merchant_id"]
    employee_id = query_data["employee_id"]
    client_id = query_data["client_id"]
    authorization_code = query_data["code"]
    with open("merchant_id", "w") as f:
        f.write(merchant_id)

    if client_id != CLIENT_ID:
        print("Invalid client_id")
    
    # try to get access token and refresh token
    token_args = {
        "client_id": client_id,
        "client_secret": CLIENT_SECRET,
        "code": authorization_code
    }

    req = requests.post(TOKEN_URL, json=token_args)
    if not req.ok:
        print("An error occurred while communicating with Clover")
    
    result = req.json()
    access_token = result["access_token"]
    with open("access_token", "w") as f:
        f.write(access_token)
