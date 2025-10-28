# Step 2: Set Up Root and Administrative

Users

When you sign up for an AWS account, an AWS account root user is created. The root
user has access to all AWS services and resources in the account. As a security best
practice, [assign administrative access to an administrative user](../../../singlesignon/latest/userguide/useraccess.md "../../../singlesignon/latest/userguide/useraccess.md") and use the root
user only to perform [tasks
that require root user access](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md").

## Secure Your AWS Account Root

User

1. To sign in as the administrative user in the IAM Identity Center, use the
   sign-in URL that was sent to your email address when you created the IAM
   Identity Center user. For help signing in using an IAM Identity Center user,
   see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

For help signing in using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS
Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user
(console)](../../../IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.md#enable-virt-mfa-for-root "../../../IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.md#enable-virt-mfa-for-root") in the _IAM User
Guide_.

## Create an Administrative

User

You should create an administrative user so that you do not use the root user for
everyday tasks.

- For your daily administrative tasks, assign administrative access to an
  administrative user in AWS IAM Identity Center (successor to AWS Single
  Sign-On). For instructions, see [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity
  Center (successor to AWS Single Sign-On) User Guide_.
- To sign in as the administrative user in the IAM Identity Center, use the
  sign-in URL that was sent to your email address when you created the IAM
  Identity Center user. For help signing in using an IAM Identity Center user,
  see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.
