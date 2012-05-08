import os

print "\n--Interactive WLAN/WPA_SUPPLICANT connection script by narc \n"

os.system("sudo ifconfig wlan0 down")
os.system("sudo ifconfig wlan0 up")
os.system("sudo killall wpa_supplicant")
os.system("sudo killall dhcpcd")

print "Scanning for available WLAN nodes...\n"

os.system("sudo iwlist wlan0 scan | grep ESSID")
print "\n"
essid = raw_input('--Insert ESSID > ')
print "Configuring SSID %s..." % essid
os.system("sudo iwconfig wlan0 essid '%s'" % essid) 

if os.path.exists('/etc/wpakeys/%s.conf' % essid):
	print "WPA key seems to exist, connecting right away..."
	os.system("sudo wpa_supplicant -i wlan0 -Dwext -c /etc/wpakeys/%s.conf &" % essid )
	os.system("sleep 5")
	print "Leasing an IP with DHCP..."
	os.system("sudo dhcpcd")
else:
	wpa_key = raw_input(' Insert WPA/WPA2 key > ')
	print 'Writing WPA keyfile conf into /etc/wpakeys/'
	os.system("sudo wpa_passphrase %s %s > /etc/wpakeys/%s.conf" % (essid, wpa_key, essid))
	os.system("sudo wpa_supplicant -i wlan0 -Dwext -c /etc/wpakeys/%s.conf &" % essid )
	os.system("sleep 5")
	print "Leasing an IP with DHCP..."
	os.system("sudo dhcpcd")

print "There you go!"
print "Some info on your current lease..."
os.system("ifconfig | grep broadcast")