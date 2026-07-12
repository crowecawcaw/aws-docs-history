# Using IAM Identity Center

|                                                                |
| -------------------------------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition and Standard Edition |

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

Amazon Quick Enterprise edition integrates with your existing directories, using either
Microsoft Active Directory or single sign-on (IAM Identity Center) using Security Assertion Markup
Language (SAML). You can use AWS Identity and Access Management (IAM) to further enhance your security, or for
custom options such as embedding dashboards.

In Quick Standard edition, you can manage users entirely within
Quick. If you prefer, you can integrate with your existing users, groups, and
roles in IAM.

You can use the following tools for identity and access to Amazon Quick:

- [IAM Identity Center](../../../quicksight/latest/user/sec-identity-management-identity-center.md "../../../quicksight/latest/user/sec-identity-management-identity-center.md") (Enterprise edition only)
- [IAM federation](../../../quicksuite/latest/userguide/iam-federation.md "../../../quicksuite/latest/userguide/iam-federation.md") (Standard and Enterprise editions)
- [AWS Directory Service for Microsoft Active Directory](../../../quicksight/latest/user/aws-directory-service.md "../../../quicksight/latest/user/aws-directory-service.md") (Enterprise edition only)
- [SAML-based single sign-on](../../../quicksight/latest/user/external-identity-providers.md "../../../quicksight/latest/user/external-identity-providers.md") (Standard and Enterprise
  edition)
- [Multifactor authentication (MFA)](../../../quicksight/latest/user/using-multi-factor-authentication-mfa.md "../../../quicksight/latest/user/using-multi-factor-authentication-mfa.md") (Standard and
  Enterprise edition)

###### Note

In the regions listed below, Amazon Quick accounts can only use [IAM Identity Center](../../../quicksight/latest/user/sec-identity-management-identity-center.md "../../../quicksight/latest/user/sec-identity-management-identity-center.md") for identity and access management.

- `af-south-1` Africa (Cape Town)
- `ap-southeast-3` Asia Pacific (Jakarta)
- `ap-southeast-5` Asia Pacific (Malaysia)
- `eu-south-1` Europe (Milan)
- `eu-south-2` Europe (Spain)
- `eu-central-2` Europe (Zurich)
- `il-central-1` Israel (Tel Aviv)
- `me-central-1` Middle East (UAE)
  IAM Identity Center helps you securely create or connect your workforce identities and manage their
  access across AWS accounts and applications.

Before you integrate your Amazon Quick account with IAM Identity Center, set up IAM Identity Center in your AWS
account. If you haven't set up IAM Identity Center in your AWS organization, see [Getting
started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity Center User Guide_.

If you want to configure an external identity provider with IAM Identity Center, see [Supported
identity providers](../../../singlesignon/latest/userguide/supported-idps.md "../../../singlesignon/latest/userguide/supported-idps.md") to view a list of supported identity providers'
configuration steps.

###### Topics

- [Configure your Amazon Quick account with IAM Identity Center](#sec-identity-management-identity-center "#sec-identity-management-identity-center")

## Configure your Amazon Quick account with IAM Identity Center

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

IAM Identity Center helps you securely create or configure your existing workforce identities and
manage their access across AWS accounts and applications. IAM Identity Center is the recommended
approach for workforce authentication and authorization on AWS for organizations of
any size and type. To learn more about IAM Identity Center, see [AWS IAM Identity Center](https://aws.amazon.com//iam/identity-center/ "https://aws.amazon.com//iam/identity-center/").

Configure Amazon Quick and IAM Identity Center so that you can sign up for a new Amazon Quick
account with an IAM Identity Center configured identity source. With IAM Identity Center, you can configure your
external identity provider as an identity source. You can also use IAM Identity Center as an identity
store if you don't want to use a third-party identity provider with Amazon Quick.
Identity methods can't be changed after your account is created.

When you integrate your Amazon Quick account with IAM Identity Center, Amazon Quick account
administrators can create a new Amazon Quick account that automatically has the identity
provider's groups available. This simplifies asset sharing at scale in
Amazon Quick.

Access to some sections of the Amazon Quick administration console is restricted by
IAM permissions. The following table summarizes the admin actions that you can perform
in Amazon Quick based on the access type that you choose.

To learn more how to sign up for an Amazon Quick account with IAM Identity Center, see [Signing up for an
Amazon Quick subscription](../../../quicksight/latest/user/signing-up.md "../../../quicksight/latest/user/signing-up.md").

The following table lists admin actions and whether they require IAM
permissions.

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

### Considerations

###### Irreversible actions

The following actions permanently prevent all users from signing in to
your Amazon Quick account. You cannot undo these actions.

- Disabling or deleting the Amazon Quick application in the IAM Identity Center console.
  If you want to delete your Amazon Quick account, see [Closing your Amazon Quick account](../../../quicksight/latest/user/closing-account.md "../../../quicksight/latest/user/closing-account.md").
- Migrating the Amazon Quick account that contains your IAM Identity Center configuration
  to an AWS Organization that does not contain the IAM Identity Center instance that your
  Amazon Quick account is configured to.
- Deleting the IAM Identity Center instance that is configured to your Amazon Quick
  account.
- Editing IAM Identity Center application attributes, for example the **requires
  assignment** attribute.
