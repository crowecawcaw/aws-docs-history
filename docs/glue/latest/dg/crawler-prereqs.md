# Crawler prerequisites

The crawler assumes the permissions of the AWS Identity and Access Management (IAM) role that you specify when
you define it. This IAM role must have permissions to extract data from your data store and
write to the Data Catalog. The AWS Glue console lists only IAM roles that have attached a trust policy
for the AWS Glue principal service. From the console, you can also create an IAM role with an IAM
policy to access Amazon S3 data stores accessed by the crawler. For more information about
providing roles for AWS Glue, see [Identity-based
policies for AWS Glue](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").

###### Note

When crawling a Delta Lake data store, you must have Read/Write permissions to the Amazon S3 location.

For your crawler, you can create a role and attach the following policies:

- The `AWSGlueServiceRole` AWS managed policy, which grants the required
  permissions on the Data Catalog
- An inline policy that grants permissions on the data source.
- An inline policy that grants `iam:PassRole` permission on the role.
  A quicker approach is to let the AWS Glue console crawler wizard create a role for you. The
  role that it creates is specifically for the crawler, and includes the
  `AWSGlueServiceRole` AWS managed policy plus the required inline policy for the
  specified data source.

If you specify an existing role for a crawler, ensure that it includes the
`AWSGlueServiceRole` policy or equivalent (or a scoped down version of this
policy), plus the required inline policies. For example, for an Amazon S3 data store, the inline
policy would at a minimum be the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket/object`*"
 ]
 }
 ]
}`

```

For an Amazon DynamoDB data store, the policy would at a minimum be the following:

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
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`table-name`*"
 ]
 }
 ]
}`

```

In addition, if the crawler reads AWS Key Management Service (AWS KMS) encrypted Amazon S3 data, then the
IAM role must have decrypt permission on the AWS KMS key. For more information, see [Step 2: Create an IAM role for AWS Glue](create-an-iam-role.md "create-an-iam-role.md").
