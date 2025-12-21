# Overview of managing access permissions

## Granting access to your billing information and

tools

By default, IAM users don't have access to the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/").

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

As an administrator, you can create roles under your AWS account that your users can assume. After you
create roles, you can attach your IAM policy to them, based on the access needed.
For example, you can grant some users limited access to some of your billing
information and tools, and grant others complete access to all of the information
and tools.

To grant IAM entities access to the Billing and Cost Management console,
complete the following:

- [Activate IAM
  Access](#ControllingAccessWebsite-Activate "#ControllingAccessWebsite-Activate") as the AWS account root user. You only need to complete this
  action once for your account.
- Create your IAM identities, such as a user, group, or role.
- Use an AWS managed policy or create a customer managed policy that
  grants permission to specific actions on the Billing and Cost Management console. For more
  information, see [Using identity-based policies for Billing](security_iam_id-based-policy-examples.md#billing-permissions-ref "security_iam_id-based-policy-examples.md#billing-permissions-ref").

For more information, see the [IAM tutorial: Grant access to the Billing console](../../../IAM/latest/UserGuide/tutorial_billing.md "../../../IAM/latest/UserGuide/tutorial_billing.md") in the
_IAM User Guide_.

###### Note

Permissions for Cost Explorer apply to all accounts and member accounts,
regardless of the IAM policies. For more information, see [Controlling access to AWS Cost Explorer](../../../cost-management/latest/userguide/ce-access.md "../../../cost-management/latest/userguide/ce-access.md").

## Activating access to the

Billing and Cost Management console

IAM users and roles in an AWS account can't access the Billing and Cost Management
console by default. This is true even if they have IAM policies that grant access to certain
Billing features. To grant access, the AWS account root user can use the
**Activate IAM Access** setting.

If you use AWS Organizations, activate this setting in each
management or member account where you want to allow IAM user and role access to
the Billing and Cost Management console. For created member accounts this option will be enabled by default.
For more information, see [Activating IAM access to
the AWS Billing and Cost Management console](billing-getting-started.md#activating-iam-access-to-billing-console "billing-getting-started.md#activating-iam-access-to-billing-console").

On the Billing console, the **Activate IAM Access** setting
controls access to the following pages:

- Home
- Budgets
- Budgets Reports
- AWS Cost and Usage Reports
- Cost categories
- Cost allocation tags
- Bills
- Payments
- Credits
- Purchase Order
- Billing preferences
- Payment methods
- Tax settings
- Cost Explorer
- Reports
- Rightsizing recommendations
- Savings Plans recommendations
- Savings Plans utilization report
- Savings Plans coverage report
- Reservations overview
- Reservations recommendations
- Reservations utilization report
- Reservations coverage report
- Preferences

###### Important

Activating IAM access alone doesn't grant roles the necessary permissions for these Billing and Cost Management
console pages. In addition to activating IAM access, you must also attach the
required IAM policies to those roles. For more information, see [Using identity-based policies for Billing](security_iam_id-based-policy-examples.md#billing-permissions-ref "security_iam_id-based-policy-examples.md#billing-permissions-ref").

The **Activate IAM Access** setting doesn't control access to
the following pages and resources:

- The console pages for AWS Cost Anomaly Detection, Savings Plans overview, Savings Plans inventory, Purchase Savings Plans, and Savings Plans cart
- The Cost Management view in the AWS Console Mobile Application
- The Billing and Cost Management SDK APIs (AWS Cost Explorer, AWS Budgets, and AWS Cost and Usage Reports APIs)
- AWS Systems Manager Application Manager
- The in-console AWS Pricing Calculator
- The cost analysis capability in Amazon Q
- The AWS Activate Console
