import pyowm

owm = pyowm.OWM('340600301a5ec349d10bf04f5c973e82')

observation = owm.weather_at_place('Porto Alegre,BR')

w = observation.get_weather()
print(w)
w.get_temperature('celsius')