# Enable IAM Identity Center

When you enable IAM Identity Center you choose an AWS IAM Identity Center instance type to enable. An instance of a
service is a single deployment of a service within your AWS environment. There are two types
of instances available for IAM Identity Center: organization instances and account instances. The instance
types available for you to enable depend upon the account type you are signed into.

The following list identifies the type of IAM Identity Center instances you can enable for each type of AWS account:

- Your AWS Organizations management account (recommended) –
  Required to create an [organization
  instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center. Use an organization instance for multi-account permissions and
  application assignments across the organization. You can replicate this instance type to
  additional Regions for enhanced resiliency of account access and flexibility in the choice of AWS application deployment Regions.
- Your AWS Organizations member account – Use to create an
  [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center to
  enable application assignments within that member account. One or more accounts with a
  member level instance can exist in an organization.
- A standalone AWS account – Use to create an
  [organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") or
  [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center. The
  standalone AWS account isn't managed by AWS Organizations. You can associate only one instance of
  IAM Identity Center with a standalone AWS account and use that instance for application assignments
  within that standalone AWS account.

###### Important

The organization management account can control whether [organization member
accounts can create account instances of IAM Identity Center](control-account-instance.md "control-account-instance.md") by using a Service Control
Policy.

For a comparison of the different capabilities provided by the different instance types, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

Before enabling IAM Identity Center, we recommend you review the [IAM Identity Center prerequisites and
considerations](identity-center-prerequisites.md "identity-center-prerequisites.md").

## To enable an instance of IAM Identity Center

Choose the tab for the type of IAM Identity Center instance you want to enable, either an organization
or account instance:

Organization (recommended)

1. Do one of the following to sign in to the AWS Management Console.
   - **New to AWS (root user)**
     – Sign in as the account owner by choosing **Root
     user** and entering your AWS account email
     address. On the next page, enter your password.
   - **Already using AWS with a standalone
     AWS account (IAM credentials)** – Sign
     in using your IAM credentials with administrative
     permissions.
   - **Already using AWS Organizations (IAM
     credentials)** – Sign in using your
     management account credentials.

2. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. (Optional) If you want to use a customer managed KMS key for encryption at rest rather than the default AWS managed key, configure the customer managed key in the **Key for encrypting IAM Identity Center data at rest** section. For more information, refer to [Implementing customer managed KMS
   keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md "identity-center-customer-managed-keys.md").

###### Important

Perform this step only if you've configured the necessary permissions for use of the KMS customer managed key. Without proper permissions, this step may fail or disrupt IAM Identity Center administration and AWS managed applications. 4. Under **Enable IAM Identity Center**, choose
**Enable**. 5. On the **Enable IAM Identity Center with AWS Organizations** page, review the
information and then select **Enable** to complete the
process.

###### Note

AWS Organizations can have IAM Identity Center enabled only in a single AWS Region.
After enabling IAM Identity Center, if you need to change the Region that IAM Identity Center is
enabled in, you must [delete](delete-config.md "delete-config.md") the
current instance and create an instance in the other Region.

After enabling your organization instance we recommend that you do the
following steps to finish setting up your environment:

- Confirm that you are using the identity source of your choice. If you
  already have an assigned identity source, you can continue to use it.
  For more information, see [Confirm your identity sources in IAM Identity Center](confirm-identity-source.md "confirm-identity-source.md").
- Register a member account as a delegated administrator. For more
  information, see [Delegated administration](delegated-admin.md "delegated-admin.md").
- IAM Identity Center provides you an access portal to AWS resources. If you filter
  access to specific AWS domains or URL endpoints by using a web content
  filtering solution such as next-generation firewalls (NGFW) or Secure
  Web Gateways (SWG), see [Update firewalls and gateways to
  allow access to the AWS access portal](enable-identity-center-portal-access.md "enable-identity-center-portal-access.md").

Account

1. Do one of the following to sign in to the AWS Management Console.
   - **New to AWS (root user)**
     – Sign in as the account owner by choosing **Root
     user** and entering your AWS account email
     address. On the next page, enter your password.
   - **Already using AWS (IAM
     credentials)** – Sign in using your IAM
     credentials with administrative permissions.
   - **Already using AWS Organizations (IAM
     credentials)** – Sign in using your member
     account administrative credentials.

2. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. If you are new to AWS or have a standalone AWS account, under
   **Enable IAM Identity Center**, choose
   **Enable**.

You see the **Enable IAM Identity Center with AWS Organizations** page. We
recommend this option, but it is not required.

Select the link **enable an account instance of
IAM Identity Center**. 4. If you are an administrator of an AWS Organizations member account, under
**Enable an account instance of IAM Identity Center**, select
**Enable an account instance**. 5. On the **Enable an account instance of IAM Identity Center** page,
review the information and _optionally_ add tags that
you want to associate with this account instance. Then select
**Enable** to complete the process.

###### Note

If your AWS account is a member of an organization, there might
be restrictions on your ability to enable an account instance of
IAM Identity Center.

    * If your organization enabled IAM Identity Center before November 15, 2023
     the ability for member accounts to create account instances is
     disabled by default and must be enabled by the management account of
     the organization.
    * If your organization enabled IAM Identity Center after November
     15, 2023 the ability for member account to create account instances
     is enabled by default. However, service control policies can be used
     to prevent the creation of account instances of IAM Identity Center within an
     organization.For more information, see [Permit account instance creation in member

accounts](enable-account-instance-console.md "enable-account-instance-console.md") and [Use Service Control Policies to control account instance creation](control-account-instance.md "control-account-instance.md").
