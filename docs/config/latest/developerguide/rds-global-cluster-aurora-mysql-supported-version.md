# rds-global-cluster-aurora-mysql-supported-version

Checks if an Amazon Aurora MySQL global database is running on a specified minimum supported engine version. The rule is NON_COMPLIANT if the database is not running on the minimum supported engine version that you specify.

**Identifier:** RDS_GLOBAL_CLUSTER_AURORA_MYSQL_SUPPORTED_VERSION

**Resource Types:** AWS::RDS::GlobalCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

minSupportedEngineVersion
Type: String

String value for the minimum supported Aurora MySQL version for the aurora MySQL global database. Aurora MySQL database engine versions use the following syntax: 'mysql-major-version.mysql_aurora.aurora-mysql-version'. The 'mysql-major-version' portion represents the version of the client protocol and general level of MySQL feature support for the corresponding Aurora MySQL version. The 'aurora-mysql-version' part is a dotted value with three parts: the Aurora MySQL major version, the Aurora MySQL minor version, and the patch level.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
