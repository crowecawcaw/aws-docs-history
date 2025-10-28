# When to sign in as a root user

Certain administrative tasks require that you must sign in as a root user. You can sign in
as a root user to an AWS account that was created by account factory in AWS Control Tower.

###### You must sign in as a root user to perform the following actions:

- Change certain account settings, including the account name, root user password, or email
  address. For more information, see [Update and move accounts with AWS Control Tower](updating-account-factory-accounts.md "updating-account-factory-accounts.md").
- To [close an AWS account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md").
- For more information about actions that require root user login credentials, see [Tasks that require root user credentials](../../../accounts/latest/reference/root-user-tasks.md "../../../accounts/latest/reference/root-user-tasks.md") in the _AWS Account Management Reference Guide_.

###### Note

To change or enable your [AWS Support
plan, you must be signed in as the root user _or_ be a
user with the appropriate IAM permissions.](troubleshooting.md#getting-support "troubleshooting.md#getting-support") .

###### To sign in as root user

1. Open the AWS sign-in page.

If you don't have the email address of the AWS account to which you require access, you
can get it from AWS Control Tower. Open the console for the management account,
choose **Accounts**, and look for the email address. 2. Enter the email address of the AWS account to which you require access, and then
choose **Next**. 3. Choose **Forgot password?** to have password reset instructions sent to
the root user email address. 4. Open the password reset email message from the root user mailbox, then follow the
instructions to reset your password. 5. Open the AWS sign-in page, then sign in with your reset password.
Alternatively, you can use the AWS Root Access Management feature, which allows root actions to be performed on member accounts, without needing to sign in as Root. For more information, see [Centrally managing root access for customers using AWS Organizations](https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/ "https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/").
