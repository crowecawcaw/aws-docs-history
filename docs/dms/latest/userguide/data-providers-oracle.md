

# Using an Oracle database as a source in DMS Schema Conversion
<a name="data-providers-oracle"></a>

You can use Oracle databases as a migration source in DMS Schema Conversion.

DMS Schema Conversion supports the following modes for Oracle as a migration source:
+ **Online mode** – Use this mode to read metadata directly from your source database. To use online mode, you need network connectivity and the appropriate database privileges.
+ **Offline mode** – Use this mode to convert schemas from exported script files stored in an Amazon S3 bucket, without requiring a connection to your source database. In offline mode, the conversion results depend on the completeness and quality of the scripts that you provide. To use offline mode, turn on **Virtual Mode** when you create the data provider. For more information, see [Virtual mode for offline source and virtual target](virtual-data-provider.md).

To connect to your Oracle database, use the Oracle System ID (SID). To find the Oracle SID, submit the following query to your Oracle database:

```
SELECT sys_context('userenv','instance_name') AS SID FROM dual;
```

You can use DMS Schema Conversion to convert database code objects from Oracle Database to the following targets:
+ Aurora MySQL
+ Aurora PostgreSQL
+ RDS for MySQL
+ RDS for PostgreSQL

For information about the supported Oracle database versions, see [Source data providers for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion).

For more information about using DMS Schema Conversion with a source Oracle database, see the [Oracle to PostgreSQL migration step-by-step walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql.html).

## Privileges for Oracle as a source
<a name="data-providers-oracle-permissions"></a>

The following privileges are required for Oracle as a source: 
+ CONNECT 
+ SELECT\_CATALOG\_ROLE 
+ SELECT ANY DICTIONARY 
+ SELECT ON SYS.ARGUMENT$