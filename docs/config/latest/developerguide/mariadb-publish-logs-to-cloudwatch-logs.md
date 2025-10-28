# mariadb-publish-logs-to-cloudwatch-logs

Checks if Amazon MariaDB database instances are configured to publish logs to Amazon CloudWatch Logs. The rule is NON_COMPLIANT if a database instance is not configured to publish logs to CloudWatch Logs.

**Identifier:** MARIADB_PUBLISH_LOGS_TO_CLOUDWATCH_LOGS

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

logTypes (Optional)
Type: String

Comma-separated list of log types for the rule to check. If not provided, the rule checks for the default log types: 'error' and 'audit'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
