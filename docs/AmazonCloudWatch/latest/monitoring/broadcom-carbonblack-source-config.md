# Source configuration for Broadcom Carbon Black

## Integrating with Broadcom Carbon Black

CloudWatch Pipeline ingests Broadcom Carbon Black event data from Amazon S3. You configure Carbon Black Cloud to export event data to an Amazon S3 bucket, then create a pipeline that reads from that bucket using Amazon SQS notifications.

To integrate CloudWatch Pipelines with Broadcom Carbon Black, complete the following high-level steps:

- Configure Carbon Black Cloud Data Forwarder to export events to an Amazon S3 bucket.
- Set up Amazon SQS notifications on the Amazon S3 bucket for new object creation.
- Create the required IAM role for pipeline access.
- Create a CloudWatch pipeline with Broadcom Carbon Black as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, ensure you have the following:

- A Broadcom Carbon Black Cloud account with Data Forwarder access
- An Amazon S3 bucket configured to receive Carbon Black event exports
- An Amazon SQS queue configured with Amazon S3 event notifications
- An AWS account with permissions to create and manage CloudWatch Pipelines

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Broadcom Carbon Black as the data source. Provide the Amazon SQS queue URL and IAM role ARN. Once you create and activate the pipeline, EDR event data from Carbon Black will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Detection Finding [2004]** – Alert events (CB Analytics, Container Runtime, Device Control, Firewall, IDS, Watchlist)
- **Authentication [3002]** – Authentication/logon events
- **Process Activity [1007]** – Process start and end events
- **Module Activity [1005]** – Module and script load events
- **File System Activity [1001]** – File modification events
- **Network Activity [4001]** – Network connection events
- **API Activity [6003]** – API call events
