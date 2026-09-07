

# WorkSpaces macOS client application
<a name="amazon-workspaces-osx-client"></a>

The following information helps you get started with the WorkSpaces macOS client application.

**Topics**
+ [Requirements](#osx-requirements)
+ [Setup and installation](#osx_setup)
+ [Determine your client version](#determine-version-osx)
+ [Connect to your WorkSpace](#osx_connecting)
+ [Manage your login information (3.0\+ clients only)](#manage-login-info-osx)
+ [Client views](#osx_views)
+ [Client language](#osx_client_lang)
+ [Display support](#osx-display-support)
+ [Proxy servers](#osx_proxy_server)
+ [IPv6 network settings](#osx_ipv6_settings)
+ [Command shortcuts](#osx_shortcuts)
+ [Remap the Windows logo key or the Command key](#osx_remap_command_key)
+ [Disconnect](#osx_disconnect)
+ [Clipboard support](#osx_clipboard_support)
+ [Diagnostic log upload](#diagnostic-log-uploads-osx)
+ [Release notes](#osx-release-notes)

## Requirements
<a name="osx-requirements"></a>

The Amazon WorkSpaces client for macOS requires an Apple supported version of macOS. For more details, please refer to the [macOS Release Notes](https://developer.apple.com/documentation/macos-release-notes) on the *Apple Developer Documentation* site.

The versions that are currently supported are listed in the following table:


| macOS version | PCoIP | DCV | 
| --- | --- | --- | 
| 12 (Monterey) and earlier | Not supported | Not supported | 
| 13 (Ventura) | Supported | Supported | 
| 14 (Sonoma) | Supported | Supported | 
| 15 (Sequoia) | Not supported | Supported | 
| 26 (Tahoe) | Supported | Supported | 

## Setup and installation
<a name="osx_setup"></a>

Download and install the latest version of the Amazon WorkSpaces client application from the [Amazon WorkSpaces Client Download](https://clients.amazonworkspaces.com/) website.

### Updating the client application
<a name="osx_update_client"></a>

The Amazon WorkSpaces client application on macOS will automatically check for available updates, and when new versions become available, will install them in the background when you’re not using it. Once the installation is complete, you simply need to open the client to begin using the latest version. This will provide you with faster access to the latest features, enhancements, and bug fixes without interrupting your productivity.

**Note**  
Automatic client updates are only applied when your client application is used to connect to WorkSpaces in the below regions.


| Region | Address | 
| --- | --- | 
| US East (N. Virginia) | us-east-1 | 
| US West (Oregon) | us-west-2 | 
| Africa (Cape Town) | af-south-1 | 
| Asia Pacific (Mumbai) | ap-south-1 | 
| Asia Pacific (Seoul) | ap-northeast-2 | 
| Asia Pacific (Singapore) | ap-southeast-1 | 
| Asia Pacific (Sydney) | ap-southeast-2 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | 
| Canada (Central) | ca-central-1 | 
| Europe (Frankfurt) | eu-central-1 | 
| Europe (Ireland) | eu-west-1 | 
| Europe (London) | eu-west-2 | 
| Europe (Paris) | eu-west-3 | 
| Israel (Tel Aviv) | il-central-1 | 
| South America (São Paulo) | sa-east-1 | 

In any other regions not listed above, the Amazon WorkSpaces client application on macOS will not update automatically; you will instead see a message when a new version is available, and will have the option to install it.

## Determine your client version
<a name="determine-version-osx"></a>

To see which version of the WorkSpaces client you have, choose **Amazon WorkSpaces**, **About Amazon WorkSpaces**, or click the gear icon in the upper-right corner and choose **About Amazon WorkSpaces**.

## Connect to your WorkSpace
<a name="osx_connecting"></a>

To connect to your WorkSpace, complete the following procedure.

### To connect to your WorkSpace for 3.0\+ clients
<a name="osx_connecting-new-clients"></a>

1. The first time that you run the client application, you are prompted for your registration code, which is contained in your welcome email. The WorkSpaces client application uses the registration code and user name to identify which WorkSpace to connect to. When you launch the client application later, the same registration code is used. To enter a different registration code, launch the client application, and then choose **Change Registration Code** at the bottom of the login page.

1. Enter your sign-in credentials in the login screen and choose **Sign In**. If your WorkSpaces administrator has enabled multi-factor authentication for your organization's WorkSpaces, you are prompted for a passcode to complete your login. Your WorkSpaces administrator will provide more information about how to obtain your passcode.

1. If your WorkSpaces administrator has not disabled the **Keep me logged in** feature, you can select the **Keep me logged in** check box at the bottom of the login screen to save your credentials securely so that you can connect to your WorkSpace easily while the client application remains running. Your credentials are securely cached up to the maximum lifetime of your Kerberos ticket.

   After the client application connects to your WorkSpace, your WorkSpace desktop is displayed.

An interruption of network connectivity causes an active session to be disconnected. This can be caused by events such as closing the laptop lid, or the loss of your wireless network connection. The WorkSpaces client application for macOS attempts to reconnect the session automatically if network connectivity is regained within a certain amount of time. The default session resume timeout is 20 minutes, but this timeout can be modified by your network administrator.

## Manage your login information (3.0\+ clients only)
<a name="manage-login-info-osx"></a>

You can view your registration code and what Region your WorkSpace is in. You can specify whether you want the WorkSpaces client application to save your current registration code, and you can assign a name to your WorkSpace. You can also specify if you want Amazon WorkSpaces to keep you logged in to a WorkSpace until you quit or your login period expires.

**To manage your login information for a WorkSpace**

1. In the WorkSpaces client application, go to **Settings**, **Manage Login Information**.

1. In the **Manage Login Information** dialog box, you can see the registration code and Region information for your WorkSpace.

1. (Optional) If you want the WorkSpaces client to remember your current registration code, select the **Remember Registration Code** check box.

1. Under **Saved registration codes**, select the WorkSpace you want to name.

1. In the **WorkSpace name** box, enter a name for the WorkSpace.

1. (Optional) If you want WorkSpaces to keep you logged in until you quit or your login period expires, select the **Keep me logged in** check box.

1. Choose **Save**.

## Client views
<a name="osx_views"></a>

You can switch to full screen mode by choosing **View**, **Enter Full Screen** (3.0\+ clients) in the client application menu.

While in full screen mode, you can switch back to window mode by moving the pointer to the top of the screen. The client application menu is displayed, and you can choose **View**, **Leave Full Screen** (3.0\+ clients) in the client application menu.

You can also toggle full screen mode by pressing Command\+Option\+Return.

## Client language
<a name="osx_client_lang"></a>

You can select the language displayed by the client by performing the following steps.

**Note**  
The WorkSpaces client applications support Japanese. However, Japanese WorkSpaces are available only in the Asia Pacific (Tokyo) Region.

**To select the client language**

1. Depending on which client you're using, do one of the following.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-osx-client.html)

1. Enter your desired language in the **Select a language** list and choose **Save**.

1. Restart the client.

## Display support
<a name="osx-display-support"></a>

WorkSpaces WorkSpaces Value, Standard, Performance, Power, PowerPro, and GPU-enabled bundles support a maximum of four displays and a maximum resolution of 3840x2160 (ultra-high definition, or UHD). The maximum supported resolution depends on the number of displays, as shown in the following table.


| Displays | Resolution | 
| --- | --- | 
| 2 | 3840x2160 | 
| 4 | 1920x1200 | 

**Note**  
You can only extend the display. You cannot duplicate the display. Duplicating the display will cause your session to be disconnected.

The WorkSpaces client application extracts the Extended Display Information Data (EDID) of all attached displays and determines the best compatibility match before starting the session. If you have a high pixel density (high DPI) display, the client application automatically scales the streaming window according to your local DPI settings. For better maximum resolution with high DPI displays, see [Enabling high DPI display for WorkSpaces](high_dpi_support.md).

**Note**  
If your screen resolution in WorkSpaces is low and objects look blurry, you need to turn on high DPI mode and adjust the display scaling settings on your Mac. For more information, see [Enabling high DPI display for WorkSpaces](high_dpi_support.md).

**To use multiple monitors with WorkSpaces**

1. Configure your local machine to use multiple monitors. For more information, see [Connect one or more external displays with your Mac](hhttps://support.apple.com/guide/mac-help/connect-an-external-display-mchl7c7ebe08/mac) in the Apple documentation.

1. Start the WorkSpaces client application and log in to your WorkSpace.

1. Depending on which client you're using, do one of the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-osx-client.html)

Your WorkSpace should now be extended across your displays. Whichever display you have designated as your primary display is also the primary display in WorkSpaces when you enter full screen mode.

**Note**  
To use full screen mode on only some of the displays in a multiple monitor setup, press and hold the Option key and then click the green maximize button ![Maximize button in the top-left corner of the WorkSpaces window](http://docs.aws.amazon.com/workspaces/latest/userguide/images/mac-maximize-button.png) in the top-left corner of the WorkSpaces window. This button expands the WorkSpaces client window to full size on a screen without extending the WorkSpace to the other displays. To return to the previous window size, press and hold the Option key and click the maximize button again.

## Proxy servers
<a name="osx_proxy_server"></a>

If your network requires you to use a proxy server to access the internet, you can enable your WorkSpaces client application to use a proxy for HTTPS (port 443) traffic. The WorkSpaces client applications use the HTTPS port for updates, registration, and authentication. 

**Note**  
The desktop streaming connections to the WorkSpace require ports 4172 and 4195 to be enabled, and do not go through the proxy server. 
Proxy servers that require authentication with a sign-in credentials are not supported.

### To use a proxy server for 3.0\+ clients
<a name="osx_proxy_server-new-clients"></a>

By default, the 3.0\+ macOS clients use the proxy server that's specified in the device operating system settings. The first time the client is launched, the device operating system proxy server setting is used. If you select another option for the proxy server, that setting is used for subsequent launches of the client.

**Note**  
If you specify a custom proxy server, a "No network" error might appear when you attempt to log in to your WorkSpace. To work around this issue, use the default operating system proxy server instead of specifying a custom proxy server in the macOS client.

1. In the WorkSpaces client application, go to **Settings**, **Manage Proxy Server**.

1. In the **Set Proxy** dialog box, select **Use proxy server**, enter the proxy server URL or IP address and the port, and choose **Save**.

## IPv6 network settings
<a name="osx_ipv6_settings"></a>

The WorkSpaces client application supports connecting to your WorkSpace via IPv4, IPv6, or dual-stack (both IPv4 and IPv6). By default, IPv4 connections are used for streaming.

**To enable an IPv6 connection**

1. In the WorkSpaces client application, go to **Settings**, **Manage Connection Settings**.

1. In the **Connection Settings** dialog, under **General Connection Settings**, check the box to **Prefer IPv6-enabled communications**.

   This setting is disabled by default, meaning that your client application will exclusively use an IPv4 network for your connection. If you enable it, your client application will prioritize using an IPv6 network, but will fall back to using an IPv4 network if IPv6 is not available.

Alternatively, organizations may also configure this setting using macOS Defaults:
+ Namespace: `com.amazon.workspaces`
+ Key: `WSUseDualStackIPv6`
  + Set its value to `1` to enable IPv6 preferred.
  + Set its value to `0` to disable IPv6 preferred (meaning it will use IPv4 exclusively).
+ Changes will take effect the next time you launch the WorkSpaces client application. Users can modify this setting, but it will revert to the Defaults value when the client is relaunched.

**Note**  
IPv6 connections are supported on the WorkSpaces client application version `5.30.1` or later.
IPv6 connection settings need to be changed before connecting to your WorkSpace. They cannot be changed while connected to your WorkSpace.

## Command shortcuts
<a name="osx_shortcuts"></a>

The WorkSpaces macOS client supports the following command shortcuts:


| If you're using... | Use these shortcuts | 
| --- | --- | 
| 3.0\+ client | Command\+Q—Quit Amazon WorkSpaces<br />Command\+Option\+Return—Toggle full screen display<br />Command\+Option\+F12—Disconnect session | 

## Remap the Windows logo key or the Command key
<a name="osx_remap_command_key"></a>

By default, the Windows logo key on a Windows keyboard and the Command key on an Apple keyboard are both mapped to the Ctrl key when you're using the Amazon WorkSpaces macOS client application. If you want to change this behavior so that these two keys are mapped to the Windows logo key for use with Windows WorkSpaces, use the following procedure.

**To map the Windows logo key or the Command key to the Windows logo key**

1. If you haven't already done so, [install or update](#osx_setup) to version 3.0.5 or later of the Amazon WorkSpaces macOS client application.

1. In the **Finder**, open your **Applications** folder, then open **Utilities**, and choose **Terminal**.

1. In the Terminal window, enter the following command, and then press the Return key.

   ```
   defaults write "com.amazon.Amazon WorkSpaces Client" remap_cmd_to_ctrl 0
   ```

1. In the Terminal app, choose **Terminal**, **Quit Terminal**.

1. If your WorkSpaces macOS client application is running, choose **Amazon WorkSpaces**, **Quit Amazon WorkSpaces** in the client to close the client application.

1. Restart the WorkSpaces macOS client application and log in to your WorkSpace. The Windows logo key or the Command key should now be mapped to the Windows logo key.

## Disconnect
<a name="osx_disconnect"></a>

To disconnect the macOS client application, you have several options: 
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Disconnect WorkSpace**. Your WorkSpace session ends, but the client application continues running in case you want to log in again.
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **End Session**. 

  When ending the session, you'll be prompted to save open documents. Selecting **End Session** in the prompt will disconnect you from the WorkSpaces client user session.
**Note**  
This option is available only for WorkSpaces Pools. 
+ In the Amazon WorkSpaces client application, go to **Amazon WorkSpaces**, and then choose **Quit Amazon WorkSpaces**. Your WorkSpace session ends, and the client application closes.
+ In the Amazon WorkSpaces client application, close the WorkSpaces client window by clicking the red close (X) button in the upper-left corner. This disconnects the session and returns you to the application homepage.
+ You can also log off of the WorkSpace. In the Amazon WorkSpaces client application, go to **View**, and then choose **Send Ctrl\+Alt\+Delete**. Choose **Sign Out**. Your WorkSpace session ends, but the client application continues running in case you want to log in again.

## Clipboard support
<a name="osx_clipboard_support"></a>

The clipboard supports a maximum uncompressed object size of 20 MB. For more information, see [I'm having trouble copying and pasting](client_troubleshooting.md#copy_paste).

**Note**  
When copying from a Microsoft Office app, the clipboard only contains the last copied item, and the item is converted into standard format. If you copy content larger than 890 KB from a Microsoft Office app, the app might become slow or unresponsive for up to 5 seconds. 

## Diagnostic log upload
<a name="diagnostic-log-uploads-osx"></a>

### Enabling diagnostic log uploads
<a name="enabling-diagnostic-log-uploads-osx"></a>

To troubleshoot issues with the WorkSpaces client, you can enable diagnostic logging. The log files that are sent to WorkSpaces include detailed information about your device and connection to the AWS network. You can enable diagnostic log uploads before or during WorkSpace streaming sessions so that these files are sent to WorkSpaces automatically.

**To send log files:**
**Note**  
You can send log files before and during WorkSpaces streaming sessions.

1. Open your Amazon WorkSpaces client.

1. At the top of the WorkSpaces sign-in page, choose **Manage Diagnostic Logging Settings**.

1. In the pop-up dialog box, choose **Enable Diagnostic Logging for Amazon WorkSpaces** and click **Save**.
**Important**  
When you report an issue to AWS support, ensure you keep track of the device ID of the client who is experiencing the issue. This device ID can be found in the diagnostics logging menu, in the WorkSpaces client navigation bar, and it helps the support team identify logs associated with your specific device. Ensure you include the device ID in the tickets that you create regarding this specific issue.

## Release notes
<a name="osx-release-notes"></a>

The following table describes the changes to each release of the client application.


| Release | Date | Changes | 
| --- | --- | --- | 
| 5.33.0 | July 7, 2026 |  +  Updated the client application as a Universal app, enabling dual support for both Apple silicon and Intel-based Macs. <br />+  Added support for URL redirection, enabling administrators to configure certain websites to be redirected from the streaming session to the local device's web browser. <br />+  Fixed an issue with the username not being pre-populated in the new user login flow when "Remember me" is selected. <br />+  Fixed an issue that prevented changing the registration code when there is no network connectivity. <br />+  Fixed an application crash that occurred when using a YubiKey for signing in under certain conditions. <br />+  Fixed an issue that prevented connecting to a WorkSpace via custom proxy when credentials are not stored locally. <br />+  Updated the DCV SDK. <br />+  Additional bug fixes and enhancements.   | 
| 5.32.0 | April 23, 2026 |  +  Added support for connecting to WorkSpaces in the US East (Ohio) and Asia Pacific (Malaysia) regions. <br />+  Made an improvement that enables microphone audio streaming only when a remote application is using it, helping to optimize performance. <br />+  Fixed an issue that was preventing copying and pasting from the clipboard between the local client device and the WorkSpace in some scenarios. <br />+  Updated the DCV SDK. <br />+  Updated the PCoIP SDK. <br />+  Other bug fixes and enhancements.   | 
| 5.31.0 | January 21, 2026 |  +  Added support for real-time audio optimization for DCV-based WorkSpaces, which routes the audio from web applications running on the WorkSpace to the local device, improving the audio call quality. <br />+  Added improved error messaging in the case of a SAML session timeout. <br />+  Other bug fixes and enhancements.   | 
| 5.30.2 | November 3, 2025 |  + Bug fixes and enhancements.  | 
| 5.30.1 | October 21, 2025 |  + Added support for connecting to your WorkSpace via IPv6.  | 
| 5.30.0 | October 13, 2025 |  + Improved the international keyboard experience with new keyboard layout options (server or client) with DCV-based WorkSpaces.<br />+  Updated the DCV SDK. <br />+  Updated the PCoIP SDK. <br />+  Updated the .NET Framework.   | 
| 5.29.1 | August 6, 2025 |  +  Bug fixes and enhancements.   | 
| 5.29.0 | July 31, 2025 |  +  Added a new automatic client update feature that automatically checks for available updates and installs them when you're not using the client, helping you to get the latest features and bug fixes. <br />+  Bug fixes and enhancements.   | 
| 5.28.1 | July 2, 2025 |  +  Bug fixes and enhancements.   | 
| 5.27.0 | April 30, 2025 |  +  Updated the DCV SDK. <br />+  Updated the PCoIP SDK. <br />+  Bug fixes and enhancements.   | 
| 5.26.2  | April 1, 2025 | Bug fixes and enhancements. | 
| 5.26.0 | March 4, 2025 |  +  Updated the DCV SDK. <br />+  Updated the .NET SDK. <br />+  Bug fixes and enhancements.   | 
| 5.25.0 | December 19, 2024 | Bug fixes and enhancements. | 
| 5.24.0 | November 22, 2024 |  +  Added a progress bar to help users better understand the expected time during the loading of their WorkSpace. <br />+  Added a notification to warn idle users they will be disconnected from their DCV WorkSpaces due to inactivity. <br />+  Updated the DCV SDK. <br />+  Updated the RestSharp library. <br />+  Bug fixes and enhancements.   | 
| 5.23.1 | October 17, 2024 |  Bug fixes and enhancements.  | 
| 5.23.0 | September 30, 2024 |  +  Renamed WSP protocol to Amazon DCV protocol. <br />+  Added support for streaming over port 443 for TCP and UDP protocols on DCV WorkSpaces. <br />+  Updated the .NET SDK. <br />+  Bug fixes and enhancements.   | 
| 5.22.1 | September 3, 2024 | Bug fixes and enhancements. | 
| 5.22.0 | August 16, 2024 | Updated the DCV SDK. | 
| 5.21.0 | July 3, 2024 | Bug fixes and enhancements. | 
| 5.20.0 | June 13, 2024 |  +  Updated PCoIP SDK. <br />+  Updated DCV SDK. <br />+  Migrated the software framework to .NET 8 LTS. <br />+  Updated system to require macOS 12 or later.   | 
| 5.19.3 | April 30, 2024 |  Fixed issue where users get immediately disconnected from their DCV WorkSpaces when connecting to it.  | 
| 5.19.0 | February 28, 2024 |  +  Added WebAuthn support for in-session authentication. <br />+  Resolved a white screen issue for DCV WorkSpaces. <br />+  Fixed the pixelation issue for DCV WorkSpaces. <br />+  Resolved crash issues for DCV WorkSpaces. <br />+  Updated DCV SDK.   | 
| 5.18.0 | January 22, 2024 |  +  Updated PCoIP SDK. <br />+  Updated DCV SDK. <br />+  Added support for macOS 14 (Sonoma). <br />+  Fixed keyboard issue where the first keystrokes were not being transmitted after unlocking the screen.   | 
| 5.17.0 | November 16, 2023 |  +  Fixed a login issue due to a custom proxy error on macOS Ventura. <br />+  Added support to configure option key behavior on DCV client. <br />+  Fixed a client crash when users change running mode. <br />+  Fixed the screen freezing issue when using a Smart Card on DCV client. <br />+  Improve stability during resizes on DCV client. <br />+  Improved visual accessibility.   | 
| 5.16.0 | October 26, 2023 |  +  Improved visual accessibility. <br />+  Updated DCV SDK.   | 
| 5.15.1 | September 20, 2023 |  +  Enabled persistent Webcam connection after fast DCV WorkSpace reconnection. <br />+  Fixed connectivity issues on DCV WorkSpaces when using a proxy server. <br />+  Updated DCV SDK. <br />+  Bug fixes and enhancements.   | 
| 5.12.0 | August 29, 2023 |  +  Updated PCoIP SDK and DCV SDK. <br />+  Resolved an login page special character processing issue. <br />+  Added a link to Amazon WorkSpaces user guide under the Support menu.   | 
| 5.11.0 | June 29, 2023 | Added options to enable or disable **Ctrl** \+ left-click as right-click and enable or disable mapping the **Command** key to the **Ctrl** key. To access both options, from the menu bar, choose **Settings**, **Manage Modifier Keys**. | 
| 5.10.0 | June 19, 2023 |  +  Improved client custom branding by storing assets in the same AWS Regions as provisioned WorkSpaces. <br />+  Resolved black screen issue when using multiple monitors with Ubuntu WorkSpaces. <br />+  Fixed client diagnostic log uploading issues, where proxy settings were not being persisted when connecting to WorkSpaces through a proxy server. <br />+  Added support for DCV extension SDK, which allows end users to customize their DCV WorkSpaces experience.   | 
| 5.9.0 | May 9, 2023 |  Updated DCV SDK to fix playback volume issues.  | 
| 5.8.0 | April 6, 2023 |  +  Added accessibility improvements. <br />+  Added support for automatic diagnostic log uploads feature, which allows you to upload WorkSpaces client log files directly to WorkSpaces to troubleshoot issues without interrupting the use of the WorkSpaces client. <br />+  Updated the DCV v2 SDK to fix InSessionLatency reporting.   | 
| 5.7.0 | February 23, 2023 |  +  Updated the DCV SDK. <br />+  Enabled trimming leading or trailing allow list in sign-in credentials.   | 
| 5.6.0 | December 27, 2022 |  +  Added support for certificate-based authentication via SAML 2.0 integration, which removes the logon prompt for the Active Directory domain password. <br />+  Resolved the issue of the Workspace menu bar being inaccessible when maximizing the Workspace application window. <br />+  Updated PCoIP SDK for the WorkSpaces macOS client.   | 
| 5.5.0 | November 14, 2022 | Updated the DCV client SDK. | 
| 5.4.0 | November 10, 2022 | Added a shortcut Command\+Alt\+F12 to disconnect your WorkSpaces. | 
| 5.3.0 | September 15, 2022 | Bug fixes and enhancements. | 
| 5.2.0 | August 24, 2022 | Fixed WorkSpaces login issue when using Smart Card. | 
| 5.1.0 | June 30, 2022 | Updated PCoIP SDK for MacOS. | 
| 4.0.7 | March 3, 2022 | Fixed a WorkSpaces connection error caused by the Proxy settings on MacBook. | 
| 4.0.6 | December 21, 2021 |  +  Resolves crashes and black screen issues related to video streaming for DCV <br />+  Updates to DCV version 1.9.8.18175   | 
| 4.0.5 | November 23, 2021 |  +  Optimizes the bandwidth and frame rates for DCV WorkSpaces <br />+  Resolves the shortcut mapping issue related to full screen mode   | 
| 4.0.4 | November 3, 2021 |  +  Resolves the spinning wheel problem on the Login screen in macOS Big Sur with PCoIP WorkSpaces <br />+  Video streaming improvements for WorkSpaces that support DCV <br />+  Bug fixes   | 
| 4.0.3 | October 4, 2021 | Bug fixes and enhancements. | 
| 4.0.2 | September 8, 2021 | Minor bug fixes and enhancements. | 
| 4.0.1 | August 5, 2021 | Minor bug fixes and enhancements. | 
| 3.1.9 | June 29, 2021 | Minor bug fixes and enhancements. | 
| 3.1.8 | May 28, 2021 |  +  Addresses a crash issue after disconnecting from PCoIP WorkSpaces <br />+  Addresses a connectivity issue with DCV WorkSpaces on M1 Mac hardware <br />+  Minor bug fixes and enhancements   | 
| 3.1.7 | April 29, 2021 |  +  Improves connectivity with WorkSpaces using the DCV <br />+  Minor bug fixes and enhancements   | 
| 3.1.6 | April 8, 2021 | Fixes for disconnects and crashes resulting from DCV audio traffic optimization | 
| 3.1.5 | April 2, 2021 |  +  Adds in-session and pre-session support for Common Access Card (CAC) and Personal Identity Verification (PIV) smart cards with DCV Windows WorkSpaces <br />+  Bidirectional video webcam support is now generally available for Windows WorkSpaces using the DCV <br />+  Minor bug fixes and enhancements   | 
| 3.1.4 | March 16, 2021 |  +  Addresses a few crash scenarios when users register, log in, and rebuild <br />+  Adds localization support for more UI elements <br />+  Minor bug fixes and enhancements   | 
| 3.1.3 | February 15, 2021 |  +  Adds support for mouse middle button dragging <br />+  Minor bug fixes and enhancements   | 
| 3.1.2 | January 8, 2021 |  +  The DCV is now generally available. Video-in functionality continues to be available as a beta feature on DCV WorkSpaces only <br />+  Minor bug fixes and enhancements   | 
| 3.1.0 | December 1, 2020 | Minor bug fixes and enhancements | 
| 3.0.12 | November 10, 2020 |  +  Adds enhancements to the session reconnect experience <br />+  Improves error messaging during session disconnects for DCV WorkSpaces <br />+  Fixes keyboard mapping issue with the **Shift** key for DCV WorkSpaces <br />+  Fixes an issue in the device-enumeration logic where video-in devices might not be shown on subsequent logins for DCV WorkSpaces   | 
| 3.0.11 | October 02, 2020 |  +  Resolves an intermittent crash issue when disconnecting from a DCV WorkSpace <br />+  Minor bug fixes and enhancements   | 
| 3.0.10 | September 16, 2020 | Adds support for health checks over port 4195 (UDP and TCP) | 
| 3.0.9 | August 14, 2020 | Minor bug fixes and enhancements | 
| 3.0.8 | July 30, 2020 |  +  For improved diagnostics, displays round trip time (RTT) as part of the network health check information <br />+  Minor bug fixes and enhancements   | 
| 3.0.7 | June 3, 2020 |  +  Adds support for multiple monitors on DCV WorkSpaces <br />+  Minor bug fixes and enhancements   | 
| 3.0.6 | April 28, 2020 |  +  Adds support for toggling between high DPI and standard DPI displays <br />+  Minor bug fixes and enhancements   | 
| 3.0.5 | March 30, 2020 |  +  Resolves an issue with the user interface displaying a login prompt if single sign-on (SSO) is enabled for Amazon WorkDocs <br />+  Adds support to map the Command key to the Windows logo key   | 
| 3.0.4 | March 3, 2020 |  +  Adds support for connecting to DCV WorkSpaces <br />+  Minor bug fixes and enhancements   | 
| 3.0.3 | February 24, 2020 | Improves readability on high DPI devices | 
| 3.0.2 | February 14, 2020 |  +  Adds keyboard shortcut to toggle full screen display <br />+  Minor bug fixes and enhancements   | 
| 3.0.0 | November 25, 2019 |  +  Improved user interface <br />+  Friendly registration code labels <br />+  Client-side GPU rendering <br />+  Minor bug fixes and enhancements   | 
| 2.5.11 | November 4, 2019 |  +  Resolves issues with support for the macOS Catalina keyboard <br />+  Minor bug fixes   | 
| 2.5.9 |  | Minor bug fixes | 
| 2.5.8 |  |  +  Resolves an intermittent crashing issue related to computer waking up when opening a laptop lid   | 
| 2.5.7 |  |  +  Adds support for German keyboard layouts with Linux WorkSpaces <br />+  Resolves an issue that results in a crash of Excel with clipboard direction   | 
| 2.5.6 |  | Minor fixes | 
| 2.5.5 |  |  +  Resolves an issue with sub-optimal resolution with external displays in full-screen mode connected using USB-C <br />+  Minor bug fixes   | 
| 2.5.2 |  |  +  Resolves an issue that results in crashes when multiple monitors are used and clients are connected to WorkSpaces running Amazon Linux 2 <br />+  Resolves an intermittent issue with the Caps lock key becoming stuck <br />+  Minor bug fixes   | 
| 2.5.1 |  |  +  Resolves an issue that periodically results in repeated key presses with WorkSpaces running Amazon Linux 2 <br />+  Adds support for localized date and time formats in the user interface <br />+  Adds handling for URIs that end with an extra '/'  <br />+  Minor user interface improvements    | 
| 2.5.0 |  | Adds support for user self-service WorkSpace management capabilities | 
| 2.4.10 |  | Minor fixes | 
| 2.4.9 |  | Minor fixes | 
| 2.4.8 |  |  +  Adds support for uniform resource identifiers (URIs), which enable login orchestration <br />+  Improves the behavior of function (Fn) keys on macOS  <br />+  Improves protocol handling <br />+  Minor fixes   | 
| 2.4.7 |  |  +  Adds support for time zone redirection for more Regions: America/Indianapolis America/Indiana/Marengo America/Indiana/Vevay America/Indiana/Indianapolis <br />+  Includes text changes to the Login page user interface   | 
| 2.4.6 |  |  +  Adds support for configuring the logging level to include advanced logging for debug scenarios  <br />+  Minor improvements to session provision handling  <br />+  Increases error handling for keyboard connections   | 
| 2.4.4 |  |  +  Minor fixes <br />+  Improves copy and paste   | 
| 2.4.2 |  | Minor fixes | 
| 2.4.0 |  |  +  New logo <br />+  Improves the user interface and stability   | 
| 2.3.7 |  |  +  Addresses a gray screen issue that occurs when displays are in different orientations <br />+  Resolves a crashing issue on macOS   | 
| 2.3.6 |  | Localization enhancements | 
| 2.3.5 |  | Minor improvements | 
| 2.3.3 |  |  +  Improves support for multiple monitors <br />+  Localization enhancements <br />+  Improves security and performance   | 
| 2.3.1 |  | Minor fixes | 
| 2.3.0 |  |  +  Improves support for multiple monitors <br />+  Improves security and stability   | 
| 2.2.3 |  | Resolves minor bugs and improves stability | 
| 2.2.1 |  |  +  Adds support for the German language <br />+  Resolves issues with time zone mapping for some Regions <br />+  Resolves a connection issue on Russian systems <br />+  Improves the Japanese user interface <br />+  Improves stability   | 
| 2.1.4 |  | Resolves a crash issue on macOS Sierra | 
| 2.1.3 |  | Closing the client expires the reconnect token. You can easily reconnect to your WorkSpace as long as the client is running. | 
| 2.1.0 |  |  +  Adds support for the following new WorkSpace states: STOPPING and STOPPED <br />+  Resolves minor bugs and improves stability   | 
| 2.0.8 |  |  +  Resolves an issue with out-of-app keyboard input passing to WorkSpaces <br />+  If Remember Me is disabled, the user name is not shown on restart <br />+  Adds a confirmation dialog box when deleting a registration code <br />+  Improves stability   | 
| 2.0.4 |  |  +  Adds support for audio in, enabling you to make calls or attend web conferences <br />+  Adds support for devices with high DPI screens <br />+  Adds support for saving registration codes, enabling you to switch WorkSpaces without re-entering the registration codes <br />+  Improves support for OS X El Capitan <br />+  Improves usability and stability   | 
| 1.1.80 |  |  +  Adds CloudWatch metrics for session latency, session launch time, and session disconnects <br />+  Improves auto session resume so that you are interrupted less frequently when network conditions are degraded <br />+  Resolves specific issues and improves stability   | 
| 1.1.6 |  |  +  Adds support for status notifications. The client application notifies you about the state of your WorkSpace when it cannot connect to the WorkSpace. <br />+  Improves the reconnect experience. The client automatically redirects to the login screen after 10 hours of inactivity. You can reconnect again if the client fails to launch a session using reconnect. <br />+  Adds support for auto session resume. The client application automatically attempts to resume your session if network connectivity is lost and then regained within the session resume timeout (default value is 20 minutes). <br />+  Improves network health checks so they are faster and more reliable <br />+  Adds client-side validation of registration codes <br />+  Improves the synchronization of Caps Lock and Num Lock status between the local device and the WorkSpace   | 
| 1.1.4 |  |  +  Adds support for saving your credentials, enabling you to easily reconnect to your WorkSpace <br />+  Improves advanced connection health checks <br />+  Improves stability   | 
| 1.0.8 |  |  +  Introduces a full-file installation package <br />+  Improves network connectivity checks <br />+  Adds version information to the **About** window   | 
| 1.0 |  | Initial release | 