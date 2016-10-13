mkdir /usr/paysvr
cp PaymentServer.py /usr/paysvr
cp paysvrstart.sh /etc/init.d
chmod +x /usr/paysvr/PaymentServer.py
chmod +x /etc/init.d/paysvrstart.sh
update-rc.d paysvrstart.sh defaults
/usr/paysvr/LinuxServer.py
