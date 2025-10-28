End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Amazon S3 policies for AWS IoT Analytics resources

You can store processed data store messages in an Amazon S3 bucket managed by AWS IoT Analytics or in one
that you manage. When you create a data store, select the Amazon S3 bucket you want by using the
`datastoreStorage` API parameter. The default is a service-managed Amazon S3
bucket.

If you choose to have data store messages stored in an Amazon S3 bucket that you manage, you
must grant AWS IoT Analytics permission to perform these actions on your Amazon S3 bucket for you:

- `s3:GetBucketLocation`
- `s3:PutObject`
- `s3:DeleteObject`
  If you use the data store as a source for an SQL query dataset, set up an Amazon S3 bucket
  policy that grants AWS IoT Analytics permission to invoke Amazon Athena queries on the contents of your
  bucket.

###### Note

We recommend that you specify `aws:SourceArn` in your bucket policy to help
prevent the confused deputy security problem. This restricts access by allowing only
those requests that come from a specified account. For more information about the
confused deputy problem, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

The following is an example of a bucket policy that grants these required
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "MyPolicyID",
 "Statement": [
 {
 "Sid": "MyStatementSid",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`",
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:iotanalytics:`us-east-1`:`123456789012`:dataset/`your-dataset`",
 "arn:aws:iotanalytics:`us-east-1`:`123456789012`:datastore/`your-datastore`"
 ]
 }
 }
 }
 ]
}`

```

For more information, see [Cross-account access](../../../athena/latest/ug/cross-account-permissions.md "../../../athena/latest/ug/cross-account-permissions.md") in the _Amazon Athena User Guide_.

###### Note

If you update the options or permissions of your customer managed data store,
you
might need to reprocess channel data to ensure that any previously
ingested data is included in dataset contents. For more information, see [Reprocessing
channel data](reprocessing.md#aws-iot-analytics-reprocessing "reprocessing.md#aws-iot-analytics-reprocessing").
