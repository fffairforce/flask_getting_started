import requests
print("Check written API")
r = requests.get("http://vcm-9129.vm.duke.edu:5000")
print(r)
answer = r.json()
print(answer)