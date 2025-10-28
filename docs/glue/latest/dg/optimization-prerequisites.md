#

Table optimization prerequisites

The table optimizer assumes the permissions of the AWS Identity and Access Management (IAM) role that you
specify when you enable optimization options (compaction, snapshot retention, and orphan file
delettion) for a table. You can either create s single role for all optimizers or create
separate roles for each optimizer.

###### Note

The orphan file deletion optimizer doesn't require the `glue:updateTable`
or `s3:putObject` permissions. The snapshot expiration and compaction optimizers
require the same set of permissions.

The IAM role must have the permissions to read data and
update metadata in the Data Catalog. You can create an IAM role and attach the following inline
policies:

- Add the following inline policy that grants Amazon S3 read/write permissions on the
  location for data that is not registered with AWS Lake Formation. This policy also includes
  permissions to update the table in the Data Catalog, and to permit AWS Glue to add logs in
  Amazon CloudWatch logs and publish metrics. For source data in Amazon S3 that isn't
  registered with Lake Formation, access is determined by IAM permissions policies for Amazon S3 and
  AWS Glue actions.

In the following inline policies, replace `bucket-name` with your Amazon S3
bucket name, `aws-account-id` and `region` with a valid AWS
account number and Region of the Data Catalog, `database_name` with the name of
your database, and `table_name` with the name of the table.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:UpdateTable",
 "glue:GetTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`<database-name>`/`<table-name>`",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`<database-name>`",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-compaction/logs:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-retention/logs:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-orphan-file-deletion/logs:*"
 ]
 }
 ]
}`

```

- Use the following policy to enable compaction for data registered with Lake Formation.

If the optimization role doesn't have `IAM_ALLOWED_PRINCIPALS` group
permissions granted on the table, the role requires Lake Formation `ALTER`,
`DESCRIBE`, `INSERT` and `DELETE` permissions on the
table.

For more information on registering an Amazon S3 bucket with Lake Formation, see [Adding an Amazon S3 location to your data lake](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:UpdateTable",
 "glue:GetTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`databaseName`/`tableName`",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`databaseName`",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-compaction/logs:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-retention/logs:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue/iceberg-orphan-file-deletion/logs:*"
 ]
 }
 ]
}`

```

- (Optional) To optimize Iceberg tables with data in Amazon S3 buckets encrypted using
  [Server-side encryption](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md"), the compaction role requires permissions to decrypt
  Amazon S3 objects and generate a new data key to write objects to the encrypted buckets. Add
  the following policy to the desired AWS KMS key. We support only bucket-level
  encryption.

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`<aws-account-id>`:role/`<optimizer-role-name>`"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*"
}
```

- (Optional) For data location registered with Lake Formation, the role used to register the location requires permissions to decrypt Amazon S3 objects
  and generate a new data key to write objects to the encrypted buckets. For more information, see [Registering an encrypted Amazon S3 location](../../../lake-formation/latest/dg/register-encrypted.md "../../../lake-formation/latest/dg/register-encrypted.md").
- (Optional) If the AWS KMS key is stored in a different AWS account, you need to
  include the following permissions to the compaction role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 ]
 }
 ]
}`

```

- The role you use to run compaction must have the `iam:PassRole` permission on the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`<optimizer-role-name>`"
 ]
 }
 ]
}`

```

- Add the following trust policy to the role for AWS Glue service to assume
  the IAM role to run the compaction process.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

- (Optional) To update the Data Catalog settings to enable catalog-level table optimizations, the IAM role used must have the `glue:UpdateCatalog`
  permission or AWS Lake Formation `ALTER CATALOG` permission on the root catalog. You can use `GetCatalog` API to verify the
  catalog properties.
