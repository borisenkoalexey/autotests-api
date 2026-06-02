import httpx


login_payload = {
    "email": "alex@mail.com",
    "password": "alex"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login response:", login_response_data)

accessToken_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=accessToken_headers)
users_me_response_data = users_me_response.json()

print("Users/me status code:", users_me_response.status_code)
print("Users/me response:", users_me_response_data)