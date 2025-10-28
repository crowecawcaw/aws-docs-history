# Change the password for the AWS account root user

You can change the email address and password from either the [Security Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") or the
**Account** page. You can also choose **Forgot password?**
on the AWS sign-in page to reset your password.

To change the root user's password, you must sign in as the AWS account root user and not as an IAM
user. To learn how to reset a _forgotten_ root user password,
see [Reset a lost or forgotten root user password](reset-root-password.md "reset-root-password.md").

To protect your password, it's important to follow these best practices:

- Change your password periodically.
- Keep your password private because anyone who knows your password can access your
  account.
- Use a different password on AWS than you use on other sites.
- Avoid passwords that are easy to guess. These include passwords such as
  `secret`, `password`, `amazon`, or `123456`.
  Also avoid things like dictionary words, your name, email address, or other personal
  information that someone can easily obtain.

###### Important

AWS accounts managed using AWS Organizations may have [centralized root access](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") enabled for member
accounts. These member accounts do not have root user credentials, can't sign in as a root user,
and are prevented from recovering the root user password. Contact your administrator if you
need to perform a task that requires root user credentials.

AWS Management Console

###### To change the password for the root user

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- You must sign in as the AWS account root user, which requires no additional
  AWS Identity and Access Management (IAM) permissions. You can't perform these steps as an IAM user or
  role.

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and sign in using your root user credentials.

For instructions, see [Sign
in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_. 2. In the upper right corner of the console, choose your account name or number,
and then select **Security Credentials**. 3. On the **Account** page, next to **Account
settings**, choose **Edit**. You are prompted to
re-authenticate for security purposes.

###### Note

If you don't see the **Edit** option, it is likely that you
are not signed in as the root user for your account. You can't modify account
settings while signed in as an IAM user or role. 4. On the **Update account settings** page, under
**Password**, choose **Edit**. 5. On the **Update your password** page, fill out the fields for
**Current password**, **New password**, and
**Confirm new password**.

###### Important

Make sure to choose a strong password. Although you can set an account
password policy for IAM users, that policy doesn't apply to the root user.

AWS requires that your password meet the following conditions:

    * It must have a minimum of 8 characters and a maximum of 128
     characters.
    * It must include a minimum of three of the following mix of character types:
     uppercase, lowercase, numbers, and ! @ # $ % ^ & \* () <> [] {} | \_+-=
     symbols.
    * It must not be identical to your AWS account name or email address.

6. Choose **Save changes**.

AWS CLI or AWS SDK
This task isn't supported in the AWS CLI or by an API operation from one of the
AWS SDKs. You can perform this task only by using the AWS Management Console.
