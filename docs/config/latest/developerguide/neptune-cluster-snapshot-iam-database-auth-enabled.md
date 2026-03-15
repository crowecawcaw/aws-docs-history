# neptune-cluster-snapshot-iam-database-auth-enabled

Checks if Amazon Neptune cluster snapshots have IAM database authentication enabled. The rule is NON_COMPLIANT if configuration.iamdatabaseAuthenticationEnabled is false.

**Identifier:** NEPTUNE_CLUSTER_SNAPSHOT_IAM_DATABASE_AUTH_ENABLED

**Resource Types:** AWS::RDS::DBClusterSnapshot

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Hyderabad), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
