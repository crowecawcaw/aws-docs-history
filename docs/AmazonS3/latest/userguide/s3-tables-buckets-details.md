# Viewing details about an Amazon S3 table bucket

You can view the general details of an Amazon S3 table bucket, such as bucket owner and type, in the console or programmatically. You can view default encryption settings,
and maintenance settings programmatically by using the S3 Tables REST API, AWS CLI or
AWS SDKs.

## Viewing table bucket details

This example shows how to get details about a table bucket by using the
AWS CLI. To use this example, replace the `user input
 placeholders` with your own information.

```
aws s3tables get-table-bucket --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket
```

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table
   buckets**.
3. Select your table bucket.
4. Select the **Properties** tab.

## Viewing table bucket encryption settings

For more information about table bucket encryption, see [Using server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-encryption.md "s3-tables-kms-encryption.md").

This example shows how to get details about encryption settings for a
table bucket by using the AWS CLI. To use this example, replace the

`user input placeholders` with your own
information.

```
aws s3tables get-table-bucket-encryption --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket
```

## Viewing table bucket maintenance configurations

For information about maintenance settings, see [Maintenance for table buckets](s3-table-buckets-maintenance.md "s3-table-buckets-maintenance.md")

This example shows how to get details about maintenance configuration settings
for a table bucket by using the AWS CLI. To use this example, replace the

`user input placeholders` with your own
information.

```
aws s3tables get-table-bucket-maintenance-configuration --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket
```
