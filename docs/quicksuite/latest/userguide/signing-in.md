# Signing in to Amazon Quick Suite

You can sign in to Amazon Quick Suite multiple ways, depending on what your Quick Suite
administrator has set up. You can sign in to Quick Suite using AWS root, AWS Identity and Access Management
(IAM), corporate Active Directory, or your native Quick Suite credentials. If your
Quick Suite account is integrated with an identity provider such as Okta, the
following procedures don't apply to you.

If you're a Quick Suite administrator, make sure to allow-list the following domains
within your organization's network.

| User type                                                                    | Domain or domains to allow-list          |
| ---------------------------------------------------------------------------- | ---------------------------------------- |
| Users who sign in directly through Quick Suite and Active<br>Directory users | `signin.aws` and `awsapps.com`           |
| AWS root user                                                                | `signin.aws.amazon.com` and `amazon.com` |
| IAM users                                                                    | `signin.aws.amazon.com`                  |

###### Important

We strongly recommend that you don't use the AWS root user for your everyday tasks,
even the administrative ones. Instead, adhere to the best practice of using the root
user only to create your first IAM user. Then securely lock away the root user
credentials and use them to perform only a few account and service management tasks. For
more information, see [AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") in the
_IAM User Guide_.

## How to sign in to Quick Suite

Use the following procedure to sign in to Quick Suite.

###### To sign in to Quick Suite

1. Go to [https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. For **Quick Suite account name**, enter your account
   name. This is the name that was created when the Quick Suite account was
   created in AWS.

If you were invited to the Quick Suite account by email, you can find
the account name inside of that email. If you don't have the email that invited
you to Quick Suite, ask the Quick Suite administrator in your
organization for the information that you need.

You can also find your Quick Suite account name by selecting the profile
icon at the upper-right of the Quick Suite console menu. In some cases,
you might not have access to your Quick Suite account or have an
administrator who can provide this information, or both. If so, contact AWS
Support and open a ticket that includes your AWS customer ID. 3. For **Username**, enter your Quick Suite user name.
User names that contain a semicolon (;) aren't supported. Choose one of the
following:

    * For organizational users – The user name is provided by your
     administrator.


    Your account can be based on IAM credentials or your email address
     if it's a root email address. Or it can be used as the user name to
     invite you into the Quick Suite account. If you received an
     invitation email from another Quick Suite user, it indicates what
     type of credentials to use.
    * For individual users – The user name that you created for
     yourself.


    This is usually the IAM credentials that you created.

The remaining steps vary depending on the user type you sign in as (directly through
Quick Suite or as an Active Directory user, AWS root user, or IAM user). For
more information, see the following sections.

### Finishing Quick Suite sign-in as a

Quick Suite or Active Directory user

If you're signing in directly through Quick Suite or are using your
corporate Active Directory credentials, you're redirected to `signin.aws`
after you enter your account name and user name. Use the following procedure to
finish signing in.

###### To finish signing in to Quick Suite if you sign in directly through

Quick Suite or use Active Directory credentials

1. For **Password**, enter your password.

Passwords are case-sensitive and must be 8–64 characters in length.
They must also contain each of the following:

    * Lowercase letters (a–z)
    * Uppercase letters (A–Z)
    * Numbers (0–9)
    * Nonalphanumeric characters
     (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

2. If your account is multi-factor authentication enabled, enter the
   multi-factor authentication code that you receive for **MFA
   code**.
3. Choose **Sign in**.

### Finishing Quick Suite sign-in as an AWS

root user

If you're signing in as an AWS root user, you're redirected to
signin.aws.amazon.com (or amazon.com) to complete the sign-in process. Your user
name is prefilled. Use the following procedure to finish signing in.

###### To finish signing in as an AWS root user

1. Choose **Next**.
2. For **password**, enter your password. For more
   information about root user passwords, see [Changing the AWS account root user password](../../../IAM/latest/UserGuide/id_credentials_passwords_change-root.md "../../../IAM/latest/UserGuide/id_credentials_passwords_change-root.md") in the
   _IAM User Guide_.
3. Choose **Sign in**.

### Finishing Quick Suite sign-in as an IAM

user

If you're signing in as an IAM user, you're redirected to signin.aws.amazon.com
(or amazon.com) to complete the sign-in process. Your user name is prefilled. Use
the following procedure to finish signing in.

###### To finish signing in as an IAM user

1. For **Password**, enter your password. For more
   information about IAM user passwords, see [Default password policy](../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md#default-policy-details "../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md#default-policy-details") in the
   _IAM User Guide_.
2. Choose **Sign in**.

If your sign-in process happens automatically and you need to use a different account, use
a private or incognito browser window. Doing this prevents the browser from reusing cached
settings.
