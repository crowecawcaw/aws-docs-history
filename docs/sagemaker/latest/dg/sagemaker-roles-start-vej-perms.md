# `StartVectorEnrichmentJob`

API: Execution role permissions

For an execution role that you can pass in a `StartVectorEnrichmentJob` API
request, you can attach the following minimum permissions policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "sagemaker-geospatial:GetVectorEnrichmentJob",
 "Resource": "arn:aws:sagemaker-geospatial:*:*:vector-enrichment-job/*"
 }
 ]
 }`

```

If your input Amazon S3 bucket is encrypted using server-side encryption with
an AWS KMS managed key (SSE-KMS), see [Using Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") for
more information.
