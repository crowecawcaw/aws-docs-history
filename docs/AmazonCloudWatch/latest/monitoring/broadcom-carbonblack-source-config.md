# Source configuration for Broadcom Carbon Black

## Integrating with Broadcom Carbon Black

CloudWatch Pipeline ingests Broadcom Carbon Black event data from Amazon S3. You configure Carbon Black Cloud to export event data to an Amazon S3 bucket using the Data Forwarder, then create a pipeline that reads from that bucket using Amazon SQS notifications.

To integrate CloudWatch Pipelines with Broadcom Carbon Black, complete the following high-level steps:

- Configure Carbon Black Cloud Data Forwarder to export events to an Amazon S3 bucket.
- Set up Amazon SQS notifications on the Amazon S3 bucket for new object creation.
- Create the required IAM role for pipeline access.
- Create a CloudWatch pipeline with Broadcom Carbon Black as the data source.
- Verify that data is flowing into the pipeline.

## Instructions to set up Amazon S3 and Amazon SQS

Setting up the Carbon Black Data Forwarder to send logs to an Amazon S3 bucket involves several steps to create the required AWS resources (Amazon S3 bucket, Amazon SQS queue, IAM roles) and configure the Carbon Black Data Forwarder to send the desired log events.

1. Create an Amazon S3 bucket to store Carbon Black logs.

###### Important

You must select the same region as your Broadcom Carbon Black instance. See the [Carbon Black documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#create-a-bucket "https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#create-a-bucket") on the Broadcom developer website to determine which AWS region your Carbon Black product URL maps to.

###### Important

CloudWatch Pipelines will not be able to apply OCSF transformations or other processing to KMS encrypted logs. If processing is needed, do not set up KMS encryption.

For detailed instructions, see [Configure the Destination: Use Amazon S3](https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#option-1-use-aws-s3 "https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#option-1-use-aws-s3") in the Carbon Black Data Forwarder documentation on the Broadcom developer website. 2. Attach an IAM policy to the Amazon S3 bucket to grant the Forwarder permissions to write to your bucket (see _Example IAM policy for Amazon S3 bucket_ below).

###### Note

The Principal ID ARN to use in the policy is based on the AWS region the Amazon S3 bucket is in. See the _Principal ID to allow by AWS Region_ table below. 3. Create an Amazon SQS queue in the same AWS region as your Amazon S3 bucket. This queue will receive notifications when new log files are added to the Amazon S3 bucket. For more information, see [Create an Amazon SQS queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.md"). 4. Attach an IAM policy to the Amazon SQS queue to allow Amazon S3 to write event notifications to the Amazon SQS queue (see _Example IAM policy for Amazon SQS queue_ below). 5. Configure the Amazon S3 bucket to generate "Object Create" event notifications to be sent to the Amazon SQS queue. For more information, see [Enable event notifications on the S3 bucket with the SQS queue as a destination](../../../AmazonS3/latest/userguide/enable-event-notifications.md "../../../AmazonS3/latest/userguide/enable-event-notifications.md"). 6. Create and configure the Carbon Black Data Forwarder, through the Carbon Black Console or API, by following the Carbon Black [Create a Forwarder](https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#2-create-a-forwarder "https://developer.carbonblack.com/reference/carbon-black-cloud/integrations/data-forwarder/quick-setup/#2-create-a-forwarder") documentation. For complete documentation, see [Carbon Black Data Forwarders](https://techdocs.broadcom.com/us/en/carbon-black/cloud/carbon-black-cloud/index/cbc-user-guide-tile/GUID-9620FAB7-FE70-45DE-9CAB-590FA358721F-en/GUID-E8D33F72-BABB-4157-A908-D8BBDB5AF349-en.html "https://techdocs.broadcom.com/us/en/carbon-black/cloud/carbon-black-cloud/index/cbc-user-guide-tile/GUID-9620FAB7-FE70-45DE-9CAB-590FA358721F-en/GUID-E8D33F72-BABB-4157-A908-D8BBDB5AF349-en.html") on the Broadcom website.

**Example IAM policy for Amazon S3 bucket**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCarbonBlackForwarderWriteAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-<aws-region>-event-forwarder"
            },
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::<bucket-name>[/<prefix>]/*"
        }
    ]
}
```

**Principal ID to allow by AWS Region**

| AWS Region                           | Principal ID                                                                                 |
| ------------------------------------ | -------------------------------------------------------------------------------------------- |
| US East (N. Virginia) us-east-1      | `arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-us-east-1-event-forwarder`      |
| Europe (Frankfurt) eu-central-1      | `arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-eu-central-1-event-forwarder`   |
| Asia Pacific (Tokyo) ap-northeast-1  | `arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-ap-northeast-1-event-forwarder` |
| Asia Pacific (Sydney) ap-southeast-2 | `arn:aws:iam::132308400445:role/mcs-psc-prod-event-forwarder-ap-southeast-2-event-forwarder` |

**Example IAM policy for Amazon SQS queue**

```
{
    "Version": "2012-10-17",
    "Id": "PolicyForS3SendMessage",
    "Statement": [
        {
            "Sid": "AllowS3SendMessage",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sqs:SendMessage",
            "Resource": "arn:aws:sqs:<aws-region>:<aws-account-number>:<queue-name>",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::<bucket-name>"
                }
            }
        }
    ]
}
```

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Broadcom Carbon Black, choose Broadcom Carbon Black as the data source. After you create the pipeline, data will be available in the selected CloudWatch Logs log group. The log group will require a [resource policy](pipeline-iam-reference.md#resource-policies "pipeline-iam-reference.md#resource-policies"). The policy is automatically added if the pipeline is created through the console.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the Broadcom Carbon Black log events (Endpoint Events v1.2.0, Alerts v2.1.0, Watchlist Hits v1.0.0, Auth Events v1.0.0, Audit Logs v1.0.0) that map to the following OCSF event classes.

When parseOCSF is enabled, if any log events aren't one of the supported log event types, the logs will be ingested in their raw form with a `@transformationError` field added and a `TransformationErrors` metric emitted.

### File System Activity (1001)

Contains the following events:

- endpoint.event.filemod

### Module Activity (1005)

Contains the following events:

- endpoint.event.moduleload
- endpoint.event.scriptload

### Process Activity (1007)

Contains the following events:

- endpoint.event.procstart
- endpoint.event.procend
- endpoint.event.crossproc
- endpoint.event.apicall

### Script Activity (1009)

Contains the following events:

- endpoint.event.fileless\_scriptload

### Detection Finding (2004)

Contains the following events:

- alert CB\_ANALYTICS
- alert WATCHLIST
- alert INTRUSION\_DETECTION\_SYSTEM
- alert HOST\_BASED\_FIREWALL
- alert DEVICE\_CONTROL
- alert CONTAINER\_RUNTIME

### Authentication (3002)

Contains the following events:

- auth.event.logonop

### Network Activity (4001)

Contains the following events:

- endpoint.event.netconn
- endpoint.event.netconn\_proxy

### Registry Key Activity (win ext) (201001)

Contains the following events:

- endpoint.event.regmod (action ends in "\_KEY" or action == "ACTION\_SET\_SECURITY")

### Registry Value Activity (win ext) (201002)

Contains the following events:

- endpoint.event.regmod (action ends in "\_VALUE")
