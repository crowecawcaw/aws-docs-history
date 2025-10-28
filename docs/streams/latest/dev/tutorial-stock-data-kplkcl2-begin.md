# Complete prerequisites

You must meet the following requirements to complete this tutorial:

## Create and use an Amazon Web Services

Account

Before you begin, make sure that you are familiar with the concepts discussed in
[Amazon Kinesis Data Streams Terminology and concepts](key-concepts.md "key-concepts.md"), particularly with
streams, shards, producers, and consumers. It is also helpful to have completed the
steps in the following guide: [Tutorial: Install and configure the AWS CLI for
Kinesis Data Streams](kinesis-tutorial-cli-installation.md "kinesis-tutorial-cli-installation.md").

You must have an AWS account and a web browser to access the AWS Management Console.

For console access, use your IAM user name and password to sign in to the
[AWS Management Console](https://console.aws.amazon.com/console/home "https://console.aws.amazon.com/console/home")
from the IAM sign-in page. For information about AWS security credentials,
including programmatic access and alternatives to long-term credentials,
see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the _IAM User Guide_.
For details about signing in to your AWS account, see [How to
sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For more information about IAM and security key setup
instructions, see [Create an
IAM User](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-an-iam-user "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-an-iam-user").

## Fulfill system software

requirements

The system that you are using to run the application must have Java 7 or higher
installed. To download and install the latest Java Development Kit (JDK), go to
[Oracle's Java SE installation site](http://www.oracle.com/technetwork/java/javase/downloads/index.html "http://www.oracle.com/technetwork/java/javase/downloads/index.html").

You need the latest [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")
version.

The consumer application requires the Kinesis Client Library (KCL) version 2.2.9 or
higher, which you can obtain from GitHub at [https://github.com/awslabs/amazon-kinesis-client/tree/master](https://github.com/awslabs/amazon-kinesis-client/tree/master "https://github.com/awslabs/amazon-kinesis-client/tree/master").

## Next steps

[Create a data stream](tutorial-stock-data-kplkcl2-create-stream.md "tutorial-stock-data-kplkcl2-create-stream.md")
