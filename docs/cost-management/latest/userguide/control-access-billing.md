# Overview of managing access permissions

## Granting access to your billing information and

tools

The AWS account owner can access billing information and tools by signing in to
the AWS Management Console using the account credentials. We recommend that you don't use the
account credentials for everyday access to the account, and especially that you
don't share account credentials with others to give them access to your
account.

For your daily administrative tasks, create an administrative user to securely
control access to AWS resources. By default, users don't have access to the [AWS Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/"). As an administrator,
you can create roles under your AWS account that your users can assume. After you
create roles, you can attach your IAM policy to them, based on the access needed.
For example, you can grant some users limited access to some of your billing
information and tools, and grant others complete access to all of the information
and tools.

###### Note

IAM is a feature of your AWS account. If you are already signed up for a
product that is integrated with IAM, you don't need to do anything else to sign
up for IAM, nor will you be charged for using it.

Permissions for Cost Explorer apply to all accounts and member accounts,
regardless of IAM policies. For more information about Cost Explorer access,
see [Controlling access to Cost Explorer](ce-access.md "ce-access.md").

## Activating access to the Billing and Cost Management

console

IAM roles within an AWS account can't access the Billing and Cost Management console pages by
default. This is true even if the role has IAM policies that grant access to
certain Billing and Cost Management features. The AWS account administrator can allow roles access to
Billing and Cost Management console pages by using the **Activate IAM Access**
setting.

On the AWS Cost Management console, the **Activate IAM Access** setting
controls access to the following pages:

- Home
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

For a list of pages the **Activate IAM Access** setting
controls for the Billing console, see [Activating access to the Billing console](../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate "../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate") in the _Billing
User Guide_.

###### Important

Activating IAM access alone doesn't grant roles the necessary permissions
for these Billing and Cost Management console pages. In addition to activating IAM access, you must
also attach the required IAM policies to those roles. For more information,
see [Using identity-based policies (IAM policies) for AWS Cost Management](billing-permissions-ref.md "billing-permissions-ref.md").

The **Activate IAM Access** setting doesn't control access to
the following pages and resources:

- The console pages for AWS Cost Anomaly Detection, Savings Plans overview, Savings Plans inventory, Purchase Savings Plans, and Savings Plans cart
- The Cost Management view in the AWS Console Mobile Application
- The Billing and Cost Management SDK APIs (AWS Cost Explorer, AWS Budgets, and AWS Cost and Usage Reports APIs)
- AWS Systems Manager Application Manager
- The in-console AWS Pricing Calculator
- The cost analysis capability in Amazon Q
- The AWS Activate Console

By default, the **Activate IAM Access** setting is deactivated.
To activate this setting, you must log in to your AWS account using the root user
credentials, and then select the setting in the **Account** page.
Activate this setting in each account where you want to allow IAM role access to
the Billing and Cost Management console pages. If you use AWS Organizations, then activate this setting in each
management or member account where you want to allow IAM role access to the
console pages.

###### Note

The **Activate IAM Access** setting isn't available to
users with administrator access. This setting is available only to the root user
of the account.

If the **Activate IAM Access** setting is deactivated, then
IAM roles in the account can't access the Billing and Cost Management console pages. This is true even if
they have administrator access or the required IAM policies.

###### To activate IAM user and role access to the Billing and Cost Management console

1. Sign in to the AWS Management Console with your root account credentials
   (specifically, the email address and password that you used to create your
   AWS account).
2. On the navigation bar, choose your account name, and then choose [Account](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account").
3. Next to **IAM User and Role Access to Billing
   Information**, choose **Edit**.
4. Select the **Activate IAM Access** check box to activate
   access to the Billing and Cost Management console pages.
5. Choose **Update**.

After you activate IAM access, you must also attach the required IAM policies
to the IAM roles. The IAM policies can grant or deny access to specific Billing and Cost Management
features. For more information, see [Using identity-based policies (IAM policies) for AWS Cost Management](billing-permissions-ref.md "billing-permissions-ref.md").
