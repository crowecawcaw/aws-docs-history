# Application compatibility policy for

AD Connector

As an alternative to AWS Directory Service for Microsoft Active Directory ([AWS Managed Microsoft AD](directory_microsoft_ad.md "directory_microsoft_ad.md")), AD Connector is an Active Directory proxy for
AWS created applications and services only. You configure the proxy to use a specified Active
Directory domain. When the application must look up a user or group in Active Directory,
AD Connector proxies the request to the directory. Similarly, when a user logs in to the
application, AD Connector proxies the authentication request to the directory. There are no
third-party applications that work with AD Connector.

The following is a list of compatible AWS applications and services:

- Amazon Chime - For detailed instructions, see [Connect to your Active
  Directory](../../../chime/latest/ag/active_directory.md "../../../chime/latest/ag/active_directory.md").
- Amazon Connect - For more information, see [How Amazon Connect works](../../../connect/latest/adminguide/what-is-amazon-connect.md#amazon-connect-fundamentals "../../../connect/latest/adminguide/what-is-amazon-connect.md#amazon-connect-fundamentals").
- Amazon EC2 for Windows or Linux – You can use the seamless Active Directory domain join feature of Amazon EC2
  Windows or Linux to join your instance to your self-managed Active Directory (on-premises).
  Once joined, the instance communicates directly with your Active Directory and bypasses
  AD Connector. For more information, see [Ways to join an Amazon EC2 instance to your Active Directory](ad_connector_join_instance.md "ad_connector_join_instance.md").
- AWS Management Console – You can use AD Connector to authenticate AWS Management Console users with their Active
  Directory credentials without setting up SAML infrastructure. For more information, see
  [Enabling AWS Management Console access with AWS Managed Microsoft AD
  credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md").
- Quick Suite - For more information, see [Managing user
  accounts in Quick Suite Enterprise Edition](../../../quicksight/latest/user/managing-users-enterprise.md "../../../quicksight/latest/user/managing-users-enterprise.md").
- AWS IAM Identity Center - For detailed instructions, see [Connect IAM Identity Center to an
  on-premises Active Directory](../../../singlesignon/latest/userguide/connectawsad.md "../../../singlesignon/latest/userguide/connectawsad.md").
- AWS Transfer Family - For detailed instructions, see [Working with Directory Service for Microsoft Active Directory](../../../transfer/latest/userguide/directory-services-users.md "../../../transfer/latest/userguide/directory-services-users.md").
- AWS Client VPN - For detailed instructions, see [Client
  authentication and authorization](../../../vpn/latest/clientvpn-admin/authentication-authorization.md "../../../vpn/latest/clientvpn-admin/authentication-authorization.md").
- WorkDocs - For detailed instructions, see [Connecting to your on-premises directory with AD Connector](../../../workdocs/latest/adminguide/connect_directory_connector.md "../../../workdocs/latest/adminguide/connect_directory_connector.md").
- Amazon WorkMail - For detailed instructions, see [Integrate Amazon WorkMail
  with an existing directory (standard setup)](../../../workmail/latest/adminguide/premises_directory.md "../../../workmail/latest/adminguide/premises_directory.md").
- WorkSpaces - For detailed instructions, see [Launch a WorkSpace using AD Connector](../../../workspaces/latest/adminguide/launch-workspace-ad-connector.md "../../../workspaces/latest/adminguide/launch-workspace-ad-connector.md").

###### Note

Amazon RDS is compatible with AWS Managed Microsoft AD only, and is not compatible with AD Connector. For
more information, see the AWS Managed Microsoft AD section in the [Directory Service FAQs](https://aws.amazon.com/directoryservice/faqs/#microsoft-ad "https://aws.amazon.com/directoryservice/faqs/#microsoft-ad") page.
