### `changeDeviceClass.py`

#### Usage

This script will ask for a file containing the device names and/or IP addresses and the device class to change those devices into. The file must contain the device names/IP addresses in a single column. For each device this script will print its device ID, IP address, production state, and former device class before changing it. 

Run this script in [ZenDMD](https://support.zenoss.com/hc/en-us/articles/202946755-An-Introduction-to-zendmd) with the following:

`zendmd --script="changeDeviceClass.py" --commit`

The `--commit` flag can be omitted, but to apply the changes to ZODB one must run `commit()` after running the script.

#### Limitations

* This will change all the devices in the file to a single device class only. This does not support changing of multiple devices to different device classes.
* This has only been tested in Zenoss 4.x
