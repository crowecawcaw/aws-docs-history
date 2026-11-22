

# Source configuration for Zscaler Internet Access

## Integrating with Zscaler Internet Access
<a name="zscaler-zia-integration"></a>

Zscaler Internet Access (ZIA) is a cloud-based secure web gateway that protects users connecting to the internet. It inspects all internet traffic to block malware, phishing, and data leaks using advanced threat detection and SSL inspection. ZIA streams its web, firewall, DNS, and admin audit logs to a customer-managed Amazon S3 bucket through Cloud Nanolog Streaming Service (Cloud NSS) feeds. CloudWatch pipelines enables you to collect this data in CloudWatch Logs.

To integrate CloudWatch pipelines with Zscaler Internet Access, complete the following high-level steps:
+ Create an Amazon S3 bucket, with a folder for each ZIA log type.
+ Create an IAM user with write access to the bucket, and an access key for that user.
+ Create an Amazon SQS queue and configure Amazon S3 event notifications to send to it.
+ Add a Cloud NSS feed in the ZIA Admin Portal for each log type you want to collect.
+ Create a CloudWatch pipeline with Zscaler Internet Access (ZIA) as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="zscaler-zia-prerequisites"></a>
+ A Zscaler Cloud Nanolog Streaming Service (Cloud NSS) subscription. This integration reads logs from Amazon S3, and Cloud NSS feeds are the NSS feed type that delivers logs directly to Amazon S3. If you don't see **Cloud NSS Feeds** in the ZIA Admin Portal, contact Zscaler Support.
+ Administrator access to the ZIA Admin Portal.
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ Permissions to create Amazon S3 buckets, Amazon SQS queues, and IAM users and policies.

## Instructions to set up Amazon S3 and Amazon SQS
<a name="zscaler-zia-s3-sqs-setup"></a>

1. Create an Amazon S3 bucket to store ZIA logs. Note the AWS Region you choose; it's part of the Amazon S3 folder URL that you enter in ZIA later. For more information, see [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
**Note**  
Keep the bucket's default encryption set to server-side encryption with Amazon S3 managed keys (SSE-S3). CloudWatch pipelines can't apply OCSF transformations or other processing to KMS encrypted logs, so don't set the bucket's default encryption to SSE-KMS.
**Note**  
Amazon S3 bucket names can't contain underscores (`_`). Use hyphens (`-`) instead.

1. Create a folder in the bucket for each log type that you plan to send, for example `web-logs/`, `firewall-logs/`, `dns-logs/`, and `admin-audit-logs/`. For each folder, copy and save its URL, for example `https://{{bucket-name}}.s3.{{aws-region}}.amazonaws.com/web-logs/`. The URL must include the Region name.

1. Create an IAM user for Cloud NSS and attach a policy that allows it to write to the bucket. Cloud NSS authenticates with an access key, so the user doesn't need console access (see *Example IAM policy for the Cloud NSS user* below).

1. Create an access key for the IAM user. Save the access key ID and secret access key; you need them when you add the Cloud NSS feed in ZIA. You can view or download the secret access key only when you create it. For more information, see [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

1. Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue receives notifications when new log files are added to the Amazon S3 bucket. For more information, see [Create an Amazon SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.html).

1. Attach an IAM policy to the Amazon SQS queue to allow Amazon S3 to write event notifications to the Amazon SQS queue (see *Example IAM policy for Amazon SQS queue* below).

1. Configure the Amazon S3 bucket to generate "Object Create" event notifications to be sent to the Amazon SQS queue. For more information, see [Enable event notifications on the S3 bucket with the SQS queue as a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html).

1. Add a Cloud NSS feed in the ZIA Admin Portal for each log type (Web, Firewall, DNS, and Admin Audit). Create a separate feed for each log type, and point each feed at that log type's folder.

   1. In the ZIA Admin Portal, go to **Administration** > **Nanolog Streaming Service**, choose **Cloud NSS Feeds**, and then choose **Add Cloud NSS Feed**.

   1. Select the log type for the feed (for example, Web Logs).

   1. Enter the following values:
      + **SIEM Type** – S3
      + **AWS Access Id** – The access key ID from step 4.
      + **AWS Secret Key** – The secret access key from step 4.
      + **S3 Folder URL** – The folder URL from step 2 for this log type.
      + **Max Batch Size** – Zscaler recommends 8 MB for Web and Firewall logs, and 1 MB for DNS and other log types.

   1. Save the feed, and then repeat these steps for each log type.

   For details about each field, see [Adding Cloud NSS Feeds](https://help.zscaler.com/zia/adding-cloud-nss-feeds) on the Zscaler website.

**Example IAM policy for the Cloud NSS user**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudNssWrite",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::<bucket-name>/*"
        }
    ]
}
```

**Example IAM policy for Amazon SQS queue**

```json
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
                },
                "StringEquals": {
                    "aws:SourceAccount": "<aws-account-number>"
                }
            }
        }
    ]
}
```

## Configuring the CloudWatch Pipeline
<a name="zscaler-zia-pipeline-config"></a>

When configuring the pipeline to read data from Zscaler Internet Access, choose Zscaler Internet Access (ZIA) as the data source. After you create the pipeline, data is available in the selected CloudWatch Logs log group. The log group requires a [resource policy](pipeline-iam-reference.md#resource-policies). If you create the pipeline in the console, CloudWatch adds the policy automatically.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="zscaler-zia-ocsf-events"></a>

This integration supports OCSF schema version v1.5.0 and events that map to DNS Activity (4003), HTTP Activity (4002), Network Activity (4001), and Authentication (3002). Events that are not listed are not mapped to OCSF and are forwarded to the sink as raw logs.

**DNS Activity (4003)** covers all events from source:
+ [DNS Logs](https://help.zscaler.com/zia/nss-feed-output-format-dns-logs) on the Zscaler website

**HTTP Activity (4002)** covers all events from source:
+ [Web Logs](https://help.zscaler.com/zia/nss-feed-output-format-web-logs) on the Zscaler website

**Network Activity (4001)** covers all events from source:
+ [Firewall Logs](https://help.zscaler.com/zia/nss-feed-output-format-firewall-logs) on the Zscaler website

**Authentication (3002)** covers events from source:
+ [Admin Audit Logs](https://help.zscaler.com/zia/nss-feed-output-format-admin-audit-logs) on the Zscaler website – Event actions: SIGN\_IN, SIGN\_OUT