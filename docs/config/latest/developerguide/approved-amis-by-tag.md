# approved-amis-by-tag

Checks if EC2 instances are using specified Amazon Machine Images (AMIs). Specify the tags that identify the AMIs. Running instances with AMIs that don't have at least one of the specified tags are NON_COMPLIANT.

**Identifier:** APPROVED_AMIS_BY_TAG

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

amisByTagKeyAndValue
Type: StringMap
Default: tag-key:tag-value,other-tag-key

Comma-separated list of up to 10 AMIs tags (tag-key:tag-value). For example, tag-key1 matches AMIs with tag-key1; tag-key2:value2 matches tag-key2 with the value 2.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
