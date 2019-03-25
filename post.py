import requests

Stu_ID = { "name": "WeiHsien Lee",
		   "net_id": "wl181",
		   "e-mail": "wl181@duke.edu"
		   }
r = requests.post("http://vcm-7631.vm.duke.edu:5000/student", json=Stu_ID)
result = r.json()
print(result)
# print(r.json())
