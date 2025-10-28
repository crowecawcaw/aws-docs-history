# Verified Access logging permissions

The IAM principal being used to configure the logging destination needs to have
certain permissions for logging to work properly. The following sections show the
permissions required for each logging destination.

###### For delivery to CloudWatch Logs:

- `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
- `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`,
  `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery`
  on all resources
- `logs:DescribeLogGroups`, `logs:DescribeResourcePolicies`, and
  `logs:PutResourcePolicy` on the destination log group

###### For delivery to Amazon S3:

- `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
- `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`,
  `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery`
  on all resources
- `s3:GetBucketPolicy` and `s3:PutBucketPolicy` on the destination bucket

###### For delivery to Firehose:

- `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
- `firehose:TagDeliveryStream` on all resources
- `iam:CreateServiceLinkedRole` on all resources
- `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`,
  `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery`
  on all resources
