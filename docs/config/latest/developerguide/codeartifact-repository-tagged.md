

# codeartifact-repository-tagged
<a name="codeartifact-repository-tagged"></a>

Checks if AWS CodeArtifact repository resources have tags. Optionally, required tag keys can be specified. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** CODEARTIFACT\_REPOSITORY\_TAGGED

**Resource Types:** AWS::CodeArtifact::Repository

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Europe (Milan), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d371c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).