

# Complete prerequisites to set up Amazon Kinesis Data Streams
<a name="before-you-begin"></a>

Before you use Amazon Kinesis Data Streams for the first time, complete the following tasks to set up your environment.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Download libraries and tools](#setting-up-downloads)
+ [Configure your development environment](#setting-up-requirements)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Download libraries and tools
<a name="setting-up-downloads"></a>

The following libraries and tools will help you work with Kinesis Data Streams: 
+ The [Amazon Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/) is the basic set of operations that Kinesis Data Streams supports. For more information about performing basic operations using Java code, see the following:
  + [Develop producers using the Amazon Kinesis Data Streams API with the AWS SDK for Java](developing-producers-with-sdk.md)
  + [Develop consumers with the AWS SDK for Java](develop-consumers-sdk.md)
  + [Create and manage Kinesis data streams](working-with-streams.md)
+ The AWS SDKs for [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/kinesis/), [Java](https://aws.amazon.com/developers/getting-started/java/), [JavaScript](https://aws.amazon.com/developer/language/java/?intClick=dc_navbar), [.NET](https://aws.amazon.com/developer/language/net/?intClick=dc_navbar), [PHP](https://aws.amazon.com/developers/getting-started/php/), [Python](https://github.com/boto/boto), and [Ruby](https://aws.amazon.com/developers/getting-started/ruby/) include Kinesis Data Streams support and samples. If your version of the AWS SDK for Java does not include samples for Kinesis Data Streams, you can also download them from [GitHub](https://github.com/aws/aws-sdk-java/tree/master/src/samples).
+ The Kinesis Client Library (KCL) provides an easy-to-use programming model for processing data. The KCL can help you get started quickly with Kinesis Data Streams in Java, Node.js, .NET, Python, and Ruby. For more information see [Reading Data from Streams](building-consumers.md).
+ The [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/) supports Kinesis Data Streams. The AWS CLI enables you to control multiple AWS services from the command line and automate them through scripts.

## Configure your development environment
<a name="setting-up-requirements"></a>

To use the KCL, ensure that your Java development environment meets the following requirements:
+ Java 1.7 (Java SE 7 JDK) or later. You can download the latest Java software from [Java SE Downloads](http://www.oracle.com/technetwork/java/javase/downloads/index.html) on the Oracle website.
+ Apache Commons package (Code, HTTP Client, and Logging)
+ Jackson JSON processor

Note that the [AWS SDK for Java](https://aws.amazon.com/sdkforjava/) includes Apache Commons and Jackson in the third-party folder. However, the SDK for Java works with Java 1.6, while the Kinesis Client Library requires Java 1.7.