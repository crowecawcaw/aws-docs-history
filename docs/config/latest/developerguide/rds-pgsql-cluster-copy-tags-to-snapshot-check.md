

# rds-pgsql-cluster-copy-tags-to-snapshot-check
<a name="rds-pgsql-cluster-copy-tags-to-snapshot-check"></a>

Checks if Amazon Relational Database Service (Amazon RDS) PostgreSQL DB clusters are configured to copy tags to snapshots. The rule is NON\_COMPLIANT if an RDS PostgreSQL DB cluster's CopyTagsToSnapshot property is set to false. 



**Identifier:** RDS\_PGSQL\_CLUSTER\_COPY\_TAGS\_TO\_SNAPSHOT\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Asia Pacific (Taipei) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1271c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).