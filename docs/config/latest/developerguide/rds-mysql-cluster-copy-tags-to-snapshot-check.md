# rds-mysql-cluster-copy-tags-to-snapshot-check

Checks if Amazon Relational Database Service (Amazon RDS) MySQL DB clusters are configured to copy tags to snapshots. The rule is NON\_COMPLIANT if an Amazon RDS MySQL DB cluster is not configured to copy tags to snapshots.

**Identifier:** RDS\_MYSQL\_CLUSTER\_COPY\_TAGS\_TO\_SNAPSHOT\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
