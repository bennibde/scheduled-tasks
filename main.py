import requests
from twilio.rest import Client
import os

account_sid = "AC1d01adc17de41831ab9f956c27fafdc6"
auth_token = os.environ.get("TW_AUTH_TOKEN")
api_key = os.environ.get("WM_API_KEY")



weather_parameters = {
    "lat":26.9019,
    "lon": 79.9786,
    "appid":api_key,
    "cnt": 4,
}

resonse = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
resonse.raise_for_status() # raises an exceotion/error if other (usuccessfull) response code
weather_data_eastbourne = resonse.json()


print(resonse.status_code)
print(weather_data_eastbourne)

will_rain = False
for interval in weather_data_eastbourne["list"]:
    condition_code = interval["weather"][0]["id"]
    if condition_code < 800:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today bra, take an umbrella with you.",
        from_="+14632822629",
        to="+491791120899",
    )
print(message.status)

