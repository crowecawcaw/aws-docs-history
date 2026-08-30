# WorkSpaces clients

You can use the Amazon WorkSpaces client to connect to your WorkSpace from a supported device.
Client applications are available for Windows, macOS, Linux, iPad, Android, Chromebook, and
you can also connect from a supported web browser.

## Choose the right client for your needs

The following table summarizes client availability by platform and protocol
support.

| Platform             | Supported client OS versions                                                         | Protocols supported        | Notes                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows              | Windows 11                                                                           | DCV, PCoIP                 | New client experience available starting with version 5.34 (DCV<br>only)                                                                     |
| macOS                | macOS 14 (Sonoma) – DCV, PCoIP<br>macOS 15 (Sequoia) – DCV<br>macOS 26 (Tahoe) – DCV | DCV, PCoIP (macOS 14 only) |                                                                                                                                              |
| Linux (Ubuntu)       | Ubuntu 22.04<br>Ubuntu 24.04                                                         | DCV                        |                                                                                                                                              |
| iPad                 | iPadOS (current)                                                                     | PCoIP                      | To connect to DCV-based WorkSpaces from an iPad device, use<br>Web access, which includes tablet-focused support.                            |
| Android / Chromebook | Android 14<br>Android 15<br>Android 16                                               | PCoIP                      | To connect to DCV-based WorkSpaces from an Android tablet or<br>Chromebook device, use Web access, which includes tablet-focused<br>support. |
| Web access           | Chrome, Edge, Firefox, Safari (latest 3 versions)                                    | DCV                        |                                                                                                                                              |
| PCoIP Zero Client    | Teradici devices                                                                     | PCoIP                      | End of support: October 2027                                                                                                                 |

## Get the WorkSpaces client

Download and install the latest version of the WorkSpaces client for your platform from
the [Amazon WorkSpaces Client Download
page](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/").

## PCoIP end of support

###### Important

AWS is ending support for PCoIP-based WorkSpaces Personal on October 31, 2027. The new
client experience supports connecting to DCV-based WorkSpaces only. If you use
PCoIP-based WorkSpaces, see [PCoIP-based
WorkSpaces Personal end of support](../adminguide/workspaces-pcoip-end-of-support.md "../adminguide/workspaces-pcoip-end-of-support.md") or contact your administrator.

## Additional client documentation by platform

- [WorkSpaces Android client application](amazon-workspaces-android-client.md "amazon-workspaces-android-client.md")
- [WorkSpaces iPad client application](amazon-workspaces-ipad-client.md "amazon-workspaces-ipad-client.md")
- [WorkSpaces Linux client application](amazon-workspaces-linux-client.md "amazon-workspaces-linux-client.md")
- [WorkSpaces macOS client application](amazon-workspaces-osx-client.md "amazon-workspaces-osx-client.md")
- [WorkSpaces PCoIP zero client](amazon-workspaces-pcoip-zero-client.md "amazon-workspaces-pcoip-zero-client.md")
- [WorkSpaces Web Access](amazon-workspaces-web-access.md "amazon-workspaces-web-access.md")
- [WorkSpaces Windows client application](amazon-workspaces-windows-client.md "amazon-workspaces-windows-client.md")

## Related topics

- [Getting started with your WorkSpace](workspaces-user-getting-started.md "workspaces-user-getting-started.md")
- [Supported features by protocol type for WorkSpaces](supported-features.md "supported-features.md")
- [PCoIP-based
  WorkSpaces Personal end of support](../adminguide/workspaces-pcoip-end-of-support.md "../adminguide/workspaces-pcoip-end-of-support.md")
- [End of life policy for
  WorkSpaces client applications](../adminguide/workspaces-eol.md "../adminguide/workspaces-eol.md")
