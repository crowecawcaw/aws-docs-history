# iam-policy-blacklisted-check

Checks in each AWS Identity and Access Management (IAM) resource, if a policy Amazon Resource Name (ARN) in the input parameter is attached to the IAM resource. The rule is NON_COMPLIANT if the policy ARN is attached to the IAM resource.

**Identifier:** IAM_POLICY_BLACKLISTED_CHECK

**Resource Types:** AWS::IAM::User, AWS::IAM::Group, AWS::IAM::Role

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Middle East (UAE), AWS Secret - West, Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

policyArns
Type: CSV
Default: arn:aws:iam::aws:policy/AdministratorAccess

Comma separated list of IAM policy arns which should not be attached to any IAM entity.

exceptionList (Optional)
Type: CSV

Comma separated list of resourcetypes and list of resource name pairs.
For example, users:[user1;user2], groups:[group1;group2], roles:[role1;role2;role3].

###### Note

For the exception list, specify the name of the resource and not the full ARN.
Not valid: `arn:aws:iam::444455556666:role/Admin`. Valid: `Admin`.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
