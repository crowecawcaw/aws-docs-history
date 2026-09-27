

# Using Amazon S3 buckets with Amazon Braket
<a name="braket-s3-bucket-support"></a>

Braket can accept a bucket to `CreateQuantumTask` or `CreateHybridJob` when it satisfies either of the following conditions:
+ The bucket name begins with `amazon-braket-`.
+ The general-purpose bucket has a tag with key `AmazonBraket` and value `true` and is enabled for attribute-based access control (ABAC). 

  For instructions on enabling ABAC on your Amazon S3 bucket, see [Enabling attribute-based access control (ABAC) for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html). For instructions on adding the `AmazonBraket` tag, see [Adding a tag to a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-tag-add.html).

As a policy example, the [AmazonBraketJobsExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBraketJobsExecutionPolicy.html) managed policy shows how to allow Braket to use buckets with either condition satisfied.

**Amazon S3 ABAC is disabled by default on general-purpose buckets**  
You must enable Amazon S3 ABAC on a tagged general-purpose bucket before using it with Amazon Braket.