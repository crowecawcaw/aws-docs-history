

# rds-sql-server-logs-to-cloudwatch
<a name="rds-sql-server-logs-to-cloudwatch"></a>

Checks if an Amazon SQL Server DB instance is configured to publish logs to Amazon CloudWatch Logs. This rule is NON\_COMPLIANT if the DB instance is not configured to publish logs to Amazon CloudWatch Logs. 



**Identifier:** RDS\_SQL\_SERVER\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

logTypes (Optional)Type: CSV  
logTypes - (Optional): Comma-separated list of log types to be published to CloudWatch Logs. Valid values are: 'error', 'agent'. Default value is 'error', 'agent'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1287c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).