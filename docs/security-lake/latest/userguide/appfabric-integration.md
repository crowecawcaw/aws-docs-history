# Integration with AWS AppFabric

**Integration type:** Source

[AWS AppFabric](../../../appfabric/latest/adminguide/what-is-appfabric.md "../../../appfabric/latest/adminguide/what-is-appfabric.md") is a no-code service that connects software as a service
(SaaS) applications across your organization, so IT and security applications
using a standard schema and central repository.

## How Security Lake receives

AppFabric findings

You can send AppFabric audit log data to Security Lake by selecting Amazon Kinesis Data
Firehose as a destination and configuring Kinesis Data Firehose to deliver data in OCSF
schema and Apache Parquet format to Security Lake.

## Prerequisites

Before you can send AppFabric audit logs to Security Lake, you must output your OCSF
normalized audit logs to a Kinesis Data Firehose stream. You can then configure Kinesis
Data Firehose to send the output to your Security Lake Amazon S3 bucket. For more
information, see [Choose
Amazon S3 for your destination](../../../firehose/latest/dev/create-destination.md#create-destination-s3 "../../../firehose/latest/dev/create-destination.md#create-destination-s3") in the
_Amazon Kinesis Developer Guide_.

## Send your AppFabric findings to

Security Lake

To send AppFabric audit logs to Security Lake after completing the preceding
prerequisite, you must enable both services and add AppFabric as a custom source in
Security Lake. For instructions on adding a custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

## Stop receiving AppFabric logs in

Security Lake

To stop receiving AppFabric audit logs, you can use the Security Lake console,
Security Lake API, or AWS CLI to delete AppFabric as a custom source. For instructions,
see [Deleting a custom source from Security Lake](delete-custom-source.md "delete-custom-source.md").
