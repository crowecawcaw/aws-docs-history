

# iam-policy-blacklisted-check
<a name="iam-policy-blacklisted-check"></a>

Checks in each AWS Identity and Access Management (IAM) resource, if a policy Amazon Resource Name (ARN) in the input parameter is attached to the IAM resource. The rule is NON\_COMPLIANT if the policy ARN is attached to the IAM resource. 



**Identifier:** IAM\_POLICY\_BLACKLISTED\_CHECK

**Resource Types:** AWS::IAM::User, AWS::IAM::Group, AWS::IAM::Role

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

policyArnsType: CSVDefault: arn:aws:iam::aws:policy/AdministratorAccess  
Comma separated list of IAM policy arns which should not be attached to any IAM entity.

exceptionList (Optional)Type: CSV  
Comma separated list of resourcetypes and list of resource name pairs. For example, users:[user1;user2], groups:[group1;group2], roles:[role1;role2;role3].  
For the exception list, specify the name of the resource and not the full ARN. Not valid: `arn:aws:iam::444455556666:role/Admin`. Valid: `Admin`.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d931c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).