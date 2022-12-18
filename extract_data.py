import http.client

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "d10fe29465msh3e79c08cb614767p1fad2fjsn9ddd0af5d091",
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
    }

conn.request("GET", "/history.json?q=Bengaluru&dt=2022-12-16&lang=en&end_dt=2022-12-17", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))