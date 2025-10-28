# cloudfront-s3-origin-non-existent-bucket

Checks if Amazon CloudFront distributions point to a non-existent S3 bucket. The rule is NON_COMPLIANT if `S3OriginConfig` for a CloudFront distribution points to a non-existent S3 bucket. The rule does not evaluate S3 buckets with static website hosting.

**Identifier:** CLOUDFRONT_S3_ORIGIN_NON_EXISTENT_BUCKET

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Periodic

**AWS Region:** Only available in China (Beijing), US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
