# Importing

Terraform state file into AWS Resilience Hub

AWS Resilience Hub supports importing Terraform state files that are encrypted using
server-side encryption (SSE) with Amazon Simple Storage Service managed keys (SSE-S3) or with AWS Key Management Service
managed keys (SSE-KMS). If your Terraform state files are encrypted using
customer-provided encryption keys (SSE-C), you will not be able to import them using
AWS Resilience Hub.

Importing Terraform state files into AWS Resilience Hub requires the following IAM
policies depending on where your state file is located.

## Importing Terraform state files from an Amazon S3 bucket located in the

primary account

The following Amazon S3 bucket policy and IAM policy are required to allow
AWS Resilience Hub read access to your Terraform state files located in an Amazon S3 bucket on
the primary account.

- Bucket policy – A bucket policy on the target Amazon S3 bucket,
  which is located in the primary account. For more information, see the
  following example.
- Identity policy – The associated identity policy for the
  Invoker role defined for this application, or the AWS current IAM
  role AWS Resilience Hub on the primary AWS account. For more information, see
  the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::<s3-bucket-name>/<path-to-state-file>"
 },
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::<s3-bucket-name>"
 }
 ]
}`

```

###### Note

If you are using the
`AWSResilienceHubAsssessmentExecutionPolicy` managed
policy, `ListBucket` permission is not required.

###### Note

If your Terraform state files are encrypted using KMS, you must add the
following `kms:Decrypt` permission.

```
{
      "Effect": "Allow",
      "Action": [
              "kms:Decrypt",
      ],
      "Resource": "<arn_of_kms_key>"
}
```

## Importing Terraform state files from an Amazon S3 bucket located in a

secondary account

- Bucket policy – A bucket policy on the target Amazon S3 bucket,
  which is located in one of the secondary accounts. For more information,
  see the following example.
- Identity policy – The associated identity policy for the AWS
  account role, which is running AWS Resilience Hub on the primary AWS account.
  For more information, see the following example.

###### Note

If you are using the
`AWSResilienceHubAsssessmentExecutionPolicy` managed
policy, `ListBucket` permission is not required.

###### Note

If your Terraform state files are encrypted using KMS, you must add the
following `kms:Decrypt` permission.

```
{
      "Effect": "Allow",
      "Action": [
              "kms:Decrypt",
      ],
      "Resource": "<arn_of_kms_key>"
}
```
