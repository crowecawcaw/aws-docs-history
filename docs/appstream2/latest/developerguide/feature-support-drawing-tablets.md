# Drawing Tablets

Drawing tablets, also known as pen tablets, are computer input devices
that let users draw with a stylus (pen). With WorkSpaces Applications, your users can connect
a drawing tablet, such as a Wacom drawing tablet, to their local computer
and use the tablet with their streaming applications.

###### Note

Drawing tablets are not supported when using the WorkSpaces Applications macOS client
application.

Following are requirements and considerations for enabling your users to use drawing tablets with their streaming applications.

- To enable your users to use this feature, you must configure your WorkSpaces Applications fleet to use an image that runs Windows Server 2019.
- To use this feature, users must access WorkSpaces Applications by using the WorkSpaces Applications client, or through the Google Chrome or Mozilla Firefox browsers only.
- Streaming applications must support Windows Ink technology. For more information, see [Pen interactions and Windows Ink in Windows apps](https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions "https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions").
- Some applications, such GIMP, must detect drawing tablets on the streaming instance to support
  pressure sensitivity. If this is the case, your users must use the
  WorkSpaces Applications client to access WorkSpaces Applications and stream these applications. In
  addition, you must qualify your users' drawing tablets, and users
  must share their drawing tablets with WorkSpaces Applications every time they start a new streaming session. For more information, see [Qualify USB Devices for Use with Streaming Applications](qualify-usb-devices.md "qualify-usb-devices.md").
- This feature is not supported on Chromebooks.
  To get started with using drawing tablets during application streaming
  sessions, users connect their drawing tablet to their local computer with
  USB, share the device with WorkSpaces Applications if required for pressure sensitivity detection, and then use the WorkSpaces Applications client or a [supported web
  browser](drawing-tablet-support-web-access-admin.md "drawing-tablet-support-web-access-admin.md") to start an WorkSpaces Applications streaming session.
