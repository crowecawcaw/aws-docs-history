

# iam-no-inline-policy-check
<a name="iam-no-inline-policy-check"></a>

Checks if the inline policy feature is not in use. The rule is NON\_COMPLIANT if an AWS Identity and Access Management (IAM) user, IAM role or IAM group has any inline policy. 



**Identifier:** IAM\_NO\_INLINE\_POLICY\_CHECK

**Resource Types:** AWS::IAM::Group, AWS::IAM::Role, AWS::IAM::User

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d923c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).