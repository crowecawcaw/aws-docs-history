

# Deleting a hybrid directory
<a name="hybrid_directory_delete"></a>

When you delete a hybrid directory, all directory data and snapshots are deleted and cannot be recovered. After the directory is deleted, all instances that were joined to the directory remain intact. However, you cannot use the directory credentials to log into these instances. You must log into these instances with a local user account.

**To delete a directory**

1. In the [Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, select **Directories**. Ensure you are in the AWS Region where your hybrid directory is deployed. For more information, see [Choosing a Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html).

1. Ensure that no AWS applications are enabled for the directory you intend to delete. Enabled AWS applications will prevent you from deleting your hybrid directory.

1. On the **Directories** page, choose your directory ID.

1. On the **Directory details** page, select the **Application management** tab. In the **AWS apps & services** section, you see which AWS applications are enabled for your directory.

   1. Disable AWS Management Console access. For more information, see [Disabling AWS Management Console access](https://docs.aws.amazon.com/ms_ad_management_console_access.xml).

   1. To disable Amazon FSx for Windows File Server, you must remove the Amazon FSx file system from the domain. For more information, see [Working with Active Directory in FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/aws-ad-integration-fsxW.html) in the *Amazon FSx for Windows File Server User Guide*.

   1. To disable Amazon Relational Database Service, you must remove the Amazon RDS instance from the domain. For more information, see [Managing a DB instance in a domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html#USER_SQLServerWinAuth.Managing) in the *Amazon RDS User Guide*.

1. In the navigation pane, choose **Directories**.

1. Select only the directory to be deleted and choose **Delete**. It takes several minutes for the directory to be deleted. When the directory has been deleted, it is removed from your directory list.

1. Manually delete any remaining domain controller objects, including any AWS Reserved OUs. You can delete the entire AWS Reserved directory to finish cleaning up your environment. 