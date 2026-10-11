

# rds-global-cluster-aurora-postgresql-supported-version
<a name="rds-global-cluster-aurora-postgresql-supported-version"></a>

Checks if an Amazon Aurora PostgreSQL global database is running on a specified minimum supported engine version. The rule is NON\_COMPLIANT if the Aurora PostgreSQL global database is not running on the minimum supported engine version that you specify. 



**Identifier:** RDS\_GLOBAL\_CLUSTER\_AURORA\_POSTGRESQL\_SUPPORTED\_VERSION

**Resource Types:** AWS::RDS::GlobalCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Middle East (UAE), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

minSupportedEngineVersionType: String  
String value for the rule to check the minimum supported engine version for the Aurora PostgreSQL global database. PostgreSQL database engine versions use a major.minor numbering scheme: X.Y. X denotes the major version, and Y represents the minor version.

longTermSupportVersion (Optional)Type: CSV  
List of string values for Aurora PostgreSQL versions that will have long-term support and are acceptable for use. Amazon Aurora PostgreSQL global databases using an Aurora PostgreSQL version specified in this parameter will be marked COMPLIANT. Aurora PostgreSQL database engine versions use a major.minor numbering scheme: X.Y. X denotes the major version, and Y represents the minor version.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1269c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).