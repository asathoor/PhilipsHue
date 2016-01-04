# File: onOff.py
# State: experimental - trying to control Philips Hue
# Colors: http://www.developers.meethue.com/documentation/hue-xy-values

import requests
import json
import random

# set up your system
server = "http://192.168.0.11/api/" # you'll have to discover this
theCode = "xxxxxxxxxxxxxxxxxxxxxx" # sample code

# fun stuff
bri = random.randrange(10,200)
transitiontime = 60
effect = "colorloop" # or: none
effect = "none" # uncomment to turn this off

# the json data
taend = json.dumps(
    {"on":True,
                    "xy":[0.3517,0.5618],
                    "bri": bri,
                    "transitiontime": transitiontime,
                    "effect":effect
                    }
    )

# execute the json
requests.put("http://192.168.0.11/api/"
                 + theCode
                 +  "/groups/0/action",
                 data=taend
             )

# andre metoder, fx GET, POST .. saadan:
svar = requests.get("http://192.168.0.11/api/"
                 + theCode
                 +  "/groups/0/action",
                 data=taend
             )

# GET info about all lights and their settings
lights = requests.get(
    server + theCode + "/lights"
    )

# yeah, print it out
print "\nLIGHTS (json info)\n"

for item in lights:
    print item

# se svar til / fra server
# print taend # will just give 200 = ok