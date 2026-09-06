

# Security best practices for AWS account administrators
<a name="best-practices-admin"></a>

If you’re an account administrator who has created a new AWS account using [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html), we recommend the following steps to help your users follow AWS security best practices when they sign in. 

1. Sign in as the root user to [ Enable multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa) and [ create an AWS administrative user](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in IAM Identity Center if you haven't already done so. Then, [ safeguard your root credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials) and don't use them for everyday tasks.

1. Sign in as the AWS account administrator and set up the following identities:
   + Create [ least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) users for other [ humans](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp).
   + Set up [ temporary credentials for workloads](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles).
   + Create access keys only for [use cases that require long-term credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials).

1. Add permissions to grant access to those identities. You can [ get started with AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies) and move towards [least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
   + [ Add permission sets to AWS IAM Identity Center (successor to AWS Single Sign-On) users](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html).
   + [ Add identity-based policies to IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) used for workloads.
   + [ Add identity-based polices for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) for use cases that require long-term credentials.
   + For more information about IAM users, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

1.  Save and share information about [Sign in to the AWS Management Console](how-to-sign-in.md). This information varies, depending on the type of identity you created.

1. Keep your root user email address and primary account contact phone number up to date to ensure that you can receive important account and security-related notifications.
   + [Modify the account name email address, or password for the AWS account root user](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html).
   + [Access or update the primary account contact](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html).

1. Review [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) to learn about additional identity and access management best practices.