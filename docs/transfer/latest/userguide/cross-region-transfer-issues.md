# Troubleshoot cross-region transfer

issues

This section describes possible solutions for issues related to transferring files across
AWS Regions.

###### Topics

- [Troubleshoot cross-region transfer permission
  issues](#cross-region-permissions "#cross-region-permissions")
- [Troubleshoot cross-region transfer
  performance issues](#cross-region-performance "#cross-region-performance")

## Troubleshoot cross-region transfer permission

issues

Description

When attempting to transfer files between Amazon S3 buckets in different regions using Transfer Family
workflows, you encounter errors such as:

```
{
  "type": "StepErrored",
  "details": {
    "errorType": "BAD_REQUEST",
    "errorMessage": "Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied)",
    "stepType": "COPY",
    "stepName": "cross_region_copy"
  }
}
```

Cause

Cross-region transfers require specific IAM permissions for both the source and
destination buckets. The IAM role used by your Transfer Family server or workflow may not have
sufficient permissions to access buckets in other regions.

Solution

To resolve cross-region transfer permission issues:

1. Ensure your IAM role has permissions for both source and destination
   buckets:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::source-bucket-name/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::destination-bucket-name/*"
 }
 ]
}`

```

2. If using KMS encryption, add permissions for both the source and destination
   KMS keys:

```
{
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": [
    "arn:aws:kms:source-region:account-id:key/source-key-id",
    "arn:aws:kms:destination-region:account-id:key/destination-key-id"
  ]
}
```

3. Verify that bucket policies in both regions allow access from your Transfer Family
   server's IAM role
4. For cross-account transfers, ensure proper cross-account permissions are
   configured

## Troubleshoot cross-region transfer

performance issues

Description

Cross-region transfers are significantly slower than expected or time out during large
file transfers.

Cause

Cross-region transfers inherently involve greater latency and may be affected by
network conditions, file sizes, and service limits. Large files or high volumes of small
files can experience performance degradation.

Solution

To improve cross-region transfer performance:

- For large files, consider using Amazon S3 Transfer Acceleration:

```
aws s3 cp --source-region us-east-1 --region us-west-2 \
    s3://source-bucket/large-file.zip s3://destination-bucket/large-file.zip \
    --acl bucket-owner-full-control --s3-accelerate
```

- For multiple small files, batch them together before transfer:
  - Use compression to combine multiple files
  - Use Amazon S3 batch operations for large-scale transfers

- Consider using Transfer Family SFTP connectors with appropriate timeout settings for
  large transfers
- For recurring transfers, consider replicating data using Amazon S3 Cross-Region
  Replication (CRR) instead of ad-hoc transfers
- Monitor transfer performance using Amazon CloudWatch metrics to identify
  bottlenecks
