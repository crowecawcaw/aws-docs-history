# Prerequisites for generating column

statistics

To generate or update column statistics, the statistics generation task assumes an
AWS Identity and Access Management (IAM) role on your behalf. Based on the permissions granted to the role, the
column statistics generation task can read the data from the Amazon S3 data store.

When you configure the column statistics generation task, AWS Glue allows you to create a
role that includes the `AWSGlueServiceRole` AWS managed policy plus the
required inline policy for the specified data source.

If you specify an existing role for generating column statistics, ensure that it
includes the `AWSGlueServiceRole` policy or equivalent (or a scoped down
version of this policy), plus the required inline policies. Follow these steps to create
a new IAM role:

###### Note

To generate statistics for tables managed by Lake Formation, the IAM role used to generate statistics requires full table access.

When you configure the column statistics generation task, AWS Glue allows you to create a
role that includes the `AWSGlueServiceRole` AWS managed policy plus the
required inline policy for the specified data source.
You can also create a role and attach the the permissions listed in the policy below, and add that role
to the column statistics generation task.

###### To create an IAM role for generating column statistics

1. To create an IAM role, see [Create an IAM role for
   AWS Glue](create-an-iam-role.md "create-an-iam-role.md").
2. To update an existing role, in the IAM console, go to the IAM role that is being used by the generate
   column statistics process.
3. In the **Add permissions** section, choose **Attach policies**. In the newly opened
   browser window, choose `AWSGlueServiceRole` AWS managed policy.
4. You also need to include permissions to read data from the Amazon S3 data location.

In the **Add permissions** section, choose **Create policy**. In the newly opened
browser window, create a new policy to use with your role. 5. In the **Create policy** page, choose the
**JSON** tab. Copy the following `JSON` code
into the policy editor field.

###### Note

In the following policies, replace account ID with a valid AWS account,
and replace `region` with the Region of the table, and
`bucket-name` with the Amazon S3 bucket name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 }
 ]
}`

```

6. (Optional) If you're using Lake Formation permissions to provide access to your data, the IAM role
   requires `lakeformation:GetDataAccess` permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationDataAccess",
 "Effect": "Allow",
 "Action": "lakeformation:GetDataAccess",
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

If the Amazon S3 data location is registered with Lake Formation, and the IAM role assumed
by the column statistics generation task doesn't have
`IAM_ALLOWED_PRINCIPALS` group permissions granted on the table,
the role requires Lake Formation `ALTER` and `DESCRIBE` permissions
on the table. The role used for registering the Amazon S3 bucket requires Lake Formation
`INSERT` and `DELETE` permissions on the table.

If the Amazon S3 data location is not registered with Lake Formation, and the IAM role
doesn't have `IAM_ALLOWED_PRINCIPALS` group permissions granted on
the table, the role requires Lake Formation `ALTER`,
`DESCRIBE`, `INSERT` and `DELETE`
permissions on the table. 7. If you've enabled the catalog-level `Automatic statistics
 generation` option, the IAM role must have the
`glue:UpdateCatalog` permission or the Lake Formation `ALTER
 CATALOG` permission on the default Data Catalog. You can use the
`GetCatalog` operation to verify the catalog properties. 8. (Optional) The column statistics generation task that writes encrypted
Amazon CloudWatch Logs requires the following permissions in the key
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CWLogsKmsPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:AssociateKmsKey"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-glue:*"
 ]
 },
 {
 "Sid": "KmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt",
 "kms:Encrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`arn of key used for ETL cloudwatch encryption`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "glue.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

9. The role you use to run column statistics must have the `iam:PassRole` permission on the role.

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
 "arn:aws:iam::`111122223333`:role/`columnstats-role-name`"
 ]
 }
 ]
}`

```

10. When you create an IAM role for generating column statistics, that role must
    also have the following trust policy that enables the service to assume the
    role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
