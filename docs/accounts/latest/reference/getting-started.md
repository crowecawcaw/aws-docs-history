# Sign up for AWS (advanced)

If you're new to AWS, the first step is to sign up for an AWS account. When you
follow the information for Sign up for AWS (advanced), AWS creates an account where you
have complete control over account configuration and where your content is stored.
Use this option if you have regulated workloads such as HIPAA, FedRAMP.

To compare this sign up with Sign up for AWS (new), see [Compare sign-up options](sign-up-for-aws.md "sign-up-for-aws.md").

To sign up for an AWS account, you'll need to provide the following information:

- **Root user email
  address** – The email address is used as the sign-in
  name for the [root user](root-user.md "root-user.md") and is required for account
  recovery. You must be able to receive email messages that are sent to this address.
  Before you can perform certain tasks, you must verify that you have access to email
  sent to this address.
- **AWS account name** – The name of the
  account appears in several places, such as on your invoice, and in consoles such as
  the Billing and Cost Management dashboard and the AWS Organizations console. We recommend that you use a standard
  way to name your accounts so that you can give your accounts names that are easy to
  recognize. For company accounts, consider using a naming standard such as _organization_-_purpose_-_environment_ (for example,
  _AnyCompany_-_audit_-_prod_). For personal
  accounts, consider using a naming standard such as _first
  name_-_last name_-_purpose_ (for example, _paulo-santos-testaccount_).
- **Address** – If your contact and billing
  address is in India, the user agreement for your account is with Amazon Web Services India Private Limited (AWS India), a
  local AWS seller in India. You must provide your CVV as part of the verification
  process. You might also have to enter a one-time password, depending on your bank.
  AWS India charges your payment method 2 INR as part of the verification process.
  AWS India refunds the 2 INR after verification is complete.
- **Phone number** – This number is used for
  identity verification purposes and to confirm the ownership of your account. You must
  be able to receive calls and SMS messages at this phone number.

###### Important

If this account is for a business, use a corporate phone number so that your
company can retain access to the AWS account even when an employee changes
positions or leaves the company.

## Step 1: Create your account

