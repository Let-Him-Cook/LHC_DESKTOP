def authenticate(username, password):
  valid_username = "admin"
  valid_password = "admin"

  if username == valid_username and password == valid_password:
    return True
  return False
