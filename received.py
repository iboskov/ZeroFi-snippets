import os
import fileinput
import time
import sys
import re

def createfile(ssid,wpapsk):
        temp_conf_file=open('test', 'w')
        temp_conf_file.write('auto wlan0\n')
        temp_conf_file.write('iface wlan0 inet dhcp\n')
        temp_conf_file.write('wpa-ssid ' + ssid + '\n')
        temp_conf_file.write('wpa-psk ' + wpapsk + '\n')
        temp_conf_file.close()

        os.system('mv test ~/testbt')

startt=time.time()
counter = 0;
for file in os.listdir("~/bluetooth"):
        while counter <= 3:
                if file.endswith('.html') is True:
                        file = open ('~/bluetooth/bluetooth_content_share.html', 'r')
                        for line in file:
                                text=line.split('<body>') [1]
                                ssid=text.split('<br>') [0]
                                ssid=re.sub(r'<.+?>','', ssid)
                                wpapsk=text.split('<br>') [1]
                                wpapsk=re.sub(r'<.+?>','', wpapsk)
                                createfile(ssid,wpapsk)
                        break
                        #sys.exit()
                elif file.endswith('.txt') is True:
                        file = open('~/bluetooth/*.txt', 'r')
                        i=0;
                        for line in file:
                                if i == 0:
                                        ssid = line
                                        i=1
                                else:
                                        wpapsk = line
                                createfile(ssid,wpapsk)
                        break
                        #sys.exit()
                else:   
                        counter+=1
                        time.sleep(5)

endt=time.time()
print(endt-startt, file=open("receivedbttime.txt", "a"))
sys.exit()

