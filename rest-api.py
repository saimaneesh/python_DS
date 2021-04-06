import requests
p={"page":2}
resp=requests.get("https://reqres.in/api/users",params=p)
'''print(resp)
print(type(resp))
print(dir(resp))
print(resp.json())'''




jr=resp.json()
print(jr)
jr["data"][0]["email"]="saimaneeesh@gmai1.com"
print(jr["data"][0]["email"])



payload={"nm":"man","job":"tcs"}
rps=requests.post("https://reqres.in/api/users",data=payload)
print(rps.json())
print(resp.json())