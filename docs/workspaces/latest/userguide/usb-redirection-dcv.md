# USB redirection for DCV WorkSpaces

Starting with WorkSpaces Windows client version 5.30.0, Amazon WorkSpaces supports generic USB redirection for the WorkSpaces app on Windows.
This allows you to access local USB devices within your virtual desktop environment. This feature complements
existing optimized redirection solutions for specific device classes such as printers and WebAuthn.

## Prerequisites

To use USB redirection for DCV WorkSpaces, you need the following:

- Windows WorkSpace agent using DCV protocol version 2.2.0.2047 or later
- WorkSpaces Windows client version 5.30.0 or later
- You must have administrator access on your device to install or update USB redirection drivers.

## Install USB redirection drivers

When you install the WorkSpaces client app, you have the option to install drivers required for USB redirection. The Amazon DCV USB drivers are installed through a separate installer that runs after the client app installation is complete.

###### Important

You must have administrator access on your device to install USB redirection drivers. You might be prompted to restart your device after installing the drivers.

You can also install USB redirection drivers from the toolbar **Devices** dialog.

## Redirect a USB device

Your administrator can enable USB redirection on a Windows WorkSpace, which allows specified devices to be redirected to the virtual desktop. Devices that are allowed for redirection appear in the devices dialog from the in-session toolbar.

###### To redirect a USB device

1. In your WorkSpace session, choose the **Devices** icon in the toolbar.
2. In the devices dialog, locate the device you want to redirect.
3. Choose **Use on my remote WorkSpace** for the device.

###### Important

Redirected devices can only be used on the WorkSpace and are not available for use on the local machine.

## Request access to blocked devices

In the devices dialog, you can see devices that are not allowed for USB redirection by your administrator. To request that your administrator enable a device for redirection, use the copy device details button next to the device and share the copied details with your administrator.

## Update USB redirection drivers

When an update is available for the USB redirection drivers, a notification appears on the devices icon in the toolbar. Choose the notification to open the devices dialog, where you can follow the instructions to update the drivers.

###### Important

You must have administrator access on your device to update USB redirection drivers. You might be prompted to restart your device after updating the drivers.
