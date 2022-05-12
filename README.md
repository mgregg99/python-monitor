# LSIT Uptime Monitor

![Screenshot](Screenshot.png)

This website was designed to give us a monitor that would give us quick stats for all of our services on one page. The info is pulled from Uptime-Kuma then displayed to the user.

## Installation Instructions

This assumes that you already have installed Uptime-Kuma

1. Clone the git repository.
2. Edit the location of the output file in the python script. Its a varible at the top of the page.
3. Edit the the crontab to run the python script. It will look something like this: ` * * * * * root python3 /home/byu.local/mgregg99/python-monitor/sqlmonitor.py`
4. Make Apache HTTPD docker container to serve the website. cd into the project then run `docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4`
