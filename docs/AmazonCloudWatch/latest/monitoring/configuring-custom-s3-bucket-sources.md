# Configuring Custom S3 Bucket Sources

With CloudWatch pipelines, you can process arbitrary logs stored in S3 buckets.

## Prerequisites

To use Amazon S3 as the source for a pipeline, first create an S3 bucket. For
instructions, see [Creating a general
purpose bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md")in the _Amazon S3 User Guide_.

###### Note

If the S3 bucket used as a source in the pipeline is in a different AWS
account, you also need to enable cross-account read permissions on the bucket.
This allows the pipeline to read and process the data. To enable cross-account
permissions, see [Bucket owner
granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3
User Guide_.

If your S3 buckets are in multiple accounts, use a `bucket_owners`
map. For an example, see [Cross-account S3 access](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/s3/#cross-account-s3-access "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/s3/#cross-account-s3-access") in the _OpenSearch_ documentation.

To set up S3-SQS processing, you also need to perform the following steps:

- [Create an Amazon SQS queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.md").
- [Enable event notifications on the S3 bucket with the SQS queue as a
  destination](../../../AmazonS3/latest/userguide/enable-event-notifications.md "../../../AmazonS3/latest/userguide/enable-event-notifications.md").

## Configure the pipeline role

Unlike other source plugins that push data to a pipeline, the S3 source plugin has
a read-based architecture in which the pipeline pulls data from the source.
Therefore, in order for a pipeline to read from S3, you must specify a role within
the pipeline's S3 source configuration that has access to both the S3 bucket and the
Amazon SQS queue. The pipeline will assume this role in order to read data from the
queue.

You can find example role permissions in [Source-specific IAM
policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies"). Note that this role must have a trust relationship with the
CloudWatch pipelines service principle. You can find an example trust policy
configuration for your pipeline role in [Trust relationships](pipeline-iam-reference.md#trust-relationships "pipeline-iam-reference.md#trust-relationships").

## Create the pipeline

After you've set up your permissions, you can configure a pipeline depending on
your Amazon S3 use case.

Select **Create pipeline** in the **Pipelines** tab under **Ingestion** in the CloudWatch Console. Follow the pipeline wizard
steps and provide the SQS queue ARN and required pipeline IAM role when prompted.
Optionally provide a data source name and type to attach to the log group
destination in CloudWatch Logs.

Be sure to configure a [CloudWatch Logs resource policy](../../../resource-policies.md "../../../resource-policies.md") if one isn't already configured to the
destination log group and then select **Create
pipeline** in the **Review and create**
step. The pipeline will be created and data will begin to flow within 5 minutes if
successful.

## Amazon S3 cross account as a source

You can grant access across accounts with Amazon S3 so that CloudWatch pipelines
can access S3 buckets in another account as a source. To enable cross-account
access, see [Bucket owner
granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3
User Guide_. After you have granted access, ensure that your pipeline
role has the required permissions.

Then, you can create a pipeline using `bucket_owners` to enable
cross-account access to an Amazon S3 bucket as a source.

**Custom source configuration**

When creating a pipeline for custom sources:

- A parser must be the first processor in the pipeline
- You can specify any supported processor for custom log pipelines
