import requests

url = "https://api.covid19api.com/summary"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

for country in response.json().get("Countries"):
    if country.get("Country") == "Iran, Islamic Republic of":
        print(country.get("NewDeaths"))
        print(country.get("TotalDeaths"))

