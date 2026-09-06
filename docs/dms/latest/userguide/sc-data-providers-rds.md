

# Using Amazon RDS for Db2 database as a target in DMS Schema Conversion
<a name="sc-data-providers-rds"></a>

You can use Amazon RDS for Db2 databases as a migration target in DMS Schema Conversion.

For more information regarding supported target databases, see [Target data providers for DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html#CHAP_Introduction.Targets.SchemaConversion).

## Privileges for Amazon RDS for Db2 as a target
<a name="sc-data-providers-rds-privileges"></a>

To use Amazon RDS for Db2 as a target, DMS Schema Conversion requires the `master_user_role` role. For more information, see [Amazon RDS for Db2 default roles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-default-roles.html) in the *Amazon Relational Database Service User Guide*.