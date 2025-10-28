# Enabling USB remotization

With Amazon DCV, clients can use a variety of specialized USB devices, such as 3D pointing devices or authentication devices. The devices are
physically connected to their computer to interact with an application that are running on a Amazon DCV server.

###### Important

Amazon DCV provides a generic mechanism for redirecting USB devices. Some devices that are sensitive to network latency might experience issues.
Additionally, some devices might not function as expected due to driver compatibility issues. Ensure that your devices work as expected before
deploying to production.

###### Note

USB remotization is only supported with the Windows client. It's not supported with the portable Windows client or the web browser client.
Additional configuration might be required on the Amazon DCV client. For information on installing USB remotization on a client, see the optional steps in
[Installable Windows client](../userguide/client-windows-install.md "../userguide/client-windows-install.md") in the _Amazon DCV User Guide_.

The Amazon DCV server uses an allow list to determine which USB devices clients are allowed to use. By default, some commonly used USB devices are
added to the allow list. This means clients can connect these USB devices to their computer and use them on the server without any additional
configuration. For more information, see [Using USB
Remotization](../userguide/using-usb.md "../userguide/using-usb.md") in the _Amazon DCV User Guide_

However, some specialized devices might not be added to the allow list by default. These devices must be manually added to the allow list on
the Amazon DCV server before they can be used by the client. After they have been added, they appear in the Windows client **Settings**
menu.

Windows Amazon DCV server
To add a USB device to the allow list, you must obtain the USB device's filter string from the client and add it to the
`usb-devices.conf` file.

###### To add a USB device to the allow list on a Windows Amazon DCV server

1. Ensure that you have installed the latest version of the Amazon DCV server and that you opted to install the USB remotization drivers. For more
   information, see [Installing the Amazon DCV Server on Windows](setting-up-installing-windows.md "setting-up-installing-windows.md").
2. Install the USB device's hardware drivers on the Amazon DCV server.
3. On the Windows client machine, navigate to `C:\Program Files (x86)\NICE\DCV\Client\bin\` in the File Manager.
4. Run `dcvusblist.exe`.
5. Right-click on the USB device in the list.
6. Choose **Copy filter string** from the dropdown menu.
7. On the server, open `C:\Program Files\NICE\DCV\Server\conf\usb-devices.conf` using your preferred text editor and add the filter string to a
   new line at the bottom of the file.
8. Save and close the file.
9. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.

Linux Amazon DCV server
To add a USB device to the allow list, add the filter string for the USB device to the `usb-devices.conf` file.

###### Adding USB devices to the allow list on a Linux Amazon DCV server

1. Ensure that you have installed the latest version of the Amazon DCV server and the DCV USB driver. For more information, see [Installing the Amazon DCV Server on Linux](setting-up-installing-linux.md "setting-up-installing-linux.md").
2. Install the USB device's hardware drivers on the Amazon DCV server.
3. On the Windows client machine, navigate to `C:\Program Files (x86)\NICE\DCV\Client\bin\` in your File Manager.
4. Run `dcvusblist.exe`.
5. Right-click on the USB device in the list.
6. Choose **Copy filter string** from the dropdown menu.
7. On the server, open `/etc/dcv/usb-devices.conf` using your preferred text editor and add the filter string to a new line at the bottom of the
   file.
8. Save and close the file.
9. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.
