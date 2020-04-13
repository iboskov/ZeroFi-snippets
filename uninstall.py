import os
os.system('mv /etc/wpa_supplicant/wpa_supplicant.conf.original /etc/wpa_supplicant/wpa_supplicant.conf')
os.system('rm -rf /etc/Zerofi')
os.system('rm -rf /usr/lib/Zerofi')
os.system('rm /etc/dnsmasq.conf')
os.system('mv /etc/dnsmasq.conf.original /etc/dnsmasq.conf')
os.system('rm /etc/hostapd/hostapd.conf')
os.system('rm /etc/network/interfaces')
os.system('mv /etc/network/interfaces.original /etc/network/interfaces')
os.system('rm /etc/resolv.conf')
os.system('mv /etc/resolv.conf.original /etc/resolv.conf')
os.system('rm /etc/systemd/system/Zerofi.service')
os.system('reboot')

