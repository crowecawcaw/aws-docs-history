# Select an organizational unit for WorkSpaces Personal

###### Note

This feature is only available for directories managed through AWS Directory Service,
including AD Connector, AWS Managed Microsoft AD, and Simple AD.

WorkSpace machine accounts are placed in the default organizational unit (OU)
for the WorkSpaces directory. Initially, the machine accounts are placed in the
Computers OU of your directory or the directory that your AD Connector is connected to.
You can select a different OU from your directory or connected directory,
or specify an OU in a separate target domain. Note that you can select only one
OU per directory.

After you select a new OU, the machine accounts for all WorkSpaces that are created
or rebuilt are placed in the newly selected OU.

###### To select an organizational unit

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose your directory.
4. Under Target domain and organizational unit, choose **Edit**.
5. To find an OU, under Target and organizational unit, you can start typing all or part of the OU name and choose
   the OU you want to use.
6. (Optional) Choose an OU distiguished name to overwrite your selected OU with a custom OU.
7. Choose **Save**.
8. (Optional) Rebuild the existing WorkSpaces to update the OU. For more information,
   see [Rebuild a WorkSpace in WorkSpaces Personal](rebuild-workspace.md "rebuild-workspace.md").
