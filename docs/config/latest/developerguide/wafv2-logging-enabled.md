

# wafv2-logging-enabled
<a name="wafv2-logging-enabled"></a>

Checks if logging is enabled on AWS WAFv2 regional and global web access control lists (web ACLs). The rule is NON\_COMPLIANT if the logging is enabled but the logging destination does not match the value of the parameter. 

**Note**  
**Amazon Security Lake Exception**  
This rule does not check logging done with Security Lake for AWS WAFV2 web ACLs.

**Identifier:** WAFV2\_LOGGING\_ENABLED

**Resource Types:** AWS::WAFv2::WebACL

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

KinesisFirehoseDeliveryStreamArns (Optional)Type: CSV  
Comma separated list of Kinesis Firehose delivery stream ARNs

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1615c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).