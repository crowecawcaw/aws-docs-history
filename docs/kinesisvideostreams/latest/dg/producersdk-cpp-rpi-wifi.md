# Join your Raspberry Pi to your Wi-Fi network

If you are using an attached monitor and keyboard, proceed to [Configure the Raspberry Pi camera](producersdk-cpp-rpi-camera.md "producersdk-cpp-rpi-camera.md").

These instructions are written to help you to set up your Raspberry Pi when run in
_headless_ mode, that is, without an attached
keyboard, monitor, or network cable. Follow the instructions below to configure your
Raspberry Pi to automatically attempt connecting to the specified network, allowing your
host machine to be able to SSH into it.

1. On your computer, create a file named `wpa_supplicant.conf`.
2. Copy the following text and paste it into the
   `wpa_supplicant.conf` file:

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="`Your Wi-Fi SSID`"
scan_ssid=1
key_mgmt=WPA-PSK
psk="`Your Wi-Fi Password`"
}
```

Replace the `ssid` and `psk` values with the information
for your Wi-Fi network. 3. Copy the `wpa_supplicant.conf` file to the SD card. It must
be copied to the root of the `boot` volume. 4. Insert the SD card into the Raspberry Pi, and power the device. It joins your
Wi-Fi network, and SSH is enabled.
