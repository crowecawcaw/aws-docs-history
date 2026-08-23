# transfer-connector-logging-enabled

Checks if AWS Transfer Family Connector publishes logs to Amazon CloudWatch. The rule is NON\_COMPLIANT if a Connector does not have a LoggingRole assigned.

**Identifier:** TRANSFER\_CONNECTOR\_LOGGING\_ENABLED

**Resource Types:** AWS::Transfer::Connector

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
