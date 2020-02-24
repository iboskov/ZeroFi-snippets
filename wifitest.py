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
