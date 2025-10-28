# Create an AWS account

These instructions are for creating an AWS account outside of India. For creating an
account in India, see [Create an AWS account with AWS India](managing-accounts-india.md#create-india-account "managing-accounts-india.md#create-india-account"). For creating an account that's part of an organization
managed by AWS Organizations, see [Creating a member account in an
organization](../../../organizations/latest/userguide/orgs_manage_accounts_create.md "../../../organizations/latest/userguide/orgs_manage_accounts_create.md") in the _AWS Organizations User Guide_.

AWS Management Console

###### To create an AWS account

1. Open the [Sign up for AWS](https://signin.aws.amazon.com/signup?request_type=register "https://signin.aws.amazon.com/signup?request_type=register") page.
2. Enter the root user email address and AWS account name, and then choose
   **Verify email address**. This will send a
   verification code to your specified email address.

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

5. Choose **Business** or **Personal**.
   Personal accounts and business accounts have the same features and
   functions.
6. Enter your company or personal information.

###### Important

For business AWS accounts, it's a best practice to enter a
company phone number rather than a number for a personal phone.
Configuring the account's root user with an individual email address or
a personal phone number can make your account insecure. 7. Read and accept the [AWS Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/"). Be sure that you read and
understand the terms of the AWS Customer Agreement. 8. Choose **Continue**. At this point, you'll receive an
email message to confirm that your AWS account is ready to use. You
can sign in to your new account by using the email address and password
you provided during sign up. However, you can't use any AWS services
until you finish activating your account. 9. Enter the information about your payment method, and then choose
**Verify and Continue**. If you want to use a
different billing address for your AWS billing information, choose
**Use a new address**.

You can't proceed with the sign-up process until you add a valid
payment method. 10. Enter your country or region code from the list, and then enter a
phone number where you can be reached in the next few minutes. 11. Enter the code displayed in the CAPTCHA, and then submit. 12. When the automated system contacts you, enter the PIN you receive and
then submit. 13. Select one of the available AWS Support plans. For a description of the
available Support plans and their benefits, see [Compare Support
plans](https://aws.amazon.com/premiumsupport/features "https://aws.amazon.com/premiumsupport/features"). 14. Choose **Complete sign up**. A confirmation page
appears that indicates that your account is being activated. 15. Check your email and spam folder for an email message that confirms
your account was activated. Activation usually takes a few minutes but
can sometimes take up to 24 hours. 16. After you receive the activation message, you can sign-in to the
[AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") to start using AWS services. For general information
about how to manage your account settings, see [Configure your AWS account](managing-accounts.md "managing-accounts.md").

AWS CLI & SDKs
You can create member accounts in an organization that is managed by AWS Organizations
by running the [CreateAccount](../../../organizations/latest/APIReference/API_CreateAccount.md "../../../organizations/latest/APIReference/API_CreateAccount.md") operation
while signed in to the organization's management account.

You can't create a standalone AWS account outside of an organization by
using an AWS Command Line Interface (AWS CLI) or AWS API operation.
