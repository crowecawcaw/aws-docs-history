# Supported features

Amazon DCV offers a Windows client, Linux client, web browser client, and macOS client. The clients
offer similar feature sets, but there are some differences. Choose the Amazon DCV client that meets
your specific requirements.

The following table compares the features that are supported by the Amazon DCV clients.

| Feature                                                                                                 | [Windows client](client-windows.md "client-windows.md") | [Web browser client](client-web.md "client-web.md") | [Linux client](client-linux.md "client-linux.md") | [macOS client](client-mac.md "client-mac.md") |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- | --------------------------------------------- |
| [Connect to Windows<br>Amazon DCV servers](using-connecting.md "using-connecting.md")                   | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Connect to Linux<br>Amazon DCV servers](using-connecting.md "using-connecting.md")                     | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [QUIC UDP transport protocol](using-connecting.md "using-connecting.md")                                | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |
| [Manage streaming modes](using-streaming.md "using-streaming.md")                                       | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Transfer files](using-transfer.md "using-transfer.md")                                                 | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Print from sessions](using-print.md "using-print.md")                                                  | ✓                                                       | ✓1                                                  | ✓                                                 | ✓                                             |
| [Copy and paste](using-copy-paste.md "using-copy-paste.md")                                             | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Smart card support](using-smartcard.md "using-smartcard.md")                                           | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |
| [USB remotization support](using-usb.md "using-usb.md")                                                 | ✓ (installable client)                                  | ✗                                                   | ✗                                                 | ✗                                             |
| [Connection file<br>support](using-connection-file.md "using-connection-file.md")                       | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |
| Stereo 2.0 audio playback                                                                               | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| Surround sound audio playback                                                                           | ✓ (up to 7.1)                                           | ✗                                                   | ✓ (up to 5.1)                                     | ✗                                             |
| Stereo 2.0 audio recording                                                                              | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| Touchscreen support                                                                                     | ✓ (Windows 10 and later)                                | ✓ 2                                                 | ✓                                                 | ✗                                             |
| Stylus support                                                                                          | ✓ (Windows 10 and later)                                | ✓ 3                                                 | ✓                                                 | ✓                                             |
| Gamepad support                                                                                         | ✓ (Windows 10 and later)                                | ✓                                                   | ✗                                                 | ✗                                             |
| [Multiple monitor support](using-multiple-screens.md "using-multiple-screens.md")                       | ✓                                                       | ✓4                                                  | ✓                                                 | ✓                                             |
| [Extending full screen across selected monitors](using-multiple-screens.md "using-multiple-screens.md") | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Webcam support](using-webcam.md "using-webcam.md")                                                     | ✓                                                       | ✓ 5                                                 | ✓                                                 | ✓                                             |
| [Setting time zone](setting-timezone.md "setting-timezone.md")                                          | ✓                                                       | ✓                                                   | ✓                                                 | ✓                                             |
| [Using accurate audio/video synchronization](using-av-sync.md "using-av-sync.md")                       | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |
| [Amazon DCV Extensions](../extsdkguide/what-is.md "../extsdkguide/what-is.md")                          | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |
| [WebAuthN](../adminguide/config-webauthn-redirect.md "../adminguide/config-webauthn-redirect.md")       | ✓                                                       | ✗                                                   | ✓                                                 | ✓                                             |

1These clients support printing to a file only. They don't support printing to a local printer.

2 Supported by Firefox, Edge, and Google Chrome.

3 Supported in Chromium-based browsers only. This includes Google
Chrome and Microsoft Edge version 79 and later. Tilt and pressure events aren't supported in
other browsers.

4Support for up to two monitors.

5Supported in Chromium-based browsers only. This includes Google
Chrome and Microsoft Edge version 79 and later. This doesn't include Firefox and Safari.

For more information about the Amazon DCV server features, see [Amazon DCV server features](../adminguide/servers.md#features "../adminguide/servers.md#features") in the _Amazon DCV Administrator Guide_.
