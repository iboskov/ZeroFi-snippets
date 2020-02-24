def update_main_config_file(ssid, server_port):
	if ssid != "":
		os.system('sed -i \'s/LGTC-AP/' + ssid + '/\' /etc/zerofi/zerofi.conf')
	else:
		with fileinput.input("/etc/zerofi/zerofi.conf", inplace=True) as file:
			for line in file:
				print(line.replace('ssid_prefix=LGTC-AP', 'ssid_prefix=LGTC_' + id), end='')
	if server_port != "":
		with fileinput.input("/etc/zerofi/zerofi.conf", inplace=True) as file:
			for line in file:
				print(line.replace('server_port=80', 'server_port=' + server_port), end='')
