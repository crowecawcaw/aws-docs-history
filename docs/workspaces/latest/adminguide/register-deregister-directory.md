# Register an existing Directory Service directory with WorkSpaces Personal

To allow WorkSpaces to use an existing Directory Service directory, you must register it with WorkSpaces.
After you register a directory, you can launch WorkSpaces in the directory.

###### Requirements

To register a directory for use with WorkSpaces, it must meet the following requirement:

- If you're using AWS Managed Microsoft AD or Simple AD, your directory can be in a
  dedicated private subnet, as long as the directory has access to the VPC where
  the WorkSpaces are located.
  For more information about directory and VPC design, see the
  [_Best Practices for Deploying Amazon WorkSpaces_](https://d1.awsstatic.com/whitepapers/Best-Practices-for-Deploying-Amazon-WorkSpaces.pdf "https://d1.awsstatic.com/whitepapers/Best-Practices-for-Deploying-Amazon-WorkSpaces.pdf") whitepaper.

###### Note

Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces.
If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30
consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces,
and you will be charged for this directory as per the
[AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/").

To delete empty directories, see
[Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md "delete-workspaces-directory.md"). If you delete your
Simple AD or AD Connector directory, you can always create a new one when you want to start using
WorkSpaces again.

###### To register an existing AWS Directory Service directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose **Create directory**.
4. On the **Create directory** page, for **WorkSpaces type**
   choose **Personal**. For **WorkSpace device management**,
   choose **AWS Directory Service**.
5. Select the directory you want to register in the **Directories in Directory Service** table
6. Select two subnets of your VPC that are not from the same Availability Zone. These subnets will
   be used to launch your WorkSpaces. For more information, see
   [Availability Zones for WorkSpaces Personal](azs-workspaces.md "azs-workspaces.md").

###### Note

If you do not know which subnets to choose, select **No Preference**. 7. For **Enable Self Service Permissions**, choose **Yes** to enable your
users to rebuild their WorkSpaces, change volume size, compute type and running mode.
Enabling may impact how much you pay for Amazon WorkSpaces. Choose **No** otherwise. 8. Choose **Register**.
Initially the value of **Registered** is `REGISTERING`.
After registration is complete, the value is `Yes`.
After you've registered the Directory Service directory, you can create a personal WorkSpace. For more information, see
[Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md "create-workspaces-personal.md").

When you are finished using the directory with WorkSpaces, you can deregister it. Note that you must deregister a
directory before you can delete it. If you want to deregister and delete a directory, you must first find and
remove all the applications and services that are registered to the directory. For more information, see
[Delete Your Directory](../../../directoryservice/latest/admin-guide/ms_ad_delete.md "../../../directoryservice/latest/admin-guide/ms_ad_delete.md") in the _AWS Directory Service Administration Guide_.

###### To deregister a directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select the directory.
4. Choose **Actions**, **Deregister**.
5. When prompted for confirmation, choose **Confirm**. After
   deregistration is complete, the directory becomes unregistered and is removed from the list.
