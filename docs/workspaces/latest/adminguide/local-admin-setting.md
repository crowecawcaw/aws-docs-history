# Manage local administrator permissions for WorkSpaces Personal

###### Note

This feature is only available for directories managed through AWS Directory Service,
including AD Connector, AWS Managed Microsoft AD, and Simple AD.

You can specify whether users are local administrators on their WorkSpaces, which
enables them to install application and modify settings on their WorkSpaces.
Users are local administrators by default. If you modify this setting, the change
applies to all new WorkSpaces that you create and any WorkSpaces that you rebuild.

###### To modify local administrator permissions

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose your directory.
4. Under Local administrator settings, choose **Edit**.
5. To ensure that users are local administrators, choose **Enable local administrator setting**.
6. Choose **Save**.
