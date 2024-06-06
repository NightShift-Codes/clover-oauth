import requests
from urllib.parse import urlencode
from config import (
    MAX_RETRIES,
    API_BASEURL
)
from exceptions import MaxCloverAPIRetriesExceededError


def clover_api_get(path, query_params: dict = None, access_token: str = None) -> dict:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json"
    }
    if query_params is not None:
        path = path + "?" + urlencode(query_params)

    for retrynum in range(MAX_RETRIES):
        req = requests.get(f"{API_BASEURL}/{path}", headers=headers)
        if not req.ok:
            print(f"Clover API returned error (attempt #{retrynum+1}): {req.status_code} reason: {req.reason} msg: {req.content}")
            continue
        else:
            break
    else:
        raise MaxCloverAPIRetriesExceededError()

    return req.json()


def get_merchant_info_clover(merchant_id: int, access_token: str):
    return clover_api_get(f"/merchants/{merchant_id}", access_token=access_token)
