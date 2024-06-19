import requests
from src.utils.api import API_BASE_URL
from src.context.user import loggedin_user

def authenticate(login, password):
    global loggedin_user # declare to modify global variable
    
    url = API_BASE_URL + "/users/auth/desktop"

    payload = {
        "login": login,
        "password": password
    }

    try:
        response = requests.post(url, json=payload)
     
        if int(response.status_code) == 200:
            user = response.json()
            
            loggedin_user["id"] = user.get("id", False)
            loggedin_user["name"] = user.get("name", False)
            loggedin_user["login"] = user.get("login", False)
            loggedin_user["password"] = user.get("password", False)
            loggedin_user["role"] = user.get("role", False)
            loggedin_user["createdAt"] = user.get("createdAt", False)
            loggedin_user["updatedAt"] = user.get("updatedAt", False)
            
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False
