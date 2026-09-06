

# Complete prerequisites
<a name="tutorial-stock-data-kplkcl-begin"></a>

The following are requirements for completing the [Tutorial: Process real-time stock data using KPL and KCL 1.x](tutorial-stock-data-kplkcl.md).

## Create and use an Amazon Web Services Account
<a name="tutorial-stock-data-kplkcl-begin-aws"></a>

Before you begin, ensure that you are familiar with the concepts discussed in [Amazon Kinesis Data Streams Terminology and concepts](key-concepts.md), particularly streams, shards, producers, and consumers. It is also helpful to have completed [Tutorial: Install and configure the AWS CLI for Kinesis Data Streams](kinesis-tutorial-cli-installation.md).

You need an AWS account and a web browser to access the AWS Management Console.

For console access, use your IAM user name and password to sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home) from the IAM sign-in page. For information about AWS security credentials, including programmatic access and alternatives to long-term credentials, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*. For details about signing in to your AWS account, see [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For more information about IAM and security key setup instructions, see [Create an IAM User](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html#create-an-iam-user).

## Fulfill system software requirements
<a name="tutorial-stock-data-kplkcl-begin-sys"></a>

The system used to run the application must have Java 7 or higher installed. To download and install the latest Java Development Kit (JDK), go to [Oracle's Java SE installation site](http://www.oracle.com/technetwork/java/javase/downloads/index.html).

If you have a Java IDE, such as [Eclipse](https://www.eclipse.org/downloads/), you can open the source code, edit, build, and run it.

You need the latest [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/) version. If you are using Eclipse as your IDE, you can install the [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/) instead. 

The consumer application requires the Kinesis Client Library (KCL) version 1.2.1 or higher, which you can obtain from GitHub at [Kinesis Client Library (Java)](https://github.com/awslabs/amazon-kinesis-client).

## Next Steps
<a name="tutorial-stock-data-kplkcl-begin-next"></a>

[Create a data stream](tutorial-stock-data-kplkcl-create-stream.md)