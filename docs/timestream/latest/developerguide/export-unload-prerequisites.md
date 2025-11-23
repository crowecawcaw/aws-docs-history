For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Prerequisites for UNLOAD from Timestream for LiveAnalytics

Following are prerequisites for writing data to S3 using `UNLOAD` from
Timestream for LiveAnalytics.

- You must have permission to read data from the Timestream for LiveAnalytics table(s) to be used in an
  `UNLOAD` command.
- You must have an Amazon S3 bucket in the same AWS Region as your Timestream for LiveAnalytics
  resources.
- For the selected S3 bucket, ensure that the [S3 bucket
  policy](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") also has permissions to allow Timestream for LiveAnalytics to export the data.
- The credentials used to execute `UNLOAD` query must have necessary AWS Identity
  and Access Management (IAM) permissions that allows Timestream for LiveAnalytics to write the data
  to S3. An example policy would be as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "timestream:Select",
 "timestream:ListMeasures",
 "timestream:WriteRecords",
 "timestream:Unload"
 ],
 "Resource": "arn:aws:timestream:us-east-2:`111122223333`:database/`database_name`/table/`table_name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:PutObject",
 "s3:GetObject",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:::`S3_Bucket_Created`",
 "arn:aws:s3:::`S3_Bucket_Created`/*"
 ]
 }
 ]
}`

```

For additional context on these S3 write permissions, refer to the [Amazon Simple
Storage Service guide](../../../AmazonS3/latest/userguide/mpuoverview.md#mpuAndPermissions "../../../AmazonS3/latest/userguide/mpuoverview.md#mpuAndPermissions"). If you are using a KMS key for encrypting the
exported data, see the following for the additional IAM policies required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "arn:aws:kms:us-east-2:`111122223333`:key/*",
 "Condition": {
 "ForAnyValue:StringLike": {
 "kms:ResourceAliases": "alias/`Alias_For_Generated_Key`"
 }
 }
 }, {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "arn:aws:kms:us-east-2:`111122223333`:key/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "kms:EncryptionContextKeys": "aws:timestream:`database_name`"
 },
 "Bool": {
 "kms:GrantIsForAWSResource": true
 },
 "StringLike": {
 "kms:ViaService": "`timestream.us-east-2.amazonaws.com`"
 },
 "ForAnyValue:StringLike": {
 "kms:ResourceAliases": "alias/`Alias_For_Generated_Key`"
 }
 }
 }
]
}`

```
