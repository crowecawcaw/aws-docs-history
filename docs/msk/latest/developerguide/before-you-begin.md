# Setting up Amazon MSK

Before you use Amazon MSK for the first time, complete the following tasks.

###### Tasks

- [Sign up for AWS](#setting-up-sign-up-for-aws "#setting-up-sign-up-for-aws")
- [Download libraries and tools](#setting-up-downloads "#setting-up-downloads")

## Sign up for AWS

When you sign up for AWS, your Amazon Web Services account is automatically
signed up for all services in AWS, including Amazon MSK. You are charged only for the services
that you use.

If you have an AWS account already, skip to the next task. If you don't have an AWS
account, use the following procedure to create one.

###### To sign up for an Amazon Web Services account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Download libraries and tools

The following libraries and tools can help you work with Amazon MSK:

- The [AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") supports
  Amazon MSK. The AWS CLI enables you to control multiple Amazon Web Services from the
  command line and automate them through scripts. Upgrade your AWS CLI to the latest
  version to ensure that it has support for the Amazon MSK features that are
  documented in this user guide. For detailed instructions on how to upgrade the
  AWS CLI, see [Installing
  the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md"). After you install the AWS CLI, you must configure it.
  For information on how to configure the AWS CLI, see [aws
  configure](../../../cli/latest/reference/configure/index.md "../../../cli/latest/reference/configure/index.md").
- The [Amazon Managed Streaming for Kafka API Reference](../../1.0/apireference/what-is-msk.md "../../1.0/apireference/what-is-msk.md") documents the API operations
  that Amazon MSK supports.
- The Amazon Web Services SDKs for
  [Go](../../../sdk-for-go/api/service/kafka.md "../../../sdk-for-go/api/service/kafka.md"), [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/"), [JavaScript](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/"), [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/"), [Node.js](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/"),
  [PHP](https://aws.amazon.com/developers/getting-started/php/ "https://aws.amazon.com/developers/getting-started/php/"),
  [Python](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/"), and [Ruby](https://aws.amazon.com/developers/getting-started/ruby/ "https://aws.amazon.com/developers/getting-started/ruby/") include
  Amazon MSK support and samples.
