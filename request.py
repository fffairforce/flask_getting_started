import requests
r = requests.get("http://adpl.suyash.io/api/sites")
print(r.text)
print(type(r.text))
