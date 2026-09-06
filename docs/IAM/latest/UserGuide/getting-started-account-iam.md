

# Setting up your AWS account
<a name="getting-started-account-iam"></a>

Before you start working with IAM, make sure you have completed the initial set up of your AWS environment.

AWS sends you a confirmation email after the sign-up process is complete. At any time, you can view your current account activity and manage your account by going to [https://aws.amazon.com/](https://aws.amazon.com/) and choosing **My Account**.

When you signed up for the service, you created an AWS account using an email address and a password. Those are your AWS root user credentials. As a best practice, you don't use your root user credentials to access AWS for daily tasks. Only use your root user credentials to perform [tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html). Also, do not share your credentials with anyone else. Instead, add people to your directory and give them access to your AWS account.

**To secure your AWS account root user**

1.  Sign in to the [AWS Management Console](https://console.aws.amazon.com/) as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

   For help signing in by using root user, see [Signing in as the root user](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial) in the *AWS Sign-In User Guide*.

1. Turn on multi-factor authentication (MFA) for your root user.

   For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html) in the *IAM User Guide*.

**Grant access to the billing console**

IAM users and roles in an AWS account can't access the Billing and Cost Management console by default. This is true even if they have IAM policies that grant access to certain Billing features. To grant access, the AWS account root user must first activate IAM access.
**Note**  
As a security best practice, we recommend that you provide access to your resources through identity federation with [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). When you enable IAM Identity Center in conjunction with AWS Organizations, the Billing and Cost Management console is enabled by default with consolidated billing for all AWS accounts in your organization. For more information, see [Consolidating billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) in the *Billing and Cost Management User Guide*.

1. Sign in to the AWS Management Console with your root user credentials (specifically, the email address and password that you used to create your AWS account).

1. On the navigation bar, select your account name, and then select [Account](https://console.aws.amazon.com/billing/home#/account).

1. Scroll down the page until you find the section **IAM User and Role Access to Billing Information**, then select **Edit**.

1. Select the **Activate IAM Access** check box to activate access to the Billing and Cost Management console pages.

1. Choose **Update**.

    The page displays the message **IAM user/role access to billing information is activated**.
**Important**  
Activating IAM access alone doesn't grant any permissions for users or roles to view the Billing and Cost Management console pages. You must also attach the required identity-based policies to IAM roles to grant access to the billing console. Roles provide temporary credentials that users can assume when needed.

1. Use the AWS Management Console to [create a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) that a user can assume to access the billing console.

1. On the **Add permissions** page for the role, add permissions to list and view details about the Billing resources in your AWS account.

   The AWS managed policy [Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/managed-policies.html#security-iam-awsmanpol-Billing) grants users permission to view and edit the Billing and Cost Management console. This includes viewing account usage, modifying budgets and payment methods. For more policy examples that you can attach to IAM roles to control access to your account’s billing information, see [AWS Billing policy examples](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html) in the *Billing and Cost Management User Guide*.