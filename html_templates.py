BEGIN_TEMPLATE = """<html>
<head><title>Oauth Login Page</title></head>
<body>
  <h1>Clover OAuth</h1>
  <a href="{AUTHORIZE_URL}?client_id={CLIENT_ID}">Start OAuth flow</a>
</body>
</html>"""

END_TEMPLATE = """<html>
<head><title>Logged In</title></head>
<body>
  <h1>Account Linked</h1>
  <a href="/merchant">Merchant info via API</a>
  <hr />
  <a href="{AUTHORIZE_URL}?client_id={CLIENT_ID}">Restart OAuth flow</a>
</body>
</html>"""

