# Tutorial: Stream JSON Log Files to Amazon S3 Using

Kinesis Agent for Windows

This tutorial presents detailed steps for setting up a data pipeline using Amazon Kinesis Agent for Microsoft Windows (Kinesis Agent for Windows).

The tutorial includes the following steps:

- Using Kinesis Agent for Windows to stream JSON-formatted log files to [Amazon Simple Storage Service
  (Amazon S3)](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") via [Amazon Data Firehose](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md"). For information about
  Kinesis Agent for Windows, see [What Is Amazon Kinesis Agent for Microsoft Windows?](what-is-kinesis-agent-windows.md "what-is-kinesis-agent-windows.md").
- Enhancing the log data before streaming using object decoration. For more information, see
  [Configuring Sink
  Decorations](sink-object-declarations.md#configuring-kinesis-agent-windows-decoration-configuration "sink-object-declarations.md#configuring-kinesis-agent-windows-decoration-configuration").
- Using [Amazon Athena](../../../athena/latest/ug.md "../../../athena/latest/ug.md") to search for particular kinds of log
  records.

###### Prerequisites

If you don't already have an AWS account, follow the instructions in [Setting Up an AWS account](getting-started.md#getting-started-setting-up "getting-started.md#getting-started-setting-up") to get
one.

###### Topics

- [Step 1: Configure AWS services](kaw-ds2s3-tutorial-step1.md "kaw-ds2s3-tutorial-step1.md")
- [Step 2: Install, Configure, and Run Kinesis Agent for Windows](kaw-ds2s3-tutorial-step2.md "kaw-ds2s3-tutorial-step2.md")
- [Step 3: Query the Log Data in Amazon S3](kaw-ds2s3-tutorial-step3.md "kaw-ds2s3-tutorial-step3.md")
- [Next Steps](#kaw-ds2s3-tutorial-step4-next "#kaw-ds2s3-tutorial-step4-next")

## Next Steps

Use the AWS Management Console to clean up the resources created during the tutorial:

1. Terminate the EC2 instance (see step 3 in [Getting Started with Amazon EC2 Windows Instances](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows")).

###### Important

If you launched an instance that was not within the [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/"), you are charged for the
instance until you terminate it. 2. Delete the Firehose delivery stream.

    1. Open the Firehose console at
     [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
    2. Choose the delivery stream that you created.
    3. Choose **Delete**.
    4. Choose **Delete delivery stream**.

3. Delete the S3 bucket. For instructions, see [How Do I Delete an
   S3 Bucket?](../../../AmazonS3/latest/user-guide/delete-bucket.md "../../../AmazonS3/latest/user-guide/delete-bucket.md") in the _Amazon Simple Storage Service User Guide_.

For more information, see the following topics:

- [Configuring Amazon Kinesis Agent for Microsoft Windows](configuring-kinesis-agent-windows.md "configuring-kinesis-agent-windows.md")
- [What Is Amazon
  Kinesis Data Firehose?](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")
- [What Is Amazon
  S3?](../../../AmazonS3/latest/dev/Welcome.md "../../../AmazonS3/latest/dev/Welcome.md")
- [What is Amazon
  Athena?](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md")
