

# iam-inline-policy-blocked-kms-actions
<a name="iam-inline-policy-blocked-kms-actions"></a>

Checks if the inline policies attached to your IAM users, roles, and groups do not allow blocked actions on all AWS KMS keys. The rule is NON\_COMPLIANT if any blocked action is allowed on all AWS KMS keys in an inline policy. 



**Identifier:** IAM\_INLINE\_POLICY\_BLOCKED\_KMS\_ACTIONS

**Resource Types:** AWS::IAM::Group, AWS::IAM::Role, AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

blockedActionsPatternsType: CSV  
Comma-separated list of blocked KMS action patterns, for example, kms:\*, kms:Decrypt, kms:ReEncrypt\*.

excludeRoleByManagementAccount (Optional)Type: boolean  
Exclude a role if it is only assumable by organization management account.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d921c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).