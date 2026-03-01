# IAM roles for custom document enrichment in Amazon Q Business

Custom document enrichment (CDE) is an Amazon Q Business feature that you can use to
manipulate your document content and document attributes. When you use the Lambda functions for CDE, you need an IAM role for the following:

- A role for `PreExtractionHookConfiguration` with permissions to run
  `PreExtractionHookConfiguration` and to access the Amazon S3 bucket when
  you use `PreExtractionHookConfiguration`.
- A role for `PostExtractionHookConfiguration` with permissions to run
  `PreExtractionHookConfiguration` and to access the Amazon S3 bucket when
  you use `PostExtractionHookConfiguration`.

###### Important

IAM roles for Custom Document Enrichmmnt (CDE) Lambda functions should belong to the
same account as the account using [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation to configure CDE.

Both AWS Identity and Access Management (IAM) roles must have the permissions to:

- Run `PreExtractionHookConfiguration` and/or
  `PostExtractionHookConfiguration`. To apply advanced alterations of
  your document metadata and content during the ingestion process, configure a Lambda function for `PreExtractionHookConfiguration` and/or
  `PostExtractionHookConfiguration`.
- (Optional) If you choose to activate Server Side Encryption for your Amazon S3 bucket, you must provide permissions to use the AWS KMS key
  customer
  to encrypt and decrypt the objects stored in your Amazon S3 bucket.
  **A role policy to allow Amazon Q to run
  `PreExtractionHookConfiguration` with encryption for your Amazon S3 bucket.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Effect": "Allow",
 "Sid": "KMSPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:`pre-extraction-lambda-function`",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**An role policy to allow Amazon Q to run
`PreExtractionHookConfiguration` without encryption.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:pre-extraction-lambda-function",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**A role policy to allow Amazon Q to run
`PostExtractionHookConfiguration` with encryption for your Amazon S3 bucket.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/key-id"
 ],
 "Effect": "Allow",
 "Sid": "KMSPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:post-extraction-lambda-function",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**An role policy to allow Amazon Q to run
`PostExtractionHookConfiguration` without encryption.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:post-extraction-lambda-function",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

We recommend that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. Their inclusion limits permissions and
securely checks if `aws:sourceAccount` and `aws:sourceArn` are the
same values as provided in the IAM role policy for the
`sts:AssumeRole` action. This approach prevents unauthorized entities from
accessing your IAM roles and their permissions. For more information, see
[confused
deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Sid": "QBusinessTrustPolicy",
 "Effect": "Allow",
 "Condition": {
 "StringLike": {
 "aws:SourceArn": "arn:aws:qbusiness:your-region:123456789012:application/<application-id>/index/<index-id>"
 },
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 }
 },
 "Principal": {
 "Service": [
 "qbusiness.amazonaws.com"
 ]
 }
 }
 ]
}`

```
