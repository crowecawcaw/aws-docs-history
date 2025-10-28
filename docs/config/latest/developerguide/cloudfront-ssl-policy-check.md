# cloudfront-ssl-policy-check

Checks if Amazon CloudFront distributions are configured with the specified security policies.The rule is NON_COMPLIANT if a CloudFront Distribution is not configured with security policies that you specify.

**Identifier:** CLOUDFRONT_SSL_POLICY_CHECK

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

securityPolicies
Type: CSV

Comma-separated list of CloudFront distribution security policies for the rule to check. For example: "TLSv1.2_2018, TLSv1.2_2019, TLSv1.2_2021". For a list of valid value, see the Amazon CloudFront Developer Guide.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
