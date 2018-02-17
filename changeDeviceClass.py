sync()

# this assumes that file is a list of devices or IPs in a single column
myfilename = raw_input('Enter filename: ')
devclass = raw_input('Enter new device class (ex. /Ignore): ')
f = open(myfilename,'r')
for line in f.read().splitlines() :
	print line
	d = find(line)
	print '%s\n%s\t%s\t%s' % (d.id, d.manageIp, d.getDeviceClassName(), d.getProdState())
	d.changeDeviceClass(devclass)
	print 'New device class is %s' % (d.getDeviceClassName())
f.close()
