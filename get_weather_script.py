# API key 9d797265d50416a0db1f6a61f7563c8a
# API url  api.openweathermap.org

import requests
from sys import argv


unit = '\u00B0C'
parameters = {'q':argv[1], 'APPID':'9d797265d50416a0db1f6a61f7563c8a'}

try:
    request = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?units=metric',
        params = parameters
    )
    data = request.json()
    print(str(data['main']['temp']) + unit)
except KeyError:
    print('Please provide a valid city name.')
