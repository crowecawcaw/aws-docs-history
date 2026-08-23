# Setting up Amazon GameLift Streams as a developer

To start using the Amazon GameLift Streams service with your projects, complete these basic setup
tasks. If you already have an AWS account and a user under that account that you want to use
with Amazon GameLift Streams, you can skip to [Download the Web SDK](#setting-up-materials "#setting-up-materials").

For more information on what you can do with an AWS account, see [Getting started with AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").

After you've completed these setup tasks, we recommend that you go to [Starting your first stream in Amazon GameLift Streams](streaming-process.md "streaming-process.md") and
step through the tutorial, which covers the entire workflow for getting your content streaming in a web client.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Get programmatic access](#setting-up-access-keys "#setting-up-access-keys")
- [Download the Amazon GameLift Streams Web SDK](#setting-up-materials "#setting-up-materials")
- [Download the AWS CLI](#setting-up-prereqs "#setting-up-prereqs")
- [Set up billing alerts](#setting-up-billing "#setting-up-billing")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

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
