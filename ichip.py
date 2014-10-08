__author__ = 'Gregory'

import urllib.request
import time

URL = 'https://icanhazip.com'

print()
print('contacting \'https://icanhazip.com\'')
print()

start = time.clock()

try:
    response = urllib.request.urlopen(URL, None, 5)
    address = str(response.read(), "utf-8").strip()

    print('External IP: ' + address)
    print()
    print('completed in ', end='')

    duration = time.clock() - start

    if duration >= 1:
        print(str(round(duration, 2)) + ' seconds')
    else:
        print(str(round(duration / 1000.0, 0)) + ' milliseconds')
except:
    print()
    print("Unable to reach server")

print()