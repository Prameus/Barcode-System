import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 4p846t80R8uR8Id8gXjtIG:3hVOjqOYnWJO6r9jB6fQ1y"
}

conn.request("GET", "/economy/goldPrice", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

transformed_data = data.decode("utf-8")
new_data = data[0]
print(new_data)
