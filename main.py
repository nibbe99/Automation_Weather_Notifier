import requests
from twilio.rest import Client

API_KEY = "dc9b29dcd3355102d94376f65f853d51"
account_sid = "AC78b70405e1cea50017c29ed204c6860c"
auth_token = "f933f3f03f5b67ba885e0d02f343ee34"


MY_LAT = 76
MY_LON = 17.945120

URL_HOUR = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LON}&units=metric&appid={API_KEY}"

def getURLJson(URL: str):
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def getWeather(Json_file):


    myMessage = ""
    for i in range(0,9):
        getWeatherId = Json_file["list"][i]["weather"][0]["id"]
        onlyHours = str(Json_file["list"][i]["dt_txt"]).split(" ")[1]

        if getWeatherId < 700 and getWeatherId >= 600:
            myMessage += onlyHours + " Will snow 🌨️ (Bad weather to go out)\n"
        elif getWeatherId < 600 and getWeatherId >= 500:
            myMessage += onlyHours + " Will rain ☂️(Bad weather to go out)\n"
        else:
            myMessage+= onlyHours + " No snow or rain! 🌞 \n"


    print("MESSAGE SENT")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=myMessage,
        from_="+16593992610",
        to="+46704376119"
    )




myResponseHour = getURLJson(URL_HOUR)

getWeather(myResponseHour)
