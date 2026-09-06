

# Enabling access to AWS applications and services for your AWS Managed Microsoft AD
<a name="ms_ad_enable_apps_services"></a>

Users can authorize AWS Managed Microsoft AD to give AWS applications and services, such as Amazon WorkSpaces, access to your Active Directory. The following AWS applications and services can be enabled or disabled to work with AWS Managed Microsoft AD.


| AWS application / service | More information... | 
| --- | --- | 
| Amazon Chime | For more information, see the [Connecting to Active Directory](https://docs.aws.amazon.com/chime/latest/ag/active_directory.html). | 
| Connect Customer | For more information, see the [Connect Customer Administration Guide](https://docs.aws.amazon.com/connect/latest/adminguide/related-services-amazon-connect.html#security-services). | 
| Amazon EC2 | For more information, see [Ways to join an Amazon EC2 instance to your AWS Managed Microsoft AD](ms_ad_join_instance.md). | 
| Amazon FSx for Windows File Server | For more information, see [Using Amazon FSx with AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-aws-managed-ad.html). | 
| Quick | For more information, see the [Using Active Directory with Quick Enterprise edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html). | 
| Amazon Relational Database Service | For more information, see the following: + [Using Kerberos authentication for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-kerberos.html)<br />+ [Using Kerberos authentication with Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos.html)<br />+ [Using Kerberos authentication with Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-kerberos.html)<br />+ [Working with AWS Managed Microsoft AD with Amazon RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html) | 
| Amazon WorkDocs | For more information, see the [Enable Amazon WorkDocs for AWS Managed Microsoft AD](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-workdocs-active-directory.html). | 
| Amazon WorkMail | For more information, see the [Creating an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_organization.html). | 
| Amazon WorkSpaces | You can create a Simple AD, AWS Managed Microsoft AD, or AD Connector directly from WorkSpaces. Simply launch **Advanced Setup** when creating your Workspace.<br />For more information, see the [Register an existing Directory Service directory with WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html). | 
| AWS Client VPN | For more information, see the [Active Directory authentication in Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ad.html). | 
| AWS IAM Identity Center | For more information, see the [Connect to a Microsoft AD directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/connectawsad.html). | 
| AWS License Manager | For more information, see the [Manage user-based subscriptions in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions.html). | 
| AWS Management Console | For more information, see [Enabling AWS Management Console access with AWS Managed Microsoft AD credentials](ms_ad_management_console_access.md). | 
| AWS Private Certificate Authority | For more information, see [AWS Private CA Connector for Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html). | 
| AWS Transfer Family | For more information, see the [Configuring an SFTP, FTPS, or FTP server endpoint](https://docs.aws.amazon.com/transfer/latest/userguide/sftp-for-transfer-family.html). | 

Once enabled, you manage access to your directories in the console of the application or service that you want to give access to your directory.

## Find AWS applications and services
<a name="find-apps-and-services"></a>

To find the AWS applications and services previously described in the Directory Service console, perform the following steps.

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories**.

1. On the **Directories** page, choose your directory ID.

1. On the **Directory details** page, select the **Application management** tab.

1. Review the list under the **AWS apps & services** section.

For more information about how to authorize or deauthorize AWS applications and services using Directory Service, see [Authorization for AWS applications and services using Directory Service](ad_manage_apps_services_authorization.md).