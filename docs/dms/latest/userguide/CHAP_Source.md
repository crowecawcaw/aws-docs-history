# Using Microsoft Azure Database for MySQL flexible server as a source for AWS DMS

With AWS DMS, you can use Microsoft Azure Database for MySQL flexible server as a source in much the same way as you do MySQL.

For information about versions of Microsoft Azure Database for MySQL flexible server that AWS DMS supports as a source, see
[Sources for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

For more information about using a customer-managed MySQL-compatible database with AWS DMS, see
[Using a self-managed
MySQL-compatible database as a source for AWS DMS](CHAP_Source.md#CHAP_Source.MySQL.CustomerManaged "CHAP_Source.md#CHAP_Source.MySQL.CustomerManaged").

## Limitations when using Azure MySQL as a source for AWS Database Migration Service

- The defaut value for the Azure MySQL flexible server system variable `sql_generate_invisible_primary_key`
  is `ON`, and the server automatically adds a generated invisible primary key (GIPK) to any table that is
  created without an explicit primary key. AWS DMS doesn’t support ongoing replication for MySQL tables with GIPK constraints.
