def reset_to_host_mode(): #reset the device in access point mode
	os.system('rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
	os.system('rm /etc/cron.zerofi/apclient_bootstrapper')
	os.system('cp /usr/lib/zerofi/reset_device/static_files/interfaces /etc/network/')
	os.system('mv /etc/dnsmasq.conf /etc/dnsmasq.conf.original')
	os.system('cp /usr/lib/zerofi/reset_device/static_files/dnsmasq.conf /etc/')
	os.system('cp /usr/lib/zerofi/reset_device/static_files/resolv.conf /etc/')
	os.system('touch /usr/lib/zerofi/APMODE')
	os.system('reboot')
