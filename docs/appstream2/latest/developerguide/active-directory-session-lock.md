

# Locking the Streaming Session When the User is Idle
<a name="active-directory-session-lock"></a>

WorkSpaces Applications relies on a setting that you configure in the GPMC to lock the streaming session after your user is idle for specified amount of time. To use the GPMC, you'll need to do the following first:
+ Obtain access to a computer or an EC2 instance that is joined to your domain.
+ Install the GPMC. For more information, see [Installing or Removing Remote Server Administration Tools for Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx) in the Microsoft documentation.
+ Log in as a domain user with permissions to create GPOs. Link GPOs to the appropriate OUs.

**To automatically lock the streaming instance when your user is idle**

1. In your directory or on a domain controller, open the command prompt as an administrator, type `gpmc.msc`, and then press ENTER.

1. In the left console tree, select the OU where you will create a new GPO or use an existing GPO, and then do either of the following: 
   + Create a new GPO by opening the context (right-click) menu and choosing **Create a GPO in this domain, Link it here**. For **Name**, provide a descriptive name for this GPO.
   + Select an existing GPO.

1. Open the context menu for the GPO, and choose **Edit**. 

1. Under **User Configuration**, expand **Policies**, **Administrative Templates**, **Control Panel**, and then choose **Personalization**. 

1. Double-click **Enable screen saver**.

1. In the **Enable screen saver** policy setting, choose **Enabled**.

1. Choose **Apply**, and then choose **OK**.

1. Double-click **Force specific screen saver**. 

1. In the **Force specific screen saver** policy setting, choose **Enabled**.

1. Under **Screen saver executable name**, enter **scrnsave.scr**. When this setting is enabled, the system displays a black screen saver on the user's desktop.

1. Choose **Apply**, and then choose **OK**.

1. Double-click **Password protect the screen saver**.

1. In the **Password protect the screen saver** policy setting, choose **Enabled**.

1. Choose **Apply**, and then choose **OK**.

1. Double-click **Screen saver timeout**.

1. In the **Screen saver timeout** policy setting, choose **Enabled**.

1. For **Seconds**, specify the length of time that users must be idle before the screen saver is applied. To set the idle time to 10 minutes, specify 600 seconds.

1. Choose **Apply**, and then choose **OK**.

1. In the console tree, under **User Configuration**, expand **Policies**, **Administrative Templates**, **System**, and then choose **Ctrl\+Alt\+Del Options**. 

1. Double-click **Remove Lock Computer**.

1. In the **Remove Lock Computer** policy setting, choose **Disabled**.

1. Choose **Apply**, and then choose **OK**.