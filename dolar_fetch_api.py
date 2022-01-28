import http.client
from math import prod

try:
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 4p846t80R8uR8Id8gXjtIG:3hVOjqOYnWJO6r9jB6fQ1y"
    }

    conn.request("GET", "/economy/goldPrice",
                 headers=headers)

except Exception as e:
    print(e)

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))

#print(data)

transformed_data = data.decode("utf-8")
new_data = transformed_data
transformed_data2 = transformed_data.replace('{"result":[', '')
transformed_data3 = transformed_data2.replace(',"success":true}', '')
transformed_data4 = transformed_data3.split(',')
#print(transformed_data)
with open('gold2.txt', 'w') as f:
    f.write(str(transformed_data4))


print(transformed_data4[5])
#print(new_data)
with open('gold.txt', 'w') as f:
    f.write(new_data)

""""
with open('gold.txt', 'r') as f:
    read = f.read()
    products = []
    for line in read:
        if products == '{"result":[':
            products.clear()
        elif line == ',':
            line = '\n'
        else:
            products.append(line)
    for word in products:
        #print(word, end="")
        pass
"""
