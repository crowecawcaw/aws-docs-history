

# mediapackage-packagingconfiguration-tagged
<a name="mediapackage-packagingconfiguration-tagged"></a>

Checks if AWS Elemental MediaPackage packaging configuration resources have tags. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** MEDIAPACKAGE\_PACKAGINGCONFIGURATION\_TAGGED

**Resource Types:** AWS::MediaPackage::PackagingConfiguration

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Melbourne), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1095c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).