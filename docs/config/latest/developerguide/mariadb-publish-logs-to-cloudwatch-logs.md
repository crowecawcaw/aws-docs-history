

# mariadb-publish-logs-to-cloudwatch-logs
<a name="mariadb-publish-logs-to-cloudwatch-logs"></a>

Checks if Amazon MariaDB database instances are configured to publish logs to Amazon CloudWatch Logs. The rule is NON\_COMPLIANT if a database instance is not configured to publish logs to CloudWatch Logs. 



**Identifier:** MARIADB\_PUBLISH\_LOGS\_TO\_CLOUDWATCH\_LOGS

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

logTypes (Optional)Type: String  
Comma-separated list of log types for the rule to check. If not provided, the rule checks for the default log types: 'error' and 'audit'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1093c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).