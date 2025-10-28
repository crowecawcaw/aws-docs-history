# aurora-mysql-cluster-audit-logging

Checks if Amazon Aurora MySQL DB clusters have audit logging enabled. The rule is NON_COMPLIANT if a DB cluster does not have audit logging enabled.

**Identifier:** AURORA_MYSQL_CLUSTER_AUDIT_LOGGING

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
