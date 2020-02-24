def scan_wifi_networks():
    iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE) #run the command iwlist scan
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

config_hash = reset_lib.config_file_hash() 
ssid_prefix = config_hash['ssid_prefix'] + " "
hostapd_reset_required = reset_lib.hostapd_reset_check(ssid_prefix)

if hostapd_reset_required == True: 
    reset_lib.update_hostapd(ssid_prefix) 
    os.system('systemctl restart networking.service')

os.system('iwconfig wlan0 mode Managed')
wifi_ap_array = scan_wifi_networks() 
os.system('/etc/init.d/hostapd restart')
