

# Enable diagnostic log uploads in WorkSpaces Personal
<a name="enable-diagnostic-log-uploads"></a>

To troubleshoot WorkSpaces client issues, enable automatic diagnostic log uploads. This is currently supported for Windows, macOS, Linux, and Web Access clients.

**Note**  
The WorkSpaces client diagnostic log uploads feature is currently unavailable in the AWS GovCloud (US-West) Region.

## Diagnostic log uploads
<a name="diagnostic-log-uploads"></a>

With Diagnostic log uploads, you can upload WorkSpaces client log files directly to WorkSpaces to troubleshoot issues without interrupting use of the WorkSpaces client. If you enable diagnostic log uploads for your users, or let your users do so themselves, the log files are sent to WorkSpaces automatically. You can enable diagnostic log uploads before or during a WorkSpaces streaming session.

To automatically upload diagnostic logs from managed devices, install a WorkSpaces client that supports diagnostic uploads. Log uploading is enabled by default. You can modify the settings in either of the following ways:

### Option 1: Using the AWS console
<a name="diagnostic-log-console"></a>

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose the directory name that you want to enable diagnostic logging for.

1. Scroll down to **Self-service permission**.

1. Choose **View details**

1. Choose **Edit**.

1. Choose **Diagnostic log uploads**.

1. Choose **Save**.

### Option 2: Using an API call
<a name="diagnostic-log-api"></a>

You can edit the directory settings to enable or disable the WorkSpaces Windows, macOS, and Linux client to upload diagnostic logs automatically using an API call. If enabled, when a client issue occurs, the logs are sent to WorkSpaces without user interaction. For more information, see the [ WorkSpaces API reference](https://docs.aws.amazon.com/workspaces/latest/api/API_ClientProperties.html).

You can also let your users choose whether to enable automatic diagnostic log uploads after client installation. For more information, see [WorkSpaces Windows client application ](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-windows-client.html), [WorkSpaces macOS client application](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-osx-client.html), and [WorkSpaces Linux client application](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html).

**Note**  
Diagnostic logs don't contain sensitive information. You can disable automatic diagnostic log uploads for your users at the directory level, or allow your users to disable these features themselves.
To access the diagnostic log uploads feature, you need to install the following versions of the WorkSpaces clients:  
5.4.0 or later of the Windows client
5.8.0 or later of the macOS client
2023.1 of the Ubuntu 22.04 client
2023.1 of the Ubuntu 20.04 client
You can also access the diagnostic log upload feature with the Web Access client