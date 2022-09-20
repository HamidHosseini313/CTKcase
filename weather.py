# Import required modules nad json
import requests
import json

# my api_key on openweathermap
myApi_key= "615231c07d2eab0f59f036af943fbcc6"

# base_url for openweathermap
urlCord= "https://api.openweathermap.org/data/2.5/weather?"

# User enter city name here
city_name = input ("Enter the city name"+ "")

# New url based on the citys name 
cityurl = urlCord + "appid=" + myApi_key+ "&q=" + city_name

# Here we get back the response for our request
response = requests.get(cityurl)

# Return respone text as JSON
json_text = response.json()

# The value of lat and lon from Json text
lat = json_text["coord"]["lat"]
lon = json_text["coord"]["lon"]

#connvert to string 
lats = str(lat)
lons = str(lon)

# complete url address
url = urlCord + "lat=" + lats + "&lon=" + lons +"&appid="+ myApi_key

# get method of requests    
# return response object
response = requests.get(url)
json_text = response.json() 

# Citys information from json text
temp        = json_text["main"]["temp"] 
country     = json_text ["sys"]["country"]
humidity    = json_text ["main"]["humidity"]
feels_like  = json_text ["main"]["feels_like"]
sky         = json_text ["weather"][0] ["description"]
wind        = json_text ["wind"]["speed"] 

# Convert kelvin to celsius (kelvin-272.15)
tempCelsius = (temp-273.15) 
feels_likeCelsius =  (feels_like-273.15) 

#Print citys information
print ("")
print ("The country is       :"  + " " +  (country))
print ("Current weather desc :"  + " " + sky) 
print ("Current temprtur     :"  + " " + str(tempCelsius))
print ("Feels_lik as         :"  + " " + str(feels_likeCelsius))
print ("Humidity is          :"  + " " + str(humidity))
print ("Current wind speed   :"  + " " + str(wind))


