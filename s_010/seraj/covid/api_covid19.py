import requests

url = "https://api.covid19api.com/summary"

payload = {}
headers = {}



# print(response.json())

# print(response.text)



def covid_analytics():
    response = requests.request("GET", url, headers=headers, data=payload)

    for country in response.json().get("Countries"):
        if country.get("Country") == "Iran, Islamic Republic of":
            return country.get("NewDeaths"), country.get("TotalDeaths")
