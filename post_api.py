import requests



payload={"nm":"man","job":"tjgj"}
rps=requests.post("https://reqres.in/api/users",data=payload)
print(rps)