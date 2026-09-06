

# Source configuration for F5 BIG-IP
<a name="f5-bigip-source-setup"></a>

## Integrating with F5 BIG-IP
<a name="f5-bigip-integration"></a>

To integrate F5 BIG-IP with CloudWatch Logs, you must configure both the source and the pipeline. First, set up your F5 BIG-IP source by configuring Amazon S3 and Amazon SQS to receive data. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

## Setup log forwarding
<a name="f5-bigip-log-forwarding"></a>

F5 BIG-IP supports real-time log delivery through Telemetry Streaming to [forward logs to Amazon S3](https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/setting-up-consumer.html#awss3-ref).

## Instructions to setup Amazon S3 and Amazon SQS
<a name="f5-bigip-s3-sqs-setup"></a>

Configuring F5 BIG-IP to send logs to an Amazon S3 bucket involves several steps. These steps focus on setting up the Amazon S3 bucket, Amazon SQS queue, and IAM credentials, and then configuring Telemetry Streaming and the CloudWatch pipeline.
+ Make sure F5 BIG-IP Telemetry Streaming is installed and configured. Create an Amazon S3 bucket to store logs. It is recommended to enable server-side encryption for security.
+ Amazon S3 bucket that stores the F5 BIG-IP logs should reside in the same AWS Region.
+ Configure the Amazon S3 bucket to create event notifications, specifically for "Object Create" events. These notifications should be sent to an Amazon SQS queue.
+ Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue will receive notifications when new log files are added to the Amazon S3 bucket.

## Configuring F5 BIG-IP log forwarding
<a name="f5-bigip-telemetry-streaming"></a>
+ Install and verify the Telemetry Streaming (TS) extension.
+ Create a log destination (Amazon S3, CloudWatch, or other supported destination).
+ Create a log publisher and map the destination.
+ Create a logging profile specific to each module (for example, ASM, Advanced WAF).
+ Apply the logging profile to the virtual server.
+ Configure Telemetry Streaming (JSON declaration).
+ Define the destination S3 bucket and log types.

## Configuring Telemetry Streaming
<a name="f5-bigip-ts-config"></a>
+ Configure Telemetry Streaming using the declarative API endpoint: `/mgmt/shared/telemetry/declare`.
+ Define the Telemetry configuration with class `Telemetry`.
+ Define a Telemetry Listener to receive logs (for example, port 6514).
+ Define a Telemetry Consumer of type Amazon S3: configure the bucket name and Region, and provide IAM access key and secret key for authentication.

## Configuring the CloudWatch Pipeline
<a name="f5-bigip-pipeline-config"></a>

When configuring the pipeline to read data from F5 BIG-IP, choose F5 BIG-IP as the data source. After filling in the required information and you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="f5-bigip-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and F5 BIG-IP events that map to Network Activity (4001) and HTTP Activity (4002). The following lists show the source for each event.

**Network Activity (4001)** contains the following log formats:
+ [AFM](https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/event-listener.html#afm)
+ [APM](https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/event-listener.html#apm)

**HTTP Activity (4002)** contains the following log formats:
+ [ASM](https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/event-listener.html#asm)
+ [LTM](https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/event-listener.html#requestlog)
+ Advanced WAF

Events that do not match any OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.