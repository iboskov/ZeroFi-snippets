@app.route('/save_credentials', methods=['GET', 'POST'])
def save_credentials():
	ssid = request.form['ssid']
	wifi_key = request.form['wifi_key']
	create_wpa_supplicant(ssid, wifi_key)
	def sleep_and_start_ap():
		time.sleep(2)
		set_ap_client_mode()
	t = Thread(target=sleep_and_start_ap)
	t.start()
	return render_template('save_credentials.html', ssid=ssid)
