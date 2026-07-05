# cloudformation-stack-service-role-check

Checks if AWS CloudFormation stacks are using service roles. The rule is NON\_COMPLIANT if a CloudFormation stack does not have service role associated with it.

**Identifier:** CLOUDFORMATION\_STACK\_SERVICE\_ROLE\_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
