#!/usr/bin/env python
from flask import *
import os
import datetime

application = Flask(__name__)
port=os.getenv("PORT")

@application.route("/")
def hello():
    return "<h1>Update Monitor App</h1><p>This is an update IP docker container that logs /update/<IP> GET requests to a log file</p>"

@application.route("/update/<ip>")
def log(ip):
    application.logger.debug("Logging IP [%s]\n" % ip)

    f = open("/log/monitor-ip.log","a")
    f.write("%s: %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),ip))
    f.close()

    return "OK\n"

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=port)
