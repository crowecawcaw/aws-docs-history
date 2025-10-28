# dms-replication-instance-multi-az-enabled

Checks if AWS Database Migration Service (DMS) replication instances are configured with multiple Availability Zones. The rule is NON_COMPLIANT if a DMS replication instance is not configured to use multiple Availability Zones.

**Identifier:** DMS_REPLICATION_INSTANCE_MULTI_AZ_ENABLED

**Resource Types:** AWS::DMS::ReplicationInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
