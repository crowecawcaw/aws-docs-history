

# Using USB remotization
<a name="using-usb"></a>

**Note**  
This feature is for installable Windows clients only.

With Amazon DCV you can use specialized USB devices such as 3D pointing devices and two-factor authentication USB dongles. These devices must be connected to your computer for them to interact with applications running on a Amazon DCV server.

**Note**  
Graphic tablets, gamepads, and smart card readers are automatically supported by Amazon DCV and do not require USB remotization to be used.

You must be authorized to use this feature. If you are not authorized, the functionality is not available in the client. For more information, see [Configuring Amazon DCV Authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization.html) in the *Amazon DCV Administrator Guide*.

After this feature is enabled, the most commonly used USB devices are supported. You can connect them to your computer and use them on the server without additional configuration required. 

However, some specialized USB devices aren't supported in the default configuration. Unsupported devices do not appear in the **Settings** menu after they're connected. These devices must be added to the USB Device **Allow List** on the Amazon DCV Server to be recognized for remotization. This list acts as a device compatibility filter, not a security access control. After they are added to this list, they will appear in the **Settings** menu on the client.

For information on this or any additional configuration that may be required on the Amazon DCV server, see [Enabling USB Remotization](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-usb-remote.html) and in the *Amazon DCV Administrator Guide*.

## Using a USB device on a Amazon DCV server
<a name="using-usb-on-server"></a>

1. Connect the USB device in any open USB slot on your computer.

1. Go to your DCV client session.

1. Choose the **Settings** icon located in the upper left of the window.  
![Settings icon highlighted in toolbar with other control icons.](http://docs.aws.amazon.com/dcv/latest/userguide/images/dcv-settings-icon.jpg)

1. Select **Removable Devices...** from the dropdown menu.  
![Removable Devices option highlighted in dropdown menu.](http://docs.aws.amazon.com/dcv/latest/userguide/images/dcv-settings-dropdown.jpg)

1. Move the slider next to the USB device in the list.  
![Removable Devices dialog with toggle slider next to Yubikey 4 OTP plus U2F device.](http://docs.aws.amazon.com/dcv/latest/userguide/images/dcv-settings-removable-devices.png)

Your USB device is ready to use now.