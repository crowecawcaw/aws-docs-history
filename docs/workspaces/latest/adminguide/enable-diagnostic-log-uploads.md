# Enable diagnostic log uploads in WorkSpaces Personal

To troubleshoot WorkSpaces client issues, enable automatic diagnostic log uploads. This is
currently supported for Windows, macOS, Linux, and Web Access clients.

###### Note

The WorkSpaces client diagnostic log uploads feature is currently unavailable in the
AWS GovCloud (US-West) Region.

## Diagnostic log uploads

With Diagnostic log uploads, you can upload WorkSpaces client log files directly to
WorkSpaces to troubleshoot issues without interrupting use of the WorkSpaces client. If you
enable diagnostic log uploads for your users, or let your users do so themselves,
the log files are sent to WorkSpaces automatically. You can enable diagnostic log uploads
before or during a WorkSpaces streaming session.

To automatically upload diagnostic logs from managed devices, install a WorkSpaces
client that supports diagnostic uploads. Log uploading is enabled by default. You
can modify the settings in either of the following ways:

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose the directory name that you want to enable diagnostic logging
   for.
4. Scroll down to **Self-service permission**.
5. Choose **View details**
6. Choose **Edit**.
7. Choose **Diagnostic log uploads**.
8. Choose **Save**.

You can edit the directory settings to enable or disable the WorkSpaces
Windows, macOS, and Linux client to upload diagnostic logs automatically
using an API call. If enabled, when a client issue occurs, the logs are sent
to WorkSpaces without user interaction. For more information, see the [WorkSpaces API reference](../api/API_ClientProperties.md "../api/API_ClientProperties.md").

You can also let your users choose whether to enable automatic diagnostic log
uploads after client installation. For more information, see [WorkSpaces
Windows client application](../userguide/amazon-workspaces-windows-client.md "../userguide/amazon-workspaces-windows-client.md") , [WorkSpaces macOS
client application](../userguide/amazon-workspaces-osx-client.md "../userguide/amazon-workspaces-osx-client.md"), and [WorkSpaces
Linux client application](../userguide/amazon-workspaces-linux-client.md "../userguide/amazon-workspaces-linux-client.md").

###### Note

- Diagnostic logs don't contain sensitive information. You can disable
  automatic diagnostic log uploads for your users at the directory level,
  or allow your users to disable these features themselves.
- To access the diagnostic log uploads feature, you need to install the
  following versions of the WorkSpaces clients:
  - 5.4.0 or later of the Windows client
  - 5.8.0 or later of the macOS client
  - 2023.1 of the Ubuntu 22.04 client
  - 2023.1 of the Ubuntu 20.04 client
  - You can also access the diagnostic log upload feature with the
    Web Access client
