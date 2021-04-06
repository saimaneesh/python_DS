import requests



payload={"nm":"man","job":"tjgj"}
rps=requests.delete("https://reqres.in/api/users/2")
print(rps)