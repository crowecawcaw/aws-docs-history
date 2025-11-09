# Working with USB Device Filter

Strings

This section describes the filter strings that are available for qualifying
USB devices for WorkSpaces Applications streaming sessions. It also provides guidance for working
with these strings. The following filter strings are available:

- `Name` — By default, the value for this filter
  string is the name of the device, but you can specify your own
  value.
- `Base Class,SubClass,Protocol` — The USB class code
  for the device. For more information, see [Defined Class
  Codes](https://www.usb.org/defined-class-codes "https://www.usb.org/defined-class-codes").
- `ID Vendor (VID)` — A unique identifier that is
  assigned by the USB organization to the manufacturer of the USB
  device.
- `ID Product (PID)` — A unique identifier that
  assigned by the manufacturer to the USB device.
- `Support Autoshare` — Lets the WorkSpaces Applications client
  automatically share the device when a streaming session starts. Set this
  value to `1` to allow automatic device sharing. Set this
  value to `0` to not allow automatic device sharing.
- `Skip Reset` — By default, when a USB device is
  shared by WorkSpaces Applications with a streaming session, the device is reset to ensure
  that it functions correctly. However, some USB devices don’t function
  correctly during the streaming session if they are reset. To prevent
  this problem from occurring, set the value for this filter string to
  `1` to instruct the WorkSpaces Applications client not to reset the device
  while it is shared with a streaming session. To ensure that the device
  is reset while it is shared with a streaming session, set this value to
  `0`. When you set a value for `Skip Reset`,
  make sure that you set the value for `Support Autoshare` to
  `0` or `1`.
  The filter string that is copied from the local computer is specific to a USB
  device. In some cases, you might want to allow an entire class of devices
  instead of allowing every possible USB device. For example, you might want to
  allow your users to use any kind of Wacom design tablets or use any USB mass
  storage device. In such scenarios, you can provide wildcard characters for
  specific filter string fields. If you don’t know the VID and PID for your USB
  devices, you can search for this information in the [USB ID
  database](https://www.the-sz.com/products/usbid/index.php "https://www.the-sz.com/products/usbid/index.php").

The following examples show how to configure filter strings for USB device
sharing during streaming sessions:

- Allow all mass storage devices automatically on starting a streaming
  session — "Mass storage, 8, \*, \*, \*, \*,1,0"
- Allow all Wacom devices automatically on starting a streaming session
  — "Wacom tablets, 3, \*, \*, 1386, \*,1,0"
- Allow all devices that provide an audio interface — "Audio, 1,
  \*, \*, \*, \*,1,0"
- Allow device X, but don't reset it while the device is shared. Don’t
  share the device automatically on starting a streaming session —
  "X, Y, \*, \*, 1386, \*,0,1"
