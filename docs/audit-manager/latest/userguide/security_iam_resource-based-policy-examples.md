# Resource-based policy

examples for AWS Audit Manager

## Amazon S3 bucket policy

The following policy allows CloudTrail to deliver evidence finder query results to the
specified S3 bucket. As a security best practice, the IAM global condition key
`aws:SourceArn` helps ensure that CloudTrail writes to the S3 bucket only
for the event data store.

###### Important

You must specify an S3 bucket for CloudTrail Lake query results delivery. For more
information, see [Specifying an existing bucket for CloudTrail Lake query
results](../../../awscloudtrail/latest/userguide/s3-bucket-policy-lake-query-results.md#specify-an-existing-bucket-for-cloudtrail-query-results-delivery "../../../awscloudtrail/latest/userguide/s3-bucket-policy-lake-query-results.md#specify-an-existing-bucket-for-cloudtrail-query-results-delivery") .

Replace the `placeholder text` with your own information,
as follows:

- Replace `amzn-s3-demo-destination-bucket` with
  the S3 bucket that you use as your export destination.
- Replace `myQueryRunningRegion` with the
  appropriate AWS Region for your configuration.
- Replace `myAccountID` with the AWS account ID
  that's used for CloudTrail. This might not be the same as the AWS account ID for
  the S3 bucket. If this is an organization event data store, you must use the
  AWS account for the management account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": [
 "s3:PutObject*",
 "s3:Abort*"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket",
 "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:cloudtrail:myQueryRunningRegion:myAccountID:eventdatastore/*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:cloudtrail:myQueryRunningRegion:myAccountID:eventdatastore/*"
 }
 }
 }
 ]
 }`

```

## AWS Key Management Service policy

If your S3 bucket has the default encryption set to `SSE-KMS`, grant
access to CloudTrail in your AWS Key Management Service key's resource policy so it can use the key. In
this case, add the following resource policy to the AWS KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "s3.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*"
 }
 ]
}`

```
