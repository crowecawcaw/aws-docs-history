

# emr-block-public-access
<a name="emr-block-public-access"></a>

Checks if an account with Amazon EMR has block public access settings enabled. The rule is NON\_COMPLIANT if BlockPublicSecurityGroupRules is false, or if true, ports other than Port 22 are listed in PermittedPublicSecurityGroupRuleRanges. 



**Identifier:** EMR\_BLOCK\_PUBLIC\_ACCESS

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d805c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).