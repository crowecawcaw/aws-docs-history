# waf-classic-logging-enabled

Checks if logging is enabled on AWS WAF classic global web access control lists (web ACLs). The rule is NON_COMPLIANT for a global web ACL, if it does not have logging enabled.

**Identifier:** WAF_CLASSIC_LOGGING_ENABLED

**Resource Types:** AWS::WAF::WebACL

**Trigger type:** Periodic

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

KinesisFirehoseDeliveryStreamArns (Optional)
Type: CSV

Comma separated list of Amazon Kinesis stream ARN for AWS WAF logs.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
