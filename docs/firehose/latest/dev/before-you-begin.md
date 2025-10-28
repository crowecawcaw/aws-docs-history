# Complete prerequisites to set up Amazon Data Firehose

Before you use Amazon Data Firehose for the first time, complete the following tasks.

###### Tasks

- [Sign up for AWS](#setting-up-sign-up-for-aws "#setting-up-sign-up-for-aws")
- [(Optional) Download libraries and tools](#setting-up-downloads "#setting-up-downloads")

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically
signed up for all services in AWS, including Amazon Data Firehose. You are charged only for the services
that you use.

If you have an AWS account already, skip to the next task. If you don't have an AWS
account, use the following procedure to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## (Optional) Download libraries and tools

The following libraries and tools will help you work with Amazon Data Firehose programmatically and from the
command line:

- The [Firehose API Operations](../APIReference/API_Operations.md "../APIReference/API_Operations.md") is the basic set of operations that Amazon Data Firehose supports.
- The AWS SDKs for [Go](../../../sdk-for-go/api/service/firehose.md "../../../sdk-for-go/api/service/firehose.md"),
  [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/"),
  [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/"), [Node.js](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/       "), [Python](https://aws.amazon.com/developers/getting-started/python/ "https://aws.amazon.com/developers/getting-started/python/"),
  and [Ruby](https://aws.amazon.com/developers/getting-started/ruby/ "https://aws.amazon.com/developers/getting-started/ruby/") include Amazon Data Firehose support and samples.

If your version of the AWS SDK for Java does not include samples for Amazon Data Firehose, you can also download
the latest AWS SDK from [GitHub](https://github.com/aws/aws-sdk-java/tree/master/src/samples "https://github.com/aws/aws-sdk-java/tree/master/src/samples").

- The [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") supports Amazon Data Firehose. The AWS CLI
  enables you to control multiple AWS services from the command line and automate
  them through scripts.
