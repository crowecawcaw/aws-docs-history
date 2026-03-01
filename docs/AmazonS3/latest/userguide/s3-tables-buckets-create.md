# Creating a table bucket

Amazon S3 table buckets are an S3 bucket type that you can use to create and store tables as S3
resources. To start using S3 Tables, you create a table bucket where you store and manage tables. When
you create a table bucket, you choose a bucket name and AWS Region. The table bucket name must be
unique for your account in the chosen Region. After you create a table bucket, you can't change the
bucket name or Region. For information about naming table buckets, see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md").

Table buckets have the following Amazon Resource Name (ARN) format:

```
arn:aws:s3tables:`region`:`owner-account-id`:bucket/`bucket-name`
```

By default, you can create up to 10 table buckets per Region in an AWS account. To request a
quota increase for table buckets or tables, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

When you create a table bucket you can specify the encryption type for that will be used to encrypt the tables you create in that bucket. For more information about bucket encryption options, see [Protecting S3 table data with encryption](s3-tables-encryption.md "s3-tables-encryption.md").

###### Prerequisites for creating table buckets

To create a table bucket, you must first do the following:

- Make sure that you have AWS Identity and Access Management (IAM) permissions for `s3tables:CreateTableBucket`.

###### Note

If you choose SSE-KMS as the default encryption type, you must have permissions for
`s3tables:PutTableBucketEncryption`, and have `DescribeKey` permission on the
chosen AWS KMS key. Additionally the AWS KMS key you use needs to grant S3 Tables permission to perform
automatic table maintenance. For more information, see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md").

To create a table bucket, you can use the Amazon S3 console, Amazon S3 REST API, AWS Command Line Interface (AWS CLI), or
AWS SDKs.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create a bucket.
3. In the left navigation pane, choose **Table buckets**.
4. Choose **Create table bucket** to open the **Create table bucket** page.
5. Under **Properties**, enter a name for your table bucket.

The table bucket name must:

    * Be unique within for your account in the current Region.
    * Be between 3 and 63 characters long
    * Consist only of lowercase letters, numbers, and hyphens (-).
    * Begin and end with a letter or number.

After you create the bucket, you can't change its name. The AWS account that creates
the bucket owns it. For information about naming table buckets, see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md"). 6. If you want to integrate your table buckets with AWS analytics services, make sure
**Enable integration** is selected under **Integration with AWS
analytics services**.

###### Note

When you create your first table bucket by using the console with the **Enable
integration** option selected, Amazon S3 attempts to automatically integrate your
table bucket with AWS analytics services. This integration allows you to use AWS analytics
services to query all tables in the current Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md"). 7. To configure default encryption, under **Encryption type**,
choose one of the following:

    * **Server-side encryption with Amazon S3 managed key
     (SSE-S3)**
    * **Server-side encryption with AWS Key Management Service key
     (SSE-KMS)**

For more information about encryption options for table data,
see [Protecting S3 table data with encryption](s3-tables-encryption.md "s3-tables-encryption.md"). 8. Choose **Create bucket**.
This example shows how to create a table bucket by using the AWS CLI. To use this example,
replace the `user input placeholders` with your own
information.

```
aws s3tables create-table-bucket \
    --region `us-east-2` \
    --name ``amzn-s3-demo-bucket1``

```

By default S3 table buckets use SSE-S3 as their default encryption setting, however, you can use the optional `--encryption-configuration` parameter to specify a different encryption type. The following examples shows how to create a bucket that uses SSE-KMS encryption. For more information on encryption settings for table buckets, see [Protecting S3 table data with encryption](s3-tables-encryption.md "s3-tables-encryption.md").

```
aws s3tables create-table-bucket \
    --region `us-east-2` \
    --name ``amzn-s3-demo-bucket1``
    --encryption-configuration '{
                    "sseAlgorithm": "aws:kms",
                    "kmsKeyArn": "arn:aws:kms:`Region`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`" }'

```
