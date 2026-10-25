

# iam-inline-policy-blocked-kms-actions
<a name="iam-inline-policy-blocked-kms-actions"></a>

Checks if the inline policies attached to your IAM users, roles, and groups do not allow blocked actions on all AWS KMS keys. The rule is NON\_COMPLIANT if any blocked action is allowed on all AWS KMS keys in an inline policy. 

**Note**  
If a single value in an inline IAM policy (for example, one Resource or Condition value) contains more than five IAM [policy variables](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-using-variables), the rule can't evaluate that policy and returns NON\_COMPLIANT, even if the policy would otherwise be compliant. To get an accurate evaluation, split any value that contains more than five policy variables so that each value contains five or fewer.  
Because all inline policies attached to a user, group, or role are evaluated together, a single inline policy that exceeds this limit causes the rule to return NON\_COMPLIANT for that user, group, or role.

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
<a name="w2aac20c16c17b7d939c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).