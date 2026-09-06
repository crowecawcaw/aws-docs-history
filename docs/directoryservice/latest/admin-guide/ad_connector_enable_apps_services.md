

# Enabling access to AWS applications and services from AD Connector
<a name="ad_connector_enable_apps_services"></a>

Users can authorize AD Connector to give AWS applications and services, such as Amazon WorkSpaces, access to your Active Directory. The following AWS applications and services can be enabled or disabled to work with AD Connector.


| AWS application / service | More information... | 
| --- | --- | 
| Amazon Chime | For more information, see the [Connecting to Active Directory](https://docs.aws.amazon.com/chime/latest/ag/active_directory.html). | 
| Connect Customer | For more information, see the [Connect Customer Administration Guide](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html). | 
| Amazon WorkDocs | For more information, see the [Getting started with Amazon WorkDocs](https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html). | 
| Amazon WorkMail | For more information, see the [ Creating an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_organization.html). | 
| Amazon WorkSpaces | You can create a Simple AD, AWS Managed Microsoft AD, or AD Connector directly from WorkSpaces. Simply launch **Advanced Setup** when creating your Workspace.<br />For more information, see the [Amazon WorkSpaces Administration Guide](https://docs.aws.amazon.com/workspaces/latest/adminguide/). | 
| AWS Client VPN | For more information, see the [AWS Client VPN User Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/). | 
| AWS IAM Identity Center | For more information, see the [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/). | 
| AWS Management Console | For more information, see [Enabling AWS Management Console access with AWS Managed Microsoft AD credentials](ms_ad_management_console_access.md). | 
| AWS Transfer Family | For more information, see the [AWS Transfer Family User Guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html). | 

Once enabled, you manage access to your directories in the console of the application or service that you want to give access to your directory. To find the AWS applications and services links described above in the Directory Service console, perform the following steps.

**To display the applications and services for a directory**

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories**.

1. On the **Directories** page, choose your directory ID.

1. On the **Directory details** page, select the **Application management** tab.

1. Review the list under the **AWS apps & services** section.

For more information about how to authorize or deauthorize AWS applications and services using Directory Service, see [Authorization for AWS applications and services using Directory Service](ad_manage_apps_services_authorization.md).