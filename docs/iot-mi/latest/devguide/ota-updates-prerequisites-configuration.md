# Prerequisites

Before creating OTA tasks, you must configure the following prerequisites:

## Configure Amazon S3 access

To enable OTA updates, you must upload your job documents to an Amazon S3 bucket and
configure appropriate access permissions:

1. Upload your OTA job document to an S3 bucket
2. Add an Amazon S3 bucket policy that grants managed integrations access to your job documents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PolicyForS3JobDocument",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotmanagedintegrations.amazonaws.com"
 },
 "Action": "s3:GetObject",
 "Resource": [
 "arn:aws:s3:::YOUR_BUCKET/*",
 "arn:aws:s3:::YOUR_BUCKET/ota_job_document.json",
 "arn:aws:s3:::YOUR_BUCKET"
 ]
 }
 ]
}`

```
