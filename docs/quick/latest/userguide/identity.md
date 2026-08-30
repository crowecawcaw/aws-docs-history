# Identity and access management in Quick

|                                                                |
| -------------------------------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition and Standard Edition |

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

The following topics describe how to set up identity and access for
Quick.

- [Using IAM Identity Center](setting-up-sso.md "setting-up-sso.md")
- [IAM federation](iam-federation.md "iam-federation.md")
- [Using Active Directory with Amazon Quick Enterprise edition](aws-directory-service.md "aws-directory-service.md")
- [Setting up IdP federation using IAM and Amazon Quick](external-identity-providers-setting-up-saml.md "external-identity-providers-setting-up-saml.md")
- [Using multi-factor authentication (MFA) with Amazon Quick](using-multi-factor-authentication-mfa.md "using-multi-factor-authentication-mfa.md")

###### Note

In the following AWS Regions, Amazon Quick accounts can only use [IAM Identity Center](setting-up-sso.md "setting-up-sso.md") for identity and access management:

- `af-south-1` Africa (Cape Town)
- `ap-southeast-3` Asia Pacific (Jakarta)
- `ap-southeast-5` Asia Pacific (Malaysia)
- `eu-south-1` Europe (Milan)
- `eu-south-2` Europe (Spain)
- `eu-central-2` Europe (Zurich)
- `il-central-1` Israel (Tel Aviv)
- `me-central-1` Middle East (UAE)
  The following sections help you configure the identity management method of your
  choice for Quick.

IAM permissions control access to some sections of the Amazon Quick
administration console. The following table lists admin actions and whether they
require IAM permissions.

| Admin action                         | IAM permissions required |
| ------------------------------------ | ------------------------ |
| **Account settings**                 | Yes                      |
| **Manage assets**                    | Yes                      |
| **Amazon Q**                         | Yes                      |
| **Manage subscriptions**             | No                       |
| **SPICE capacity**                   | No                       |
| **Index capacity**                   | Yes                      |
| **Manage users (view)**              | No                       |
| **Manage users > Role groups**       | Yes                      |
| **Manage domains**                   | No                       |
| **Mobile settings**                  | No                       |
| **Manage IP/VPC restrictions**       | Yes                      |
| **Manage VPC connections**           | Yes                      |
| **Manage OAuth client applications** | Yes                      |
| **KMS keys**                         | Yes                      |
| **AWS resources**                    | Yes                      |
| **Default access policy**            | Yes                      |
| **IAM policy assignments**           | Yes                      |
| **AWS actions**                      | Yes                      |
| **Extension access**                 | Yes                      |
| **Custom permissions**               | Yes                      |
| **Configure SageMaker**              | Yes                      |
| **Brand customization**              | Yes                      |
| **Agent customization**              | Yes                      |
| **Email customization**              | Yes                      |
| **Quick Usage Metrics**              | Yes                      |

If you have the Amazon Quick admin role, you can perform actions that do not
require IAM permissions. To perform actions that require IAM permissions, sign in to
the AWS Management Console as an IAM principal with the appropriate
`quicksight:*` permissions. You can also perform some admin actions
programmatically through the Amazon Quick API. For a list of available API operations,
see the [Amazon Quick API Reference](../../../quicksight/latest/APIReference/Welcome.md "../../../quicksight/latest/APIReference/Welcome.md").

###### Topics

- [Using IAM](iam.md "iam.md")
- [Using IAM Identity Center](setting-up-sso.md "setting-up-sso.md")
- [IAM federation](iam-federation.md "iam-federation.md")
- [Using Active Directory with Amazon Quick Enterprise edition](aws-directory-service.md "aws-directory-service.md")
- [Using multi-factor authentication (MFA) with Amazon Quick](using-multi-factor-authentication-mfa.md "using-multi-factor-authentication-mfa.md")
