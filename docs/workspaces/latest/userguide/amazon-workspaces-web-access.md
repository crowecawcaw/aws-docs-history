

# WorkSpaces Web Access
<a name="amazon-workspaces-web-access"></a>

**Note**  
As of November 7, 2025, Amazon WorkSpaces PCoIP Web Access is no longer open to new customers. The feature will only receive critical functional and security updates going forward. While existing users can continue using the feature, new users will not be able to connect to their PCoIP WorkSpaces using Web Access.  
For continued Web Access usage, we recommend evaluating [migration to DCV protocol](https://aws.amazon.com/blogs/desktop-and-application-streaming/seamlessly-modify-existing-amazon-workspaces-to-use-the-workspaces-streaming-protocol/), which has Web Access support that offers improved performance and enhanced features including SAML and certificate-based authentication. Alternatively, PCoIP users can switch to [WorkSpaces client applications](https://clients.amazonworkspaces.com/) for full feature support.

You can access your DCV-based Windows and Linux-based WorkSpaces from the convenience of your web browser. You may choose this option if you prefer not to install one of the Amazon WorkSpaces client applications, or if you are accessing your WorkSpace from a personal device.

The following information will help you get started with WorkSpaces web access.

**Requirements**
+ Your administrator must enable web access on your WorkSpace. For more information, check with your administrator or see [Enable and Configure WorkSpaces Web Access](https://docs.aws.amazon.com/workspaces/latest/adminguide/web-access.html) in the Amazon WorkSpaces Administration Guide.
+ Web access is supported with DCV-based WorkSpaces where the WorkSpace is running Windows or Linux.
  + On Windows, macOS, and Linux devices: Web access for Amazon DCV is supported on Google Chrome, Microsoft Edge, Apple Safari and Mozilla Firefox browsers when running on the latest three browser versions.
  + On Android tablets, Chromebooks, and iPads: Web access for Amazon DCV is supported on Google Chrome and Apple Safari browsers when running on the latest three browser versions.
+ Web access for PCoIP-based WorkSpaces has the following limitations:
  + Web access for PCoIP is not supported in the AWS GovCloud (US), Asia Pacific (Mumbai), Africa (Cape Town), Israel (Tel Aviv), or Europe (Paris) regions.
  + Web access for PCoIP is only supported for Windows-based WorkSpaces.
  + Web access for PCoIP is only supported on Google Chrome and Mozilla Firefox browsers on Windows, macOS and Linux devices when running on the latest three browser versions.
  + Web access for PCoIP does not support multiple monitors.
  + Web access for PCoIP does not support connecting to GPU-enabled WorkSpaces.

**Note**  
YUV444 encoding is not supported with WorkSpaces web access. If your administrator uses a Group Policy setting to enable YUV444 encoding, this may cause issues during login or rendering issues during your session.

**Topics**
+ [Display support](#web-access-views)
+ [Proxy servers](#web-access-proxy)
+ [Supported features for DCV-based WorkSpaces](#wsp-for-wsp-client)
+ [Supported features and gestures on Android tablets and iPads](#supported-features-tablets)
+ [Installing WorkSpaces Web Access as a Progressive Web Application](#web-access-pwa)
+ [Enabling diagnostic log uploads](#enable-diagnostic-logging)

## Display support
<a name="web-access-views"></a>

WorkSpaces Web Access supports up to two monitors when connecting to DCV-based WorkSpaces.

## Proxy servers
<a name="web-access-proxy"></a>

If you are required to use a proxy server to access the internet, you can configure your browser to use the proxy server.

**Requirements**
+ Proxy with authentication is not currently supported.
+ Proxy server support for Web Access may vary by browser. Refer to your browser’s proxy settings for more information.

## Supported features for DCV-based WorkSpaces
<a name="wsp-for-wsp-client"></a>

The following features are supported for DCV-based WorkSpaces.

### Copying and pasting
<a name="web-client-copy-paste"></a>

You can use the web client to copy and paste plain text and PNG images between your local device and the WorkSpaces session. On Google Chrome and Microsoft Edge, you can use keyboard shortcuts and context (right-click) menu to copy and paste text and images. On Mozilla Firefox and Apple Safari you can use the clipboard dialog to copy and paste plain text; images are not supported.

### Using a webcam
<a name="web-client-webcam"></a>

Webcam functionality is supported on Google Chrome and Microsoft Edge. On Mozilla Firefox, webcams are supported with Windows-based WorkSpaces only. Webcams are not supported on Apple Safari.

**Selecting the webcam you want to use**

1. Choose the drop-down with your **Workspaces Name** on the top right of your WorkSpaces session, and then choose **Preferences**.

1. Choose the **Audio and Video** tab, scroll down to **Camera**, and then select the camera to use.

1. Select **Save**.

**Note**  
Cameras will appear only if your administrator has enabled webcam support for your WorkSpace. You can't change the webcam selection while the webcam is in use.

**Using a webcam during your session**

Toggle the webcam button in the client toolbar as shown below to enable or disable your webcam during your session. The webcam button appears on the toolbar only if webcam support is enabled and at least one webcam is connected to your local device.

![The webcam button in the WorkSpaces Web Access client.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/webaccess-webcam-button.png)


The following table shows different webcam states:


| Icon | Description | 
| --- | --- | 
|  ![The webcam is disabled.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/webaccess-webcam-disabled.png)  | The webcam is disabled. Toggle the button to enable the webcam. If you didn't previously select the webcam to use, the default webcam is used. | 
|  ![The webcam is enabled.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/webaccess-webcam-enabled.png)  | The webcam is enabled, but it's not in use. Toggle the button to disable the webcam. | 
|  ![The webcam is in use.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/webaccess-webcam-inuse.png)  | The webcam is in use by a remote application in the WorkSpaces session. Toggle the button to disable the webcam. | 

### Using multiple screens
<a name="web-client-multiple-screens"></a>

To use multiple screens, choose the multiscreen button in the client as shown in the following example. Multiple screens are supported with up to two monitors.

![The multiscreen button in the WorkSpaces Web Access client.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/webaccess-multiscreen-button.png)


## Supported features and gestures on Android tablets and iPads
<a name="supported-features-tablets"></a>

Android tablets are supported on Google Chrome, and iPads are supported on Apple Safari. Touch input is supported for both device types.

**Gestures**
+ Use a two-finger single tap gesture or use the client toolbar button to toggle the on-screen keyboard.
+ Use a pinch gesture to zoom in our out on the screen. When zoomed in, use a two-finger slide gesture to pan the screen horizontally or vertically.
+ Use a three-finger single tap gesture to show the client toolbar when it has been hidden by auto-hide.

**Trackpad mode**
+ To enable track pad mode, choose the drop-down with your **WorkSpace Name** on the top right of your WorkSpaces session, and then choose **Enable trackpad mode**.
+ Once trackpad mode is enabled:
  + Use a short one-finger tap to trigger a mouse left click.
  + Use a longer one-finger tap to trigger a mouse right click.

**Screen resolution and other functionality**
+ Your screen resolution may be automatically adjusted to fit the tablet screen size.
+ If you rotate the tablet device, the screen will automatically resize itself.
+ Full screen is not supported on Apple Safari on iPads.

## Installing WorkSpaces Web Access as a Progressive Web Application
<a name="web-access-pwa"></a>

You can install WorkSpaces Web Access as a Progressive Web Application (PWA) on your device. A PWA lets you access your WorkSpace in a dedicated, full-screen window without browser UI elements such as the toolbar or address bar. After you install it, you can launch WorkSpaces Web Access directly from your device home screen or taskbar. The PWA uses the same connection and authentication method as WorkSpaces Web Access. The PWA automatically stays current without requiring updates. When a web client update is released, it is applied the next time you fully close and reopen the PWA.

**Requirements**
+ Your administrator must enable web access on your WorkSpace.
+ PWA is supported with Amazon DCV-based WorkSpaces on the following platforms and browsers:
  + Windows – Chrome and Edge
  + macOS – Chrome and Safari
  + Android and Chromebook – Chrome
  + iPad and iOS – Chrome and Safari

**To install on Windows, macOS, or Android/Chromebook devices using Chrome or Edge**

1. Navigate to your organization's WorkSpaces Web Access sign-in page URL in a supported browser.

1. In the browser address bar, choose the **Install** icon (usually a monitor with a down arrow) to the right of the URL. Alternatively, choose the browser menu (three vertical dots), choose **Cast, Save, and Share**, and then choose **Install page as app**.

1. In the dialog box, confirm or edit the website details, and then choose **Install**.

**To install on macOS devices using Safari**

1. Navigate to your organization's WorkSpaces Web Access sign-in page URL in a supported browser.

1. On the top toolbar, choose **File**, then **Add to dock**.

1. In the dialog box, confirm or edit the website details, and then choose **Add**.

**To install on iOS or iPadOS devices using Safari or Chrome**

1. Navigate to your organization's WorkSpaces Web Access sign-in page URL in a supported browser.

1. To the right of the address bar, choose **Share**, and then choose **Add to Home Screen**.

1. Confirm or edit the website details, and then choose **Add**.

**To uninstall on Windows, macOS, or Android/Chromebook devices using Chrome or Edge**

1. Open the app, and then choose the three-dot menu in the title bar.

1. Choose **Uninstall**.

**To uninstall on macOS devices using Safari**

1. Open the context (right-click) menu on the app icon in the Dock.

1. Choose **Options**, and then choose **Remove from Dock**.

**To uninstall on Android, iOS, or iPadOS devices using Safari or Chrome**

1. Press and hold the app icon on your home screen.

1. Choose **Remove** or **Uninstall**.

**Note**  
You must install the PWA from the same Regional endpoint as the WorkSpaces Region. You can't install the PWA from one Region (for example, `us-east-1`) and use it to access a WorkSpace in a different Region (for example, `us-west-2`). To make sure that you are on the correct Regional endpoint, enter the registration code on the WorkSpaces sign-in page in a regular browser tab and allow the browser to redirect you to the correct Regional endpoint. Then, install the PWA from that page.

**Note**  
On Android, iOS, and iPadOS devices, minimizing the PWA window might temporarily disconnect your session because mobile browsers restrict network connections for background applications. When you return to the PWA window, wait a few seconds for the connection to re-establish. If the disconnection exceeds the timeout period set by your administrator, you must sign in again.

## Enabling diagnostic log uploads
<a name="enable-diagnostic-logging"></a>

To troubleshoot issues with WorkSpaces web access, you can enable diagnostic logging. The log files that are sent to AWS include detailed information about your device and connection to the AWS network. You can enable automatic diagnostic log uploads before or during your WorkSpace streaming sessions.

**To send log files**

1. Open the Amazon WorkSpaces Web Access page. If you’re currently in your WorkSpaces session, disconnect from it so you return to the pre-session page.

1. At the top of the pre-session page, choose **Settings**, then **Diagnostic logging**.

1. Ensure **Diagnostic logging** is enabled.

1. (Optional) To generate debugging-level details and verbose performance data, choose **Advanced logging**.