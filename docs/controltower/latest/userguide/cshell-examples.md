# Interact with AWS Control Tower through AWS CloudShell

After you launch AWS CloudShell from the AWS Management Console, you can immediately start to interact with
AWS Control Tower from the command line interface. AWS CLI commands work in the standard way in
CloudShell.

###### Note

When using AWS CLI in AWS CloudShell, you don't need to download or install any additional
resources. You're already authenticated within the shell, so you don't need to configure
credentials before making calls.

# Use AWS CloudShell to help set up AWS Control Tower

Before performing these procedures, unless it's otherwise indicated, you must be signed
in to the AWS Management Console in the home Region for your landing zone, and you must be signed in as
an IAM Identity Center user or IAM user with administrative permissions for the management account that contains your
landing zone.

1. Here's how you can use AWS Config CLI commands in AWS CloudShell to determine the status of
   your configuration recorder and delivery channel before you start to configure your
   AWS Control Tower landing zone.

**Example: Check your AWS Config status**

###### View commands:

    * `aws configservice describe-delivery-channels`
    * `aws configservice describe-delivery-channel-status`
    * `aws configservice describe-configuration-recorders`
    * The normal response is something like `"name": "default"`

2. If you have an existing AWS Config recorder or delivery channel that you need to
   delete before you set up your AWS Control Tower landing zone, here are some commands you can
   enter:

**Example: Manage your pre-existing AWS Config resources**

###### Delete commands:

    * `aws configservice stop-configuration-recorder --configuration-recorder-name
     `NAME-FROM-DESCRIBE-OUTPUT``
    * `aws configservice delete-delivery-channel --delivery-channel-name
     `NAME-FROM-DESCRIBE-OUTPUT``
    * `aws configservice delete-configuration-recorder
     --configuration-recorder-name
     `NAME-FROM-DESCRIBE-OUTPUT``


    ###### Important

    Do not delete the AWS Control Tower resources for AWS Config. Loss of these resources can
     cause AWS Control Tower to enter an inconsistent state.

###### For more information, see the AWS Config documentation

    * [Managing the Configuration Recorder (AWS CLI)](../../../config/latest/developerguide/stop-start-recorder.md#managing-recorder_cli "../../../config/latest/developerguide/stop-start-recorder.md#managing-recorder_cli")
    * [Managing the
     Delivery Channel](../../../config/latest/developerguide/manage-delivery-channel.md "../../../config/latest/developerguide/manage-delivery-channel.md")

3. This example shows AWS CLI commands you'd enter from AWS CloudShell to enable or disable
   trusted access for AWS Organizations. For AWS Control Tower you do not need to enable or disable
   trusted access for AWS Organizations, it is just an example. However, you may need to
   enable or disable trusted access for other AWS services if you're automating or
   customizing actions in AWS Control Tower.

###### Example: Enable or disable trusted service access

    * `aws organizations enable-aws-service-access`
    * `aws organizations disable-aws-service-access`

# Example: Create an Amazon S3 bucket with AWS CloudShell

In the following example, you can use AWS CloudShell to create an Amazon S3 bucket and then use the
**PutObject** method to add a code file as an object in that
bucket.

1. To create a bucket in a specified AWS Region, enter the following command in the
   CloudShell command line:

```
aws s3api create-bucket --bucket insert-unique-bucket-name-here --region us-east-1
```

If the call is successful, the command line displays a response from the service
similar to the following output:

```
{
    "Location": "/insert-unique-bucket-name-here"
}
```

###### Note

If you don't adhere to the [rules for naming
buckets](../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules") (using only lowercase letters, for example), the following error is
displayed: **`An error occurred (InvalidBucketName) when calling the
 CreateBucket operation: The specified bucket is not valid.`** 2. To upload a file and add it as an object to the bucket that was just created, call the
**PutObject** method:

```
aws s3api put-object --bucket insert-unique-bucket-name-here --key add_prog --body add_prog.py
```

If the object is uploaded successfully to the Amazon S3 bucket, the command line displays a
response from the service similar to the following output:

```
{
           "ETag": "\"ab123c1:w:wad4a567d8bfd9a1234ebeea56\""}
```

The `ETag` is the hash of the object that's been stored. It can be used to
[check the integrity of the object uploaded to Amazon S3](https://aws.amazon.com/premiumsupport/knowledge-center/data-integrity-s3/ "https://aws.amazon.com/premiumsupport/knowledge-center/data-integrity-s3/").
