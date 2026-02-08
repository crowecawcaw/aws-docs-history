# Delete a directory for WorkSpaces Personal

###### Note

Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces.
If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30
consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces,
and you will be charged for this directory as per the
[AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/").

If you delete your Simple AD or AD Connector directory, you can always create a new one
when you want to start using WorkSpaces again.

**What happens when you delete a directory:** When you delete a directory, the following occurs:

- When a Simple AD or AWS Directory Service for Microsoft Active Directory directory is deleted, all of the directory data and snapshots
  are deleted and cannot be recovered. After the directory is deleted, any Amazon EC2 instances that are joined to the
  directory remain intact. You cannot, however, use your directory credentials to log in to these instances.
  You need to log in to these instances with an AWS account that is local to the instance.
- When an AD Connector directory is deleted, your on-premises directory remains intact. Any Amazon EC2 instances
  that are joined to the directory also remain intact and remain joined to your on-premises directory. You
  can still use your directory credentials to log in to these instances.

## Delete an Entra ID or Custom WorkSpaces directory

Entra ID WorkSpaces directory allows you to create Entra ID-joined Windows 10 or 11 BYOL WorkSpaces. For more information,
see [Create a dedicated Microsoft Entra ID directory with WorkSpaces Personal](launch-entra-id.md "launch-entra-id.md").

Custom WorkSpaces directory allows you to create WorkSpaces that are not Active Directory domain-joined, but use your own device management software and IAM
Identity Center. For more information,
see [Create a dedicated Custom directory with WorkSpaces Personal](launch-custom.md "launch-custom.md").

###### To delete an Entra ID or Custom WorkSpaces directory

1. Delete all the WorkSpaces in the directory. For more information, see [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md "delete-workspaces.md").
2. In the navigation pane, choose **Directories**.
3. Select the directory.
4. Choose **Actions**, **Delete**.
5. When prompted for confirmation, enter **delete**.

## Delete an AWS Directory Service directory

You can delete the AWS Directory Service directory for your WorkSpaces if it is no longer in use by other WorkSpaces
or other applications, such as WorkDocs, Amazon WorkMail, or Amazon Chime. Note that you must deregister a directory before you can delete it.

###### To deregister a directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select the directory.
4. Choose **Actions**, **Deregister**.
5. When prompted for confirmation, choose **Deregister**. After
   deregistration is complete, the value of **Registered** is `No`.

###### To delete a directory

1. Delete all WorkSpaces in the directory. For more information, see
   [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md "delete-workspaces.md").
2. Find and remove all of the applications and services that are registered to the directory. For
   more information, see [Delete Your Directory](../../../directoryservice/latest/admin-guide/ms_ad_delete.md "../../../directoryservice/latest/admin-guide/ms_ad_delete.md")
   in the _AWS Directory Service Administration Guide_.
3. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
4. In the navigation pane, choose **Directories**.
5. Select the directory and choose **Actions**,
   **Deregister**.
6. When prompted for confirmation, choose **Deregister**.
7. Select the directory again and choose **Actions**,
   **Delete**.
8. When prompted for confirmation, choose **Delete**.

###### Note

Removing application assignments can sometimes take more time than expected. If you receive
the following error message, verify that you've removed all application assignments, and then
wait 30 to 60 minutes before trying again to delete the directory:

```
An Error Has Occurred
Cannot delete the directory because it still has authorized applications.
Additional directory details can be viewed at the Directory Service console.
```

9. (Optional) After you delete all resources in the virtual private cloud (VPC) for your directory,
   you can delete the VPC and release the Elastic IP address used for the NAT gateway. For more information,
   see [Deleting your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#VPC_Deleting "../../../vpc/latest/userguide/working-with-vpcs.md#VPC_Deleting") and [Working with Elastic IP addresses](../../../vpc/latest/userguide/vpc-eips.md#WorkWithEIPs "../../../vpc/latest/userguide/vpc-eips.md#WorkWithEIPs") in the _Amazon VPC User Guide_.
10. (Optional) To delete any custom bundles and images that you are finished with, see
    [Delete a custom bundle or image in WorkSpaces Personal](delete_bundle.md "delete_bundle.md").
