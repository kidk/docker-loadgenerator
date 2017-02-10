import requests
import os
import time

def request_get():
    print "get request %s" % os.environ['URL']
    requests.get(os.environ['URL'])

while True:
    request_get()

    time.sleep(0.1)
