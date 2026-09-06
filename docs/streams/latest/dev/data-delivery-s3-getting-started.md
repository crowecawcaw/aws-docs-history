# Getting started with S3 general purpose delivery

This tutorial walks you through creating your first Amazon S3 delivery to send records
from an Amazon Kinesis Data Streams stream to a general purpose Amazon S3 bucket, verifying it, and cleaning up.

## Prerequisites

Before you begin, ensure the following prerequisites are met:

- A Kinesis Data Streams stream configured with On-Demand Standard or On-Demand
  Advantage capacity mode.
- An IAM service execution role that grants Kinesis Data Streams permission to
  deliver records to your destination. See [IAM permissions for data delivery](data-delivery-iam.md "data-delivery-iam.md").
- A general purpose Amazon S3 bucket for the destination.
- The AWS CLI installed and configured, if you use the AWS CLI.

## Step 1: Create the delivery

Create an Amazon S3 delivery with the AWS Management Console or the AWS CLI. For the full procedure
and all configuration options, see [Create an Amazon S3 delivery](data-delivery-s3-create.md "data-delivery-s3-create.md").

## Step 2: Verify the delivery

Verify that the delivery reached the ACTIVE state. For the procedure, see
[Describe an Amazon S3 delivery](data-delivery-s3-describe.md "data-delivery-s3-describe.md").

## Step 3: Monitor the delivery

After the delivery is active, monitor its health using Amazon CloudWatch metrics published in
the `AWS/Kinesis` namespace with the dimensions `ChannelName`
and `StreamName`. Amazon S3 delivery metrics are prefixed with
`DeliveryToS3`. For the full list of metrics, see
[Monitoring data delivery](data-delivery-monitoring.md "data-delivery-monitoring.md").

## Step 4: Clean up

To avoid ongoing charges, delete the resources you created when you no longer need
them. An active delivery continues to process records and incurs delivery charges
until you delete it, and any data already written to your destination continues to
incur Amazon S3 storage charges.

1. Delete the delivery. See [Delete an Amazon S3 delivery](data-delivery-s3-delete.md "data-delivery-s3-delete.md").
2. If you no longer need the service execution role – for example, if
   it is not used by any other delivery – delete it. Detach any customer managed
   policy, delete any inline policy, and then delete the role using the IAM
   `detach-role-policy`, `delete-role-policy`, and
   `delete-role` commands. For details, see
   [Deleting
   roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the _IAM User Guide_.
3. If you no longer need the destination bucket or the dead-letter queue
   bucket, delete them in Amazon S3 to stop incurring storage charges.
