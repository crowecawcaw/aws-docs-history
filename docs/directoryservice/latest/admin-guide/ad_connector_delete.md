

# Deleting your AD Connector
<a name="ad_connector_delete"></a>

When an AD Connector is deleted, your on-premises directory remains intact. All instances that are joined to the directory also remain intact and remain joined to your on-premises directory. You can still use your directory credentials to log in to these instances.

**To delete AD Connector**

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, select **Directories**. Ensure you are in the AWS Region where your AD Connector is deployed. For more information, see [Choosing a Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html).

1. Ensure that no AWS applications are enabled for the AD Connector you intend to delete. Enabled AWS applications will prevent you for deleting your AD Connector.

   1. On the **Directories** page, choose your directory ID.

   1. On the **Directory details** page, select the **Application management** tab. In the **AWS apps & services** section, you see which AWS applications are enabled for your AD Connector.
      + Disable AWS Management Console access. For more information, see [Disabling AWS Management Console access](ms_ad_management_console_access.md#console_disable).
      + To disable Amazon WorkSpaces, you must deregister the service from the directory in the WorkSpaces console. For more information, see [Delete a directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html) in the *Amazon WorkSpaces Administration Guide*.
      + To disable WorkDocs, you must delete the WorkDocs site in the WorkDocs console. For more information, see [Delete a site](https://docs.aws.amazon.com/workdocs/latest/adminguide/delete_site.html) in the *Amazon WorkDocs Administration Guide*.
      + To disable Amazon WorkMail, you must remove the Amazon WorkMail organization in the Amazon WorkMail console. For more information, see [Remove an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/remove_organization.html) in the *Amazon WorkMail Administrator Guide*.
      + To disable Amazon FSx for Windows File Server, you must remove the Amazon FSx file system from the domain. For more information, see [Working with Active Directory in FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/aws-ad-integration-fsxW.html) in the *Amazon FSx for Windows File Server User Guide*.
      + To disable Amazon Relational Database Service, you must remove the Amazon RDS instance from the domain. For more information, see [Managing a DB instance in a domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html#USER_SQLServerWinAuth.Managing) in the *Amazon RDS User Guide*.
      + To disable AWS Client VPN Service, you must remove the directory service from the Client VPN Endpoint. For more information, see [Work with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working.html) in the *AWS Client VPN Administrator Guide*.
      + To disable Connect Customer, you must delete the Connect Customer Instance. For more information, see [Delete your Connect Customer instance](https://docs.aws.amazon.com/connect/latest/adminguide/delete-connect-instance.html) in the *Amazon Connect Administration Guide*.
      + To disable Amazon Quick, you must unsubscribe from Amazon Quick. For more information, see [Closing your Amazon Quick account](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html) in the *Amazon Quick User Guide*.
**Note**  
If you are using AWS IAM Identity Center and have previously connected it to the AWS Managed Microsoft AD directory you plan to delete, you must first change the identity source before you can delete it. For more information, see [Change your identity source ](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-change.html) in the *IAM Identity Center User Guide*.

1. In the navigation pane, choose **Directories**.

1. Select only the AD Connector to be deleted and click **Delete**. It takes several minutes for the AD Connector to be deleted. When the AD Connector has been deleted, it is removed from your directory list.