

# Source configuration for Jamf Protect
<a name="jamf-protect-source-config"></a>

## Integrating with Jamf Protect
<a name="jamf-protect-integration"></a>

Jamf Protect integration uses Amazon S3 and Amazon SQS to ingest log data into CloudWatch pipelines. Jamf Protect supports native Amazon S3 delivery through Action Configurations (for macOS Security data) and Data Streams (for Jamf Security Cloud data), eliminating the need for an intermediate log forwarder such as Fluent Bit. Amazon SQS notifications alert the pipeline when new log objects arrive.

## Prerequisites
<a name="jamf-protect-prerequisites"></a>
+ An AWS account with permissions to create Amazon S3 buckets, Amazon SQS queues, and IAM roles
+ A Jamf Protect tenant with administrative access to configure Action Configurations or Data Streams
+ IAM credentials for Jamf Protect to write to Amazon S3

## Instructions to setup Amazon S3 and Amazon SQS
<a name="jamf-protect-s3-sqs-setup"></a>

Complete the following steps to configure the Amazon S3 and Amazon SQS infrastructure for Jamf Protect log ingestion.

### Step 1: Create Amazon S3 bucket
<a name="jamf-protect-step1"></a>

Create an Amazon S3 bucket to store Jamf Protect logs. The bucket must reside in the same AWS Region where you plan to create the CloudWatch pipeline.

### Step 2: Create Amazon SQS queue
<a name="jamf-protect-step2"></a>

Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue receives notifications when new log files are added to the bucket.

### Step 3: Connect Amazon S3 to Amazon SQS
<a name="jamf-protect-step3"></a>

Configure the Amazon S3 bucket to send event notifications for `s3:ObjectCreated:*` events to the Amazon SQS queue.

### Step 4: Configure Amazon SQS queue policy
<a name="jamf-protect-step4"></a>

Configure the Amazon SQS queue policy to allow the Amazon S3 bucket to send messages to the queue. Apply the following policy to your Amazon SQS queue:

```
{
  "Version": "2012-10-17",
  "Id": "AllowS3ToSQS",
  "Statement": [
    {
      "Sid": "AllowS3BucketNotification",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:<region>:<account-id>:<queue-name>",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:s3:::<YOUR-BUCKET>"
        },
        "StringEquals": {
          "aws:SourceAccount": "<account-id>"
        }
      }
    }
  ]
}
```

### Step 5: Configure Jamf Protect to export logs to Amazon S3
<a name="jamf-protect-step5"></a>

Configure Jamf Protect to deliver log data directly to your Amazon S3 bucket.

**macOS Security (Action Configuration)**

1. In the Jamf Protect console, navigate to Action Configurations.

1. Create or edit an Action Configuration.

1. Configure the Amazon S3 destination with your bucket name, region, and IAM credentials.

**Jamf Security Cloud (Data Streams)**

1. In the Jamf Protect console, navigate to Integrations, then choose Data Streams.

1. Create a new Data Stream with Amazon S3 as the destination.

1. Provide the bucket name, region, and IAM credentials.

### Step 6: Attach bucket policy
<a name="jamf-protect-step6"></a>

Apply the following bucket policy to your Amazon S3 bucket to allow the Jamf IAM user to write objects:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "s3-access",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<<YOUR-ACCOUNT>>:user/<<JAMF-IAM-USER>>"
      },
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::<<YOUR-BUCKET>>/jamf-protect-logs/*"
    },
    {
      "Sid": "s3-list-bucket",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<<YOUR-ACCOUNT>>:user/<<JAMF-IAM-USER>>"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::<<YOUR-BUCKET>>",
      "Condition": {
        "StringLike": {
          "s3:prefix": "jamf-protect-logs/*"
        }
      }
    }
  ]
}
```

### Step 7: Verify
<a name="jamf-protect-step7"></a>

Verify the setup by confirming that log files appear in the Amazon S3 bucket and that Amazon SQS notifications are being generated. Check the Amazon SQS queue for messages indicating new object creation events.

## Configuring the CloudWatch pipeline
<a name="jamf-protect-pipeline-config"></a>
+ Choose Jamf Protect as the data source when creating the pipeline.
+ Provide the Amazon SQS queue URL and IAM role ARN.
+ Select the destination CloudWatch Logs log group.
+ After you create the pipeline, data will be available in the selected log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="jamf-protect-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. The following table shows the mapping between Jamf Protect data types and OCSF event classes.


| Event name | OCSF event class | 
| --- | --- | 
| Alerts | Detection Finding [2004] | 
| Telemetry | Pass-through | 
| Unified Logs | Pass-through | 
| Threat Events | Detection Finding [2004] | 
| Network Traffic | Network Activity [4001] / DNS Activity [4003] | 
| Access Events (ZTNA) | Pass-through | 
| Device Data | Device Inventory Info [5001] | 
| App Insights | Software Inventory Info [5020] | 
| Vulnerability Data | Vulnerability Finding [2002] | 