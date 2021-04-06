import requests




payload={"nm":"man","job":"tjgj"}
rps=requests.put("https://reqres.in/api/users/2")
print(rps.json())