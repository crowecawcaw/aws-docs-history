# Setting up for Amazon Q Business

Before you begin using Amazon Q Business for the first time, complete the following
tasks.

###### Topics

- [Initial AWS account setup](#initial-account-setup "#initial-account-setup")
- [(Optional) Install the AWS CLI](#cli-install-setup "#cli-install-setup")
- [(Optional) Set up the AWS SDKs](#service-sdk-setup "#service-sdk-setup")
- [Consider AWS Regions and endpoints](#service-endpoints "#service-endpoints")
- [Set up required permissions](#permissions "#permissions")

## Initial AWS account setup

### Sign up for an AWS account

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

### Create a user with administrative access

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

## (Optional) Install the AWS CLI

The AWS Command Line Interface (AWS CLI) is a unified developer tool for managing
AWS services, including Amazon Q Business.

1. To install the AWS CLI, follow the instructions in [Installing the AWS Command Line
   Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the _AWS Command Line
   Interface User Guide_.
2. To configure the AWS CLI and set up a profile to call the AWS CLI, follow the instructions in [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command
   Line Interface User Guide_.
3. To confirm that the AWS CLI profile is configured, run the following
   command:

```
aws configure ––profile default
```

If your profile has been configured correctly, you will see output similar to the
following:

```
AWS Access Key ID [****************52FQ]:
AWS Secret Access Key [****************xgyZ]:
Default region name [us-west-2]:
Default output format [json]:
```

4. To verify that the AWS CLI is configured for use with Amazon Q Business, run the following commands:

```
aws qbusiness help
```

If the AWS CLI is configured correctly, you will see a list of the
supported AWS CLI commands for Amazon Q Business, Amazon Q Business
runtime, and Amazon Q Business events.

## (Optional) Set up the AWS SDKs

Download and install the AWS SDKs that you want to use. This guide provides
examples for Python. For information about other AWS SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

The package for the Python SDK is called
_Boto3_.

Before you run the following Python commands, you must first download and
install [Python 3.6 or
later](https://www.python.org/downloads/ "https://www.python.org/downloads/") for your operating system. Support for Python 3.5 and earlier
is deprecated.

If you don't have pip included in your Python Scripts
directory, you can download [get-pip.py](https://bootstrap.pypa.io/get-pip.py "https://bootstrap.pypa.io/get-pip.py") and store this in your Scripts directory. You can also set your
Python directory as a [Path or environment
variable](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH "https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH") using a terminal program.

To install Python, complete the following steps:

```
# Install the latest Boto3 release via pip
pip install boto3

# You can install a specific version of Boto3 for compatibility reasons
# Install Boto3 version 1.0 specifically
pip install boto3==1.0.0

# Make sure Boto3 is no older than version 1.15.0
pip install boto3>=1.15.0

# Avoid versions of Boto3 newer than version 1.15.3
pip install boto3<=1.15.3
```

To use Boto3, you must set up authentication credentials for your
AWS account using the [IAM
console](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey").

## Consider AWS Regions and endpoints

An _endpoint_ is a URL that's the entry point for a web
service. Each endpoint is associated with a specific AWS Region.

If you use a combination of the Amazon Q Business console, the AWS CLI,
and the Amazon Q Business SDKs, pay attention to their default Regions. All Amazon Q Business components of a given application must be created in the same Region.
Examples of a component include a retriever, an index, and a chat experience. To understand
why this is important, see [Considerations for choosing an AWS Region](../../../singlesignon/latest/userguide/get-started-prereqs-considerations.md "../../../singlesignon/latest/userguide/get-started-prereqs-considerations.md") in the IAM Identity Center User
Guide.

For regions and endpoints supported by Amazon Q Business, see [Service quotas
for Amazon Q Business](quotas-regions.md "quotas-regions.md").

## Set up required permissions

If you use Amazon Q Business through the AWS Management Console, basic required permissions are
added on your behalf.

To use Amazon Q Business as an IAM user on the AWS CLI, or AWS SDK, you must
attach the following permissions to allow Amazon Q Business to create and manage
resources on your behalf:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessFullAccessPermissions",
 "Effect": "Allow",
 "Action": "qbusiness:*",
 "Resource": "*"
 }
 ]
}`

```

If you're using Q Apps, add the following permissions:

```
"qapps:*"
```

If you're using Q Apps, add the following permissions:

```
"quicksight:*"
```

If you're using a customer managed key, add the following permissions:

```
"kms:DescribeKey"
"kms:CreateGrant"
```

If you're using IAM Identity Center, add the following permissions:

```
"sso:CreateApplication",
"sso:PutApplicationAuthenticationMethod",
"sso:PutApplicationAccessScope",
"sso:PutApplicationGrant",
"sso:DeleteApplication",
"organizations:DescribeOrganization",
"sso-directory:DescribeGroup",
"sso-directory:DescribeUser",
"sso:DescribeApplication",
"sso:DescribeInstance"
```

To assign user subscriptions to applications, you must include permissions to call the
necessary user subscription-related APIs. The subscription-related APIs give permission to
create, update, cancel, and view all user subscriptions for an application. You can assign
user subscriptions through both the Amazon Q Business console and programmatically using
the AWS CLI or AWS SDKs.

**To allow Amazon Q to assign user subscriptions, use the following
role policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessSubscriptionPermissions",
 "Effect": "Allow",
 "Action": [
 "qbusiness:UpdateSubscription",
 "qbusiness:CreateSubscription",
 "qbusiness:CancelSubscription",
 "qbusiness:ListSubscriptions"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/subscription/`subscription-id`"
 ]
 },
 {
 "Sid": "QBusinessServicePermissions",
 "Effect": "Allow",
 "Action": [
 "user-subscriptions:UpdateClaim",
 "user-subscriptions:CreateClaim",
 "organizations:DescribeOrganization",
 "iam:CreateServiceLinkedRole",
 "sso-directory:DescribeGroup",
 "sso-directory:DescribeUser",
 "sso:DescribeApplication",
 "sso:DescribeInstance"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Grant permission to create data sources

with ACLs disabled

By default, when Amazon Q administrators create data sources, ACLs are on.
Some administrators may want to create data sources with ACLs disabled. You can grant them
permission by attaching the IAM action `DisableAclOnDataSource` to their role
or policy. With this permission, the administrator can create data sources with the ACL
field disabled. If an administrator creates a data source with the ACL field set to enabled,
they can't change the field to disabled. If they want to use a data source with ACLs
disabled, they need to create a new data source.

We don't recommend disabling ACLs in production environments.

###### Warning

When ACLs are disabled for a data source, all documents ingested by the data source
become accessible to all end users of the Amazon Q Business application.

You can check if data source connectors were created with ACLs disabled and whether
Amazon Q administrators have the `DisableAclOnDataSource` IAM
policy. To check ACLs on a data source, review `CreateDataSource` and
`UpdateDataSource` event logs in CloudTrail. To check if administrators have been
granted the `DisableAclOnDataSource`IAM action, review permissions in the IAM
console.

As a best practice, we recommend you use an explicit deny on the
`DisableAclOnDataSource`IAM action and that you only grant the
`DisableAclOnDataSource` permission when requested by Amazon Q
administrators.

###### Note

This feature is only available for use with the following connectors:
ServiceNow Online, Confluence, SharePoint,
Jira, Google Drive, OneDrive,
Salesforce, Zendesk, GitHub, MS
Teams, and Slack.

###### Example An example policy using `qbusiness:DisableAclOnDataSource`

The following is an example policy showing how to use
`qbusiness:DisableAclOnDataSource`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExplicitDenyACLDisable",
 "Effect": "Deny",
 "Action": [
 "qbusiness:DisableAclOnDataSource"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

For a complete list of IAM roles for Amazon Q Business, see [IAM
roles for Amazon Q Business](iam-roles.md "iam-roles.md").
