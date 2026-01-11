# cloudfront-accesslogs-enabled

Checks if Amazon CloudFront distributions are configured to deliver access logs to an Amazon S3 bucket using standard logging (legacy). The rule is NON_COMPLIANT if a CloudFront distribution does not have legacy logging configured.

**Identifier:** CLOUDFRONT_ACCESSLOGS_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

S3BucketName (Optional)
Type: String

The name of the Amazon S3 bucket for storing server access logs

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
