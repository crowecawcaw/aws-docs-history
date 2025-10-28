# How to maintain your vehicle's Wi-Fi

connection

The following troubleshooting guide provides you tips for maintaining your vehicle's connection.

## How to

troubleshoot Wi-Fi connection if your vehicle's Wi-Fi LED indicator flashes blue, then turns red for two
seconds, and finally off

Check the following to verify you have the valid Wi-Fi connection settings.

- Verify that the USB drive has only one disk partition with only one _wifi-creds.txt_
  file on it. If multiple _wifi-creds.txt_ files are found, all of them will be processed
  in the order they were found, which may lead to unpredictable behavior.
- Verify the Wi-Fi network's SSID and password are correctly specified in
  _wifi-creds.txt_ file. An example of this file is shown as follows:

```
###################################################################################
#                                   AWS DeepRacer                                 #
# File name: wifi-creds.txt                                                       #
#                                                                                 #
# ...                                                                             #
###################################################################################

# Provide your SSID and password below
ssid: ' MyHomeWi-Fi'
password: myWiFiPassword

```

- Verify both the field names of `ssid` and `password` in the
  _wifi-creds.txt_ file are in lower case.
- Verify that each of the field name and value is separated by one colon (:). For example. `ssid : '
MyHomeWi-Fi'`
- Verify that the field value containing a space is enclosed by a pair of single quotes. On Mac, TextEdit
  or some other text editor shows single quotes as of the '...' form, but not of ‘...’. If the field value
  does not contain spaces, the value can be without single quotes.

## What does it mean when the vehicle's

Wi-Fi or power LED indicator flashes blue?

If the USB drive contains _wifi-creds.txt_ file, the Wi-Fi LED indicator flashes blue while
the vehicle is attempting to connect to the Wi-Fi network specified in the file.

If the USB drive has the `models` directory, the Power LED flashes blue while the vehicle is
attempting to load the model files inside the directory.

If the USB drive has both the _wifi-creds.txt_ file and the `models`
directory, the vehicle will process the two sequentially, starting with an attempt to connect to Wi-Fi and then
loading models.

The Wi-Fi LED might also turn red for two seconds if the Wi-Fi connection attempt fails.

## How can I connect to the

vehicle's device console using its hostname?

When connecting to the vehicle's device console using its hostname, make sure you type:
`https://`hostname`.local` in the browser, where
`hostname` value (of the
`AMSS-`1234`` format) is printed on the bottom of the AWS DeepRacer
vehicle. )

## How to connect to vehicle's

device console using its IP address

To connect to the device console using IP address as shown in the _device-status.txt_ file
(found on the USB drive), make sure the following conditions are met.

- Check your laptop or mobile devices are in the same network as the AWS DeepRacer vehicle.
- Check if you have connected to any VPN, if so, disconnect first.
- Try a different Wi-Fi network. For example, turn on personal hotspot on your phone.
