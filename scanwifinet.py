
def scan_wifi_networks():
	iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
	ap_list, err = iwlist_raw.communicate()
	ap_array = []
	for line in ap_list.decode('utf-8').rsplit('\n'):
		if 'ESSID' in line:
			if 'x00' in line:
				pass
			else:
				ap_ssid = line[27:-1]
			if ap_ssid != '':
				ap_array.append(ap_ssid)
	return ap_array
