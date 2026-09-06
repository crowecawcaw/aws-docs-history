

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Upload your event data to an Amazon S3 bucket
<a name="uploading-to-an-s3-bucket"></a>

After you create a CSV file with your event data, upload the file to your Amazon S3 bucket.

**To upload to an Amazon S3 bucket**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

   The **Create bucket** wizard opens.

1. In **Bucket name**, enter a DNS-compliant name for your bucket.

   The bucket name must:
   + Be unique across all of Amazon S3.
   + Be between 3 and 63 characters long.
   + Not contain uppercase characters.
   + Start with a lowercase letter or number.

   After you create the bucket, you can't change its name. For information about naming buckets, see [ Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules) in the *Amazon Simple Storage Service User Guide*.
**Important**  
Avoid including sensitive information, such as account numbers, in the bucket name. The bucket name is visible in the URLs that point to the objects in the bucket.

1. In **Region**, choose the AWS Region where you want the bucket to reside. You must select the same Region in which you are using Amazon Fraud Detector, that is US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Singapore) or Asia Pacific (Sydney). 

1. In **Bucket settings for Block Public Access**, choose the Block Public Access settings that you want to apply to the bucket. 

   We recommend that you leave all settings enabled. For more information about blocking public access, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide*.

1. Choose **Create bucket**.

1. Upload training data file to your Amazon S3 bucket. Note the Amazon S3 location path for your training file (for example, s3://bucketname/object.csv).