import os
import fileinput
import urllib.request, urllib.error
import time

def config_file_hash():
	config_file = open('/etc/Zerofi/Zerofi.conf')
	config_hash = {}

	for line in config_file:
		line_key = line.split("=")[0]
		line_value = line.split("=")[1].rstrip()
		config_hash[line_key] = line_value

	return config_hash

def hostapd_reset_check(ssid_prefix):
	hostapd_conf = open('/etc/hostapd/hostapd.conf', 'r')
	reset_required = True

	for line in hostapd_conf:
	    if ssid_prefix in line:
	        reset_required = False

	return reset_required

def update_hostapd(ssid_prefix):
	os.system('cp -a /usr/lib/Zerofi/reset_device/static_files/hostapd.conf /etc/hostapd/')

	with fileinput.input("/etc/hostapd/hostapd.conf", inplace=True) as file:
		for line in file:
			print(line.replace("beaglebone", ssid_prefix), end='')

def is_wifi_active():
	counter = 0
	while counter <10: 
		try:
			urllib.request.urlopen("http://google.com")
		except urllib.error.URLError as err: 
			wifi_active = False
		else:
			wifi_active = True
			break
		time.sleep(10)
		counter = counter+1
	return wifi_active

def reset_to_host_mode(): #reset the device in access point mode
	os.system('rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
	os.system('cp /usr/lib/Zerofi/reset_device/static_files/interfaces /etc/network/')
	os.system('mv /etc/dnsmasq.conf /etc/dnsmasq.conf.original')
	os.system('cp /usr/lib/Zerofi/reset_device/static_files/dnsmasq.conf /etc/')
	os.system('cp /usr/lib/Zerofi/reset_device/static_files/resolv.conf /etc/')
	os.system('touch /usr/lib/Zerofi/APMODE')
	os.system('reboot')
