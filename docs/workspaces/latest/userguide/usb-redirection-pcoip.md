# USB redirection for PCoIP WorkSpaces

USB is used to connect computers to devices, such as
scanners, printers, external drives, and security keys. USB redirection enables access to
local USB devices within your virtual desktop environment.

PCoIP Windows WorkSpaces support redirection of a locally attached YubiKey for universal 2nd factor authentication from the Windows WorkSpaces client application.

###### Note

YubiKey redirection is only supported for Windows WorkSpaces clients.

## Requirements

- USB redirection is disabled by default on Windows PCoIP WorkSpaces. You must
  enable USB redirection for WorkSpaces. You can configure USB device
  rules to define which devices can be redirected. For more information, see
  [Manage your Windows WorkSpaces](../adminguide/group_policy.md "../adminguide/group_policy.md")
- Install WorkSpaces client version 4.0 or later, with the USB redirection driver, locally.
  For more information, see [Setup and installation](amazon-workspaces-windows-client.md#windows_setup "amazon-workspaces-windows-client.md#windows_setup").

## Supported USB devices

The following is a list of USB YubiKey models that are validated to work with the
PCoIP Windows WorkSpaces redirection for U2F:

- YubiKey 4
- YubiKey 5 NFC
- YubiKey 5 Nano
- YubiKey 5C
- YubiKey 5C Nano
- YubiKey 5 NFC
- Most USB type C to USB type A adapters can be used with a supported YubiKey

## Unsupported USB devices

Most USB mass storage devices and some scanners and printers use data transfer types, including control,
interrupt, and bulk. Devices using these data transfer types are not supported but they may be redirected
in your WorkSpaces. Isochronous transfers, which are commonly used in webcams, are not
supported. Therefore, USB webcams are not supported.

The following USB device is validated to work with PCoIP WorkSpaces for U2F authentication,
although it is not supported:

- Thetis Security Key

The following USB device doesn't work with PCoIP WorkSpaces for U2F authentication:

- Kensington Security Key

## Connecting your USB device to your WorkSpace

###### To connect your local USB device to your WorkSpace

###### Warning

When you connect a local USB device to your WorkSpace, it is no longer available for use by
your local computer. For example, if you redirect your USB mouse to the WorkSpace, your computer
cannot receive mouse input from the redirected USB mouse until you disconnect it from the WorkSpace.

USB device connections do not persist across WorkSpaces streaming sessions. You must
connect your USB device each time that you connect to your WorkSpace. Up to 10 USB
devices can be redirected concurrently in a WorkSpaces streaming session.

1. Log in to a PCoIP Windows WorkSpace using the WorkSpaces Windows client application.
2. On the client interface, click the **Devices** icon to list the
   locally attached USB devices.
3. Select the USB device and choose **Use with WorkSpaces**
   from the menu next to the device name.
4. Your USB device is ready to use with your WorkSpace.

## Disconnecting your USB device from your WorkSpace

###### To disconnect your local USB device from your WorkSpace

1. On the client interface, click the icon to list the locally attached
   USB devices.
2. Select the USB device and choose **Use with local device**
   from the menu next to the device name.
3. Your USB device is ready to use with your local computer.

## Reinstalling or upgrading your USB redirection drivers

###### To reinstall or upgrade USB redirection drivers

Follow these steps to do a clean re-installation or upgrade of the drivers.

1. Uninstall the USB redirection drivers by running the following command.

```
[Amazon WorkSpaces directory]\pcoipusb\bin\USB\PCoIP_Client_USB_uninstaller.exe
```

2. Reboot your machine.
3. Open the **Registry Editor** editor.
4. Under **HKLM**, search for **fusbhub**.
5. Remove the registry key, which is the item in the left pane with the folder icon.
   In this case it is the **fuhub** key, containing
   **fusbhub**. If you cannot remove this registry key, make note
   of the .inf file name that's associated with the registry entry. The .inf file name
   usually starts with "oem," for example "oem9.inf". Open the command line (using
   administrator privileges), and run the following prompt, substituting the .inf file
   name for `oem9.inf`.

```
pnputil -f -d `oem9.inf`
```

6. Repeat step 5 until **fusbhub** is completely removed from the registry editor.
7. Reboot your machine.
8. For upgrades only, you must download the latest client and install it. You can
   choose to install USB drivers during the client installation.
9. After you log into your WorkSpace, select the
   **Devices** icon
   ![Devices icon](images/devices-icon.png)
   , and reinstall the USB driver. Alternatively, you
   can invoke the following PowerShell script (using administrator privileges).

```
[Amazon WorkSpaces directory]\pcoipusb\install-pcoip-usb-driver.ps1
```
