# WorkSpaces Web Access

###### Note

Starting November 7, 2025, Amazon WorkSpaces PCoIP Web Access will no longer be open to new customers. After this date, the feature will only receive critical functional and security updates. While existing users can continue using the feature, new users will not be able to connect to their PCoIP WorkSpaces using Web Access.

For continued Web Access usage, we recommend evaluating [migration to DCV protocol](https://aws.amazon.com/blogs/desktop-and-application-streaming/seamlessly-modify-existing-amazon-workspaces-to-use-the-workspaces-streaming-protocol/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/seamlessly-modify-existing-amazon-workspaces-to-use-the-workspaces-streaming-protocol/"), which has Web Access support that offers improved performance and enhanced features including SAML and certificate-based authentication. Alternatively, PCoIP users can switch to [WorkSpaces client applications](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/") for full feature support.

You can access your DCV-based Windows and Linux-based WorkSpaces from the convenience of your web browser. You may choose
this option if you prefer not to install one of the Amazon WorkSpaces client applications, or if you are accessing your WorkSpace
from a personal device.

The following information will help you get started with WorkSpaces web access.

###### Requirements

- Your administrator must enable web access on your WorkSpace. For more information, check with your administrator or
  see [Enable and Configure WorkSpaces Web Access](../adminguide/web-access.md "../adminguide/web-access.md") in the Amazon WorkSpaces Administration Guide.
- Web access is supported with DCV-based WorkSpaces where the WorkSpace is running Windows or Linux.
  - On Windows, macOS, and Linux devices: Web access for Amazon DCV is supported on Google Chrome, Microsoft Edge, Apple Safari and Mozilla Firefox browsers when running on the latest three browser versions.
  - On Android tablets, Chromebooks, and iPads: Web access for Amazon DCV is supported on Google Chrome and Apple Safari browsers when running on the latest three browser versions.

- Web access for PCoIP-based WorkSpaces has the following limitations:
  - Web access for PCoIP is not supported in the AWS GovCloud (US), Asia Pacific (Mumbai), Africa (Cape Town), Israel (Tel Aviv), or Europe (Paris) regions.
  - Web access for PCoIP is only supported for Windows-based WorkSpaces, not Linux-based WorkSpaces.
  - Web access for PCoIP is only supported on Google Chrome and Mozilla Firefox browsers on Windows, macOS and Linux devices when running on the latest three browser versions.
  - Web access for PCoIP does not support multiple monitors.
  - Web access for PCoIP does not support connecting to GPU-enabled WorkSpaces.

###### Note

YUV444 encoding is not supported with WorkSpaces web access. If your administrator uses a Group Policy setting to enable YUV444 encoding, this may cause issues during login or rendering issues during your session.

###### Contents

- [Display support](#web-access-views "#web-access-views")
- [Proxy servers](#web-access-proxy "#web-access-proxy")
- [Supported features for DCV-based WorkSpaces](#wsp-for-wsp-client "#wsp-for-wsp-client")
- [Supported features and gestures on Android tablets and iPads](#supported-features-tablets "#supported-features-tablets")
- [Enabling diagnostic log uploads](#enable-diagnostic-logging "#enable-diagnostic-logging")

## Display support

WorkSpaces Web Access supports up to two monitors when connecting to DCV-based WorkSpaces.

## Proxy servers

If you are required to use a proxy server to access the internet, you can configure
your browser to use the proxy server.

###### Requirements

- Proxy with authentication is not currently supported.
- Proxy server support for Web Access may vary by browser. Refer to your browser’s proxy
  settings for more information.

## Supported features for DCV-based WorkSpaces

The following features are supported for DCV-based WorkSpaces.

### Copying and pasting

You can use the web client to copy and paste plain text and PNG images between your
local device and the WorkSpaces session. On Google Chrome and Microsoft Edge, you can use keyboard
shortcuts and context (right-click) menu to copy and paste text and images. On Mozilla Firefox
and Apple Safari you can use the clipboard dialog to copy and paste plain text; images are
not supported.

### Using a webcam

Webcam functionality is supported on Google Chrome and Microsoft Edge. On Mozilla Firefox, webcams
are supported with Windows-based WorkSpaces only. Webcams are not supported on Apple Safari.

###### Selecting the webcam you want to use

1. Choose the drop-down with your **Workspaces Name** on the top right of
   your WorkSpaces session, and then choose **Preferences**.
2. Choose the **Audio and Video** tab, scroll down to **Camera**,
   and then select the camera to use.
3. Select **Save**.

###### Note

Cameras will appear only if your administrator has enabled webcam support for your WorkSpace.
You can't change the webcam selection while the webcam is in use.

**Using a webcam during your session**

Toggle the webcam button in the client toolbar as shown below to enable
or disable your webcam during your session. The webcam button appears on the toolbar
only if webcam support is enabled and at least one webcam is connected to
your local device.

![The webcam button in the WorkSpaces Web Access client.](images/webaccess-webcam-button.png)

The following table shows different webcam states:

| Icon                    | Description                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The webcam is disabled. | The webcam is disabled. Toggle the button to enable the webcam. If you didn't previously select the webcam to use, the default webcam is used. |
| The webcam is enabled.  | The webcam is enabled, but it's not in use. Toggle the button to disable the webcam.                                                           |
| The webcam is in use.   | The webcam is in use by a remote application in the WorkSpaces session. Toggle the button to disable the webcam.                               | ### Using multiple screens To use multiple screens, choose the multiscreen button in the client as shown in the following example. Multiple screens are supported with up to two monitors. ![The multiscreen button in the WorkSpaces Web Access client.](images/webaccess-multiscreen-button.png) ## Supported features and gestures on Android tablets and iPads Android tablets are supported on Google Chrome, and iPads are supported on Apple Safari. Touch input is supported for both device types. ###### Gestures <br>• Use a two-finger single tap gesture or use the client toolbar button to toggle the on-screen keyboard. <br>• Use a pinch gesture to zoom in our out on the screen. When zoomed in, use a two-finger slide gesture to pan the screen horizontally or vertically. <br>• Use a three-finger single tap gesture to show the client toolbar when it has been hidden by auto-hide. ###### Trackpad mode <br>• To enable track pad mode, choose the drop-down with your **WorkSpace Name** on the top right of your WorkSpaces session, and then choose **Enable trackpad mode**. <br>• Once trackpad mode is enabled: + Use a short one-finger tap to trigger a mouse left click. + Use a longer one-finger tap to trigger a mouse right click. ###### Screen resolution and other functionality <br>• Your screen resolution may be automatically adjusted to fit the tablet screen size. <br>• If you rotate the tablet device, the screen will automatically resize itself. <br>• Full screen is not supported on Apple Safari on iPads. ## Enabling diagnostic log uploads To troubleshoot issues with WorkSpaces web access, you can enable diagnostic logging. The log files that are sent to AWS include detailed information about your device and connection to the AWS network. You can enable automatic diagnostic log uploads before or during your WorkSpace streaming sessions. ###### To send log files 1. Open the Amazon WorkSpaces Web Access page. If you’re currently in your WorkSpaces session, disconnect from it so you return to the pre-session page. 2. At the top of the pre-session page, choose **Settings**, then **Diagnostic logging**. 3. Ensure **Diagnostic logging** is enabled. 4. (Optional) To generate debugging-level details and verbose performance data, choose **Advanced logging**. |
