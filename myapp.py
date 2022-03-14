import requests

number = int(input("Enter the if no: "))

URL = f"http://127.0.0.1:8000/stuinfo/{number}"

r = requests.get(url=URL);
data = r.json();
print(data)


URL = f"http://127.0.0.1:8000/stuinfo/"

r = requests.get(url=URL)
print(type(r))
data = r.json()
print(type(data))
