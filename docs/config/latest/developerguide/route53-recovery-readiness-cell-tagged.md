

# route53-recovery-readiness-cell-tagged
<a name="route53-recovery-readiness-cell-tagged"></a>

Checks if Amazon Route 53 Recovery Readiness cells have tags. Optionally, you can specify tag keys. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** ROUTE53\_RECOVERY\_READINESS\_CELL\_TAGGED

**Resource Types:** AWS::Route53RecoveryReadiness::Cell

**Trigger type:** Configuration changes

**AWS Region:** Only available in US West (Oregon) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1353c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).