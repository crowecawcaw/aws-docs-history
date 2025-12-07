# Source configuration for Zscaler Internet Access

## Integrating with Zscaler Internet Access

Zscaler Internet Access (ZIA) is a cloud-based secure web gateway that protects users connecting to the internet. It inspects all internet traffic to block malware, phishing, and data leaks using advanced threat detection and SSL inspection. ZIA enforces security policies in real time without requiring on-premises hardware. It ensures safe and compliant internet access for users anywhere. CloudWatch pipelines enables you to collect this data in CloudWatch Logs.

## Instructions to setup Amazon S3 and Amazon SQS

Configuring ZIA to send logs to an Amazon S3 bucket involves several steps, primarily focused on setting up the Amazon S3 bucket, Amazon SQS queue, IAM roles, and then configuring the Amazon Telemetry Pipeline.

- Create Amazon S3 bucket that stores ZIA logs and create separate folders for each log type. Create IAM user and grant s3 write permission, console access not needed only CLI and create Access key and Secret key for this account.
- Configure NSS feeds with Amazon S3 bucket details to push logs.
- Configure the Amazon S3 bucket to create event notifications, specifically for "Object Create" events. These notifications should be sent to an Amazon SQS queue.
- Create an Amazon SQS queue in the same AWS region as your Amazon S3 bucket. This queue will receive notifications when new log files are added to the Amazon S3 bucket.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Zscaler Internet Access, choose Zscaler Internet Access (ZIA) as the data source. After filling in the required information and you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to DNS Activity (4003), HTTP Activity (4002), Network Activity (4001), and Authentication (3002). Each event comes from a source as mentioned below.

**DNS Activity** covers all events from source:

- DNS Logs

**HTTP Activity** covers all events from source:

- Web Logs

**Network Activity** covers all events from source:

- Firewall Logs

**Authentication** covers events from source:

- Admin Audit Logs - Event actions: SIGN_IN, SIGN_OUT
