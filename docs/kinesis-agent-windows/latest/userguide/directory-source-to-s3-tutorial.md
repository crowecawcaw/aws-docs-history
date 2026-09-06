

# Tutorial: Stream JSON Log Files to Amazon S3 Using Kinesis Agent for Windows
<a name="directory-source-to-s3-tutorial"></a>

This tutorial presents detailed steps for setting up a data pipeline using Amazon Kinesis Agent for Microsoft Windows (Kinesis Agent for Windows). 

The tutorial includes the following steps:
+ Using Kinesis Agent for Windows to stream JSON-formatted log files to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) via [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/). For information about Kinesis Agent for Windows, see [What Is Amazon Kinesis Agent for Microsoft Windows?](what-is-kinesis-agent-windows.md).
+ Enhancing the log data before streaming using object decoration. For more information, see [Configuring Sink Decorations](sink-object-declarations.md#configuring-kinesis-agent-windows-decoration-configuration).
+ Using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) to search for particular kinds of log records.

**Prerequisites**  
If you don't already have an AWS account, follow the instructions in [Sign up for an AWS account](getting-started.md#sign-up-for-aws) to get one.

**Topics**
+ [Step 1: Configure AWS services](kaw-ds2s3-tutorial-step1.md)
+ [Step 2: Install, Configure, and Run Kinesis Agent for Windows](kaw-ds2s3-tutorial-step2.md)
+ [Step 3: Query the Log Data in Amazon S3](kaw-ds2s3-tutorial-step3.md)
+ [Next Steps](#kaw-ds2s3-tutorial-step4-next)

## Next Steps
<a name="kaw-ds2s3-tutorial-step4-next"></a>

Use the AWS Management Console to clean up the resources created during the tutorial:

1. Terminate the EC2 instance (see step 3 in [Getting Started with Amazon EC2 Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows)).
**Important**  
If you launched an instance that was not within the [AWS Free Tier](https://aws.amazon.com/free/), you are charged for the instance until you terminate it.

1. Delete the Firehose delivery stream.

   1. Open the Firehose console at [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/).

   1. Choose the delivery stream that you created.

   1. Choose **Delete**.

   1. Choose **Delete delivery stream**.

1. Delete the S3 bucket. For instructions, see [How Do I Delete an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/delete-bucket.html) in the *Amazon Simple Storage Service User Guide*.

For more information, see the following topics:
+ [Configuring Amazon Kinesis Agent for Microsoft Windows](configuring-kinesis-agent-windows.md)
+ [What Is Amazon Kinesis Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
+ [What Is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
+ [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)