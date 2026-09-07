

# WorkSpaces Windows client application
<a name="amazon-workspaces-windows-client"></a>

The following information will help you get started with the WorkSpaces Windows client application.

**Topics**
+ [Requirements](#windows-requirements)
+ [New client experience (Public Preview)](#windows-new-client-experience)
+ [Setup and installation](#windows_setup)
+ [Determining your client version](#determine-version-windows)
+ [Client updates](#windows_update_client)
+ [Client language](#windows_client_lang)
+ [Connecting to your WorkSpace](#windows_connecting)
+ [Managing your sign-in information](#manage-login-info-windows)
+ [Network connectivity and reconnecting to your WorkSpace](#windows-network-connectivity)
+ [Connection settings](#windows-connection-settings)
+ [Using external displays](#using-external-displays)
+ [Keyboard shortcuts](#keyboard-shortcuts)
+ [Disconnecting and exiting](#windows_disconnect)
+ [Clipboard support](#windows_clipboard_support)
+ [Diagnostic logging](#diagnostic-log-uploads-users)
+ [Release notes](#windows-release-notes)

## Requirements
<a name="windows-requirements"></a>
+ The Amazon WorkSpaces client for Windows requires a Microsoft supported version of Windows 11. For more details, see [Windows 11 release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information). For information about supported WorkSpaces client versions, see [End of life policy for WorkSpaces client applications](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-eol.html).

## New client experience (Public Preview)
<a name="windows-new-client-experience"></a>

Starting with version 5.34, the WorkSpaces client for Windows includes a new client experience alongside the current (classic) experience. The new client experience includes an updated interface and is designed to be easier to use, with a simplified connection flow, easier-to-find settings and session tools, more helpful error messaging, and a new Session Health feature.

**Note**  
The new client experience supports connecting to DCV-based WorkSpaces only.

### Switching between experiences
<a name="windows-switching-experiences"></a>

By default, the client opens in the classic experience. If your administrator has not disabled the new experience, after entering your registration code, you will see a link on the top right of the client application that lets you try the new experience. Choose **Try New WorkSpaces** to start.

**Note**  
Switching experiences may take a few moments.

![The WorkSpaces Windows client with the Try New WorkSpaces link in the upper-right corner.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-try-new.png)


If your administrator has set a policy that requires a specific experience (new or classic), the option to switch is hidden and the client uses the experience your administrator selected. For more information, contact your administrator.

### Returning to the classic experience
<a name="windows-returning-to-classic"></a>

If you switched to the new experience and want to return to classic, choose the **Return to classic** option on the top right of the new experience.

**Note**  
Switching back may take a few moments.

![The new client experience with the Return to classic option in the upper-right corner.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-return-to-classic.png)


### Preview badge
<a name="windows-preview-badge"></a>

While the new experience is in Public Preview, a **Preview** badge appears in the client. Choose the badge to see release notes, known limitations, and a link to send your feedback to AWS.

![The Preview badge in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-preview-badge.png)


### What's different in the new client experience?
<a name="windows-whats-different"></a>

The new experience includes the following changes and improvements:
+ **Updated interface** — a redesigned user interface with a cleaner layout, easier-to-find settings and tools, and a modern look-and-feel.
+ **Simplified connection and sign-in flow** — a revised flow for registering and connecting to a WorkSpace, and additional customization options for managing WorkSpaces you frequently access. For more details, see [Connecting to your WorkSpace](#windows_connecting) and [Managing your sign-in information](#manage-login-info-windows).
+ **Support for color themes** — choose between light, dark, or follow your system's theme settings. Change this from the **WorkSpaces** menu > **Settings** > **Appearance**.  
![The Appearance settings showing light, dark, and system theme options in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-appearance-themes.png)
+ **New toolbar** — a consolidated toolbar available during your WorkSpace session, providing access to keyboard shortcuts, device controls you can use for your session (camera, microphone, audio, USB devices), file transfer options, and a new Session Health feature. In addition, the new toolbar includes a set of window actions you can take – minimize, maximize / full screen, and disconnect / close.
  + When your session is in **windowed mode**, the toolbar appears at the top of the session window, as part of the window title, so it does not block your session view.  
![The new client toolbar at the top of the session window in windowed mode.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-toolbar-windowed.png)
  + When your session is in **full screen mode**, the toolbar floats near the top of the screen for a few seconds, and then automatically hides away to help you focus.
    + If you need to move it out of the way, click-and-hold anywhere on it, drag it alongside the top edge of the screen, and drop it into any other horizontal position.
    + If you want the toolbar to reappear, move your mouse near the top edge of the screen near the minimized toolbar and it will reappear in full.
    + If you want to keep the toolbar always visible, choose **Pin the toolbar** (pin icon).  
![The floating in-session toolbar in full screen mode with the Pin the toolbar control.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-toolbar-pin.png)
+ **Session Health** — a new feature that monitors session quality conditions (including network status, service reachability, Wi-Fi signal strength, network latency, bandwidth, and local device metrics which may sometimes affect your session, such as local device CPU utilization and memory usage) and suggests actions you can take to resolve issues.
  + The **Session health** icon will change color if anything needs attention, and choosing the icon will open the panel on the right side where details will be provided. Choose the relevant questions at the bottom of the panel to learn more.
  + If you need to move the panel out of the way, choose **Undock** (undock icon) on the top right of the panel, and you can move it freely around the session. Choose **Dock** (dock icon) to move it back to the right side.  
![The Session Health panel open on the right side of the session.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-session-health.png)  
![The Session Health panel showing network status, service reachability, and latency.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-session-health-panel1.png)  
![The Session Health panel showing local device metrics and recommended actions.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-session-health-panel2.png)
+ **Simplified full screen mode and usage of multiple external displays** — For more details, see [Full screen mode and using multiple displays](#full-screen-mode).
+ **New Devices panel to manage local devices you can use in your WorkSpace session** — including your local speakers, microphone, and camera, in addition to other USB devices that have been enabled by your administrator.  
![The Devices panel for managing local speakers, microphone, camera, and USB devices.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-devices-panel.png)
+ **New File transfer experience to move files to and from your WorkSpace** — when this feature is enabled by your administrator.
  + Choose the **File transfer** (folder icon) in the toolbar to get started.
  + Choose the **Back**, **Forward**, **Up**, and **Refresh** icons to navigate your WorkSpace storage folders.
  + Choose **Upload here** to select a file from your local device to transfer to your WorkSpace.
  + Select a file on your WorkSpace and choose **Download** to transfer it to your local device.
  + Navigate to your desired location on your WorkSpace storage hierarchy and choose **New folder** to create a new folder in that location.  
![The File transfer window with upload, download, and folder navigation controls.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-file-transfer.png)
+ **New My WorkSpace Details panel** — providing key information about your WorkSpace at a glance, with the ability to copy and paste it.  
![The My WorkSpace Details panel showing key information about the WorkSpace.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-workspace-details.png)
+ **Improved error messaging** — connection errors and disconnection events now include descriptions of what happened and, where applicable, steps you can take to resolve the issue.
+ **Updated diagnostic logging support** — a new option to send logs on demand, with a reference code for AWS Support, in addition to the existing automatic diagnostic logging option. For more details, see [Diagnostic logging](#diagnostic-log-uploads-users).
+ **A way for you to send feedback to AWS** — available anytime by choosing **Amazon WorkSpaces** > **Help** > **Send feedback to AWS**. Your feedback submission is governed by the [AWS Privacy Notice](https://aws.amazon.com/privacy/).  
![The Help menu with the Send feedback to AWS option in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-send-feedback.png)  
![The feedback form for sending feedback to AWS in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-feedback-form.png)

### Known limitations
<a name="windows-known-issues"></a>
+ At launch, the new client experience is supported in English only. Additional supported languages will be added shortly after launch.
+ The USB redirection driver is currently not available to download from the client settings menu; it's available during the installation process when you install the client for all users on the Windows device.

## Setup and installation
<a name="windows_setup"></a>

You can download the latest version of the WorkSpaces client for Windows from the [Amazon WorkSpaces Client Download page](https://clients.amazonworkspaces.com/).

You have two options for how to install the Amazon WorkSpaces client application:
+ **Install just for you.** If you choose this option and you share your local device with other users, the WorkSpaces client application is available only to you. If other users on the machine also want to use the WorkSpaces client application, they must install the application for their own use.
+ **Install for all users of your device.** If you choose this option, the WorkSpaces client application is available to anyone who logs on to your local device. Installing the WorkSpaces client application for all users requires you to have administrator credentials on your local device.

If you have questions about which option to choose, ask your administrator for guidance.

### Installing the USB redirection driver
<a name="install-usb-redirection"></a>

To use your local USB devices on your WorkSpace, you will need to install the USB redirection driver. To install this driver, install the WorkSpaces application for all users, and then check the box to **Install driver for USB redirection**. This requires you to have administrator credentials on your local device.

## Determining your client version
<a name="determine-version-windows"></a>

**Classic client experience**

Choose **Amazon WorkSpaces** > **About Amazon WorkSpaces**.

**New client experience**

Choose **Amazon WorkSpaces** > **About**.

![The About dialog showing the client version in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-about.png)


## Client updates
<a name="windows_update_client"></a>

The WorkSpaces client for Windows automatically checks for available updates, and when new versions become available, installs them in the background when you are not using it. Once the installation is complete, open the client to begin using the latest version.

**Note**  
Automatic client updates are supported in most AWS Regions. In Regions where automatic client updates are not supported, or if your administrator has disabled automatic client updates, a message appears in the client when a new version is available and you have the option to install it.

Client updates maintain the same installation context as the original installation. This means if the WorkSpaces client was originally installed for all users on the local device, future automatic updates will apply to all users. Similarly, if the client was installed for a single user, future updates will only apply to that specific user.

## Client language
<a name="windows_client_lang"></a>

You can choose the language displayed by the WorkSpaces client for Windows.

**To choose the client language**

1. Choose **Settings** > **Change Language**.

1. Choose your desired language from the dropdown and choose **Save**.

**Note**  
The new client experience is currently supported in English only. Support for additional languages will be added in a future update.

## Connecting to your WorkSpace
<a name="windows_connecting"></a>

**Classic client experience**

1. Open the WorkSpaces client. If this is your first time, the client prompts you to enter a registration code, which should be included in your welcome email or provided by your administrator. Enter the registration code and choose **Register**.

1. On the sign-in screen, enter your credentials and choose **Sign in**. If multi-factor authentication is enabled, enter the verification code you received when prompted. If your administrator has not disabled it, you can select the **Keep me logged in** checkbox at the bottom of the sign-in screen to securely save your credentials. This enables you to reconnect to your WorkSpace without re-entering your credentials while the client remains open.

1. After your session connection is established, your WorkSpace will be displayed.

1. The next time you open the WorkSpaces client, the last used registration code is pre-populated. Choose **Continue** or **Register** to continue to the sign-in step.

1. To enter a different registration code, choose **Change Registration Code** at the bottom of the sign-in page, choose from other saved registration codes in the dropdown, or type in your new registration code.

**New client experience**

1. Open the WorkSpaces client. If this is your first time, the client prompts you to enter a registration code, which should be included in your welcome email or provided by your administrator. Enter the registration code, optionally give your WorkSpace a friendly name, and choose **Add**.

1. On the sign-in screen, enter your credentials and choose **Sign in**. If multi-factor authentication is enabled, enter the verification code you received when prompted.

1. After your session connection is established, your WorkSpace will be displayed.

1. The next time you open the WorkSpaces client, your WorkSpace will appear on the home screen and you can proceed with the sign-in step directly.

1. To enter a different registration code, choose **Change** next to the currently selected WorkSpace, choose from other saved WorkSpaces in the list, or choose **Add a new WorkSpace** to enter your new registration code.

![The registration screen for adding a WorkSpace with a registration code and friendly name.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-add-workspace.png)


![The WorkSpace list with options to set default, rename, change color, and remove a WorkSpace.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-workspace-list.png)


## Managing your sign-in information
<a name="manage-login-info-windows"></a>

**Classic client experience**

To view and manage your saved registration codes, choose **Settings** > **Manage Login Information**. From here, you can view the Region your WorkSpaces are in, add or edit a friendly name for your WorkSpaces, manage the **Keep me logged in** option for your WorkSpaces, and **Remove** any registration codes you no longer need.

**New client experience**

To view and manage your saved WorkSpaces, choose **Change** next to the currently selected WorkSpace. In the WorkSpace list, you can:
+ Choose **Set as default** (star icon) on a saved WorkSpace to set it as default – this will pre-select this WorkSpace when you start the application, and also sorts it at the top of the list.
+ Choose **Rename** (pencil icon) on a saved WorkSpace to rename it.
+ Choose **Change color** (color icon) on a saved WorkSpace to change its color (useful for easy recognition in the list).
+ Choose **Remove** (trash icon) to remove a WorkSpace you no longer need.
+ Choose **Add a new WorkSpace** at the bottom of the list to add a new WorkSpace.

![The WorkSpace list with options to set default, rename, change color, and remove a WorkSpace.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-workspace-list.png)


## Network connectivity and reconnecting to your WorkSpace
<a name="windows-network-connectivity"></a>

An interruption of network connectivity may result in your active session being disconnected. This can be caused by events such as closing the laptop lid or the loss of your wireless network connection. The WorkSpaces client for Windows attempts to reconnect the session automatically if network connectivity is recovered within a certain amount of time. The default session resumption timeout is 20 minutes, but this timeout can be modified by your administrator.

## Connection settings
<a name="windows-connection-settings"></a>

### IPv6 settings
<a name="ipv6-network-settings"></a>

The WorkSpaces client for Windows supports connecting to your WorkSpace using IPv4 and IPv6 connections.

**Classic client experience**

By default, the classic client experience uses an IPv4 connection for streaming. To enable streaming over an IPv6 connection:

1. Choose **Settings** > **Manage Connection Settings**.

1. Under **General Connection Settings**, choose **Prefer IPv6-enabled communications**. This will prefer an IPv6 connection when your network supports it, and fall back to using IPv4 if not.

**Note**  
IPv6 connections are supported on the WorkSpaces client application version 5.30.1 or later. You cannot change IPv6 settings if you are in an active WorkSpace session. Change the setting before connecting to your WorkSpace.

**New client experience**

By default, the new client experience prefers an IPv6 connection for streaming when your network supports it, and falls back to using IPv4 if not. If you want to change this to use IPv4 only:

1. Choose **Amazon WorkSpaces** > **Settings** > **Connections**.

1. Disable the **Use IPv6 when available** toggle.

![The Connections settings with the Use IPv6 when available toggle.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-connections-ipv6.png)


**Note**  
If you are in an active WorkSpace session, changes to IPv6 connection settings will take effect on the next session.

### Proxy servers
<a name="windows_proxy_server"></a>

If your administrator requires you to use a proxy server, configure the proxy in the client settings before connecting to your WorkSpace.

**Classic client experience**

By default, the classic client experience uses the proxy server settings specified in your local device operating system. To view or make changes to these settings:

1. Choose **Settings** > **Manage Connection Settings**.

1. Under **Proxy Settings**, choose:
   + **Don't use proxy server** to disable the usage of a proxy server.
   + **Use your device operating system settings** to use the proxy server settings from your local device operating system.
   + **Customize proxy server** to use a custom proxy server. Enter the IP address or URL and port number for your custom proxy server.

1. After making your changes, choose **Save**.

**New client experience**

1. Choose **Amazon WorkSpaces** > **Settings** > **Connections**.

1. Under **Use a proxy server**, choose **Set up**. Choose:
   + **Don't use a proxy server** to disable the usage of a proxy server.
   + **Use your computer's proxy settings** to use the proxy server settings from your local computer. Choose **Open your computer's proxy settings** to view and change these settings locally.
   + **Use a custom HTTPS proxy server** to use a custom proxy server. Enter the IP address or URL and port number for your custom proxy server. Choose **Save**.

![The Connections settings showing proxy server options.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-connections-proxy.png)


**Note**  
If you are in an active WorkSpace session, changes to proxy server settings will take effect on the next session.

## Using external displays
<a name="using-external-displays"></a>

### Display support
<a name="windows-display-support"></a>

You can use locally connected external displays in your WorkSpaces session, enabling you to extend the WorkSpace to them. The maximum supported number of displays and maximum supported display resolution is shown in the following table.


| Number of displays | Maximum display resolution | 
| --- | --- | 
| 2 | 3840x2160 | 
| 4 | 1920x1200 | 

### Full screen mode and using multiple displays
<a name="full-screen-mode"></a>

**Classic client experience**

While in windowed mode, you can switch to full screen mode by choosing **View** > **Enter Full Screen**.

While in full screen mode, you can switch back to windowed mode by moving your mouse to the top of the screen, waiting a moment for the menu to reappear, and choosing **View** > **Leave Full Screen**.

**To use multiple displays**

1. Connect the displays to your local device and configure your local display settings as needed.

1. In the WorkSpaces client for Windows, log in to your WorkSpace.

1. To extend your WorkSpace session to all your connected displays, choose **View** > **Enter Full Screen On All Displays**.

1. To extend your WorkSpaces session to a subset of your connected displays, choose **View** > **Enter Full Screen On Selected Displays**. Your connected displays will appear; select the displays you want to extend your session to.

**Note**  
You'll need to select displays that are adjacent to each other.
To make changes to your connected displays, display layout, or other display settings, visit your local device display settings.

**New client experience**

To configure your default full screen mode:

1. Choose **Amazon WorkSpaces** > **Settings** > **Display**.

1. Under **Full screen mode**, choose:
   + **Maximize window** to maximize your WorkSpace session on your current display, while not going full screen – use this when you want to see your local device taskbar simultaneously with your WorkSpace.
   + **Full screen on current display** to go full screen on your current (single) display.
   + **Full screen on all displays** to go full screen on all your connected displays.
   + **Full screen on selected displays** to go full screen on a subset of your connected displays. When choosing this option, your connected displays will appear; select the displays you want to extend your session to.

1. After making changes, the default behavior of the **Maximize** / **Full screen** icon (on the top right of the client) will adjust accordingly. When in windowed mode, choose the **Maximize** / **Full screen** icon to go into your selected mode. When in maximized or full screen mode, choose the **Restore** / **Exit full screen** icon to go back to windowed mode.

**Note**  
You'll need to select displays that are adjacent to each other.
To make changes to your connected displays, display layout, or other display settings, visit your local device display settings.

![The Display settings showing full screen mode options in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-display-fullscreen.png)


![The Display settings with the full screen on selected displays option.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-display-selected.png)


![The monitor selection screen for choosing which connected displays to use.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-display-select-monitors.png)


![The Maximize and Full screen icon in the upper-right corner of the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-maximize-icon.png)


## Keyboard shortcuts
<a name="keyboard-shortcuts"></a>

The following keyboard shortcuts are supported in the WorkSpaces client:
+ **Ctrl \+ Alt \+ Enter** — Toggle full screen mode (that is, enter or exit full screen mode)
+ **Ctrl \+ Alt \+ Shift \+ ArrowDown** — Minimize the WorkSpaces client window
+ **Ctrl \+ Alt \+ Shift \+ F11** — Clear keyboard focus
+ **Ctrl \+ Alt \+ F12** — Disconnect from your WorkSpace session

**Classic client experience**

In the classic client experience, in addition to the supported keyboard shortcuts described above, you can send a Ctrl \+ Alt \+ Del command to your WorkSpace from the client. To do so, choose **View** > **Send Ctrl \+ Alt \+ Del**.

**New client experience**

In the new client experience, in addition to the supported keyboard shortcuts described above, you can send a Ctrl \+ Alt \+ Del command to your WorkSpace from the client. To do so, use one of the following options:
+ Choose **Keyboard shortcuts** (keyboard icon) > **Send Ctrl \+ Alt \+ Del**.
+ Press **Ctrl \+ Alt \+ End** on your local device keyboard.

![The Keyboard shortcuts menu with the Send Ctrl+Alt+Del option.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-keyboard-shortcuts.png)


## Disconnecting and exiting
<a name="windows_disconnect"></a>

**Classic client experience**

To disconnect from your WorkSpace session while leaving it active, use one of the following methods:
+ Choose **Amazon WorkSpaces** > **Disconnect WorkSpace**. Your WorkSpace session will be disconnected, but will remain active, and the client continues running in case you want to sign in again.
+ Close the WorkSpaces client window by choosing **Close** (X icon) in the upper right corner. Your WorkSpace session will be disconnected, but will remain active, and the client continues running in case you want to sign in again.

To disconnect from and end your WorkSpace session, use one of the following methods:
+ Choose **Amazon WorkSpaces** > **End Session**. Before ending the session, you'll be prompted to save open documents. Your session will end and you will be disconnected.
**Note**  
This option is only available for WorkSpaces Pools.
+ Choose **Amazon WorkSpaces** > **Quit Amazon WorkSpaces**. Your WorkSpace session will end, and the client will close.
+ You can also sign out from the WorkSpace itself. Your WorkSpace session will end, and the client continues running in case you want to sign in again.

**New client experience**

To disconnect from your WorkSpace session while leaving it active, use one of the following methods:
+ Choose **Amazon WorkSpaces** > **Disconnect**. Your WorkSpace session will be disconnected, but will remain active, and the client continues running in case you want to sign in again.
+ Close the WorkSpaces client window by choosing **Disconnect** (X icon) in the upper right corner. Your WorkSpace session will be disconnected, but will remain active, and the client continues running in case you want to sign in again.

To disconnect from and end your WorkSpace session, use one of the following methods:
+ Choose **Amazon WorkSpaces** > **Exit**. Your WorkSpace session will end, and the client application will close.
+ You can also sign out from the WorkSpace itself. Your WorkSpace session will end, and the client continues running in case you want to sign in again.

![The Amazon WorkSpaces menu showing the Disconnect option in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-disconnect.png)


![The Amazon WorkSpaces menu showing the Exit option in the new client experience.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-exit.png)


**Note**  
The new client experience will prompt you to confirm before disconnecting or exiting. You can disable this prompt by choosing **Don't ask me again**. If you want to change this later, choose **Amazon WorkSpaces** > **Settings** > **Appearance** and manage the settings under **Confirmation dialogs**.

![The Appearance settings with the Confirmation dialogs options.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-confirmation-dialogs.png)


## Clipboard support
<a name="windows_clipboard_support"></a>

The clipboard supports copying and pasting of text and images between your local computer and your WorkSpace. Copy and paste supports a maximum uncompressed object size of 20 MB.

## Diagnostic logging
<a name="diagnostic-log-uploads-users"></a>

**Classic client experience**

To troubleshoot issues with your WorkSpaces client for Windows, you can enable diagnostic logging. The log files are sent automatically to AWS and include information about your device and connection to the AWS network.

To enable diagnostic logging:

1. Choose **Settings** > **Manage Diagnostic Logging Settings**.

1. Check the box to enable Diagnostic Logging.

**New client experience**

The new client experience provides enhanced diagnostic capabilities:
+ **Automatic diagnostic logging:** The new client sends diagnostic logs automatically. You can enable or disable this by choosing **Amazon WorkSpaces** > **Settings** > **Logging** > **Automatically upload your logs**.
+ **Send logs on demand:** You can send diagnostic logs to AWS when you want, such as when you're troubleshooting an issue. When you send your current logs, you will receive a reference code that you can share with AWS Support to help troubleshoot your issue.

To send your current logs:

1. Choose **Amazon WorkSpaces** > **Settings** > **Logging**.

1. Under **Send current logs**, choose **Send logs to AWS**.

1. Copy the reference code displayed and provide it to AWS Support.

Your client device ID is also displayed on this screen and can be copied for reference.

![The Logging settings with automatic upload and Send logs to AWS options.](http://docs.aws.amazon.com/workspaces/latest/userguide/images/wsp-windows-newclient-logging.png)


## Release notes
<a name="windows-release-notes"></a>

The following table describes the changes to each release of the Windows client application. As a general security best practice, we recommend that WorkSpaces customers update client software as relevant patches become available to obtain the latest updates. For additional information on all the supported WorkSpaces client versions, see [WorkSpaces client application end of life policy](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-eol.html).


| Release | Date | Changes | 
| --- | --- | --- | 
| 5.34.1 | September 4, 2026 |  +  [Windows] Temporarily disabled support for honoring printer preferences, an enhancement introduced in client version 5.34.0, due to an issue causing delays with printer detection.   | 
| 5.34.0 | August 25, 2026 |  +  Added a preview of the new, modernized Amazon WorkSpaces client experience. Administrators can use the [Client Experience Policy](https://docs.aws.amazon.com/workspaces/latest/adminguide/control-client-experience.html) to control which experience their users receive. If enabled, users will see the option to try the new experience in the top right of the classic client, and can switch back. <br />+  Added support for honoring printer preferences when printing from a DCV-based WorkSpaces session. <br />+  Fixed an issue that prevented the session from automatically reconnecting when the WorkSpace was temporarily unreachable. <br />+  Fixed an issue that prevented signing in when a saved username included a domain prefix. <br />+  Fixed an issue that prevented connecting to WorkSpaces Pools in certain scenarios. <br />+  Improved the stability of the client application when connected displays change rapidly, such as with docking and undocking. <br />+  Fixed an issue that caused a black border to appear on certain dialog panels. <br />+  Updated the Microsoft Teams client plugin used for Microsoft Teams optimization. <br />+  Updated the DCV SDK. <br />+  Additional bug fixes and enhancements.   | 
| 5.33.0 | June 8, 2026 |  +  Fixed an issue that prevented logging in via SAML 2.0 when the client was launched with Administrator privileges. <br />+  Fixed an issue that prevented transferring files with multibyte file names (common for some non-English languages). <br />+  Added support for URL redirection, enabling administrators to configure certain websites to be redirected from the streaming session to the local device's web browser. <br />+  Added the display of battery level from the local device inside the streaming session, helping you know when your battery is running low when on-the-go. <br />+  Fixed an issue with the username not being pre-populated in the new user login flow when "Remember me" is selected. <br />+  Fixed an issue that prevented changing the registration code when there is no network connectivity. <br />+  Updated the DCV SDK. <br />+  Additional bug fixes and enhancements.   | 
| 5.32.2 | May 21, 2026 |  +  Fixed an issue with Microsoft Teams optimization not working as expected.   | 
| 5.32.1 | May 14, 2026 |  +  Fixed an issue where, under certain conditions, the client may not launch correctly on Windows 11 devices with the April 2026 cumulative update (KB5083769) installed.   | 
| 5.32.0 | April 20, 2026 |  +  Updated the keyboard shortcut to help users navigate from the client application to their local operating system, from Ctrl\+Alt\+DownArrow to Ctrl\+Alt\+Shift\+DownArrow. <br />+  Added support for connecting to WorkSpaces in the US East (Ohio) and Asia Pacific (Malaysia) regions. <br />+  Fixed an issue where, in certain display configurations, not all valid displays were able to be selected. <br />+  Fixed an issue where the new client update banner was persisting after a client update in certain configurations. <br />+  Updated the PCoIP SDK. <br />+  Updated the DCV SDK. <br />+  Bug fixes and enhancements.   | 
| 5.31.0 | January 21, 2026 |  +  Added advanced printing support for DCV-based WorkSpaces using native local printer drivers, enabling features such as two-sided printing, page selection, and layout options. <br />+  Fixed an issue with the automatic client update functionality that was preventing automatic updates in certain scenarios when VBScript is not present. <br />+  Added improved error messaging in the case of a SAML session timeout. <br />+  Other bug fixes and enhancements.   | 
| 5.30.0 | October 21, 2025 |  +  Improved international keyboard experience with new keyboard layout options (server or client) with DCV-based WorkSpaces. <br />+  Added support for generic USB redirection, enabling local USB devices to work with Windows-based Personal WorkSpaces using the DCV protocol. <br />+  Made an improvement that enables microphone audio streaming only when a remote application is using it, helping to optimize performance. <br />+  Fixed an issue with the automatic update function which was preventing automatic updates if the client is installed in a custom folder. <br />+  Fixed an issue that caused the application to crash under certain conditions when streaming with DCV. <br />+ Updated the DCV SDK.<br />+ Updated the PCoIP SDK.<br />+ Updated the .NET Framework.  | 
| 5.29.2 | August 26, 2025 |  +  Bug fixes and enhancements.   | 
| 5.29.1 | August 5, 2025 |  +  Bug fixes and enhancements.   | 
| 5.29.0 | July 31, 2025 |  +  Added a new automatic client update feature that will automatically check for available updates and install them when you're not using the client, helping you to get the latest features and bug fixes. <br />+  Bug fixes and enhancements.   | 
| 5.28.0 | July 1, 2025 |  +  Updated the DCV SDK. <br />+  Bug fixes and enhancements.   | 
| 5.27.1 | May 5, 2025 |  +  Bug fixes and enhancements.   | 
| 5.27.0 | April 30, 2025 |  +  Added support for extending full-screen across a selection of available connected monitors for Amazon DCV WorkSpaces. <br />+  Updated the DCV SDK. <br />+  Updated the PCoIP SDK. <br />+  Bug fixes and enhancements.   | 
| 5.26.2 | April 1, 2025 | Bug fixes and enhancements. | 
| 5.26.1  | March 11, 2025 | Bug fixes and enhancements. | 
| 5.26.0 | March 4, 2025 |  +  Added a `Ctrl+Alt+DownArrow` keyboard shortcut to help users navigate from the client application to their local operating system. <br />+  Updated the DCV SDK. <br />+  Updated the WebView2 SDK. <br />+  Updated the .NET SDK. <br />+  Bug fixes and enhancements.   | 
| 5.25.0 | December 19, 2024 |  +  Added a progress bar to help users better understand the expected time during the loading of their WorkSpace. <br />+  Updated the DCV SDK. <br />+  Bug fixes and enhancements.   | 
| 5.24.1 | November 22, 2024 |  +  Added a notification to warn idle users they will be disconnected from their DCV WorkSpaces due to inactivity. <br />+  Improved WorkSpaces client installation process. <br />+  Updated the DCV SDK. <br />+  Updated WolfSSL for PCoIP SDK. <br />+  Updated the RestSharp library. <br />+  Bug fixes and enhancements.   | 
| 5.23.0 | September 30, 2024 |  +  Renamed WSP protocol to Amazon DCV protocol. <br />+  Added support for file upload and download on DCV WorkSpaces. <br />+  Added support for streaming over port 443 for TCP and UDP protocols on DCV WorkSpaces. <br />+  Updated the .NET SDK. <br />+  Bug fixes and enhancements.   | 
| 5.22.1 | September 3, 2024 | Bug fixes and enhancements. | 
| 5.22.0 | August 16, 2024 |  +  Added support to persist webcam and microphone settings for future sessions on DCV WorkSpaces. <br />+  Updated the DCV SDK.   | 
| 5.21.0 | July 3, 2024 | Bug fixes and enhancements. | 
| 5.20.0 | June 13, 2024 |  +  Updated PCoIP SDK. <br />+  Updated DCV SDK. <br />+  Migrated the software framework to .NET 8 LTS. <br />+  Updated system to require Windows 11 - Version 22000 or later and Windows 10 - Version 1607 or later.   | 
| 5.19.3 | April 30, 2024 |  +  Updated DCV SDK. <br />+  Fixed issue where white screens appear in all displays when using multiple monitors with WorkSpaces and clicking full screen. <br />+  Fixed issue where users get immediately disconnected from their DCV WorkSpaces when connecting to it. <br />+  Fixed issue where the device dialog box isn't showing correct localized language when switching languages.   | 
| 5.19.0 | February 28, 2024 |  +  Updated DCV SDK. <br />+  Added WebAuthn support for in-session authentication.   | 
| 5.18.0 | January 22, 2024 | Updated DCV SDK. | 
| 5.17.0 | November 16, 2023 |  +  Fixed USB redirection issue for PCoIP WorkSpaces. <br />+  Fixed a client crash when users change running mode. <br />+  Fixed a client crash related to printer redirection on DCV client. <br />+  Bug fixes and enhancements.   | 
| 5.16.0 | October 26, 2023 |  +  Added installation guidance. Users on 4.0.6\+ version clients with USB redirection enabled need to uninstall old client before upgrading <br />+  Added restrictions that only admins have permission to modify custom installation folder <br />+  Updated DCV SDK   | 
| 5.15.1 | September 20, 2023 |  +  Added resiliency for network issues for DCV WorkSpaces <br />+  Updated DCV SDK <br />+  Bug fixes and enhancements   | 
| 5.13.0 | August 29, 2023 |  +  Updated PCoIP SDK and DCV SDK <br />+  Resolved an login page special character processing issue <br />+  Resolved a crashing issue when closing the Network dialog on the upper right of the client application <br />+  Added a link to Amazon WorkSpaces user guide under the Support menu   | 
| 5.12.1 | August 16, 2023 | Bug fixes and enhancements | 
| 5.12.0 | July 11, 2023 | Bug fixes and enhancements | 
| 5.11.0 | July 3, 2023 |  +  Bug fixes and enhancements <br />+  Added **Ctrl**\+**Alt**\+**Shift**\+**F11** as a keyboard shortcut to access the client menu during a streaming session <br />+  Fixed the issue where the text was getting cut off on the client login page when the operating system text size was set to 200% <br />+  Fixed a bug where the keyboard focus in the dialog box did not cycle through all the device selections when multiple devices were available for redirection. <br />+  Incrementally enhanced accessibility to color contrast and names for elements.   | 
| 5.10.0 | June 19, 2023 |  +  Improved client custom branding by storing assets in the same AWS Regions as provisioned WorkSpaces <br />+  Resolved black screen issue when using multiple monitors with Ubuntu WorkSpaces <br />+  Fixed client diagnostic log uploading issues, where proxy settings were not being persisted when connecting to WorkSpaces through a proxy server <br />+  Added support for DCV extension SDK, which allows end users to customize their DCV WorkSpaces experience   | 
| 5.9.0 | May 9, 2023 |  +  Resolved the issue of displaying the **Keep me logged in** option in the **Manage Login Information** dialog when logging into WorkSpaces with SAML credentials  <br />+  Resolved the issue of users not being able to log into WorkSpaces when proxy server is enabled <br />+  Resolved a keyboard focusing issue when navigating menu items using the `Tab` key <br />+  Updated DCV SDK to fix connectivity issues when using QUIC on DCV WorkSpaces   | 
| 5.8.0 | April 6, 2023 |  +  Fixed a bug that prevented users from logging in under certain scenarios <br />+  Fixed a bug to bring certificate selection dialog to the front during smart card logon <br />+  Updated DCV v2 SDK to fix minor bugs   | 
| 5.7.0 | February 23, 2023 |  +  Enabled trimming leading or trailing allow list in sign-in credentials <br />+  Resolved a crashing issue due to empty registration code <br />+  Provided sufficient color contrast, text labels, and instructions in user interface components, such as a login page and a menu bar.   | 
| 5.6.4 | February 1, 2023 |  +  Fixed sign-in credential validation issue <br />+  Fixed caps lock flicker issue   | 
| 5.6.2 | January 18, 2023 | Bug fixes and enhancements | 
| 5.6.0 | December 27, 2022 |  +  Added support for certificate-based authentication via SAML 2.0 integration, which removes the logon prompt for the Active Directory domain password <br />+  Resolved an issue of the **Alt** key getting continuously pressed in WorkSpaces <br />+  Resolved an issue of the **Num Lock** state that was inverted between WorkSpaces and local machine <br />+  Updated PCoIP SDK for the WorkSpaces Windows client <br />+  Bug fixes and enhancements   | 
| 5.5.0 | November 14, 2022 |  +  Added a shortcut **Ctrl**\+**Alt**\+**F12** to disconnect your WorkSpace <br />+  Resolved a keystroke-invoking issue when using **Alt** key with mouse clicks   | 
| 5.4.0 | October 5, 2022 |  Added support for automatic diagnostic log uploads feature that allows you to upload WorkSpaces client log files directly to WorkSpaces to troubleshoot issues without interrupting use of the WorkSpaces client.  | 
| 5.3.0 | September 15, 2022 |  +  Updated DCV SDK for Windows <br />+  Resolved an issue of the WorkSpaces clients not being able to save their user names after closing their WorkSpace   | 
| 5.2.1 | August 24, 2022 | Fixed the WorkSpaces login page rendering issues on Windows 8.1 | 
| 5.2.0 | August 2, 2022 | Updated PCoIP SDK for the WorkSpaces Windows client | 
| 5.1.0 | June 30, 2022 | Updated DCV SDK for Windows | 
| 5.0.0 | June 2, 2022 |  +  Updated PCoIP SDK for the WorkSpaces Windows client <br />+  Resolved issues when screen sharing WorkSpaces in Microsoft Teams <br />+  Bug fixes and enhancements   | 
| 4.0.6 | December 21, 2021 |  +  Enhances PCoIP USB redirection driver. The driver includes important updates and we recommend that all users install it <br />+  Resolves failures when using smart cards for authentication for DCV <br />+  Resolves crashes and black screen issues related to video streaming for DCV <br />+  Updates to DCV version 1.9.8.18175   | 
| 4.0.5 | November 23, 2021 |  +  Optimizes the bandwidth and frame rates for DCV WorkSpaces <br />+  Resolves the shortcut mapping issue related to full screen mode <br />+  Resolves the issue of the Alt key being pressed automatically   | 
| 4.0.4 | November 3, 2021 |  +  Resolves the issue of users not being able to switch between Korean and English languages using the Alt key on a physical keyboard <br />+  Resolves the mouse scrolling issue that is related to the mouse settings in Windows 10 <br />+  Video streaming improvements for WorkSpaces that support DCV <br />+  Bug fixes   | 
| 4.0.3 | October 4, 2021 |  +  Resolves crashes due to double-byte user names (for example, Japanese characters) on local machines <br />+  Resolves mouse-scrolling issues on 64-bit Windows 8.1 <br />+  Bug fixes and enhancements   | 
| 4.0.2 | September 1, 2021 |  +  Minor bug fixes and enhancements   Client version 4.0 supports Windows 8.1 and Windows 10. Attempting to install version 4.0 on Windows 7 or 8 will result in errors. If you are on Windows 7 or Windows 8, update your OS or download the latest 32 bit client (v3.x) from the [Amazon WorkSpaces Client Download](https://clients.amazonworkspaces.com/) page.     | 
| 4.0.1 | July 30, 2021 |  +  Adds USB redirection support for YubiKey U2F authentication on PCoIP Windows WorkSpaces <br />+  Minor bug fixes and enhancements   | 
| 4.0.0 | June 30, 2021 | The first 64-bit release of the Windows client application | 
| 3.1.10 | August 5, 2021 | Minor bug fixes and enhancements | 
| 3.1.9 | June 29, 2021 |  +  This release includes fixes to custom login workflows with a URI and is recommended for all users <br />+  Bug fixes and enhancements   | 
| 3.1.8 | May 28, 2021 |  +  Fixes the reconnect page redirection after disconnection when **Keep me logged in** is selected <br />+  Minor bug fixes and enhancements   | 
| 3.1.7 | April 29, 2021 |  +  Improves connectivity with WorkSpaces using the DCV <br />+  Resolves a crash issue related to proxy servers <br />+  Minor bug fixes and enhancements   | 
| 3.1.6 | April 8, 2021 | Fixes for disconnects and crashes resulting from DCV audio traffic optimization | 
| 3.1.5 | April 2, 2021 |  +  Adds Settings UI to enable/disable hardware acceleration <br />+  Bidirectional video web cam support is now generally available for Windows WorkSpaces using the DCV <br />+  Minor bug fixes and enhancements   | 
| 3.1.4 | March 16, 2021 |  +  Disables hardware acceleration by default to address screen flickering and mouse mispositioning issues observed with certain display driver versions. To manually turn on hardware acceleration, users can restart the WorkSpaces app after creating a registry string value of **EnableHwAcc** under **HKEY\_CURRENT\_USER\\SOFTWARE\\Amazon Web Services. LLC\\Amazon WorkSpaces**.  <br />+  Addresses a few crash scenarios when users register, log in, and rebuild <br />+  Adds localization support for more UI elements <br />+  Minor bug fixes and enhancements   | 
| 3.1.3 | February 15, 2021 |  +  Fixes issue with double Shift key presses not working in some apps <br />+  Improves settings UI for proxy configurations <br />+  Minor bug fixes and enhancements   | 
| 3.1.2 | January 8, 2021 |  +  The DCV is now generally available. Video-in functionality continues to be available as a beta feature on DCV WorkSpaces only <br />+  Fixes an intermittent issue that impacts client application upgrades <br />+  Fixes an issue with the login screen being magnified <br />+  Minor bug fixes and enhancements   | 
| 3.1.1 | December 1, 2020 |  +  Adds support for smart card authentication in the AWS GovCloud (US-West) Region <br />+  Minor bug fixes and enhancements   Version 3.1.1 is available only in the AWS GovCloud (US-West) Region   | 
| 3.1.0 | December 1, 2020 |  +  Resolves intermittent flickering issue inside of an active WorkSpaces session <br />+  Minor bug fixes and enhancements   | 
| 3.0.12 | November 10, 2020 |  +  Adds support for optionally disabling the use of the default proxy server <br />+  Adds enhancements to the session reconnect experience <br />+  Improves error messaging during session disconnects for DCV WorkSpaces <br />+  Fixes keyboard mapping issue with the **Shift** key for DCV WorkSpaces   | 
| 3.0.11 | October 02, 2020 |  +  Resolves an issue with enumeration of video-in devices on DCV WorkSpaces <br />+  Resolves an intermittent crash issue when disconnecting from a DCV WorkSpace <br />+  Minor bug fixes and enhancements   | 
| 3.0.10 | September 16, 2020 |  +  Resolves an issue with loading the login screen <br />+  Resolves an issue with persisting a user's screen size preference when the user chooses full screen mode and then exits this mode <br />+  Resolves an issue that causes the menu bar to be hidden after a user exits full screen mode <br />+  Resolves an input method editor (IME) issue <br />+  Adds support for health checks over port 4195 (UDP and TCP)   | 
| 3.0.9 | August 14, 2020 | Minor bug fixes and enhancements | 
| 3.0.8 | July 30, 2020 |  +  Adds monochrome cursor support on DCV WorkSpaces <br />+  For improved diagnostics, displays round trip time (RTT) as part of the network health check information <br />+  Minor bug fixes and enhancements   | 
| 3.0.7 | June 3, 2020 |  +  Adds support for multiple monitors on DCV WorkSpaces <br />+  Minor bug fixes and enhancements   | 
| 3.0.6 | April 28, 2020 |  +  Adds support for toggling between high DPI and standard DPI displays <br />+  Minor bug fixes and enhancements   | 
| 3.0.5 | March 30, 2020 | Resolves an issue with the user interface displaying a login prompt if single sign-on (SSO) is enabled for Amazon WorkDocs | 
| 3.0.4 | March 3, 2020 | Minor bug fixes and enhancements | 
| 3.0.2 | February 14, 2020 |  +  Adds keyboard shortcut to toggle full screen display <br />+  Adds support for connecting to DCV WorkSpaces <br />+  Minor bug fixes and enhancements   | 
| 3.0.0 | November 25, 2019 |  +  Improved user interface <br />+  Friendly registration code labels <br />+  Minor bug fixes and enhancements   | 
| 2.5.11 | November 4, 2019 | Minor bug fixes | 
| 2.5.10 |  |  +  Resolves an intermittent issue related to invalid keystrokes sent when closing a laptop lid <br />+  Minor fixes   | 
| 2.5.9 |  |  +  Resolves the issue of displaying a blank app icon image on the Windows 10 task bar after WorkSpace client upgrades <br />+  Minor bug fixes   | 
| 2.5.8 |  | Resolves an intermittent crashing issue related to computer waking up when opening a laptop lid | 
| 2.5.7 |  |  +  Adds support for German keyboard layouts with Linux WorkSpaces <br />+  Resolves an issue that results in a crash of Excel with clipboard direction   | 
| 2.5.6 |  | Minor fixes | 
| 2.5.5 |  | Minor fixes | 
| 2.5.2 |  |  +  Resolves an intermittent issue with the Caps Lock key becoming stuck <br />+  Minor bug fixes    | 
| 2.5.1 |  |  +  Resolves an issue that periodically results in repeated key presses with WorkSpaces running Amazon Linux 2 <br />+  Adds support for localized date and time formats in the user interface <br />+  Minor user interface improvements    | 
| 2.5.0 |  | Adds support for user self-service WorkSpace management capabilities | 
| 2.4.10 |  | Minor fixes | 
| 2.4.9 |  | Minor fixes | 
| 2.4.8 |  |  +  Adds support for uniform resource identifiers (URIs), which enable login orchestration <br />+  Minor fixes   | 
| 2.4.7 |  |  +  Resolves an issue with the user interface text not displaying correctly on Microsoft Surface Pro 4 models (Windows only) <br />+  Adds support for time zone redirection for more Regions: America/Indianapolis America/Indiana/Marengo America/Indiana/Vevay America/Indiana/Indianapolis <br />+  Includes user interface text changes for the Login page    | 
| 2.4.6 |  |  +  Adds support for configuring the logging level to include advanced logging for debug scenarios  <br />+  Minor improvements to session provision handling   | 
| 2.4.5 |  | Adds a check to ensure that certificates issued by Amazon Trust Services are trusted by Windows during installation. By default, an up-to-date Windows local Root CA list includes Starfield Service Root Certificate Authority - G2, and therefore trusts Amazon Trust Services certificates. If the local Root CA list is outdated, the client installer installs the Starfield Service Root Certificate Authority - G2 certificate to the system. If you do not have administrator access to the client device, you'll be prompted to confirm the installation of the Root CA certificate. | 
| 2.4.4 |  |  +  Minor fixes <br />+  Improves copy and paste   | 
| 2.4.2 |  | Minor fixes | 
| 2.4.0 |  |  +  New logo <br />+  Improves the user interface and stability   | 
| 2.3.7 |  | Addresses a gray screen issue that occurs when displays are in different orientations | 
| 2.3.6 |  | Localization enhancements | 
| 2.3.5 |  | Minor improvements | 
| 2.3.3 |  |  +  Improves the support for multiple monitors <br />+  Localization enhancements <br />+  Improves security and performance   | 
| 2.3.2 |  | Installer fixes | 
| 2.3.1 |  | Minor fixes | 
| 2.3.0 |  |  +  Improves support for multiple monitors <br />+  Improves security and stability   | 
| 2.2.3 |  | Resolves minor bugs and improves stability | 
| 2.2.1 |  |  +  Adds support for the German language <br />+  Resolves time zone mapping issues for some Regions <br />+  Resolves a connection issue on Russian systems <br />+  Improves the Japanese user interface <br />+  Improves stability   | 
| 2.1.3 |  | Closing the client expires the reconnect token. You can easily reconnect to your WorkSpace as long as the client is running. | 
| 2.1.1 |  | Minor improvement to protocol handling | 
| 2.1.0 |  |  +  Adds support for the following new WorkSpace states: STOPPING and STOPPED <br />+  Resolves minor bugs and improves stability   | 
| 2.0.8 |  |  +  Resolves a conflict with running iTunes or Garmin processes during installation <br />+  Adds support for a password-free installation experience if installing only for the current user <br />+  Resolves an issue with Excel formatting when copying and pasting data in BIFF5 format <br />+  If Remember Me is disabled, the user name is not shown on restart <br />+  Adds a confirmation dialog box when deleting a registration code <br />+  Improves stability   | 
| 2.0.6 |  | Resolves bugs and includes other improvements | 
| 2.0.4 |  |  +  Adds support for audio in, enabling you to make calls or attend web conferences <br />+  Adds support for devices with high DPI screens <br />+  Adds support for saving registration codes, enabling you to switch WorkSpaces without re-entering the registration codes <br />+  Improves support for Windows 10 <br />+  Improves usability and stability   | 
| 1.1.80 |  |  +  Adds CloudWatch metrics for session latency, session launch time, and session disconnects <br />+  Improves auto-session resume so that you are interrupted less frequently when network conditions are degraded <br />+  Resolves specific issues and improves stability   | 
| 1.1.6 |  |  +  Adds support for status notifications. The client application notifies you about the state of your WorkSpace when it cannot connect to the WorkSpace. <br />+  Improves the reconnect experience. The client automatically redirects to the login screen after 10 hours of inactivity. You can reconnect again if the client fails to launch a session using reconnect. <br />+  Adds support for auto-session resume. The client application automatically attempts to resume your session if network connectivity is lost and then regained within the session-resume timeout (default value is 20 minutes). <br />+  Improves network health checks so they are faster and more reliable <br />+  Adds client-side validation of registration codes <br />+  Improves the synchronization of Caps Lock and Num Lock status between the local device and the WorkSpace   | 
| 1.1.4 |  |  +  Adds support for saving your credentials, enabling you to easily reconnect to your WorkSpace <br />+  Improves advanced connection-health checks <br />+  Improves stability   | 
| 1.0.8 |  |  +  Introduces a full-file installation package <br />+  Improves network connectivity checks <br />+  Adds version information to the **About** window   | 
| 1.0 |  | Initial release | 