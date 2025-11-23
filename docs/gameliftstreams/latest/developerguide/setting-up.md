# Setting up Amazon GameLift Streams as a developer

To start using the Amazon GameLift Streams service with your projects, complete these basic setup
tasks. If you already have an AWS account and a user under that account that you want to use
with Amazon GameLift Streams, you can skip to [Download the Web SDK](#setting-up-materials "#setting-up-materials").

For more information on what you can do with an AWS account, see [Getting started with AWS](https://aws.amazon.com//getting-started/ "https://aws.amazon.com//getting-started/").

After you've completed these setup tasks, we recommend that you go to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md") and
step through the tutorial, which covers the entire workflow for getting your content streaming in a web client.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Get programmatic access](#setting-up-access-keys "#setting-up-access-keys")
- [Download the Amazon GameLift Streams Web SDK](#setting-up-materials "#setting-up-materials")
- [Download the AWS CLI](#setting-up-prereqs "#setting-up-prereqs")
- [Set up billing alerts](#setting-up-billing "#setting-up-billing")

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

## Get programmatic access

In addition to your user sign-in credentials for the AWS Management Console, you need credentials for
programmatic access, such as when working with the AWS Command Line Interface (AWS CLI). Programmatic
credentials consist of a two-part set of access keys. Use one of the following methods
to generate your access keys:

- Method 1 – If you're using an administrative user created with the IAM Identity Center,
  see [Getting IAM role credentials for AWS CLI access](../../../singlesignon/latest/userguide/howtogetcredentials.md "../../../singlesignon/latest/userguide/howtogetcredentials.md") to generate temporary security credentials
  for short-term access to AWS resources. When following these instructions, make sure you're
  signed in through your account's AWS access portal URL with your administrative user name and
  password (not your root user).
- Method 2 – If you're using an existing IAM user and you haven't yet transitioned to
  using the IAM Identity Center, see [Managing access keys for IAM users (console)](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey") to generate long-term
  credentials for your user.

###### Note

As a best practice, use temporary credentials instead of long-term access keys.
Temporary credentials include an access key ID, a secret access key, and a security
token that indicates when the credentials expire. For more information, see [Best practices for managing AWS access keys](../../../general/latest/gr/aws-access-keys-best-practices.md "../../../general/latest/gr/aws-access-keys-best-practices.md") in the
_AWS General Reference_.

## Download the Amazon GameLift Streams Web SDK

You can get started without any additional materials by using the in-console streaming experience. We recommend this as a starting
point because it allows you to evaluate how your application performs on the Amazon GameLift Streams without setting up any additional infrastructure. For
more information, proceed to [Getting started with Amazon GameLift Streams](getting-started.md "getting-started.md").

When you're ready to build your own Amazon GameLift Streams integration, download the Amazon GameLift Streams Web SDK, available in the Resources section of the
[Getting Started product page](https://aws.amazon.com/gamelift/streams/getting-started/ "https://aws.amazon.com/gamelift/streams/getting-started/"). Amazon GameLift Streams is built to be integrated into your web applications. You will need to integrate our
JavaScript-based Web SDK to setup streaming from your website or browser-based applications. The download also contains a sample web
server that uses the Amazon GameLift Streams service, and a sample web client for connecting to streams.

For more information about setting up your own Amazon GameLift Streams solution, refer to [Amazon GameLift Streams backend service and web client](sdk.md "sdk.md").

## Download the AWS CLI

To use Amazon GameLift Streams with your content, we recommend that you get the AWS Command Line Interface (AWS CLI). The AWS CLI is an open source tool that gives you
equivalent AWS SDK functionality by running commands from a terminal program.

1. Download and install the latest version of the AWS CLI for your operating system. See these [install instructions](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
   _AWS Command Line Interface User Guide_.
2. Configure the tool with your user access credentials and other preferences, as described in [Setting up the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md"). With this configuration, you won't have to
   explicitly specify your credentials and other settings with every command.
3. Use the following command to verify your installation and get a list of available Amazon GameLift Streams commands:

```
aws gameliftstreams help
```

## Set up billing alerts

A stream group incurs cost per active stream capacity per second. To make sure your cost and
usage stays within your budget, see [Create billing alerts to monitor usage](pricing.md#pricing-billing-alerts "pricing.md#pricing-billing-alerts").
