# `clover-oauth`

This repo contains a minimum example of using Clover's OAuth2 flow to obtain an access token and make requests against their API.

### Getting Started

```bash
python --version  # must be >=3.11
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Also, create an REST app on the Clover development instance as described in [the Clover docs](https://docs.clover.com/docs/creating-an-app#).

Make sure to set the Site URL to `http://localhost:5000` and make note of the App ID (Oauth Client ID) and the App Secret (Client Secret). Copy `.env.example` into `.env` and replace the placeholder values for `CLIENT_ID` and `CLIENT_SECRET` with the App ID and App Secret for your app.

### Running

```bash
python app.py
```

Now, open a browser and navigate to `http://localhost:5000`.