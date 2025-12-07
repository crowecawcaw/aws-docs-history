# Source configuration for SentinelOne

## Integrating with SentinelOne Singularity Endpoint

SentinelOne Singularity Endpoint is an AI-powered endpoint security platform that provides real-time protection against malware, ransomware, and zero-day attacks. It uses behavioral analysis and machine learning to detect and stop threats autonomously. The platform supports automated response, rollback, and threat remediation. It gives centralized visibility and control across all endpoints. CloudWatch pipelines enables you to collect this data in CloudWatch Logs.

## Instructions to setup Amazon S3 and Amazon SQS

Configuring SentinelOne Singularity Endpoint to send logs to an Amazon S3 bucket involves several steps, primarily focused on setting up the Amazon S3 bucket, Amazon SQS queue, IAM roles, and then configuring the Amazon Telemetry Pipeline.

- Create Amazon S3 bucket that stores SentinelOne Singularity Endpoint logs.
- Configure Singularity Cloud Funnel or intermediate Syslog server with Amazon S3 bucket details to push logs.
- Configure the Amazon S3 bucket to create event notifications, specifically for "Object Create" events. These notifications should be sent to an Amazon SQS queue.
- Create an Amazon SQS queue in the same AWS region as your Amazon S3 bucket. This queue will receive notifications when new log files are added to the Amazon S3 bucket.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose SentinelOne Singularity Endpoint as the data source. After filling in the required information and you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the SentinelOne Singularity Endpoint events that maps to File System Activity (1001), Process Activity (1007), HTTP Activity (4002) and DNS Activity (4003).

**File System Activity** contains the following events:

- MALICIOUSFILE
- FILECREATION
- FILEDELETION
- FILEMODIFICATION
- FILERENAME
- FILESCAN

**Process Activity** contains the following events:

- PROCESSCREATION
- PROCESSTERMINATION
- DUPLICATETHREAD
- REMOTETHREAD
- PROCESSMODIFICATION
- DUPLICATEPROCESS
- OPENPROCESS
- PROCESSINJECTION
- PROCESSMODIFIER
- PROCESSEXIT
- OPENPRIVILEGEDPROCESSFROMKERNEL

[Show moreShow less](# "#")
**HTTP Activity** contains the following events:

- HTTP

**DNS Activity** contains the following events:

- DNS
