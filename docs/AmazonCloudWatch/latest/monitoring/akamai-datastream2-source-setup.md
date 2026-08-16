# Source configuration for Akamai DataStream 2

## Integrating with Akamai DataStream 2

To integrate Akamai DataStream 2 Data Replicator with CloudWatch Logs, you must configure
both the source and the pipeline. First, set up your Akamai DataStream 2 source by
configuring Amazon S3 and Amazon SQS to receive data. Then, configure the CloudWatch pipeline to
ingest the data from your source into CloudWatch Logs.

## Log forwarding setup

Akamai DataStream 2 supports real-time log delivery through DataStream 2 to
[forward logs to Amazon S3](https://techdocs.akamai.com/datastream2/v3/docs/stream-amazon-s3 "https://techdocs.akamai.com/datastream2/v3/docs/stream-amazon-s3").

## Instructions to setup Amazon S3 and Amazon SQS

Configuring Akamai DataStream 2 to send logs to an Amazon S3 bucket involves several
steps. These steps focus on setting up the Amazon S3 bucket, Amazon SQS queue, and IAM roles,
and then configuring the CloudWatch pipeline.

- Create an Amazon S3 bucket that stores Akamai logs and create separate folders
  for each log type (for example, DNS, CDN, EdgeWorkers). Create an IAM user
  and grant S3 write permission, then create an access key and secret key for
  this account.
- Make sure the Akamai DataStream 2 log exporter is configured to send logs to
  Amazon S3. DataStream 2 uploads logs to Amazon S3 over TLS, so you need to enable
  [server-side
  encryption](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md") for Amazon S3. Refer to the [Akamai S3 streaming setup guide](https://techdocs.akamai.com/datastream2/v3/docs/stream-amazon-s3 "https://techdocs.akamai.com/datastream2/v3/docs/stream-amazon-s3") for detailed instructions.
- Configure the Amazon S3 bucket to create event notifications, specifically for
  "Object Create" events. These notifications should be sent to an Amazon SQS
  queue.
- Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This
  queue will receive notifications when new log files are added to the Amazon S3
  bucket.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Akamai DataStream 2, choose
Akamai DataStream 2 as the data source. After filling in the required information
and you create the pipeline, data will be available in the selected CloudWatch Logs log
group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and [Akamai
DataStream 2](https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters "https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters") events that map to DNS Activity (4003), HTTP Activity (4002),
and Base Event (0). Any events that don't conform to the mentioned OCSF schema are
passed through.

**DNS Activity (4003)** contains the following event logs:

- [DNS Logs](https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edge-dns-and-global-traffic-management-fields "https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edge-dns-and-global-traffic-management-fields")
- [GTM Logs](https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edge-dns-and-global-traffic-management-fields "https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edge-dns-and-global-traffic-management-fields")

**HTTP Activity (4002)** contains the following event logs:

- [CDN Logs](https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#delivery-fields "https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#delivery-fields")

**Base Event (0)** contains the following event logs:

- [EdgeWorkers Logs](https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edgeworkers-fields "https://techdocs.akamai.com/datastream2/v3/docs/data-set-parameters#edgeworkers-fields")

###### Note

DNS and Global Traffic Management (GTM) logs share the same format. No
separate OCSF mappings are required.

Events that do not match any OCSF mapping transformation are automatically passed
through and sent directly to the configured sink without additional processing.
