# Enabling high DPI display for WorkSpaces

The Amazon WorkSpaces Android version 2.4.21 or later client application and the version 3.0+ client applications for
Windows, macOS, and Linux support high pixel density (high DPI) displays. Screen resolution is defined by the
number of pixels per inch (PPI) or dots per inch (DPI) that the screen can display horizontally and vertically.
Some common screen resolutions are:

- 1280x720 – High definition (HD), also known as 720p
- 1920x1080 – FHD (Full HD), also known as 1080p
- 2560x1440 – QHD/WQHD (Quad HD), also known as 1440p
- 3840x2160 – UHD (Ultra HD), also known as 4K 2160p
- 7680×4320 – FUHD (Full Ultra HD), also known as 8K 4320p

###### Note

Although all of these resolutions are labeled "high definition (HD)," that doesn't mean
that a monitor with one of these resolutions is a high DPI display.

###### Contents

- [Overview](#high-dpi-overview "#high-dpi-overview")
- [Limitations](#high-dpi-limitations "#high-dpi-limitations")
- [Enabling high DPI mode for Android](#high-dpi-android "#high-dpi-android")
- [Enabling high DPI mode for Windows, macOS, or Linux](#w39aac25c17 "#w39aac25c17")
- [Adjusting the scaling settings on a Windows WorkSpace](#w39aac25c19 "#w39aac25c19")
- [Adjusting the scaling settings on a Linux WorkSpace](#w39aac25c21 "#w39aac25c21")

## Overview

High DPI (also known as HiDPI) displays are those that use twice as many physical pixels to represent images
than the virtual pixels that make up an image. For example, if an image is 128 virtual pixels wide and 128
virtual pixels tall, on a high DPI display that image would be rendered using 256 physical pixels in both
directions, making the image twice as crisp.

For better maximum resolution of your WorkSpaces on high DPI displays, you can enable high DPI mode in the
WorkSpaces client applications for Android, Windows, macOS, and Linux.

## Limitations

Enabling high DPI mode might affect the performance of your WorkSpace. To accommodate the
bandwidth of your network, the streaming protocol upgrades or downgrades the number of
pixels that you receive as needed to maintain performance. However, in high latency, high
packet loss, or low bandwidth environments, high DPI mode might affect the performance of your WorkSpace.
We recommend that you turn off high DPI mode if it is affecting your WorkSpace performance.

For Windows WorkSpaces, high DPI mode supports multiple monitors. However, the Android client supports only a
single monitor.

###### Note

Graphics bundles support only a single monitor configuration with a maximum resolution of 2560x1600.

The maximum display size supported for high DPI mode in the Amazon WorkSpaces client applications is 3840x2160. For more
information about display support in the WorkSpaces client applications, see [Display Support for the Android Client](amazon-workspaces-android-client.md#android_display_support "amazon-workspaces-android-client.md#android_display_support"), [Display Support for the Linux Client](amazon-workspaces-linux-client.md#linux-display-support "amazon-workspaces-linux-client.md#linux-display-support"), [Display Support for the macOS Client](amazon-workspaces-osx-client.md#osx-display-support "amazon-workspaces-osx-client.md#osx-display-support"),
or [Display Support for the Windows Client](amazon-workspaces-windows-client.md#windows-display-support "amazon-workspaces-windows-client.md#windows-display-support").

## Enabling high DPI mode for Android

###### To enable high DPI mode for Android

1. Open your Amazon WorkSpaces version 2.4.21 or later client application and log in to your WorkSpace.
2. In the WorkSpaces client application, swipe from the left side of the screen to open the sidebar menu,
   and then choose **Settings**.
3. In the **Settings** dialog box, select **High DPI Mode**,
   then choose **OK**.

The screen resolution of your WorkSpace will change to match the high DPI resolution of your device.

## Enabling high DPI mode for Windows, macOS, or Linux

###### To enable high DPI mode for Windows, macOS, or Linux

1. Open your Amazon WorkSpaces 3.0+ client application and log in to your WorkSpace.
2. In the WorkSpaces client application, go to **Settings**,
   **Display Settings**.
3. In the **Display Settings** dialog box, select **High DPI Mode**,
   then click **Save**.

The screen resolution of your WorkSpace will change to match the high DPI resolution of your monitor.

###### Note

If you're using a Mac and your screen resolution in WorkSpaces is low and objects look blurry, do the
following:

1. Open **System Preferences**.
2. Choose **Displays**.
3. Do one of the following to adjust the display scaling, depending on your display type:

| If you're using...  | Do this                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| A built-in display  | On the **Display\*<br>• tab, under **Resolution**,<br>choose **Scaled**, and then choose **Default\*\*. |
| An external display | On the **Display\*<br>• tab, choose **Default for display\*\*.                                          |

If the images and text in your WorkSpace are smaller than you prefer, you will also need
to adjust the display scale settings on your Windows or Linux WorkSpace.

###### Important

- **Be sure to adjust the display scale settings within the
  WorkSpace itself, not the display scale settings for the local Windows,
  Linux, or Mac machine that you are using to access the
  WorkSpace.**
- When you dock or undock a laptop, or switch to another client device, you
  might need to readjust the scaling settings in the WorkSpace to suit the new
  monitor.

## Adjusting the scaling settings on a Windows WorkSpace

###### To adjust the scaling settings on a Windows WorkSpace

1. In your Windows WorkSpace, go to the Windows **Start** menu and choose
   **Settings**.
2. In the **Windows Settings** dialog box, choose **System**.
3. Choose **Display**.

###### Note

If you see the message "The display settings cannot be changed from a remote session," this
means that you're using a DCV WorkSpace. At this time, you can't adjust the display
scale settings for a DCV WorkSpace. 4. Under **Change the size of text, apps, and other items**, set the amount of
scaling you prefer. 5. A message appears that says "Some apps won't respond to scaling changes until you sign out."
To sign out, you can choose **Sign out now** below that message. Note that
signing out disconnects your WorkSpace session, so save your work before signing out. 6. To restart your WorkSpace session, either choose **Reconnect** on
the WorkSpaces client login page, or log in again. 7. If you are using multiple monitors, repeat these steps to set the scaling settings for each monitor.

## Adjusting the scaling settings on a Linux WorkSpace

###### To adjust the scaling settings on a Linux WorkSpace

###### Note

- These steps assume that you're using the default MATE environment for Amazon Linux WorkSpaces.
- For Linux WorkSpaces, high DPI mode isn't available for multiple monitors at this time.

1. In your Linux WorkSpace, go to **System** > **Preferences** >
   **Appearance**.
2. In the **Appearance Preferences** dialog box, choose the **Fonts**
   tab.
3. Choose **Details** in the lower-right corner.
4. In the **Font Rendering Details** dialog box, under **Resolution**,
   you will see a **Dots per inch (DPI)** setting. To manually adjust this setting, turn
   off **Automatic detection**.
5. Adjust the font size by using the **Dots per inch (DPI)** setting.
6. Close the dialog box.
