mkdir /usr/demosvr

cp LinuxServer.py /usr/demosvr

cp demosvrstart.sh /etc/init.d


chmod +x /usr/demosvr/LinuxServer.py

chmod +x /etc/init.d/demosvrstart.sh


update-rc.d demosvrstart.sh defaults

/usr/demosvr/LinuxServer.py