These instructions are for creating an AWS account outside of India. For creating an
account in India, see [Create an AWS account with AWS India](managing-accounts-india.md#create-india-account "managing-accounts-india.md#create-india-account"). For creating an account that's part of an organization
managed by AWS Organizations, see [Creating a member account in an
organization](../../../organizations/latest/userguide/orgs_manage_accounts_create.md "../../../organizations/latest/userguide/orgs_manage_accounts_create.md") in the _AWS Organizations User Guide_.

AWS Management Console

###### To create an AWS account

1. Open the [Sign up for AWS](https://signin.aws.amazon.com/signup?request_type=register "https://signin.aws.amazon.com/signup?request_type=register") page.
2. Enter the root user email address and AWS account name, and then choose
   **Verify email address**. This sends a
   verification code to your email address.

###### Important

If this account is for a business, use a secure corporate
distribution list (for example, `it.admins@example.com`)
so that your company can retain access to the AWS account even
when an employee changes positions or leaves the company. Because
the email address can be used to reset the account's root user
credentials, protect access to this distribution list or
address. 3. Enter your verification code, and then choose
**Verify**. 4. Enter a strong password for your root user, confirm it, and then choose
**Continue**. AWS requires that your password
meet the following conditions:

    * It must have a minimum of 8 characters and a maximum of 128
     characters.
    * It must include a minimum of three of the following mix of
     character types: uppercase, lowercase, numbers, and ! @ # $ % ^
     & \* () <> [] {} | \_+-= symbols.
    * It must not be identical to your AWS account name or email
     address.

5. Choose your account plan. For more information, see [Free
Tier plans](../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md "../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md"). 6. Enter your contact information, then read and accept the [AWS Customer
Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/"). Make sure you understand the terms before
accepting.

###### Important

If this account is for a business, it's a best practice to enter a
company phone number rather than a number for a personal phone.
Configuring the account's root user with an individual email address or
a personal phone number can make your account insecure. 7. Enter your billing information. If you want to use a different
billing address for your AWS billing information, choose
**Use a new address**.

You can't proceed with the sign-up process until you add a valid
payment method. 8. You might need to confirm your identity:

    1. For **Country or region code**, enter a phone number that can
     be reached in the next few minutes.
    2. For **Phone number**, enter a phone number that can be reached in the next few minutes.
    3. Choose **Send SMS**.
    4. When the automated system contacts you, enter the code you
     receive and then choose
     **Continue**.

9. Choose one of the available AWS Support plans. For a description of the
available Support plans and their benefits, see [Compare Support
plans](https://aws.amazon.com/premiumsupport/features "https://aws.amazon.com/premiumsupport/features"). 10. Choose **Complete sign up**. A confirmation page
appears that indicates that your account is being activated. 11. Check your email and spam folder for an email message that confirms
your account was activated. Activation usually takes a few minutes but
can sometimes take up to 24 hours. 12. After you receive the activation message, you can sign-in to the
[AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") to start using AWS services. For general information
about how to manage your account settings, see [Configure your AWS account](managing-accounts.md "managing-accounts.md").

For multiple AWS accounts managed through AWS Organizations, assign administrative
access to an administrative user in IAM Identity Center. For instructions, see [Set up AWS account access for an IAM Identity Center administrative user](../../../singlesignon/latest/userguide/get-started-assign-account-access-admin-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-admin-user.md") in
the _IAM Identity Center User Guide_.

AWS CLI & SDKs
You can create member accounts in an organization that is managed by AWS Organizations
by running the [CreateAccount](../../../organizations/latest/APIReference/API_CreateAccount.md "../../../organizations/latest/APIReference/API_CreateAccount.md") operation
while signed in to the organization's management account.

You can't create a standalone AWS account outside of an organization by
using an AWS Command Line Interface (AWS CLI) or AWS API operation.

## Step 2: (Recommended) Install the AWS CLI

Install the AWS CLI by following the instructions at [Installing the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). You need version 2.32.0 or later.

You can use the AWS CLI to have an agent manage AWS resources on your behalf.

After you install the AWS CLI, use the following command to sign in
programmatically:

```
aws login
```

This automatically rotates your credentials every 15 minutes, keeping your session
valid for up to 12 hours without manual intervention.

Use the following command to verify your credentials are working:

```
aws sts get-caller-identity
```

For more information about accessing your AWS account, see [Accessing your AWS account](accounts-access-account.md "accounts-access-account.md").

## Step 3: (Recommended) Set up the AWS MCP Server

The AWS MCP Server is a managed server that gives agents access to AWS through the
Model Context Protocol (MCP). Agents can search AWS documentation and retrieve service
information without authentication. To execute AWS API calls, run Python scripts in a
sandboxed environment, or follow curated skills, agents authenticate through your
existing IAM credentials. For more information, see [What is the AWS
Agent Toolkit?](../../../agent-toolkit/latest/userguide/what-is-agent-toolkit.md "../../../agent-toolkit/latest/userguide/what-is-agent-toolkit.md")

After you complete the sign-up process, see the following topics:

- [Related AWS services](accounts-related-services.md "accounts-related-services.md")
- [Using the AWS account root user](root-user.md "root-user.md")
- [Accessing your AWS account](accounts-access-account.md "accounts-access-account.md")
- [Plan your AWS account governance structure](plan-acct-structure.md "plan-acct-structure.md")
- [Configure your AWS account](managing-accounts.md "managing-accounts.md")
- [Troubleshoot your AWS account](troubleshooting.md "troubleshooting.md")
- [Manage accounts in India](managing-accounts-india.md "managing-accounts-india.md")
- [Close an AWS account](manage-acct-closing.md "manage-acct-closing.md")
