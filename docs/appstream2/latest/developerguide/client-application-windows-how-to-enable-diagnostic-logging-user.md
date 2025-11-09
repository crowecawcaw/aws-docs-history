# Logging

To help with troubleshooting if an issue with the WorkSpaces Applications client occurs, you
can enable diagnostic logging. The log files that are sent to WorkSpaces Applications (AWS)
include detailed information about your device and connection to the AWS
network. You can enable automatic log uploads so that these files are sent to
WorkSpaces Applications (AWS) automatically. You can also upload log files on an as-needed basis,
before or during an WorkSpaces Applications streaming session.

**Automatic logging**

You can enable automatic logging when you
install the WorkSpaces Applications client. For information
about how to enable automatic logging when you install the WorkSpaces Applications client, see
step 5 in [Setup for Windows](client-application-windows-installation-user.md "client-application-windows-installation-user.md").

**On-demand logging**

If an issue occurs during an WorkSpaces Applications streaming session, you can also
send log files on an as-needed basis. If an issue occurs that causes the WorkSpaces Applications
client to stop responding, a notification prompts you to choose whether to send
an error report and the associated log files to WorkSpaces Applications (AWS).

The following procedures describe how to send log files before you sign in to
an WorkSpaces Applications streaming session and during an WorkSpaces Applications streaming session.

###### To send log files before an WorkSpaces Applications streaming session

1. On your local PC where the WorkSpaces Applications client is installed, in the lower left of your screen,
   choose the Windows search icon on the taskbar, and enter
   `AppStream` in the Search box.
2. In the search results, select **Amazon AppStream** to start the WorkSpaces Applications client.
3. At the bottom of the WorkSpaces Applications sign-in page, choose the **Send Diagnostic Logs** link.
4. To continue connecting to WorkSpaces Applications, if your WorkSpaces Applications administrator has provided you with a web
   address (URL) to use to connect to WorkSpaces Applications for application streaming,
   enter the URL, and then choose **Connect**.

###### To send log files during an WorkSpaces Applications streaming session

1. If you are not already connected to WorkSpaces Applications and streaming an application, use the WorkSpaces Applications client to start a streaming session.
2. In the upper right of the WorkSpaces Applications session window, choose the **Profiles** icon, and then choose **Send Diagnostic Logs**.
