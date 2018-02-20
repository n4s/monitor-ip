#!/usr/bin/env python
from flask import *
import os
import datetime
import re

application = Flask(__name__)
port=os.getenv("PORT")

@application.route("/")
def hello():
    return "<h1>Update Monitor App</h1><p>This is an update IP docker container that logs /update/<IP> GET requests to a log file</p>"

# update ip path
@application.route("/update/<ip>")
def log(ip):
    application.logger.debug("Logging IP [%s]\n" % ip)

    f = open("/log/monitor-ip.log","a")
    f.write("%s: %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),ip))
    f.close()

    return "OK\n"

# get ip path
@application.route("/ip")
def getip():
    # open file, go to end, look for last "\n"
    try:
        f = open("/log/monitor-ip.log")
        f.seek(0, 2)
        while f.tell() > 0:
            f.seek(-2,1)
            c = f.read(1)
            if c == '\n':
                break

        line = f.readline().strip()
        f.close()

        # get IP
        m = re.search("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", line)
        ip =  m.group(0)
        application.logger.debug("Returning IP [%s]\n" % ip)
        return "%s\n" % ip
    except:
        return "ERROR - can not open log file\n"


if __name__ == "__main__":
    application.run(host='0.0.0.0',port=port)
