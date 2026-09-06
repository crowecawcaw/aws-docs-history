

# cloudformation-stack-notification-check
<a name="cloudformation-stack-notification-check"></a>

Checks if your CloudFormation stacks send event notifications to an Amazon SNS topic. Optionally checks if specified Amazon SNS topics are used. The rule is NON\_COMPLIANT if CloudFormation stacks do not send notifications. 



**Identifier:** CLOUDFORMATION\_STACK\_NOTIFICATION\_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Europe (Spain) Region

**Parameters:**

snsTopic2 (Optional)Type: String  
SNS topic ARN.

snsTopic1 (Optional)Type: String  
SNS topic ARN.

snsTopic5 (Optional)Type: String  
SNS topic ARN.

snsTopic4 (Optional)Type: String  
SNS topic ARN.

snsTopic3 (Optional)Type: String  
SNS topic ARN.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d295c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).