# imagebuilder-distributionconfiguration-tagged

Checks if ImageBuilder DistributionConfiguration resources have tags. Optionally, required tag keys can be specified. The rule is NON_COMPLIANT if there are no tags or the specified tag keys are not present. It does not consider tags starting with 'aws:'.

**Identifier:** IMAGEBUILDER_DISTRIBUTIONCONFIGURATION_TAGGED

**Resource Types:** AWS::ImageBuilder::DistributionConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

requiredKeyTags (Optional)
Type: CSV

Comma-separated list of tag keys for the rule to check. If provided, the rule is NON_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
