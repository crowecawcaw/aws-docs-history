

# Delete a WorkSpace in WorkSpaces Personal
<a name="delete-workspaces"></a>

When you are finished with a WorkSpace, you can delete it. You can also delete related resources.

**Warning**  
Deleting a WorkSpace is a permanent action and cannot be undone. The WorkSpace user's data does not persist and is destroyed. For help with backing up user data, contact AWS Support.

**Note**  
Simple AD and AD Connector are available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the [AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/).  
To delete empty directories, see [Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md). If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.

**To delete a WorkSpace**

You can delete a WorkSpace that is in any state except **Suspended**.

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**.

1. Select your WorkSpace and choose **Delete**.

1. When prompted for confirmation, choose **Delete WorkSpace**. It takes approximately 5 minutes to delete a WorkSpace. During deletion, the status of the WorkSpace is set to **Terminating**. When the deletion is complete, the WorkSpace disappears from the console.

1. (Optional) To delete any custom bundles and images that you are finished with, see [Delete a custom bundle or image in WorkSpaces Personal](delete_bundle.md).

1. (Optional) After you delete all WorkSpaces in a directory, you can delete the directory. For more information, see [Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md).

1. (Optional) After you delete all resources in the virtual private cloud (VPC) for your directory, you can delete the VPC and release the Elastic IP address used for the NAT gateway. For more information, see [ Deleting your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#VPC_Deleting) and [ Working with Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#WorkWithEIPs) in the *Amazon VPC User Guide*.

**To delete a WorkSpace using the AWS CLI**  
Use the [terminate-workspaces](https://docs.aws.amazon.com/cli/latest/reference/workspaces/terminate-workspaces.html) command.