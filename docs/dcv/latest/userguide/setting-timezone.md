

# Setting the time zone
<a name="setting-timezone"></a>

DCV allows you to set the time zone for your session to display either the time zone you are currently or the time zone of where the remote desktop you are using is located.

This is referred to as time zone redirection.

Once this feature is either enabled or disabled the DCV client will save this settting for each time the user signs on to the client.

When collaborating sessions, the first client to connect to the session, known as the primary connection, will set the time zone for the session even if the primary connection leaves the session. For more information, see [Collaborating on a Amazon DCV session](managing-sessions-session-collaboration.md). 

To use this feature, your administrator will have to enable it. If you do not have the option to change your displayed time zone and would like to do so, contact your administrator. For more information, see [ Modifying Configuration Parameters](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref-modify.html) in the *Amazon DCV Administrator Guide*.

To set your time zone, do one of the following depending on your client:
+ **For Windows**

  1. Go to the **Settings** icon.

  1. Select **Time Zone Redirection** from the drop down menu.
**Note**  
It will indicate if the feature is **Enabled** or **Disabled** under the menu item.  
![Time Zone Redirection Disable option highlighted in a settings menu.](http://docs.aws.amazon.com/dcv/latest/userguide/images/TZR_windows_circle.png)
+ **For macOS**

  1. Go to the **DCV Viewer** icon from the toolbar at the top.

  1. Select **Preferences** from the drop-down menu.

  1. Select the **General** tab.

  1. Check the box for **Enable timezone redirection**.  
![Preferences window with General tab showing Enable timezone redirection checkbox selected.](http://docs.aws.amazon.com/dcv/latest/userguide/images/mac-preferences-general-timezone.png)
+ **For Linux**

  1. Go to the **Settings** icon.

  1. Select **Preferences** from the drop-down menu.

  1. Select the **General** tab in the **Preferences** windows.

  1. Check the box for **Timezone Redirection**.  
![Preferences dialog with General tab showing Enable timezone redirection checkbox circled.](http://docs.aws.amazon.com/dcv/latest/userguide/images/linux-pref-general-timezone.png)
+ **For web based clients**

  1. Go to **Preferences**.

  1. Click on the switch for **Time Zone Redirection**.  
![Preferences dialog with General tab showing Time Zone Redirection toggle set to Enabled.](http://docs.aws.amazon.com/dcv/latest/userguide/images/TZR_web_circle.png)