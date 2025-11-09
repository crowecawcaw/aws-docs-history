# wafv2-logging-enabled

Checks if logging is enabled on AWS WAFv2 regional and global web access control lists (web ACLs). The rule is NON_COMPLIANT if the logging is enabled but the logging destination does not match the value of the parameter.

###### Note

**Amazon Security Lake Exception**

This rule does not check logging done with Security Lake for AWS WAFV2 web ACLs.

**Identifier:** WAFV2_LOGGING_ENABLED

**Resource Types:** AWS::WAFv2::WebACL

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

KinesisFirehoseDeliveryStreamArns (Optional)
Type: CSV

Comma separated list of Kinesis Firehose delivery stream ARNs

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
