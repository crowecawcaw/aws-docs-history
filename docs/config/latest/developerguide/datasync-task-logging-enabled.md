

# datasync-task-logging-enabled
<a name="datasync-task-logging-enabled"></a>

Checks if an AWS DataSync task has Amazon CloudWatch logging enabled. The rule is NON\_COMPLIANT if an AWS DataSync task does not have Amazon CloudWatch logging enabled or if the logging level is not equivalent to the logging level that you specify. 



**Identifier:** DATASYNC\_TASK\_LOGGING\_ENABLED

**Resource Types:** AWS::DataSync::Task

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

logLevel (Optional)Type: String  
String value for the logging level. Valid values include: 'BASIC' and 'TRANSFER'. If not specified, the default value is 'BASIC'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d443c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).