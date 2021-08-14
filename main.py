import requests
from twilio.rest import Client

API_KEY = 'weather token'
LAT = 52.669540
LON = 4.847190
API_NAME = 'https://api.openweathermap.org/data/2.5/onecall'
account_sid = 'twilio sid'
auth_token = 'twilio token'

parameter = {
    'lat': LAT,
    'lon': LON,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY
}

response = requests.get(API_NAME, params=parameter)
response.raise_for_status()

data = response.json()
weather_hourly = data['hourly'][0:12]

next_hours = [weather_data['weather'][0]['id'] for weather_data in weather_hourly]

isRain = False
for next_hour in next_hours:
    if int(next_hour) < 700:
        isRain = True

if isRain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="The weather is not so nice today! Take an umbrella with you when you go outside.",
        from_='+12107873196',
        to='+310640709263'
    )

print(message.status)