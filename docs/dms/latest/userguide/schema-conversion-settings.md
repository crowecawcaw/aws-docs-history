# Specifying schema conversion settings for

migration projects

After you create a migration project, you can specify conversion settings in DMS Schema Conversion.
Configuring your schema conversion settings improves the performance of the converted
code.

###### To edit conversion settings

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration
   projects** page opens.
3. Choose your migration project. Choose **Schema conversion**,
   then **Launch schema conversion**.
4. Choose **Settings**. The **Settings** page
   opens.
5. In the **Conversion** section, change the settings.
6. Choose **Apply**, and then choose **Schema
   conversion**.
   For all conversion pairs, you can limit the number of comments with action items in
   the converted code. To limit the number of comments in the converted code, open the
   conversion settings in your migration project.

For the **Comments in converted SQL code**, choose the severity level
of action items. DMS Schema Conversion adds comments in the converted code for action items of the
selected severity and higher. For example, to minimize the number of comments in your
converted code, choose **Errors only**.

To include comments for all action items in your converted code, choose **All
messages**.

Other conversion settings are different for each pair of source and target databases.

###### Topics

- [Understanding Oracle to MySQL
  conversion settings](schema-conversion-oracle-mysql.md "schema-conversion-oracle-mysql.md")
- [Understanding Oracle to
  PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md "schema-conversion-oracle-postgresql.md")
- [Understanding SQL Server to
  MySQL conversion settings](schema-conversion-sql-server-mysql.md "schema-conversion-sql-server-mysql.md")
- [Understanding SQL Server
  to PostgreSQL conversion settings](schema-conversion-sql-server-postgresql.md "schema-conversion-sql-server-postgresql.md")
- [Understanding PostgreSQL to
  MySQL conversion settings](schema-conversion-postgresql-mysql.md "schema-conversion-postgresql-mysql.md")
- [Understanding IBM Db2 for Linux, UNIX and Windows to Amazon RDS for PostgreSQL conversion settings](schema-conversion-db2-luw-postgresql.md "schema-conversion-db2-luw-postgresql.md")
- [Understanding IBM Db2 for z/OS to Amazon RDS for Db2 conversion settings](schema-conversion-db2-zos-db2.md "schema-conversion-db2-zos-db2.md")
- [Understanding SAP ASE (Sybase ASE) to PostgreSQL conversion settings](schema-conversion--sybase-ASE.md "schema-conversion--sybase-ASE.md")
