

# Sign in to the AWS Management Console as the root user
<a name="introduction-to-root-user-sign-in-tutorial"></a>

When you first create an AWS account, you begin with one sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account *root user* and is accessed by signing in with the email address and password that you used to create the account.

**Important**  
We strongly recommend that you don't use the root user for your everyday tasks. Safeguard your root user credentials and use them to perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*.

This sign-in method is only supported for accounts created with Sign up for AWS (advanced). For more information, see [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html).

## To sign in as the root user
<a name="root-user-sign-in-tutorial"></a>

You can sign in as the root user while you are already signed in to another identity in the AWS Management Console. For details, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) in the *AWS Management Console Getting Started Guide*.

AWS accounts managed using AWS Organizations may not have root user credentials, and you must contact an administrator to perform root user actions in your member account. If you can't sign in as the root user, see [Troubleshooting AWS account sign-in issues](troubleshooting-sign-in-issues.md).

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).
**Note**  
If you signed in previously as an **IAM user** using this browser, your browser might display the IAM user sign-in page instead. Choose **Sign in using root user email**.

1. Choose **Root user**.   


1. Under **Root user email address**, enter the email address associated with your root user. Then, select **Next**.

1. If you’re prompted to complete a security check, enter the characters presented to you to continue. If you can't complete the security check, try listening to the audio or refreshing the security check for a new set of characters.
**Tip**  
Type the alphanumeric characters you see (or hear) in order without spaces.  


1. Enter your password.  


1. Authenticate with MFA. MFA is enforced by default on the root user. For root users of standalone and member accounts, you must manually enable MFA, which is strongly recommended. For more information, see [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) in the *AWS Identity and Access Management User Guide*.
**Tip**  
As a security best practice, we recommend removing all root user credentials from member accounts in your AWS organization to help prevent unauthorized use. If you choose this option, member accounts can't sign in as the root user, perform password recovery, or set up MFA. In this case, only the management account administrator can perform a task that requires root user credentials in a member account. For details, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management) in the *AWS Identity and Access Management User Guide*.

1. Choose **Sign in**. The AWS Management Console appears.

After authentication the AWS Management Console opens to the Console Home page.

## To sign in as the root user using our new AWS experience
<a name="root-user-sign-in-new-experience"></a>

If you signed up for AWS using our new AWS experience, you can sign in to the AWS Management Console as the root user of your management account.

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

1. Choose our new AWS experience.

1. Choose the **IAM user** icon.

1. Choose **Sign in using root user email**.

1. Under **Root user email address**, enter the email address associated with your root user. Then, select **Next**.

1. If you're prompted to complete a security check, enter the characters presented to you to continue. If you can't complete the security check, try listening to the audio or refreshing the security check for a new set of characters.
**Tip**  
Type the alphanumeric characters you see (or hear) in order without spaces.  


1. Enter your password.  


1. Authenticate with MFA. MFA is enforced by default on the root user. For root users of standalone and member accounts, you must manually enable MFA, which is strongly recommended. For more information, see [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) in the *AWS Identity and Access Management User Guide*.
**Tip**  
As a security best practice, we recommend removing all root user credentials from member accounts in your AWS organization to help prevent unauthorized use. If you choose this option, member accounts can't sign in as the root user, perform password recovery, or set up MFA. In this case, only the management account administrator can perform a task that requires root user credentials in a member account. For details, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management) in the *AWS Identity and Access Management User Guide*.

1. Choose **Sign in**. The AWS Management Console appears.

## Additional information
<a name="root-user-sign-in-tutorial-more-info"></a>

If you want more information about the AWS account root user, refer to the following resources.
+ For an overview of the root user, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html).
+ For details about using the root user, see [Using the AWS account root user](https://docs.aws.amazon.com/accounts/latest/reference/root-user.html).
+ For step-by-step directions on how to reset your root user password, see [I forgot my root user password for my AWS account](troubleshooting-sign-in-issues.md#troubleshoot-forgot-root-password).