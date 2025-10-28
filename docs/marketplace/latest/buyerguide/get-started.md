# Getting started

To get started, enable Private Marketplace by creating a service-linked role and enabling trusted access in AWS Organizations. You can perform this action only from the management account of your organization using a role or user with AWS Identity and Access Management (IAM) permissions in the [AWSPrivateMarketplaceAdminFullAccess](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess") managed policy. This policy has all permissions required to enable, configure, and manage Private Marketplace.

## Enabling Private Marketplace

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Settings**.
3. Choose **Edit integrations** in Private Marketplace settings.
4. Choose **Enable trusted access across your organization**.
5. Choose **Create a Private Marketplace service-linked role for this account**.
6. Choose **Create integration**.

You can't undo this integration from the AWS Marketplace console. Use the IAM console to delete the service-linked role, or the Organizations console to disable trusted access.

###### Note

You can also enable Private Marketplace by visiting the **Get started** page under **Private Marketplace** in the navigation pane in the AWS Marketplace console.

## Registering a delegated

administrator

After enabling Private Marketplace in your organization, you can register a trusted account as a delegated administrator. This reduces the work for the management account administrator by letting the delegated administrator account create and manage Private Marketplace experiences in your organization. Additionally, Organizations gives a delegated administrator account read-only access to view organization structure, memberships, and policies. For more information, see [Delegated administrator for AWS services that work with Organizations](../../../organizations/latest/userguide/orgs_integrate_delegated_admin.md "../../../organizations/latest/userguide/orgs_integrate_delegated_admin.md").

###### To register a delegated administrator

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Settings**.
3. Choose **Register new administrator** in Private Marketplace settings.
4. Enter the AWS account ID that you want to register as a delegated administrator. The account must be a member of your organization.
5. Choose **Create a Private Marketplace service-linked role for this account**.
6. Choose **Register**.

You can remove the delegated administrator at any time and register a different account, if needed.
