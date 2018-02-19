This container monitors the IP coming from OPNsense and writes it in a logfile in the mounted volume.
It receives a GET request with the IP with the following path: /update/<IP> The container simply writes the
IP in the log and returns OK\n for each request.

## Usage
To use this container just run it as follows:
~~~
docker run -d --restart unless-stopped --name monitor-ip -p 12000:80 -v `pwd`/log:/log nasacct/monitor-ip
~~~

where log is a local directory that will have the log file monitor-ip.log
