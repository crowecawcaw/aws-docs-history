

# imagebuilder-infrastructureconfiguration-tagged
<a name="imagebuilder-infrastructureconfiguration-tagged"></a>

Checks if EC2 Image Builder infrastructure configuration resources have tags. Optionally, required tag keys can be specified. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. 



**Identifier:** IMAGEBUILDER\_INFRASTRUCTURECONFIGURATION\_TAGGED

**Resource Types:** AWS::ImageBuilder::InfrastructureConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d967c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).