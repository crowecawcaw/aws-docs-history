# Setting up DynamoDB (web service)

To use the Amazon DynamoDB web service:

1. [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
2. [Configure your
   credentials](#SettingUp.DynamoWebService.ConfigureCredentials "#SettingUp.DynamoWebService.ConfigureCredentials") (used to access DynamoDB programmatically).

###### Note

If you plan to interact with DynamoDB only through the AWS Management Console, you don't
need an AWS access key, and you can skip ahead to [Using the console](AccessingDynamoDB.md#ConsoleDynamoDB "AccessingDynamoDB.md#ConsoleDynamoDB").

## Signing up for AWS

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Configuring your credentials

Before you can access DynamoDB programmatically or through the AWS CLI, you must
configure your credentials to enable authorization for your applications.

There are several ways to do this. For example, you can manually create the
credentials file to store your access key ID and secret access key. You also can use
the AWS CLI command `aws configure` to automatically create the file.
Alternatively, you can use environment variables. For more information about
configuring your credentials, see the programming-specific AWS SDK developer
guide.

To install and configure the AWS CLI, see [Using the AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI").

## Integrating with other DynamoDB services

You can integrate DynamoDB with many other AWS services. For more information, see
the following:

- [Using DynamoDB with other AWS services](OtherServices.md "OtherServices.md")
- [CloudFormation for DynamoDB](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md")
- [Using AWS Backup with DynamoDB](backuprestore_HowItWorksAWS.md "backuprestore_HowItWorksAWS.md")
- [AWS Identity and Access Management (IAM) and DynamoDB](identity-and-access-mgmt.md "identity-and-access-mgmt.md")
- [Using
  AWS Lambda with Amazon DynamoDB](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md")
