# Deleting your AD Connector

When an AD Connector is deleted, your on-premises directory remains intact. All instances that are joined to the directory also remain intact and remain joined to your on-premises directory. You can still use your directory credentials to log in to these instances.

###### To delete AD Connector

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**. Ensure you are in the AWS Region where your AD Connector is deployed. For more information, see [Choosing a Region](../../../awsconsolehelpdocs/latest/gsg/select-region.md "../../../awsconsolehelpdocs/latest/gsg/select-region.md").
2. Ensure that no AWS applications are enabled for the AD Connector you intend to delete. Enabled AWS applications will prevent you for deleting your AD Connector.
   1. On the **Directories** page, choose your directory ID.
   2. On the **Directory details** page, select the
      **Application management** tab. In the **AWS apps & services**
      section, you see which AWS applications are enabled for your AD Connector.
      - Disable AWS Management Console access. For more information, see [Disabling AWS Management Console access](ms_ad_management_console_access.md#console_disable "ms_ad_management_console_access.md#console_disable").
      - To disable Amazon WorkSpaces, you must deregister the service from the directory in the
        WorkSpaces console. For more information, see [Delete a directory](../../../workspaces/latest/adminguide/delete-workspaces-directory.md "../../../workspaces/latest/adminguide/delete-workspaces-directory.md") in the
        _Amazon WorkSpaces Administration Guide_.
      - To disable WorkDocs, you must delete the WorkDocs site in the WorkDocs
        console. For more information, see [Delete a site](../../../workdocs/latest/adminguide/delete_site.md "../../../workdocs/latest/adminguide/delete_site.md") in the
        _Amazon WorkDocs Administration Guide_.
      - To disable Amazon WorkMail, you must remove the Amazon WorkMail organization in the
        Amazon WorkMail console. For more information, see [Remove an
        organization](../../../workmail/latest/adminguide/remove_organization.md "../../../workmail/latest/adminguide/remove_organization.md") in the
        _Amazon WorkMail Administrator Guide_.
      - To disable Amazon FSx for Windows File Server, you must remove the Amazon FSx file system from the domain. For more information, see [Working with Active Directory in FSx for Windows File Server](../../../fsx/latest/WindowsGuide/aws-ad-integration-fsxW.md "../../../fsx/latest/WindowsGuide/aws-ad-integration-fsxW.md") in the
        _Amazon FSx for Windows File Server User Guide_.
      - To disable Amazon Relational Database Service, you must remove the Amazon RDS instance from the domain. For more information, see [Managing a DB instance in a domain](../../../AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.md#USER_SQLServerWinAuth.Managing "../../../AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.md#USER_SQLServerWinAuth.Managing") in the
        _Amazon RDS User Guide_.
      - To disable AWS Client VPN Service, you must remove the directory service from the Client VPN Endpoint. For more information, see [Work with Client VPN](../../../vpn/latest/clientvpn-admin/cvpn-working.md "../../../vpn/latest/clientvpn-admin/cvpn-working.md") in the
        _AWS Client VPN Administrator Guide_.
      - To disable Amazon Connect, you must delete the Amazon Connect Instance. For more information, see [Delete your Amazon Connect instance](../../../connect/latest/adminguide/delete-connect-instance.md "../../../connect/latest/adminguide/delete-connect-instance.md") in the
        _Amazon Connect Administration Guide_.
      - To disable Amazon Quick Suite, you must unsubscribe from Amazon Quick Suite. For more information, see [Closing your Amazon Quick Suite account](../../../quicksight/latest/user/closing-account.md "../../../quicksight/latest/user/closing-account.md") in the
        _Amazon Quick Suite User Guide_.

   ###### Note

   If you are using AWS IAM Identity Center and have previously connected it to the AWS Managed Microsoft AD directory you plan to
   delete, you must first change the identity source before you can delete it. For
   more information, see [Change your identity source](../../../singlesignon/latest/userguide/manage-your-identity-source-change.md "../../../singlesignon/latest/userguide/manage-your-identity-source-change.md") in the _IAM Identity Center User Guide_.

3. In the navigation pane, choose **Directories**.
4. Select only the AD Connector to be deleted and click **Delete**. It takes
   several minutes for the AD Connector to be deleted. When the AD Connector has been deleted, it is
   removed from your directory list.
