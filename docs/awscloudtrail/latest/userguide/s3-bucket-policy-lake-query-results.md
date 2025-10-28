# Amazon S3 bucket policy for CloudTrail Lake query results

By default, Amazon S3 buckets and objects are private. Only the resource owner (the AWS
account that created the bucket) can access the bucket and objects it contains. The resource
owner can grant access permissions to other resources and users by writing an access
policy.

To deliver CloudTrail Lake query results to an S3 bucket, CloudTrail must have the required permissions, and it
cannot be configured as a [Requester
Pays](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") bucket.

CloudTrail adds the following fields in the policy for you:

- The allowed SIDs
- The bucket name
- The service principal name for CloudTrail
  As a security best practice, add an `aws:SourceArn` condition key to the Amazon S3
  bucket policy. The IAM global condition key `aws:SourceArn` helps ensure that
  CloudTrail writes to the S3 bucket only for the event data store.

The following policy allows CloudTrail to deliver query results to the bucket from supported
AWS Regions. Replace `amzn-s3-demo-bucket`,
`myAccountID`, and
`myQueryRunningRegion` with the appropriate values for your
configuration. The `myAccountID` is the AWS account ID used for
CloudTrail, which may not be the same as the AWS account ID for the S3 bucket.

###### Note

If your bucket policy includes a statement for a KMS key, we recommend using a fully qualified
KMS key ARN. If you use a KMS key alias instead, AWS KMS resolves the key within the requester’s account.
This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket owner.

If this is an organization event data store, the event data store ARN must include the
AWS account ID for the management account. This is because the management account
maintains ownership of all organization resources.

**S3
bucket policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSCloudTrailLake1",
 "Effect": "Allow",
 "Principal": {"Service": "cloudtrail.amazonaws.com"},
 "Action": [
 "s3:PutObject*",
 "s3:Abort*"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:sourceAccount": "`111111111111`"
 },
 "ArnLike": {
 "aws:sourceArn": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/*"
 }
 }
 },
 {
 "Sid": "AWSCloudTrailLake2",
 "Effect": "Allow",
 "Principal": {"Service":"cloudtrail.amazonaws.com"},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:sourceAccount": "`111111111111`"
 },
 "ArnLike": {
 "aws:sourceArn": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/*"
 }
 }
 }
 ]
}`

```

###### Contents

- [Specifying an existing bucket for CloudTrail Lake query results](s3-bucket-policy-lake-query-results.md#specify-an-existing-bucket-for-cloudtrail-query-results-delivery "s3-bucket-policy-lake-query-results.md#specify-an-existing-bucket-for-cloudtrail-query-results-delivery")
- [Additional resources](s3-bucket-policy-lake-query-results.md#cloudtrail-lake-S3-bucket-policy-resources "s3-bucket-policy-lake-query-results.md#cloudtrail-lake-S3-bucket-policy-resources")

## Specifying an existing bucket for CloudTrail Lake query results

If you specified an existing S3 bucket as the storage location for CloudTrail Lake query
results delivery, you must attach a policy to the bucket that allows CloudTrail to deliver the
query results to the bucket.

###### Note

As a best practice, use a dedicated S3 bucket for CloudTrail Lake query results.

###### To add the required CloudTrail policy to an Amazon S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket where you want CloudTrail to deliver your Lake query results, and then
   choose **Permissions**.
3. Choose **Edit**.
4. Copy the [S3 bucket policy for query results](#s3-bucket-policy-lake-query "#s3-bucket-policy-lake-query") to the **Bucket Policy
   Editor** window. Replace the placeholders in italics with the names
   of your bucket, Region, and account ID.

###### Note

If the existing bucket already has one or more policies attached, add the
statements for CloudTrail access to that policy or policies. Evaluate the
resulting set of permissions to be sure that they are appropriate for the
users who access the bucket.

## Additional resources

For more information about S3 buckets and policies, see [Using
bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the _Amazon Simple Storage Service User Guide_.
