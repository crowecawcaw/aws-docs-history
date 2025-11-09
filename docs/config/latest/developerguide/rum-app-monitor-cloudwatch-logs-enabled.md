# rum-app-monitor-cloudwatch-logs-enabled

Checks if Amazon CloudWatch RUM app monitors have CloudWatch logs enabled. The rule is NON_COMPLIANT if configuration.CwLogEnabled is false.

**Identifier:** RUM_APP_MONITOR_CLOUDWATCH_LOGS_ENABLED

**Resource Types:** AWS::RUM::AppMonitor

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
