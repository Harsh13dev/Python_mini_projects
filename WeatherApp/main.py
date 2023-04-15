import requests
import json

city = input("Enter the city: ")
url =f'''http://api.weatherstack.com/current?access_key=83fe15ceeb41712ba19bf0da5ae19509&query={city}'''

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]
print(w,'This is value of w')
is_day= w["is_day"]
print(is_day,'This is is day value')