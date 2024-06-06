# If you have another environment file, change this to that filename
ENV_FILENAME = ".env"

from dotenv import dotenv_values
clover_vars = dotenv_values(ENV_FILENAME)


# Extract keys to global variables
CLIENT_ID = clover_vars["CLIENT_ID"]
CLIENT_SECRET = clover_vars["CLIENT_SECRET"]
TOKEN_URL = clover_vars["TOKEN_URL"]
AUTHORIZE_URL = clover_vars["AUTHORIZE_URL"]
API_BASEURL = clover_vars["API_BASEURL"]
MAX_RETRIES = clover_vars.get("MAX_RETRIES", 3)
