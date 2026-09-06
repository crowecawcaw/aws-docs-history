

# sqs-queue-policy-full-access-check
<a name="sqs-queue-policy-full-access-check"></a>

Checks if the SQS queue access policy allows full access. The rule is NON\_COMPLIANT if the SQS policy contains `SQS:\*` within `Action` and `Effect` is `Allow`. 



**Identifier:** SQS\_QUEUE\_POLICY\_FULL\_ACCESS\_CHECK

**Resource Types:** AWS::SQS::Queue

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1545c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).