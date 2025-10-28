# Create an Amazon S3 bucket for Amazon MWAA

This guide describes the steps to create an Amazon S3 bucket to store your Apache Airflow Directed Acyclic Graphs (DAGs), custom plugins in a `plugins.zip` file, and Python dependencies in a `requirements.txt` file.

###### Contents

- [Before you begin](mwaa-s3-bucket.md#mwaa-s3-bucket-before "mwaa-s3-bucket.md#mwaa-s3-bucket-before")
- [Create the bucket](mwaa-s3-bucket.md#mwaa-s3-bucket-create "mwaa-s3-bucket.md#mwaa-s3-bucket-create")
- [What's next?](mwaa-s3-bucket.md#mwaa-s3-bucket-next-up "mwaa-s3-bucket.md#mwaa-s3-bucket-next-up")

## Before you begin

- The Amazon S3 bucket name can't be changed after you create the bucket. To learn more, refer to [Rules for bucket naming](../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules") in the _Amazon Simple Storage Service User Guide_.
- An Amazon S3 bucket used for an Amazon MWAA environment must be configured to **Block all public access**, with **Bucket Versioning** enabled.
- An Amazon S3 bucket used for an Amazon MWAA environment must be located in the same AWS Region as an Amazon MWAA environment. To access a list of AWS Regions for Amazon MWAA, refer to
  [Amazon MWAA endpoints and quotas](../../../general/latest/gr/mwaa.md "../../../general/latest/gr/mwaa.md") in the _AWS General Reference_.

## Create the bucket

This section describes the steps to create the Amazon S3 bucket for your environment.

###### To create a bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. In **Bucket name**, enter a DNS-compliant name for your bucket.

The bucket name must:

    * Be unique across all of Amazon S3.
    * Be between 3 and 63 characters long.
    * Not contain uppercase characters.
    * Start with a lowercase letter or number.

###### Important

Avoid including sensitive information, such as account numbers, in the bucket name. The bucket name is available in the URLs that point to the objects in the bucket. 4. Choose an AWS Region in **Region**. This must be the same AWS Region as your Amazon MWAA environment.

    1. We recommend choosing a region close to you to minimize latency and costs and address regulatory requirements.

5. Choose **Block all public access**.
6. Choose **Enable** in **Bucket Versioning**.
7. **Optional** - _Tags_. Add key-value tag pairs to identify your Amazon S3 bucket in **Tags**. For example, `Bucket` : `Staging`.
8. **Optional** - _Server-side encryption_. You can optionally **Enable** one of the following encryption options on your Amazon S3 bucket.
   1. Choose **Amazon S3 key (SSE-S3)** in **Server-side encryption** to enable server-side encryption for the bucket.
   2. Choose **AWS Key Management Service key (SSE-KMS)** to use an AWS KMS key for encryption on your Amazon S3 bucket:
      1. **AWS managed key (aws/s3)** - If you choose this option, you can either use an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") managed by Amazon MWAA, or specify a [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for encryption of your Amazon MWAA environment.
      2. **Choose from your AWS KMS keys** or **Enter AWS KMS key ARN** - If you choose to specify a [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in this step, you must specify an AWS KMS key ID or ARN. [AWS KMS aliases and multi-region keys are not supported by Amazon MWAA](custom-keys-certs.md "custom-keys-certs.md"). The AWS KMS key you specify must also be used for encryption on your Amazon MWAA environment.

9. **Optional** - _Advanced settings_. If you want to enable Amazon S3 Object Lock:
   1. Choose **Advanced settings**, **Enable**.

   ###### Important

   Enabling Object Lock will permanently allow objects in this bucket to be locked. To learn more, refer to [Locking Objects Using Amazon S3 Object Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md") in the _Amazon Simple Storage Service User Guide_. 2. Choose the acknowledgement.

10. Choose **Create bucket**.

## What's next?

- Learn how to create the required Amazon VPC network for an environment in [Create the VPC network](vpc-create.md "vpc-create.md").
- Learn how to how to manage access permissions in [How do I set ACL bucket permissions?](../../../AmazonS3/latest/user-guide/set-bucket-permissions.md "../../../AmazonS3/latest/user-guide/set-bucket-permissions.md")
- Learn how to delete a storage bucket in [How do I delete an S3 Bucket?](../../../AmazonS3/latest/user-guide/delete-bucket.md "../../../AmazonS3/latest/user-guide/delete-bucket.md").
