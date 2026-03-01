# Specifying server-side encryption with AWS KMS keys (SSE-KMS) in table buckets

All Amazon S3 table buckets have encryption configured by default, and all new tables created
in an table bucket are automatically encrypted at rest. Server-side encryption with Amazon S3
managed keys (SSE-S3) is the default encryption configuration for every table bucket. If you
want to specify a different encryption type, you can use server-side encryption with
AWS Key Management Service (AWS KMS) keys (SSE-KMS).

You can specify SSE-KMS encryption in your `CreateTableBucket` or
`CreateTable` requests, or you can set the default encryption configuration
in the table bucket in a `PutTableBucketEncryption` request.

###### Important

To allow automatic maintenance on SSE-KMS encrypted tables and table buckets you must
grant the maintenance.s3tables.amazonaws.com service principal permission to use your
KMS key. For more information, see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md").

## Specifying encryption for table buckets

You can specify SSE-KMS as the default encryption type when you create a new table
bucket, for examples, see [Creating a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md"). After creating a table bucket, you can
specify the use of SSE-KMS as the default encryption setting using REST API operations,
AWS SDKs, and the AWS Command Line Interface (AWS CLI).

###### Note

When you specify SSE-KMS as the default encryption type, the key you use for encryption must allow access to the S3 Tables maintenance service principal. If the maintenance service principal does not have access, you will be unable to create tables in that table bucket. For more information, see [Granting the S3 Tables maintenance service principal permissions to your KMS key](s3-tables-kms-permissions.md#tables-kms-maintenance-permissions "s3-tables-kms-permissions.md#tables-kms-maintenance-permissions").

To use the following example AWS CLI command, replace the `user input placeholders` with your own information.

```

aws s3tables put-table-bucket-encryption \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`; \
    --encryption-configuration '{
        "sseAlgorithm": "aws:kms",
        "kmsKeyArn": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
    }' \
    --region us-east-1

```

You can remove the default encryption setting for a table bucket using the [DeleteTableBucketEncryption](../API/API_s3TableBuckets_DeleteTableBucketEncryption.md "../API/API_s3TableBuckets_DeleteTableBucketEncryption.md") API operation. When you remove encryption
settings new tables created in the table bucket will use the default SSE-S3
encryption.

## Specifying encryption for tables

You can apply SSE-KMS encryption to a new table when you create it using query
engines, REST API operations, AWS SDKs, and the AWS Command Line Interface (AWS CLI). The encryption settings
you specify when creating a table take precedence over the default encryption setting of
the table bucket.

###### Note

When you use SSE-KMS encryption for a table the key you use for encryption must allow the S3 Tables maintenance service principal to access it. If the maintenance service principal does not have access, you will be unable to create the table. For more information, see [Granting the S3 Tables maintenance service principal permissions to your KMS key](s3-tables-kms-permissions.md#tables-kms-maintenance-permissions "s3-tables-kms-permissions.md#tables-kms-maintenance-permissions").

###### **Required permissions**

The following permissions are required to create encrypted tables

- `s3tables:CreateTable`
- `s3tables:PutTableEncryption`

The following AWS CLI example creates a new table with a basic schema, and encrypts it with a customer managed AWS KMS key. To use the command, replace the `user input placeholders` with your own information.

```
aws s3tables create-table \
  --table-bucket-arn "arn:aws:s3tables:`Region`:`ownerAccountId`:bucket/`amzn-s3-demo-table-bucket`" \
  --namespace "mydataset" \
  --name "orders" \
  --format "ICEBERG" \
  --encryption-configuration '{
    "sseAlgorithm": "aws:kms",
    "kmsKeyArn": "arn:aws:kms:`Region`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
  }' `\
 --metadata '{
 "iceberg": {
 "schema": {
 "fields": [
 {
 "name": "order_id",
 "type": "string",
 "required": true
 },
 {
 "name": "order_date",
 "type": "timestamp",
 "required": true
 },
 {
 "name": "total_amount",
 "type": "decimal(10,2)",
 "required": true
 }
 ]
 }
 }
 }'`

```
