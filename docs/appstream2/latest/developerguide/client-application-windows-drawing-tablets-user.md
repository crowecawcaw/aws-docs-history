# Drawing Tablets

Drawing tablets, also known as pen tablets, are computer input devices that
let you draw with a stylus (pen). With AppStream 2.0, you can connect a drawing tablet,
such as a Wacom drawing tablet, to your local computer and use the tablet with
your streaming applications.

Following are requirements and considerations for using drawing tablets with your streaming applications.

- To use this feature, you must connect to AppStream 2.0 by using the AppStream 2.0 client, or through the Google Chrome or Mozilla Firefox browsers only.
- The applications that you stream must support Windows Ink technology. For more information,
  see [Pen interactions and Windows Ink in Windows apps](https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions "https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions").
- Depending on the streaming applications that you use, your drawing tablet might require USB
  redirection to function as expected. This is because some applications,
  such as GIMP, require USB
  redirection to support pressure sensitivity. If this is the case for
  your streaming applications, you must connect to AppStream 2.0 by using the
  AppStream 2.0 client and share the drawing tablet with your streaming session.
- This feature is not supported on Chromebooks.
  To get started with using a drawing tablet during your application streaming
  sessions, connect your drawing tablet to your local computer with USB, share the device with AppStream 2.0 if required for pressure sensitivity detection, and then
  start an AppStream 2.0 streaming session. You can use the AppStream 2.0 client or a [supported web browser](web-browser-user.md "web-browser-user.md") to start a streaming session.
