# Using an Oracle Data Warehouse database as a source in DMS Schema Conversion

You can use Oracle Data Warehouse databases as a migration source in DMS Schema Conversion
to convert database code objects and application code to Amazon Redshift.

For information about supported Oracle database versions, see
[Source data providers for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion "CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion").
For more information about using DMS Schema Conversion with a source Oracle database, see the
[Oracle to PostgreSQL migration step-by-step walkthrough](../sbs/schema-conversion-oracle-postgresql.md "../sbs/schema-conversion-oracle-postgresql.md").

## Privileges for using an Oracle Data Warehouse database as a source

The following privileges are required for Oracle Data Warehouse as a source:

- CONNECT
- SELECT\_CATALOG\_ROLE
- SELECT ANY DICTIONARY
