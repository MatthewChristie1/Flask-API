import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1200, "name" : "Jimbo", "views" : 121000},
        {"likes": 86, "name" : "How to make REST API", "views" : 100},
        {"likes": 957, "name" : "How to teabag", "views" : 9853000},
        {"likes": 95217, "name" : "How to marry", "views" : 921212400}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
input()
#response = requests.delete(BASE + "video/0")
#print(response)
#input()
response = requests.get(BASE + "video/6")
print(response.json())
input()


