

# WorkSpaces clients
<a name="amazon-workspaces-clients"></a>

You can use the Amazon WorkSpaces client to connect to your WorkSpace from a supported device. Client applications are available for Windows, macOS, Linux, iPad, Android, Chromebook, and you can also connect from a supported web browser.

## Choose the right client for your needs
<a name="choose-the-right-client"></a>

The following table summarizes client availability by platform and protocol support.


| Platform | Supported client OS versions | Protocols supported | Notes | 
| --- | --- | --- | --- | 
| Windows | Windows 11 | DCV, PCoIP | New client experience available starting with version 5.34 (DCV only) | 
| macOS | macOS 14 (Sonoma) – DCV, PCoIP<br />macOS 15 (Sequoia) – DCV<br />macOS 26 (Tahoe) – DCV | DCV, PCoIP (macOS 14 only) |  | 
| Linux (Ubuntu) | Ubuntu 22.04<br />Ubuntu 24.04 | DCV |  | 
| iPad | iPadOS (current) | PCoIP | To connect to DCV-based WorkSpaces from an iPad device, use Web access, which includes tablet-focused support. | 
| Android / Chromebook | Android 14<br />Android 15<br />Android 16 | PCoIP | To connect to DCV-based WorkSpaces from an Android tablet or Chromebook device, use Web access, which includes tablet-focused support. | 
| Web access | Chrome, Edge, Firefox, Safari (latest 3 versions) | DCV |  | 
| PCoIP Zero Client | Teradici devices | PCoIP | End of support: October 2027 | 

## Get the WorkSpaces client
<a name="get-the-workspaces-client"></a>

Download and install the latest version of the WorkSpaces client for your platform from the [Amazon WorkSpaces Client Download page](https://clients.amazonworkspaces.com/).

## PCoIP end of support
<a name="clients-pcoip-end-of-support"></a>

**Important**  
AWS is ending support for PCoIP-based WorkSpaces Personal on October 31, 2027. The new client experience supports connecting to DCV-based WorkSpaces only. If you use PCoIP-based WorkSpaces, see [PCoIP-based WorkSpaces Personal end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-pcoip-end-of-support.html) or contact your administrator.

## Additional client documentation by platform
<a name="additional-client-documentation"></a>
+ [WorkSpaces Android client application](amazon-workspaces-android-client.md)
+ [WorkSpaces iPad client application](amazon-workspaces-ipad-client.md)
+ [WorkSpaces Linux client application](amazon-workspaces-linux-client.md)
+ [WorkSpaces macOS client application](amazon-workspaces-osx-client.md)
+ [WorkSpaces PCoIP zero client](amazon-workspaces-pcoip-zero-client.md)
+ [WorkSpaces Web Access](amazon-workspaces-web-access.md)
+ [WorkSpaces Windows client application](amazon-workspaces-windows-client.md)

## Related topics
<a name="clients-related-topics"></a>
+ [Getting started with your WorkSpace](workspaces-user-getting-started.md)
+ [Supported features by protocol type for WorkSpaces](supported-features.md)
+ [PCoIP-based WorkSpaces Personal end of support](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-pcoip-end-of-support.html)
+ [End of life policy for WorkSpaces client applications](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-eol.html)