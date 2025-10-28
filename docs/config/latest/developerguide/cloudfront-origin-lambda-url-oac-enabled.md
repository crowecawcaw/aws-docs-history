# cloudfront-origin-lambda-url-oac-enabled

Checks if Amazon CloudFront distributions with Amazon Lambda Function URL origins have origin access control (OAC) enabled. The rule is NON_COMPLIANT if any Lambda Function URL origin in a CloudFront distribution does not have OAC enabled.

**Identifier:** CLOUDFRONT_ORIGIN_LAMBDA_URL_OAC_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
