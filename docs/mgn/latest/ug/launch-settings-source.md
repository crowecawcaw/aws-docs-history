

# Review launch settings for a source server
<a name="launch-settings-source"></a>

The launch settings are a set of instructions that comprise an EC2 launch template and other settings, which determine how a test or cutover instance is launched for each source server on AWS. 

Launch settings, including the EC2 launch template, are automatically created every time you add a server to AWS Transform MGN.

The launch settings can be modified at any time, including before the source servers have even completed initial sync. 

To edit the launch settings for a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to the source server.

1. Choose **Test and cutover**, then choose **Edit launch settings**.

1. Modify the settings as needed and save your changes.

[Learn more about individual launch settings.](launch-settings.md)