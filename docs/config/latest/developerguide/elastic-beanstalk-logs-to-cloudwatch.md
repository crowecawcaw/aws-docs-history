

# elastic-beanstalk-logs-to-cloudwatch
<a name="elastic-beanstalk-logs-to-cloudwatch"></a>

Checks if AWS Elastic Beanstalk environments are configured to send logs to Amazon CloudWatch Logs. The rule is NON\_COMPLIANT if the value of `StreamLogs` is false. 



**Identifier:** ELASTIC\_BEANSTALK\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::ElasticBeanstalk::Environment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

RetentionInDays (Optional)Type: String  
Checks the number of days to keep log events before they expire. Valid values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653. The rule is NON\_COMPLIANT if the value of `logs.RetentionInDays` does not match this parameter.

DeleteOnTerminate (Optional)Type: String  
Checks if logs are configured to be deleted upon termination of the environment. Valid values are `true` or `false`. The rule is NON\_COMPLIANT if the value of `logs.DeleteOnTerminate` does not match this parameter.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d771c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).