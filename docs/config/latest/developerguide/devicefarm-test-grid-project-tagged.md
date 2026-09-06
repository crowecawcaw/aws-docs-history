

# devicefarm-test-grid-project-tagged
<a name="devicefarm-test-grid-project-tagged"></a>

Checks if AWS Device Farm test grid projects have tags. Optionally, you can specify tag keys. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** DEVICEFARM\_TEST\_GRID\_PROJECT\_TAGGED

**Resource Types:** AWS::DeviceFarm::TestGridProject

**Trigger type:** Configuration changes

**AWS Region:** Only available in US West (Oregon) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d461c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).