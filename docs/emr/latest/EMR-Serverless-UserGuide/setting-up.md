# Prerequisites for getting started with EMR Serverless

This section describes the administrative prerequisites
for running EMR Serverless. These include account configuration and permissions management.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Grant permissions](#setting-up-iam "#setting-up-iam")
- [Install and configure the AWS CLI](#setting-up-cli "#setting-up-cli")
- [Open the console](#opening-console "#opening-console")

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

## Grant permissions

In production environments, we suggest that you use finer-grained policies. For
examples of such policies, refer to [User access policy examples for
EMR Serverless](security-iam-user-access-policies.md "security-iam-user-access-policies.md"). To learn more about access
management, refer to [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the IAM User Guide.

For users who need to get started with EMR Serverless in a sandbox environment, use a policy similar to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRStudioCreate",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreateStudioPresignedUrl",
 "elasticmapreduce:DescribeStudio",
 "elasticmapreduce:CreateStudio",
 "elasticmapreduce:ListStudios"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "EMRServerlessFullAccess",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowEC2ENICreationWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "ops.emr-serverless.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowEMRServerlessServiceLinkedRoleCreation",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/*"
 ]
 }
 ]
}`

```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Grant programmatic access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Install and configure the AWS CLI

If you want to use EMR Serverless APIs, install the latest version of the
AWS Command Line Interface (AWS CLI). You don't need the AWS CLI to use EMR Serverless from the
EMR Studio console, and get started without the CLI by following the steps
in [Getting started with EMR Serverless from the console](gs-console.md "gs-console.md").

###### To set up the AWS CLI

1. To install the latest version of the AWS CLI for macOS, Linux, or Windows, refer to
   [Installing or
   updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. To configure the AWS CLI and secure setup of your access to AWS services,
   including EMR Serverless, refer to [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config").
3. To verify the setup, enter the following DataBrew command at the command
   prompt.

```
aws emr-serverless help
```

AWS CLI commands use the default AWS Region from your configuration, unless
you set it with a parameter or a profile. To set your AWS Region with a
parameter, add the `--region` parameter to each
command.

To set your AWS Region with a profile, first add a named profile in the
`~/.aws/config` file or the
`%UserProfile%/.aws/config` file (for Microsoft Windows). Follow
the steps in [Named profiles for
the AWS CLI](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md"). Next, set your AWS Region and other settings with a
command similar to the one in the following example.

```
[profile emr-serverless]
aws_access_key_id = ACCESS-KEY-ID-OF-IAM-USER
aws_secret_access_key = SECRET-ACCESS-KEY-ID-OF-IAM-USER
region = us-east-1
output = text
```

## Open the console

Most of the console-oriented topics in this section start from the [Amazon EMR console](https://console.aws.amazon.com/elasticmapreduce/home "https://console.aws.amazon.com/elasticmapreduce/home"). If you aren't
already signed in to your AWS account, sign in, then open the [Amazon EMR console](https://console.aws.amazon.com/elasticmapreduce/home "https://console.aws.amazon.com/elasticmapreduce/home") and continue to the next section
to continue getting started with Amazon EMR.
