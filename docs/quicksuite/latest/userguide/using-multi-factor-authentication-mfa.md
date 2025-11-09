# Using multi-factor authentication

(MFA) with Amazon Quick Suite

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

###### Important

Amazon Quick Suite recommends that you integrate new Quick Suite subscriptions with
IAM Identity Center for identity management. This IAM identity federation user guide is provided as
a reference for existing account configurations. For more information on integrating
your Quick Suite account with IAM Identity Center, see [Configure your Quick Suite account with
IAM Identity Center](../../../quicksight/latest/user/sec-identity-management-identity-center.md "../../../quicksight/latest/user/sec-identity-management-identity-center.md").

###### Note

IAM identity federation doesn't support syncing identity provider groups with
Amazon Quick Suite.

There are several ways that you can use multi-factor authentication (MFA) with
Quick Suite. You can use it with AWS Identity and Access Management (IAM). You can use it with AD Connector
or your [AWS Directory
Service](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/") for Microsoft Active Directory, also known as AWS
Microsoft Active Directory or AWS Managed Microsoft Active Directory. And if
you use an external identity provider (IdP), AWS doesn't need to have any
information about MFA because that is part of the authentication handled by the IdP.

For more information, see the following:

- [Using multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
  IAM User Guide
- [Enable Multi-Factor Authentication for AWS Managed Microsoft
  AD](../../../directoryservice/latest/admin-guide/mfa_ad.md "../../../directoryservice/latest/admin-guide/mfa_ad.md") in the AWS Directory Service Administration Guide
- [Enable Multi-Factor Authentication for AD Connector](../../../directoryservice/latest/admin-guide/ad_connector_mfa.md "../../../directoryservice/latest/admin-guide/ad_connector_mfa.md") in the
  AWS Directory Service Administration Guide
  If you're a developer, see the following:

- [How do I use an MFA token to authenticate access to my AWS
  resources through the AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/ "https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/") in the [AWS Knowledge
  Center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/")
- [Configuring MFA-protected API access](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the IAM User Guide
