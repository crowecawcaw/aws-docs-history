

# Getting started with streaming tables
<a name="data-delivery-st-getting-started"></a>

 This tutorial walks you through creating your first streaming table delivery to send records from an Amazon Kinesis Data Streams stream to a streaming table on Apache Iceberg, verifying it, and cleaning up. 

## Prerequisites
<a name="data-delivery-st-gs-prerequisites"></a>

Before you begin, ensure the following prerequisites are met:
+ A Kinesis Data Streams stream configured with On-Demand Standard or On-Demand Advantage capacity mode.
+ An IAM service execution role that grants Kinesis Data Streams permission to deliver records to your destination. See [IAM permissions for data delivery](data-delivery-iam.md).
+ A schema registered in AWS Glue Schema Registry.
+ An S3 table bucket for the destination Iceberg table.
+ An Amazon S3 bucket for the dead-letter queue.
+ The AWS CLI installed and configured, if you use the AWS CLI.

## Step 1: Create the delivery
<a name="data-delivery-st-gs-create"></a>

 Create a streaming table delivery with the AWS Management Console or the AWS CLI. For the full procedure and all configuration options, see [Create a streaming table delivery](data-delivery-st-create.md). 

## Step 2: Verify the delivery
<a name="data-delivery-st-gs-verify"></a>

 Verify that the delivery reached the ACTIVE state. For the procedure, see [Describe a streaming table delivery](data-delivery-st-describe.md). 

## Step 3: Monitor the delivery
<a name="data-delivery-st-gs-monitor"></a>

 After the delivery is active, monitor its health using Amazon CloudWatch metrics published in the `AWS/Kinesis` namespace with the dimensions `ChannelName` and `StreamName`. Streaming table delivery metrics are prefixed with `DeliveryToIceberg`. For the full list of metrics, see [Monitoring data delivery](data-delivery-monitoring.md). 

## Step 4: Clean up
<a name="data-delivery-st-gs-cleanup"></a>

 To avoid ongoing charges, delete the resources you created when you no longer need them. An active delivery continues to process records and incurs delivery charges until you delete it, and any data already written to your destination continues to incur Amazon S3 storage charges. 

1. Delete the delivery. See [Delete a streaming table delivery](data-delivery-st-delete.md).

1. If you no longer need the service execution role – for example, if it is not used by any other delivery – delete it. Detach any customer managed policy, delete any inline policy, and then delete the role using the IAM `detach-role-policy`, `delete-role-policy`, and `delete-role` commands. For details, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*.

1. If you no longer need the destination table bucket or the dead-letter queue bucket, delete them in Amazon S3 to stop incurring storage charges.