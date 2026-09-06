

# cloudfront-ssl-policy-check
<a name="cloudfront-ssl-policy-check"></a>

Checks if Amazon CloudFront distributions are configured with the specified security policies.The rule is NON\_COMPLIANT if a CloudFront Distribution is not configured with security policies that you specify. 



**Identifier:** CLOUDFRONT\_SSL\_POLICY\_CHECK

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

securityPoliciesType: CSV  
Comma-separated list of CloudFront distribution security policies for the rule to check. For example: "TLSv1.2\_2018, TLSv1.2\_2019, TLSv1.2\_2021". For a list of valid value, see the Amazon CloudFront Developer Guide.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d327c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).