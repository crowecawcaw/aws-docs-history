# aurora-global-database-encryption-at-rest

Checks if Amazon Aurora Global Databases have storage encryption enabled. This rule is NON_COMPLIANT if an Amazon Aurora Global Database does not have storage encryption enabled.

**Identifier:** AURORA_GLOBAL_DATABASE_ENCRYPTION_AT_REST

**Resource Types:** AWS::RDS::GlobalCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
