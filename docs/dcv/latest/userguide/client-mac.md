

# macOS client
<a name="client-mac"></a>

The Amazon DCV macOS client is supported on Apple Mac computers only. The macOS client is a standalone application that runs on the macOS operating system.

The macOS client is installed using a `.dmg` software package.

For instructions on how to connect to a Amazon DCV session using the macOS client, see [Connecting to a Amazon DCV session using the macOS client](using-connecting-mac.md).

**To install the macOS client**

1. Download the correct macOS client installer depending on your client computer.
   + [macOS client for Intel processors](https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Clients/nice-dcv-viewer-2026.0.14405.x86_64.dmg)
   + [macOS client for Apple Silicon processors](https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Clients/nice-dcv-viewer-2026.0.14405.arm64.dmg)
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that always point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.

1. Run the downloaded `.dmg` file.

   If you get an error stating that the application can't be opened because it's from an unidentified developer, see the [Safely open apps on your Mac](https://support.apple.com/en-ie/HT202491) webpage.

1. Drag **DCV Viewer** to the **Applications** folder.

1. (Optional) For easy access, add the application to the **Dock**.

1. (Optional) Grant **Notification** permission when prompted. This allows the client to deliver session event alerts even when the application is in the background.

1. (Optional) When entering full screen, macOS may prompt you to grant **Accessibility** permission. This is required for input forwarding (capturing system shortcuts and sending them to the remote session). To grant access manually, enable **DCV Viewer** in your macOS Accessibility settings.
**Note**  
This prompt appears only when input forwarding is enabled. By default, input forwarding is active in full screen mode. Your administrator can change this behavior.