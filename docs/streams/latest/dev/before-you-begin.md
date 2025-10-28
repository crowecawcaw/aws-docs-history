# Complete prerequisites to set up Amazon Kinesis Data Streams

Before you use Amazon Kinesis Data Streams for the first time, complete the following tasks to set up your environment.

###### Tasks

- [Sign up for AWS](#setting-up-sign-up-for-aws "#setting-up-sign-up-for-aws")
- [Download libraries and tools](#setting-up-downloads "#setting-up-downloads")
- [Configure your development environment](#setting-up-requirements "#setting-up-requirements")

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically
signed up for all services in AWS, including Kinesis Data Streams. You are charged only for the
services that you use.

If you have an AWS account already, skip to the next task. If you don't have an AWS
account, use the following procedure to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Download libraries and tools

The following libraries and tools will help you work with Kinesis Data Streams:

- The [Amazon Kinesis API Reference](../../../kinesis/latest/APIReference.md "../../../kinesis/latest/APIReference.md") is the basic set of operations that Kinesis Data Streams supports. For more
  information about performing basic operations using Java code, see the
  following:
  - [Develop producers using the Amazon Kinesis Data Streams API
    with the AWS SDK for Java](developing-producers-with-sdk.md "developing-producers-with-sdk.md")
  - [Develop consumers with the AWS SDK for Java](develop-consumers-sdk.md "develop-consumers-sdk.md")
  - [Create and manage Kinesis data streams](working-with-streams.md "working-with-streams.md")

- The AWS SDKs for [Go](../../../sdk-for-go/api/service/kinesis.md "../../../sdk-for-go/api/service/kinesis.md"), [Java](https://aws.amazon.com/developers/getting-started/java/ "https://aws.amazon.com/developers/getting-started/java/"), [JavaScript](https://aws.amazon.com/developer/language/java/?intClick=dc_navbar "https://aws.amazon.com/developer/language/java/?intClick=dc_navbar"), [.NET](https://aws.amazon.com/developer/language/net/?intClick=dc_navbar "https://aws.amazon.com/developer/language/net/?intClick=dc_navbar"), [PHP](https://aws.amazon.com/developers/getting-started/php/ "https://aws.amazon.com/developers/getting-started/php/"), [Python](https://github.com/boto/boto "https://github.com/boto/boto"), and
  [Ruby](https://aws.amazon.com/developers/getting-started/ruby/ "https://aws.amazon.com/developers/getting-started/ruby/")
  include Kinesis Data Streams support and samples. If your version of the AWS SDK for Java does not
  include samples for Kinesis Data Streams, you can also download them from [GitHub](https://github.com/aws/aws-sdk-java/tree/master/src/samples "https://github.com/aws/aws-sdk-java/tree/master/src/samples").
- The Kinesis Client Library (KCL) provides an easy-to-use programming model
  for processing data. The KCL can help you get started quickly with
  Kinesis Data Streams in Java, Node.js, .NET, Python, and Ruby. For more information see [Reading Data from Streams](building-consumers.md "building-consumers.md").
- The [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") supports Kinesis Data Streams. The AWS CLI
  enables you to control multiple AWS services from the command line and automate
  them through scripts.

## Configure your development environment

To use the KCL, ensure that your Java development environment meets the
following requirements:

- Java 1.7 (Java SE 7 JDK) or later. You can download the latest Java software
  from [Java SE Downloads](http://www.oracle.com/technetwork/java/javase/downloads/index.html "http://www.oracle.com/technetwork/java/javase/downloads/index.html") on the Oracle website.
- Apache Commons package (Code, HTTP Client, and Logging)
- Jackson JSON processor

Note that the [AWS SDK for Java](https://aws.amazon.com/sdkforjava/ "https://aws.amazon.com/sdkforjava/") includes
Apache Commons and Jackson in the third-party folder. However, the SDK for Java works with
Java 1.6, while the Kinesis Client Library requires Java 1.7.
