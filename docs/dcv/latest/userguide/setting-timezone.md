

# Setting the time zone
<a name="setting-timezone"></a>

Amazon DCV can set your session's time zone to either your local time zone or the time zone where the remote desktop is located. This is called time zone redirection.

When you enable or disable this feature, the Amazon DCV client remembers your choice and applies it every time you sign in.

In collaborative sessions, the time zone is set by the first client that connects to the session (the primary connection), even if that client later leaves the session. For more information, see [Collaborating on an Amazon DCV session](managing-sessions-session-collaboration.md).

Time zone redirection is enabled by default. If you cannot change this option in your client, your administrator has locked it. To change it, contact your administrator. For more information, see [Modifying Configuration Parameters](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref-modify.html) in the *Amazon DCV Administrator Guide*.

To set your time zone, do one of the following depending on your client:
+ **For Windows**

  1. Go to the **Settings** icon.

  1. Select **Time Zone Redirection** from the drop down menu.
**Note**  
The menu item shows whether the feature is enabled or disabled.  
![Time Zone Redirection Disable option highlighted in a settings menu.](https://docs.aws.amazon.com/dcv/latest/userguide/images/TZR_windows_circle.png)
+ **For macOS**

  1. Go to the **DCV Viewer** icon from the toolbar at the top.

  1. Select **Preferences** from the drop-down menu.

  1. Select the **General** tab.

  1. Check the box for **Enable timezone redirection**.  
![Preferences window with General tab showing Enable timezone redirection checkbox selected.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-preferences-general-timezone.png)
+ **For Linux**

  1. Go to the **Settings** icon.

  1. Select **Preferences** from the drop-down menu.

  1. Select the **General** tab in the **Preferences** windows.

  1. Check the box for **Timezone Redirection**.  
![Preferences dialog with General tab showing Enable timezone redirection checkbox circled.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-pref-general-timezone.png)
+ **For web based clients**

  1. Choose **Preferences**.

  1. Choose the **Time Zone Redirection** switch.  
![Preferences dialog with General tab showing Time Zone Redirection toggle set to Enabled.](https://docs.aws.amazon.com/dcv/latest/userguide/images/TZR_web_circle.png)