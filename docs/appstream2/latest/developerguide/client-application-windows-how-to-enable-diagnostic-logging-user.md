# Logging

To help with troubleshooting if an issue with the AppStream 2.0 client occurs, you
can enable diagnostic logging. The log files that are sent to AppStream 2.0 (AWS)
include detailed information about your device and connection to the AWS
network. You can enable automatic log uploads so that these files are sent to
AppStream 2.0 (AWS) automatically. You can also upload log files on an as-needed basis,
before or during an AppStream 2.0 streaming session.

**Automatic logging**

You can enable automatic logging when you
install the AppStream 2.0 client. For information
about how to enable automatic logging when you install the AppStream 2.0 client, see
step 5 in [Setup for Windows](client-application-windows-installation-user.md "client-application-windows-installation-user.md").

**On-demand logging**

If an issue occurs during an AppStream 2.0 streaming session, you can also
send log files on an as-needed basis. If an issue occurs that causes the AppStream 2.0
client to stop responding, a notification prompts you to choose whether to send
an error report and the associated log files to AppStream 2.0 (AWS).

The following procedures describe how to send log files before you sign in to
an AppStream 2.0 streaming session and during an AppStream 2.0 streaming session.

###### To send log files before an AppStream 2.0 streaming session

1. On your local PC where the AppStream 2.0 client is installed, in the lower left of your screen,
   choose the Windows search icon on the taskbar, and enter
   `AppStream` in the Search box.
2. In the search results, select **Amazon AppStream** to start the AppStream 2.0 client.
3. At the bottom of the AppStream 2.0 sign-in page, choose the **Send Diagnostic Logs** link.
4. To continue connecting to AppStream 2.0, if your AppStream 2.0 administrator has provided you with a web
   address (URL) to use to connect to AppStream 2.0 for application streaming,
   enter the URL, and then choose **Connect**.

###### To send log files during an AppStream 2.0 streaming session

1. If you are not already connected to AppStream 2.0 and streaming an application, use the AppStream 2.0 client to start a streaming session.
2. In the upper right of the AppStream 2.0 session window, choose the **Profiles** icon, and then choose **Send Diagnostic Logs**.
