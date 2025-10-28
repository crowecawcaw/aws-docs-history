# AWS managed policies for Amazon SageMaker geospatial

These AWS managed policies add permissions required to use SageMaker geospatial. The policies
are available in your AWS account and are used by execution roles created from the SageMaker AI console.

###### Topics

- [AWS
  managed policy: AmazonSageMakerGeospatialFullAccess](#security-iam-awsmanpol-AmazonSageMakerGeospatialFullAccess "#security-iam-awsmanpol-AmazonSageMakerGeospatialFullAccess")
- [AWS
  managed policy: AmazonSageMakerGeospatialExecutionRole](#security-iam-awsmanpol-AmazonSageMakerGeospatialExecutionRole "#security-iam-awsmanpol-AmazonSageMakerGeospatialExecutionRole")
- [Amazon SageMaker AI updates to Amazon SageMaker geospatial
  managed policies](#security-iam-awsmanpol-geospatial-updates "#security-iam-awsmanpol-geospatial-updates")

## AWS

managed policy: AmazonSageMakerGeospatialFullAccess

This policy grants permissions that allow full access to Amazon SageMaker geospatial through the AWS Management Console
and SDK.

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker-geospatial` – Allows principals full access to all
  SageMaker geospatial resources.
- `iam` – Allows principals to pass an IAM role to SageMaker geospatial.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sagemaker-geospatial:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": ["iam:PassRole"],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker-geospatial.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonSageMakerGeospatialExecutionRole

This policy grants permissions commonly needed to use SageMaker geospatial.

**Permissions details**

This AWS managed policy includes the following permissions.

- `s3` – Allows principals to add and retrieve objects from Amazon S3
  buckets. These objects are limited to those whose name contains "SageMaker",
  "Sagemaker", or "sagemaker".
- `sagemaker-geospatial` – Allows principals to access Earth
  observation jobs through the `GetEarthObservationJob` API.

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
 "Action": "sagemaker-geospatial:GetEarthObservationJob",
 "Resource": "arn:aws:sagemaker-geospatial:*:*:earth-observation-job/*"
 },
 {
 "Effect": "Allow",
 "Action": "sagemaker-geospatial:GetRasterDataCollection",
 "Resource": "arn:aws:sagemaker-geospatial:*:*:raster-data-collection/*"
 }
 ]
}`

```

## Amazon SageMaker AI updates to Amazon SageMaker geospatial

managed policies

View details about updates to AWS managed policies for SageMaker geospatial since this service
began tracking these changes.

| Policy                                                                                                                                                                                     | Version | Change                                                         | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------------------- | ----------------- |
| [AmazonSageMakerGeospatialExecutionRole](#security-iam-awsmanpol-AmazonSageMakerGeospatialExecutionRole "#security-iam-awsmanpol-AmazonSageMakerGeospatialExecutionRole") - Updated policy | 2       | Add `sagemaker-geospatial:GetRasterDataCollection` permission. | May 10, 2023      |
| [AmazonSageMakerGeospatialFullAccess](#security-iam-awsmanpol-AmazonSageMakerGeospatialFullAccess "#security-iam-awsmanpol-AmazonSageMakerGeospatialFullAccess") - New policy              | 1       | Initial policy                                                 | November 30, 2022 |
| AmazonSageMakerGeospatialExecutionRole - New policy                                                                                                                                        | 1       | Initial policy                                                 | November 30, 2022 |
