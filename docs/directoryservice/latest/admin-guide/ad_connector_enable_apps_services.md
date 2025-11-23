# Enabling access to AWS applications and services from AD Connector

Users can authorize AD Connector to give AWS applications and services, such as Amazon WorkSpaces, access to your
Active Directory. The following AWS applications and services can be enabled or disabled to work
with AD Connector.

| AWS application / service | More information...                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Chime              | For more information, see the [Connecting to Active Directory](../../../chime/latest/ag/active_directory.md "../../../chime/latest/ag/active_directory.md").                                                                                                                                                                           |
| Amazon Connect            | For more information, see the [Amazon Connect Administration Guide](../../../connect/latest/adminguide/what-is-amazon-connect.md "../../../connect/latest/adminguide/what-is-amazon-connect.md").                                                                                                                                      |
| Amazon WorkDocs           | For more information, see the [Getting started with Amazon WorkDocs](../../../workdocs/latest/adminguide/getting_started.md "../../../workdocs/latest/adminguide/getting_started.md").                                                                                                                                                 |
| Amazon WorkMail           | For more information, see the [Creating an organization](../../../workmail/latest/adminguide/add_new_organization.md "../../../workmail/latest/adminguide/add_new_organization.md").                                                                                                                                                   |
| Amazon WorkSpaces         | You can create a Simple AD, AWS Managed Microsoft AD, or AD Connector directly from WorkSpaces.<br>Simply launch \*_Advanced Setup_<br>• when creating your Workspace.<br>For more information, see the [Amazon WorkSpaces Administration Guide](../../../workspaces/latest/adminguide.md "../../../workspaces/latest/adminguide.md"). |
| AWS Client VPN            | For more information, see the [AWS Client VPN User Guide](../../../vpn/latest/clientvpn-user.md "../../../vpn/latest/clientvpn-user.md").                                                                                                                                                                                              |
| AWS IAM Identity Center   | For more information, see the [AWS IAM Identity Center User Guide](../../../singlesignon/latest/userguide.md "../../../singlesignon/latest/userguide.md").                                                                                                                                                                             |
| AWS Management Console    | For more information, see [Enabling AWS Management Console access with AWS Managed Microsoft AD<br>credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md").                                                                                                                                              |
| AWS Transfer Family       | For more information, see the [AWS Transfer Family User Guide](../../../transfer/latest/userguide/what-is-aws-transfer-family.md "../../../transfer/latest/userguide/what-is-aws-transfer-family.md").                                                                                                                                 |

Once enabled, you manage access to your directories in the console of the application or
service that you want to give access to your directory. To find the AWS applications and
services links described above in the Directory Service console, perform the following steps.

###### To display the applications and services for a directory

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Application management** tab.
4. Review the list under the **AWS apps & services** section.
   For more information about how to authorize or deauthorize AWS applications and services using Directory Service, see [Authorization for AWS applications and services using Directory Service](ad_manage_apps_services_authorization.md "ad_manage_apps_services_authorization.md").
