

# Changing display resolution
<a name="changing-resolution"></a>

By default, Amazon DCV automatically adapts the display resolution of the remote machine to match the current size of the client. When the client window is resized, DCV requests the server to change its display resolution to a size that fits within the client window.

Amazon DCV can configure a resolution according to the settings and the server system configuration.
+ Web client resolution is limited by default to 1920x1080 (from web-client-max-head-resolution server setting).
+ Native clients are limited by default to 4096x2160 (from max-head-resolution).

Note that the available resolutions and number of monitors depend on the configuration of the server, make sure to follow the [prerequisites guide](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing.html) to properly setup the system environment and drivers for best performance.

**Important**  
Maximum supported per-monitor resolution is 4096x4096 for up to 4 monitors. Higher resolutions or more than 4 monitors are not supported in any configuration.

If you prefer a fixed resolution on the server, which does not change even when the client window is resized, select the **Display Resolution** menu and specify the desired resolution. If you decide to re-enable automatic resize, you can select **Adapt automatically **.

This functionality is available on the Windows client, web browser client, Linux client, and macOS client. The steps depend on the client used.

------
#### [ Windows ]

1. Click on the **Settings** icon from the menu at the top.

1. Select **Display Resolution** from the menu.

1. Select your preferred resolution from the drop-down menu.

------
#### [ macOS ]

1. Choose the **Display** toolbar button.

1. From the **Resolution** menu, choose **Auto** to automatically fit the remote desktop to the window size, the current remote desktop resolution to keep it unchanged, or a specific fixed resolution.  
![Display resolution options including Auto, current remote resolution, 3840x2160, 2560x1440, 1920x1080, 1280x720, 1024x768, and 800x600.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-display-resolution.png)

**Tip**  
You can also change the resolution from the menu bar. Choose the **Connection** menu, then select **Display**, **Resolution**, and choose the desired option.

------
#### [ Linux ]

1. Click on the **Display Settings** menu icon from the toolbar at the top.

1. Select your preferred resolution from the **Resolution** menu.
**Note**  
Selecting **Auto** allows the client to adapt the resolution automatically when the client window is resized.  
![Resolution menu with Auto selected, showing resolutions 1920x1080, 1280x720, 1024x768, and 800x600.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-pref-display-resolution.png)

------