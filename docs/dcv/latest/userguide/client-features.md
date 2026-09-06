

# Supported features
<a name="client-features"></a>

Amazon DCV offers a Windows client, Linux client, web browser client, and macOS client. The clients offer similar feature sets, but there are some differences. Choose the Amazon DCV client that meets your specific requirements.

The following table compares the features that are supported by the Amazon DCV clients.


| Feature | [Windows client](client-windows.md) | [Web browser client](client-web.md) | [Linux client](client-linux.md) | [macOS client](client-mac.md) | 
| --- | --- | --- | --- | --- | 
| [Connect to Windows Amazon DCV servers](using-connecting.md) | ✓ | ✓ | ✓ | ✓ | 
| [Connect to Linux Amazon DCV servers](using-connecting.md) | ✓ | ✓ | ✓ | ✓ | 
| [QUIC UDP transport protocol](using-connecting.md) | ✓ | ✗ | ✓ | ✓ | 
| [Manage streaming modes](using-streaming.md) | ✓ | ✓ | ✓ | ✓ | 
| [Transfer files](using-transfer.md) | ✓ | ✓ | ✓ | ✓ | 
| [Print from sessions](using-print.md) | ✓ | ✓1 | ✓ | ✓ | 
| [Copy and paste](using-copy-paste.md) | ✓ | ✓ | ✓ | ✓ | 
| [Smart card support](using-smartcard.md) | ✓ | ✗ | ✓ | ✓ | 
| [USB remotization support](using-usb.md) | ✓ (installable client) | ✗ | ✗ | ✗ | 
| [Connection file support](using-connection-file.md) | ✓ | ✗ | ✓ | ✓ | 
| Stereo 2.0 audio playback | ✓ | ✓ | ✓ | ✓ | 
| Surround sound audio playback | ✓ (up to 7.1) | ✗ | ✓ (up to 5.1) | ✗ | 
| Stereo 2.0 audio recording | ✓ | ✓ | ✓ | ✓ | 
| Touchscreen support | ✓ (Windows 10 and later) | ✓ 2 | ✓ | ✗ | 
| Stylus support | ✓ (Windows 10 and later) | ✓ 3 | ✓ | ✓ | 
| Gamepad support | ✓ (Windows 10 and later) | ✓ | ✗ | ✗ | 
| [Multiple monitor support](using-multiple-screens.md) | ✓ | ✓4 | ✓ | ✓ | 
| [Extending full screen across selected monitors](using-multiple-screens.md) | ✓ | ✓ | ✓ | ✓ | 
| [Webcam support](using-webcam.md) | ✓ | ✓ 5 | ✓ | ✓ | 
| [Setting time zone](setting-timezone.md) | ✓ | ✓ | ✓ | ✓ | 
| [Using accurate audio/video synchronization](using-av-sync.md) | ✓ | ✗ | ✓ | ✓ | 
| [Amazon DCV Extensions](https://docs.aws.amazon.com/dcv/latest/extsdkguide/what-is.html) | ✓ | ✗ | ✓ | ✓ | 
| [WebAuthN](https://docs.aws.amazon.com/dcv/latest/adminguide/config-webauthn-redirect.html) | ✓ | ✗ | ✓ | ✓ | 

1These clients support printing to a file only. They don't support printing to a local printer.

2 Supported by Firefox, Edge, and Google Chrome.

3 Supported in Chromium-based browsers only. This includes Google Chrome and Microsoft Edge version 79 and later. Tilt and pressure events aren't supported in other browsers.

4Support for up to two monitors.

5Supported in Chromium-based browsers only. This includes Google Chrome and Microsoft Edge version 79 and later. This doesn't include Firefox and Safari.

For more information about the Amazon DCV server features, see [ Amazon DCV server features](https://docs.aws.amazon.com/dcv/latest/adminguide/servers.html#features) in the *Amazon DCV Administrator Guide*.