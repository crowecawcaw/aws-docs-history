

# iam-oidc-provider-client-id-list-check
<a name="iam-oidc-provider-client-id-list-check"></a>

Checks if AWS IAM OIDC providers are configured with approved client IDs. The rule is NON\_COMPLIANT if configuration.ClientIdList contains IDs not specified in the required rule parameter. 



**Identifier:** IAM\_OIDC\_PROVIDER\_CLIENT\_ID\_LIST\_CHECK

**Resource Types:** AWS::IAM::OIDCProvider

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

allowedClientIdsType: CSV  
Comma-separated list of client IDs for the rule to check. The rule is NON\_COMPLIANT if configuration.ClientIdList contains values not specified in this parameter.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d925c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).