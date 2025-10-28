# Step 3: Configure security settings

**IAM role**

The crawler assumes this role. It must have permissions similar to the AWS managed
policy `AWSGlueServiceRole`. For Amazon S3 and DynamoDB sources, it must also have
permissions to access the data store. If the crawler reads Amazon S3 data encrypted with
AWS Key Management Service (AWS KMS), then the role must have decrypt permissions on the AWS KMS key.

For an Amazon S3 data store, additional permissions attached to the role would be similar
to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket/object`*"
 ]
 }
 ]
}`

```

For an Amazon DynamoDB data store, additional permissions attached to the role would be
similar to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeTable",
 "dynamodb:Scan"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:`111122223333`:table/`table-name`*"
 ]
 }
 ]
}`

```

In order to add your own JDBC driver, additional permissions need to be added.

- Grant permissions for the following job actions: `CreateJob`, `DeleteJob`,
  `GetJob`, `GetJobRun`, `StartJobRun`.
- Grant permissions for Amazon S3 actions: `s3:DeleteObjects`, `s3:GetObject`,
  `s3:ListBucket`, `s3:PutObject`.

###### Note

The `s3:ListBucket` is not needed if the Amazon S3 bucket policy is disabled.

- Grant service principal access to bucket/folder in the Amazon S3 policy.

Example Amazon S3 policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/driver-parent-folder/driver.jar",
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 }
 ]
}`

```

AWS Glue creates the following folders (`_crawler` and `_glue_job_crawler`
at the same level as the JDBC driver in your Amazon S3 bucket. For example, if the driver path is
`<s3-path/driver_folder/driver.jar>`, then the following folders
will be created if they do not already exist:

- <s3-path/driver_folder/\_crawler>
- <s3-path/driver_folder/\_glue_job_crawler>

Optionally, you can add a security configuration to a crawler to specify at-rest encryption options.

For more information, see [Step 2: Create an IAM role for AWS Glue](create-an-iam-role.md "create-an-iam-role.md") and [Identity and access management for AWS Glue](security-iam.md "security-iam.md").

**Lake Formation configuration - optional**

Allow the crawler to use Lake Formation credentials for crawling the data source.

Checking **Use Lake Formation credentials for crawling S3 data source** will allow the crawler to use Lake Formation credentials for crawling the data source. If the data source belongs to another account, you must provide the registered account ID. Otherwise, the crawler will crawl only those data sources associated to the account. Only applicable to Amazon S3 and Data Catalog data sources.

**Security configuration - optional**

Settings include security configurations. For more information, see the following:

- [Encrypting data written by
  AWS Glue](encryption-security-configuration.md "encryption-security-configuration.md")

###### Note

Once a security configuration has been set on a crawler, you can change, but you cannot remove it.
To lower the level of security on a crawler, explicitly set the security feature to `DISABLED` within your configuration, or create a new
crawler.
