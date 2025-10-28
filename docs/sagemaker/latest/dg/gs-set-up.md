# Complete Amazon SageMaker AI prerequisites

Before you can set up Amazon SageMaker AI, you must complete the following prerequisites.

- **Required**: You will need to create an Amazon Web Services
  (AWS) account to get access to all of the AWS services and resources for the
  account.
- **Highly recommended**: We highly recommend that you
  create an administrative user to manage AWS resources for the account, to adhere
  to the [Security best practices in
  IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"). It is assumed that you have an administrative user for many of
  the administrative tasks throughout the SageMaker AI developer guide.
- **Optional**: Configure the AWS Command Line Interface (AWS CLI) if you
  intend to manage your AWS services and resources for the account using the
  AWS CLI.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [(Optional) Configure the AWS CLI](#gs-cli-prereq "#gs-cli-prereq")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

When you create an administrative user to set up SageMaker AI, the administrative user should
include specific permissions to create SageMaker AI resources. To view the permissions, expand the
following administrator permissions section.

When you create your administrative user using the preceding instructions, your
administrative user should already include the permissions contained in the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy, as well as the following permissions.
These policies are needed to create a SageMaker AI domain among other tasks.

If you intend to create your own custom policy, these permissions are required to
create a domain and get set up with SageMaker AI. For information about adding policies,
see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:domain/*",
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:app/*",
 "arn:aws:sagemaker:*:*:flow-definition/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "servicecatalog:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

**Optional**: If you intend to manage your AWS services and
resources for the account using the AWS CLI, proceed to the following instructions ([(Optional) Configure the AWS CLI](#gs-cli-prereq "#gs-cli-prereq")).

**After you have completed your prerequisites**, continue on
to the setup instructions. You can continue on to your setup instructions by choosing one of
the following options.

- **[Use quick setup](onboard-quick-start.md "onboard-quick-start.md")**: Fastest setup for
  individual users with default settings.
- **[Use custom setup](onboard-custom.md "onboard-custom.md")**: Advanced setup for
  enterprise Machine Learning (ML) administrators. Ideal option for ML administrators
  setting up SageMaker AI for many users or an organization.

## (Optional) Configure the AWS CLI

To manage your domain and other AWS services and resources using the AWS CLI,
complete the setup in [Set up the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in
the _AWS Command Line Interface User Guide for Version 2_.

**After you have completed your prerequisites**, continue
on to the setup instructions. You can continue on to your setup instructions by choosing
one of the following options.

- **[Use quick setup](onboard-quick-start.md "onboard-quick-start.md")**: Fastest setup
  for individual users with default settings.
- **[Use custom setup](onboard-custom.md "onboard-custom.md")**: Advanced setup for
  enterprise Machine Learning (ML) administrators. Ideal option for ML
  administrators setting up SageMaker AI for many users or an organization.
