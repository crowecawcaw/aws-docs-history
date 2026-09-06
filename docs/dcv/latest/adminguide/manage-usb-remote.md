

# Enabling USB remotization
<a name="manage-usb-remote"></a>

With Amazon DCV, clients can use a variety of specialized USB devices, such as 3D pointing devices or authentication devices. The devices are physically connected to their computer to interact with an application that are running on a Amazon DCV server.

**Important**  
Amazon DCV provides a generic mechanism for redirecting USB devices. Some devices that are sensitive to network latency might experience issues. Additionally, some devices might not function as expected due to driver compatibility issues. Ensure that your devices work as expected before deploying to production.

**Note**  
USB remotization is only supported with the Windows client. It's not supported with the portable Windows client or the web browser client. Additional configuration might be required on the Amazon DCV client. For information on installing USB remotization on a client, see the optional steps in [Installable Windows client](https://docs.aws.amazon.com/dcv/latest/userguide/client-windows-install.html) in the *Amazon DCV User Guide*.

The Amazon DCV server uses a device compatibility filter to determine which USB devices are recognized for remotization. This filter is not a security access control and should not be relied upon as a security boundary. By default, some commonly used USB devices are included in the device compatibility filter. This means clients can connect these USB devices to their computer and use them on the server without any additional configuration. For more information, see [Using USB Remotization](https://docs.aws.amazon.com/dcv/latest/userguide/using-usb.html) in the *Amazon DCV User Guide*

However, some specialized devices might not be included in the device compatibility filter by default. These devices must be manually added to the filter configuration on the Amazon DCV server before they are recognized for remotization. After they have been added, they appear in the Windows client **Settings** menu.

------
#### [ Windows Amazon DCV server ]

To add a USB device to the device compatibility filter, you must obtain the USB device's filter string from the client and add it to the `usb-devices.conf` file.

**To add a USB device to the device compatibility filter on a Windows Amazon DCV server**

1. Ensure that you have installed the latest version of the Amazon DCV server and that you opted to install the USB remotization drivers. For more information, see [Installing the Amazon DCV Server on Windows](setting-up-installing-windows.md).

1. Install the USB device's hardware drivers on the Amazon DCV server.

1. On the Windows client machine, navigate to `C:\Program Files (x86)\NICE\DCV\Client\bin\` in the File Manager.

1. Run `dcvusblist.exe`.

1. Right-click on the USB device in the list.

1. Choose **Copy filter string** from the dropdown menu.

1. On the server, open `C:\Program Files\NICE\DCV\Server\conf\usb-devices.conf` using your preferred text editor and add the filter string to a new line at the bottom of the file.

1. Save and close the file.

1. [Stop](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [restart](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html) the Amazon DCV server.

------
#### [ Linux Amazon DCV server ]

To add a USB device to the device compatibility filter, add the filter string for the USB device to the `usb-devices.conf` file.

**Adding USB devices to the device compatibility filter on a Linux Amazon DCV server**

1. Ensure that you have installed the latest version of the Amazon DCV server and the DCV USB driver. For more information, see [Installing the Amazon DCV Server on Linux](setting-up-installing-linux.md).

1. Install the USB device's hardware drivers on the Amazon DCV server.

1. On the Windows client machine, navigate to `C:\Program Files (x86)\NICE\DCV\Client\bin\` in your File Manager.

1. Run `dcvusblist.exe`.

1. Right-click on the USB device in the list.

1. Choose **Copy filter string** from the dropdown menu.

1. On the server, open `/etc/dcv/usb-devices.conf` using your preferred text editor and add the filter string to a new line at the bottom of the file.

1. Save and close the file.

1. [Stop](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [restart](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html) the Amazon DCV server.

------