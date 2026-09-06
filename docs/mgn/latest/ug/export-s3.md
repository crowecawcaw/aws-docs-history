

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Exporting your data inventory to an S3 bucket
<a name="export-s3"></a>

To export your inventory to an S3 bucket, take the following steps:

1. Select **Export** from the left-hand navigation menu (under** Import and export**) and you’ll be navigated to the **Export inventory** tab.

1. Select **Export to S3 bucket**.

1. Choose **Browse S3** to choose the Amazon S3 storage target to which you want to export the data.

1. Specify the Amazon S3 bucket owner (the current AWS account or a different one) according to your preferences. If you select a different AWS account, you must enter the bucket owner’s account ID.
**Note**  
You must have write privileges to export an inventory to a specific bucket.
It is highly recommended that you [apply S3 bucket security practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) where your CSV files are stored. [Learn more about S3 permissions and policies.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html)

1. Choose **Export**.