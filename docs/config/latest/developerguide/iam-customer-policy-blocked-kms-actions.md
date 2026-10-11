

# iam-customer-policy-blocked-kms-actions
<a name="iam-customer-policy-blocked-kms-actions"></a>

Checks if the managed AWS Identity and Access Management (IAM) policies that you create do not allow blocked actions on AWS KMS keys. The rule is NON\_COMPLIANT if any blocked action is allowed on AWS KMS keys by the managed IAM policy. 

**Note**  
To be considered non-public, an IAM policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-using-variables).

**Identifier:** IAM\_CUSTOMER\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Resource Types:** AWS::IAM::Policy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

blockedActionsPatternsType: CSV  
Comma-separated list of blocked KMS action patterns. For example, you can list kms:Decrypt\* or kms:ReEncrypt as blocked action patterns. The rule is NON\_COMPLIANT if the managed IAM policy allows any action pattern listed in this parameter.

excludePermissionBoundaryPolicy (Optional)Type: boolean  
Boolean flag to exclude the evaluation of IAM policies used as permissions boundaries. If set to 'true', the rule will not include permissions boundaries in the evaluation. Otherwise, all IAM policies in scope are evaluated when value is set to 'false.' Default value is 'false'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d933c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).