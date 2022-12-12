import requests
while True:
    response = requests.get("https://randomuser.me/api")
    if response.status_code == 200:
        user = response.json()["results"][0]
        age = user["dob"]["date"]
        if int(age[:4]) in [1990, 1980, 1989, 1999]:
            name = user["name"]["first"]
            print(name, age)