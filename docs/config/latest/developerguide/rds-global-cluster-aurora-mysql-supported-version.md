

# rds-global-cluster-aurora-mysql-supported-version
<a name="rds-global-cluster-aurora-mysql-supported-version"></a>

Checks if an Amazon Aurora MySQL global database is running on a specified minimum supported engine version. The rule is NON\_COMPLIANT if the database is not running on the minimum supported engine version that you specify. 



**Identifier:** RDS\_GLOBAL\_CLUSTER\_AURORA\_MYSQL\_SUPPORTED\_VERSION

**Resource Types:** AWS::RDS::GlobalCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

minSupportedEngineVersionType: String  
String value for the minimum supported Aurora MySQL version for the aurora MySQL global database. Aurora MySQL database engine versions use the following syntax: 'mysql-major-version.mysql\_aurora.aurora-mysql-version'. The 'mysql-major-version' portion represents the version of the client protocol and general level of MySQL feature support for the corresponding Aurora MySQL version. The 'aurora-mysql-version' part is a dotted value with three parts: the Aurora MySQL major version, the Aurora MySQL minor version, and the patch level.

longTermSupportVersion (Optional)Type: CSV  
List of string values for Aurora MySQL versions that will have long-term support and are acceptable for use. Amazon Aurora MySQL global databases using an Aurora MySQL version specified in this parameter will be marked COMPLIANT. Aurora MySQL database engine versions use the following syntax: 'mysql-major-version.mysql\_aurora.aurora-mysql-version'. The 'mysql-major-version' portion represents the version of the client protocol and general level of MySQL feature support for the corresponding Aurora MySQL version. The 'aurora-mysql-version' part is a dotted value with three parts: the Aurora MySQL major version, the Aurora MySQL minor version, and the patch level.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1241c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).