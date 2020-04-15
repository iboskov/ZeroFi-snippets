FILE="~/Zerofi/initialboot"
#apt-get install python3 python3-pip dnsmasq hostapd -y
#pip3 install flask pexpect
if [ -e "$FILE" ];
then
   ./initial_setup.py
else
   exit 0
fi

