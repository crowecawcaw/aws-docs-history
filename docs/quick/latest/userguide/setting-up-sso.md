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
any size and type. To learn more about IAM Identity Center, see [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/").

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

### Set up Amazon Quick with IAM Identity Center multi-Region

You can create an Amazon Quick Enterprise subscription in a supported AWS Region
that is configured as an additional Region for your IAM Identity Center instance. When you call
`CreateAccountSubscription` against a target Region endpoint, that Region
becomes the capacity Region for your Quick default namespace.

This procedure applies only to the IAM Identity Center authentication method. It does not create
a second Quick subscription or replicate an existing one. Each
AWS account supports one Quick account subscription.

#### Region concepts

The following Region types are relevant to this procedure:

- **IAM Identity Center primary Region** – The
  Region where your IAM Identity Center instance was originally created.
- **IAM Identity Center additional Region** – A
  Region to which your IAM Identity Center instance is replicated and active.
- **Quick capacity Region**
  – The Region where your Quick default namespace is
  provisioned. This is determined by the endpoint Region
  where you call `CreateAccountSubscription`.

#### Prerequisites

For detailed instructions, see [Multi-Region IAM Identity Center](../../../singlesignon/latest/userguide/multi-region-iam-identity-center.md "../../../singlesignon/latest/userguide/multi-region-iam-identity-center.md") and [Replicate to an additional Region](../../../singlesignon/latest/userguide/replicate-to-additional-region.md "../../../singlesignon/latest/userguide/replicate-to-additional-region.md") in the
_AWS IAM Identity Center User Guide_.

Before you create your Quick subscription in an additional Region,
complete the following steps in the order shown:

1. Configure a multi-Region customer managed KMS key for your IAM Identity Center
   instance in the primary Region.
2. Create a replica of the customer managed KMS key in the target
   Region.
3. Add the target Region to IAM Identity Center and wait until the Region status is
   `ACTIVE`.
4. If your organization uses an external identity provider, add the target
   Region's Assertion Consumer Service (ACS) URL to your identity
   provider configuration. For more information, see [Multi-Region workforce access](../../../singlesignon/latest/userguide/multi-region-workforce-access.md "../../../singlesignon/latest/userguide/multi-region-workforce-access.md") in the
   _AWS IAM Identity Center User Guide_.
5. Confirm that the target Region is a supported Quick signup
   Region. For a list of supported Regions, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs "regions.md#regions-qs").

#### To create a subscription in an additional Region

Use the AWS Command Line Interface or an AWS SDK to create an Amazon Quick Enterprise
subscription in the target Region.

###### To create the subscription (AWS CLI)

1. Configure the AWS CLI to use the target Region. The configured Region
   determines the `CreateAccountSubscription` endpoint.
2. Run the following command. Replace the placeholder values with your
   own.

```
aws quicksight create-account-subscription \
    --aws-account-id <ACCOUNT_ID> \
    --account-name "<ACCOUNT_NAME>" \
    --notification-email <EMAIL> \
    --edition ENTERPRISE \
    --authentication-method IAM_IDENTITY_CENTER \
    --iam-identity-center-instance-arn <IDC_INSTANCE_ARN> \
    --admin-group "<ADMIN_GROUP_NAME>" \
    --region <TARGET_REGION>
```

The following list describes the required and recommended
parameters:

    * `--aws-account-id` – Your 12-digit
     AWS account ID.
    * `--account-name` – A name for the
     Quick account.
    * `--notification-email` – The email address
     for service notifications.
    * `--edition ENTERPRISE` – IAM Identity Center
     authentication requires Enterprise edition.
    * `--authentication-method IAM_IDENTITY_CENTER`
     – Specifies IAM Identity Center as the authentication method.
    * `--iam-identity-center-instance-arn` – The
     ARN of your IAM Identity Center instance.
    * `--admin-group` or
     `--admin-pro-group` – The name of the IAM Identity Center
     group to assign as Quick administrators.
    * `--region` – The target Region for the
     Quick capacity Region. This must be an active IAM Identity Center
     additional Region and a supported Quick signup
     Region.

#### Verify the subscription

After the command completes, confirm that the subscription exists and is
active.

###### To verify the subscription (AWS CLI)

1. Run the following command to check the account status:

```
aws quicksight describe-account-subscription \
    --aws-account-id <ACCOUNT_ID> \
    --region <TARGET_REGION>
```

Confirm that `AccountSubscriptionStatus` is
`ACCOUNT_CREATED`. 2. Run the following command to verify the namespace and capacity
Region:

```
aws quicksight list-namespaces \
    --aws-account-id <ACCOUNT_ID> \
    --region <TARGET_REGION>
```

Confirm that `CreationStatus` is `CREATED` and
that `CapacityRegion` matches the target Region.

#### Considerations

Review the following considerations:

- You must use Amazon Quick Enterprise edition for IAM Identity Center
  authentication.
- You must specify either `--admin-group` or
  `--admin-pro-group` when you use IAM Identity Center
  authentication.
- You must choose a target Region that is both an active IAM Identity Center
  additional Region and a supported Quick signup Region.
- You can create only one Quick account subscription for each
  AWS account. If your account already has a subscription,
  `CreateAccountSubscription` returns a resource-exists
  error.
- You cannot change the authentication method after the
  Quick account is created.

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
