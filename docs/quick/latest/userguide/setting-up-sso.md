# Using IAM Identity Center

|                                                                |
| -------------------------------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition and Standard Edition |

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

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

To learn more how to sign up for an Amazon Quick account with IAM Identity Center, see [Signing up for an
Amazon Quick subscription](../../../quicksight/latest/user/signing-up.md "../../../quicksight/latest/user/signing-up.md").

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
