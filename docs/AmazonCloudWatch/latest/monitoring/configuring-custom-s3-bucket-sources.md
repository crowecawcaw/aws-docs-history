

# Configuring Custom S3 Bucket Sources
<a name="configuring-custom-s3-bucket-sources"></a>

With CloudWatch pipelines, you can process arbitrary logs stored in S3 buckets.

## Prerequisites
<a name="s3-prerequisites"></a>

To use Amazon S3 as the source for a pipeline, first create an S3 bucket. For instructions, see [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)in the *Amazon S3 User Guide*.

**Note**  
If the S3 bucket used as a source in the pipeline is in a different AWS account, you also need to enable cross-account read permissions on the bucket. This allows the pipeline to read and process the data. To enable cross-account permissions, see [Bucket owner granting cross-account bucket permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon S3 User Guide*.  
If your S3 buckets are in multiple accounts, use a `bucket_owners` map. For an example, see [Cross-account S3 access](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/s3/#cross-account-s3-access) in the *OpenSearch* documentation.

To set up S3-SQS processing, you also need to perform the following steps:
+ [Create an Amazon SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.html).
+ [ Enable event notifications on the S3 bucket with the SQS queue as a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html).

## Configure the pipeline role
<a name="configure-pipeline-role"></a>

Unlike other source plugins that push data to a pipeline, the S3 source plugin has a read-based architecture in which the pipeline pulls data from the source. Therefore, in order for a pipeline to read from S3, you must specify a role within the pipeline's S3 source configuration that has access to both the S3 bucket and the Amazon SQS queue. The pipeline will assume this role in order to read data from the queue.

You can find example role permissions in [Source-specific IAM policies](pipeline-iam-reference.md#source-specific-iam-policies). Note that this role must have a trust relationship with the CloudWatch pipelines service principle. You can find an example trust policy configuration for your pipeline role in [Trust relationships](pipeline-iam-reference.md#trust-relationships).

## Create the pipeline
<a name="create-s3-pipeline"></a>

After you've set up your permissions, you can configure a pipeline depending on your Amazon S3 use case.

Select **Create pipeline** in the **Pipelines** tab under **Ingestion** in the CloudWatch Console. Follow the pipeline wizard steps and provide the SQS queue ARN and required pipeline IAM role when prompted. Optionally provide a data source name and type to attach to the log group destination in CloudWatch Logs.

Be sure to configure a [CloudWatch Logs resource policy](https://docs.aws.amazon.com/resource-policies.html) if one isn't already configured to the destination log group and then select **Create pipeline** in the **Review and create** step. The pipeline will be created and data will begin to flow within 5 minutes if successful.

## Amazon S3 cross account as a source
<a name="cross-account-s3-access"></a>

You can grant access across accounts with Amazon S3 so that CloudWatch pipelines can access S3 buckets in another account as a source. To enable cross-account access, see [Bucket owner granting cross-account bucket permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon S3 User Guide*. After you have granted access, make sure that your pipeline role has the required permissions.

Then, you can create a pipeline using `bucket_owners` to enable cross-account access to an Amazon S3 bucket as a source.

**Custom source configuration**

When creating a pipeline for custom sources:
+ A parser must be the first processor in the pipeline
+ You can specify any supported processor for custom log pipelines