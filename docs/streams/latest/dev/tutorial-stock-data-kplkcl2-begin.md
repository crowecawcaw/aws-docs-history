

# Complete prerequisites
<a name="tutorial-stock-data-kplkcl2-begin"></a>

You must meet the following requirements to complete this tutorial:

## Create and use an Amazon Web Services Account
<a name="tutorial-stock-data-kplkcl2-begin-aws"></a>

Before you begin, make sure that you are familiar with the concepts discussed in [Amazon Kinesis Data Streams Terminology and concepts](key-concepts.md), particularly with streams, shards, producers, and consumers. It is also helpful to have completed the steps in the following guide: [Tutorial: Install and configure the AWS CLI for Kinesis Data Streams](kinesis-tutorial-cli-installation.md).

You must have an AWS account and a web browser to access the AWS Management Console.

For console access, use your IAM user name and password to sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home) from the IAM sign-in page. For information about AWS security credentials, including programmatic access and alternatives to long-term credentials, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*. For details about signing in to your AWS account, see [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For more information about IAM and security key setup instructions, see [Create an IAM User](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html#create-an-iam-user).

## Fulfill system software requirements
<a name="tutorial-stock-data-kplkcl2-begin-sys"></a>

The system that you are using to run the application must have Java 7 or higher installed. To download and install the latest Java Development Kit (JDK), go to [Oracle's Java SE installation site](http://www.oracle.com/technetwork/java/javase/downloads/index.html).

You need the latest [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/) version. 

The consumer application requires the Kinesis Client Library (KCL) version 2.2.9 or higher, which you can obtain from GitHub at [https://github.com/awslabs/amazon-kinesis-client/tree/master](https://github.com/awslabs/amazon-kinesis-client/tree/master).

## Next steps
<a name="tutorial-stock-data-kplkcl2-begin-next"></a>

[Create a data stream](tutorial-stock-data-kplkcl2-create-stream.md)