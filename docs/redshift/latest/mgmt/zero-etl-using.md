Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting zero-ETL integrations

Use the following sections to help troubleshoot problems that you have with zero-ETL
integrations.

Use the following information to troubleshoot common issues with zero-ETL integrations with
Aurora MySQL.

###### Topics

- [Creation of the integration
  failed](#zero-etl-using.troubleshooting.creation "#zero-etl-using.troubleshooting.creation")
- [Tables don't have
  primary keys](#zero-etl-using.troubleshooting.primary-key "#zero-etl-using.troubleshooting.primary-key")
- [Aurora MySQL tables
  aren't replicating to Amazon Redshift](#zero-etl-using.troubleshooting.not-replicating "#zero-etl-using.troubleshooting.not-replicating")
- [Unsupported data types
  in tables](#zero-etl-using.troubleshooting.unsupported-data "#zero-etl-using.troubleshooting.unsupported-data")
- [Data manipulation language
  commands failed](#zero-etl-using.troubleshooting.failed-dml "#zero-etl-using.troubleshooting.failed-dml")
- [Tracked changes
  between data sources don't match](#zero-etl-using.troubleshooting.tracked-changes-failure "#zero-etl-using.troubleshooting.tracked-changes-failure")
- [Authorization
  failed](#zero-etl-using.troubleshooting.authorization "#zero-etl-using.troubleshooting.authorization")
- [Number of tables is more
  than 100K or the number of schemas is more than 4950](#zero-etl-using.troubleshooting.table-limits "#zero-etl-using.troubleshooting.table-limits")
- [Amazon Redshift can't load
  data](#zero-etl-using.troubleshooting.data-load "#zero-etl-using.troubleshooting.data-load")
- [Workgroup parameter
  settings are incorrect](#zero-etl-using.troubleshooting.case-sensitive "#zero-etl-using.troubleshooting.case-sensitive")
- [Database isn't created
  to activate a zero-ETL integration](#zero-etl-using.troubleshooting.db-creation "#zero-etl-using.troubleshooting.db-creation")
- [Table is in the Resync
  Required or Resync Initiated state](#zero-etl-using.troubleshooting.resync "#zero-etl-using.troubleshooting.resync")
- [Integration lag
  growing](#zero-etl-using.troubleshooting.integration-lag "#zero-etl-using.troubleshooting.integration-lag")

### Creation of the integration

failed

If the creation of the zero-ETL integration failed, the status of the integration is
`Inactive`. Make sure that the following are correct for your source Aurora
DB cluster:

- You created your cluster in the Amazon RDS console.
- Your source Aurora DB cluster is running a supported version. For a list of
  supported versions, see [Supported Regions and Aurora DB engines for zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.md"). To
  validate this, go to the **Configuration** tab for the cluster and
  check the **Engine version**.
- You correctly configured binlog parameter settings for your cluster. If your
  Aurora MySQL binlog parameters are set incorrectly or not associated with the source
  Aurora DB cluster, creation fails. See [Configure DB cluster parameters](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters").

In addition, make sure the following are correct for your Amazon Redshift data
warehouse:

- Case sensitivity is turned on. See [Turn on case sensitivity for your
  data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
- You added the correct authorized principal and integration source for your
  namespace. See [Configure authorization for your Amazon Redshift data
  warehouse](zero-etl-using.md "zero-etl-using.md").

### Tables don't have

primary keys

In the destination database, one or more of the tables don't have a primary key
and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
You can add primary keys to the tables and Amazon Redshift will resynchronize the tables.
Alternatively, although not recommended, you can drop these tables on Aurora and create
tables with a primary key. For more information, see [Amazon Redshift best
practices for designing tables](../dg/c_designing-tables-best-practices.md "../dg/c_designing-tables-best-practices.md").

### Aurora MySQL tables

aren't replicating to Amazon Redshift

If you don't see one or more tables reflected in Amazon Redshift, you can run the following
command to resynchronize them. Replace `dbname` with the name
of your Amazon Redshift database. And, replace `table1` and
`table2` with the names of the tables to be
synchronized.

```
ALTER DATABASE `dbname` INTEGRATION REFRESH TABLES `table1`, `table2`;
```

For more information, see see [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_.

Your data might not be replicating because one or more of your source tables doesn't
have a primary key. The monitoring dashboard in Amazon Redshift displays the status of these tables
as `Failed`, and the status of the overall zero-ETL integration changes to `Needs
 attention`. To resolve this issue, you can identify an existing key in your
table that can become a primary key, or you can add a synthetic primary key. For
detailed solutions, see [Handle tables without primary keys while creating Amazon Aurora MySQL or RDS for MySQL
zero-ETL integrations with Amazon Redshift.](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_.

Also confirm that if your target is an Amazon Redshift cluster, that the cluster is not
paused.

### Unsupported data types

in tables

In the database that you created from the integration in Amazon Redshift and in which data
is replicated from the Aurora DB cluster, one or more of the tables have unsupported data
types and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
Then, remove these tables and recreate new tables on Amazon RDS. For more information on
unsupported data types, see [Data type differences between Aurora and Amazon Redshift databases](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping") in the
_Amazon Aurora User Guide_.

### Data manipulation language

commands failed

Amazon Redshift could not run DML commands on the Redshift tables. To resolve this issue,
use SVV_INTEGRATION_TABLE_STATE to view the failed tables. Amazon Redshift automatically
resynchronizes the tables to resolve this error.

### Tracked changes

between data sources don't match

This error occurs when changes between Amazon Aurora and Amazon Redshift don't match,
leading to the integration entering a `Failed` state.

To resolve this, delete the zero-ETL integration and create it again in Amazon RDS. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Authorization

failed

Authorization failed because the source Aurora DB cluster was removed as an
authorized integration source for the Amazon Redshift data warehouse.

To resolve this issue, delete the zero-ETL integration and create it again on Amazon RDS. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Number of tables is more

than 100K or the number of schemas is more than 4950

For a destination data warehouse, the number of tables is more than 100K or the
number of schemas is more than 4950. Amazon Aurora can't send data to Amazon Redshift. The
number of tables and schemas exceeds the set limit. To resolve this issue, remove any
unnecessary schemas or tables from the source database.

### Amazon Redshift can't load

data

Amazon Redshift can't load data to the zero-ETL integration.

To resolve this issue, delete the zero-ETL integration on Amazon RDS and create it again. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Workgroup parameter

settings are incorrect

Your workgroup doesn't have case sensitivity turned on.

To resolve this issue, go to the **Properties** tab on the
integration details page, choose the parameter group, and turn on the case-sensitive
identifier from the **Properties** tab. If you don't have an
existing parameter group, create one with the case-sensitive identifier turned on. Then,
create a new zero-ETL integration on Amazon RDS. For more information, see [Creating zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Database isn't created

to activate a zero-ETL integration

There isn't a database created for the zero-ETL integration to activate it.

To resolve this issue, create a database for the integration. For more information,
see [Creating destination databases in
Amazon Redshift](zero-etl-using.md "zero-etl-using.md").

### Table is in the \*\*Resync

Required** or **Resync Initiated\*\* state

Your table is in the **Resync Required** or **Resync
Initiated** state.

To gather more detailed error information about why your table is in that state, use
the [SYS_LOAD_ERROR_DETAIL](../dg/SYS_LOAD_ERROR_DETAIL.md "../dg/SYS_LOAD_ERROR_DETAIL.md") system view.

### Integration lag

growing

The integration lag of your zero-ETL integrations can grow if there is a heavy use of
SAVEPOINT in your source database.

Use the following information to troubleshoot common issues with zero-ETL integrations with
Aurora PostgreSQL.

###### Topics

- [Creation of the integration
  failed](#zero-etl-using.troubleshooting.creation "#zero-etl-using.troubleshooting.creation")
- [Tables don't have
  primary keys](#zero-etl-using.troubleshooting.primary-key "#zero-etl-using.troubleshooting.primary-key")
- [Aurora PostgreSQL tables
  aren't replicating to Amazon Redshift](#zero-etl-using.troubleshooting.not-replicating "#zero-etl-using.troubleshooting.not-replicating")
- [Unsupported data types
  in tables](#zero-etl-using.troubleshooting.unsupported-data "#zero-etl-using.troubleshooting.unsupported-data")
- [Data manipulation language
  commands failed](#zero-etl-using.troubleshooting.failed-dml "#zero-etl-using.troubleshooting.failed-dml")
- [Tracked changes
  between data sources don't match](#zero-etl-using.troubleshooting.tracked-changes-failure "#zero-etl-using.troubleshooting.tracked-changes-failure")
- [Authorization
  failed](#zero-etl-using.troubleshooting.authorization "#zero-etl-using.troubleshooting.authorization")
- [Number of tables is more
  than 100K or the number of schemas is more than 4950](#zero-etl-using.troubleshooting.table-limits "#zero-etl-using.troubleshooting.table-limits")
- [Amazon Redshift can't load
  data](#zero-etl-using.troubleshooting.data-load "#zero-etl-using.troubleshooting.data-load")
- [Workgroup parameter
  settings are incorrect](#zero-etl-using.troubleshooting.case-sensitive "#zero-etl-using.troubleshooting.case-sensitive")
- [Database isn't created
  to activate a zero-ETL integration](#zero-etl-using.troubleshooting.db-creation "#zero-etl-using.troubleshooting.db-creation")
- [Table is in the Resync
  Required or Resync Initiated state](#zero-etl-using.troubleshooting.resync "#zero-etl-using.troubleshooting.resync")

### Creation of the integration

failed

If the creation of the zero-ETL integration failed, the status of the integration is
`Inactive`. Make sure that the following are correct for your source Aurora
DB cluster:

- You created your cluster in the Amazon RDS console.
- Your source Aurora DB cluster is running supported version. For a list of
  supported versions, see [Supported Regions and Aurora DB engines for zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Zero-ETL-Postgres "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Zero-ETL-Postgres"). To
  validate this, go to the **Configuration** tab for the cluster and
  check the **Engine version**.
- You correctly configured binlog parameter settings for your cluster. If your
  Aurora PostgreSQL binlog parameters are set incorrectly or not associated with the
  source Aurora DB cluster, creation fails. See [Configure DB cluster parameters](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters").

In addition, make sure the following are correct for your Amazon Redshift data
warehouse:

- Case sensitivity is turned on. See [Turn on case sensitivity for your
  data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
- You added the correct authorized principal and integration source for your
  endterm="zero-etl-using.redshift-iam.title"/>.

### Tables don't have

primary keys

In the destination database, one or more of the tables don't have a primary key
and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
You can add primary keys to the tables and Amazon Redshift will resynchronize the tables.
Alternatively, although not recommended, you can drop these tables on Aurora and create
tables with a primary key. For more information, see [Amazon Redshift best
practices for designing tables](../dg/c_designing-tables-best-practices.md "../dg/c_designing-tables-best-practices.md").

### Aurora PostgreSQL tables

aren't replicating to Amazon Redshift

If you don't see one or more tables reflected in Amazon Redshift, you can run the following
command to resynchronize them. Replace `dbname` with the name
of your Amazon Redshift database. And, replace `table1` and
`table2` with the names of the tables to be
synchronized.

```
ALTER DATABASE `dbname` INTEGRATION REFRESH TABLES `table1`, `table2`;
```

For more information, see see [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_.

Your data might not be replicating because one or more of your source tables doesn't
have a primary key. The monitoring dashboard in Amazon Redshift displays the status of these tables
as `Failed`, and the status of the overall zero-ETL integration changes to `Needs
 attention`. To resolve this issue, you can identify an existing key in your
table that can become a primary key, or you can add a synthetic primary key. For
detailed solutions, see [Handle tables without primary keys while creating Amazon Aurora PostgreSQL zero-ETL integrations with
Amazon Redshift.](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_.

Also confirm that if your target is an Amazon Redshift cluster, that the cluster is not
paused.

### Unsupported data types

in tables

In the database that you created from the integration in Amazon Redshift and in which data
is replicated from the Aurora DB cluster, one or more of the tables have unsupported data
types and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
Then, remove these tables and recreate new tables on Amazon RDS. For more information on
unsupported data types, see [Data type differences between Aurora and Amazon Redshift databases](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping") in the
_Amazon Aurora User Guide_.

### Data manipulation language

commands failed

Amazon Redshift could not run DML commands on the Redshift tables. To resolve this issue,
use SVV_INTEGRATION_TABLE_STATE to view the failed tables. Amazon Redshift automatically
resynchronizes the tables to resolve this error.

### Tracked changes

between data sources don't match

This error occurs when changes between Amazon Aurora and Amazon Redshift don't match,
leading to the integration entering a `Failed` state.

To resolve this, delete the zero-ETL integration and create it again in Amazon RDS. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Authorization

failed

Authorization failed because the source Aurora DB cluster was removed as an
authorized integration source for the Amazon Redshift data warehouse.

To resolve this issue, delete the zero-ETL integration and create it again on Amazon RDS. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Number of tables is more

than 100K or the number of schemas is more than 4950

For a destination data warehouse, the number of tables is more than 100K or the
number of schemas is more than 4950. Amazon Aurora can't send data to Amazon Redshift. The
number of tables and schemas exceeds the set limit. To resolve this issue, remove any
unnecessary schemas or tables from the source database.

### Amazon Redshift can't load

data

Amazon Redshift can't load data to the zero-ETL integration.

To resolve this issue, delete the zero-ETL integration on Amazon RDS and create it again. For more
information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Workgroup parameter

settings are incorrect

Your workgroup doesn't have case sensitivity turned on.

To resolve this issue, go to the **Properties** tab on the
integration details page, choose the parameter group, and turn on the case-sensitive
identifier from the **Properties** tab. If you don't have an
existing parameter group, create one with the case-sensitive identifier turned on. Then,
create a new zero-ETL integration on Amazon RDS. For more information, see [Creating zero-ETL integrations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md").

### Database isn't created

to activate a zero-ETL integration

There isn't a database created for the zero-ETL integration to activate it.

To resolve this issue, create a database for the integration. For more information,
see [Creating destination databases in
Amazon Redshift](zero-etl-using.md "zero-etl-using.md").

### Table is in the \*\*Resync

Required** or **Resync Initiated\*\* state

Your table is in the **Resync Required** or **Resync
Initiated** state.

To gather more detailed error information about why your table is in that state, use
the [SYS_LOAD_ERROR_DETAIL](../dg/SYS_LOAD_ERROR_DETAIL.md "../dg/SYS_LOAD_ERROR_DETAIL.md") system view.

Use the following information to troubleshoot common issues with zero-ETL integrations with
RDS for MySQL.

###### Topics

- [Creation of the integration
  failed](#zero-etl-using.troubleshooting.creation "#zero-etl-using.troubleshooting.creation")
- [Tables don't have
  primary keys](#zero-etl-using.troubleshooting.primary-key "#zero-etl-using.troubleshooting.primary-key")
- [RDS for MySQL tables
  aren't replicating to Amazon Redshift](#zero-etl-using.troubleshooting.not-replicating "#zero-etl-using.troubleshooting.not-replicating")
- [Unsupported data types
  in tables](#zero-etl-using.troubleshooting.unsupported-data "#zero-etl-using.troubleshooting.unsupported-data")
- [Data manipulation language
  commands failed](#zero-etl-using.troubleshooting.failed-dml "#zero-etl-using.troubleshooting.failed-dml")
- [Tracked changes
  between data sources don't match](#zero-etl-using.troubleshooting.tracked-changes-failure "#zero-etl-using.troubleshooting.tracked-changes-failure")
- [Authorization
  failed](#zero-etl-using.troubleshooting.authorization "#zero-etl-using.troubleshooting.authorization")
- [Number of tables is more
  than 100K or the number of schemas is more than 4950](#zero-etl-using.troubleshooting.table-limits "#zero-etl-using.troubleshooting.table-limits")
- [Amazon Redshift can't load
  data](#zero-etl-using.troubleshooting.data-load "#zero-etl-using.troubleshooting.data-load")
- [Workgroup parameter
  settings are incorrect](#zero-etl-using.troubleshooting.case-sensitive "#zero-etl-using.troubleshooting.case-sensitive")
- [Database isn't created
  to activate a zero-ETL integration](#zero-etl-using.troubleshooting.db-creation "#zero-etl-using.troubleshooting.db-creation")
- [Table is in the Resync
  Required or Resync Initiated state](#zero-etl-using.troubleshooting.resync "#zero-etl-using.troubleshooting.resync")

### Creation of the integration

failed

If the creation of the zero-ETL integration failed, the status of the integration is
`Inactive`. Make sure that the following are correct for your source RDS DB
instance:

- You created your instance in the Amazon RDS console.
- Your source RDS DB instance is running a supported version of RDS for MySQL. For a
  list of supported versions, see [Supported Regions and DB engines for Amazon RDS zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.md "../../../AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.md"). To
  validate this, go to the **Configuration** tab for the instance and
  check the **Engine version**.
- You correctly configured binlog parameter settings for your instance. If your
  RDS for MySQL binlog parameters are set incorrectly or not associated with the source
  RDS DB instance, creation fails. See [Configure DB instance parameters](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.parameters "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.parameters").

In addition, make sure the following are correct for your Amazon Redshift data
warehouse:

- Case sensitivity is turned on. See [Turn on case sensitivity for your
  data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
- You added the correct authorized principal and integration source for your
  namespace. See [Configure authorization for your Amazon Redshift data
  warehouse](zero-etl-using.md "zero-etl-using.md").

### Tables don't have

primary keys

In the destination database, one or more of the tables don't have a primary key
and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
You can add primary keys to the tables and Amazon Redshift will resynchronize the tables.
Alternatively, although not recommended, you can drop these tables on RDS and create
tables with a primary key. For more information, see [Amazon Redshift best
practices for designing tables](../dg/c_designing-tables-best-practices.md "../dg/c_designing-tables-best-practices.md").

### RDS for MySQL tables

aren't replicating to Amazon Redshift

If you don't see one or more tables reflected in Amazon Redshift, you can run the following
command to resynchronize them. Replace `dbname` with the name
of your Amazon Redshift database. And, replace `table1` and
`table2` with the names of the tables to be
synchronized.

```
ALTER DATABASE `dbname` INTEGRATION REFRESH TABLES `table1`, `table2`;
```

For more information, see see [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_.

Your data might not be replicating because one or more of your source tables doesn't
have a primary key. The monitoring dashboard in Amazon Redshift displays the status of these tables
as `Failed`, and the status of the overall zero-ETL integration changes to `Needs
 attention`. To resolve this issue, you can identify an existing key in your
table that can become a primary key, or you can add a synthetic primary key. For
detailed solutions, see [Handle tables without primary keys while creating Aurora MySQL-Compatible Edition or RDS for MySQL
zero-ETL integrations with Amazon Redshift.](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_.

Also confirm that if your target is an Amazon Redshift cluster, that the cluster is not
paused.

### Unsupported data types

in tables

In the database that you created from the integration in Amazon Redshift and in which data
is replicated from the RDS DB instance, one or more of the tables have unsupported data
types and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
Then, remove these tables and recreate new tables on Amazon RDS. For more information on
unsupported data types, see [Data type differences between RDS and Amazon Redshift databases](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping") in the
_Amazon RDS User Guide_.

### Data manipulation language

commands failed

Amazon Redshift could not run DML commands on the Redshift tables. To resolve this issue,
use SVV_INTEGRATION_TABLE_STATE to view the failed tables. Amazon Redshift automatically
resynchronizes the tables to resolve this error.

### Tracked changes

between data sources don't match

This error occurs when changes between Amazon Aurora and Amazon Redshift don't match,
leading to the integration entering a `Failed` state.

To resolve this, delete the zero-ETL integration and create it again in Amazon RDS. For more
information, see [Creating zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md")
and [Deleting
zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md").

### Authorization

failed

Authorization failed because the source RDS DB instance was removed as an authorized
integration source for the Amazon Redshift data warehouse.

To resolve this issue, delete the zero-ETL integration and create it again on Amazon RDS. For more
information, see [Creating zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md")
and [Deleting zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md").

### Number of tables is more

than 100K or the number of schemas is more than 4950

For a destination data warehouse, the number of tables is more than 100K or the
number of schemas is more than 4950. Amazon Aurora can't send data to Amazon Redshift. The
number of tables and schemas exceeds the set limit. To resolve this issue, remove any
unnecessary schemas or tables from the source database.

### Amazon Redshift can't load

data

Amazon Redshift can't load data to the zero-ETL integration.

To resolve this issue, delete the zero-ETL integration on Amazon RDS and create it again. For more
information, see [Creating zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md")
and [Deleting zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md").

### Workgroup parameter

settings are incorrect

Your workgroup doesn't have case sensitivity turned on.

To resolve this issue, go to the **Properties** tab on the
integration details page, choose the parameter group, and turn on the case-sensitive
identifier from the **Properties** tab. If you don't have an
existing parameter group, create one with the case-sensitive identifier turned on. Then,
create a new zero-ETL integration on Amazon RDS. For more information, see [Creating
zero-ETL integrations](../../../AmazonRDS/latest/UserGuide/zero-etl.md "../../../AmazonRDS/latest/UserGuide/zero-etl.md").

### Database isn't created

to activate a zero-ETL integration

There isn't a database created for the zero-ETL integration to activate it.

To resolve this issue, create a database for the integration. For more information,
see [Creating destination databases in
Amazon Redshift](zero-etl-using.md "zero-etl-using.md").

### Table is in the \*\*Resync

Required** or **Resync Initiated\*\* state

Your table is in the **Resync Required** or **Resync
Initiated** state.

To gather more detailed error information about why your table is in that state, use
the [SYS_LOAD_ERROR_DETAIL](../dg/SYS_LOAD_ERROR_DETAIL.md "../dg/SYS_LOAD_ERROR_DETAIL.md") system view.

Use the following information to troubleshoot common issues with zero-ETL integrations with
Amazon DynamoDB.

###### Topics

- [Creation of
  the integration failed](#zero-etl-dynamodb-integrations-troubleshooting-creation "#zero-etl-dynamodb-integrations-troubleshooting-creation")
- [Unsupported data types in tables](#zero-etl-dynamodb-integrations-troubleshooting-unsupported-data-types "#zero-etl-dynamodb-integrations-troubleshooting-unsupported-data-types")
- [Unsupported table and attribute names](#zero-etl-dynamodb-integrations-troubleshooting-unsupported-table-names "#zero-etl-dynamodb-integrations-troubleshooting-unsupported-table-names")
- [Authorization failed](#zero-etl-dynamodb-integrations-troubleshooting-authorization "#zero-etl-dynamodb-integrations-troubleshooting-authorization")
- [Amazon Redshift
  can't load data](#zero-etl-dynamodb-integrations-troubleshooting-data-load "#zero-etl-dynamodb-integrations-troubleshooting-data-load")
- [Workgroup or cluster parameter settings are incorrect](#zero-etl-dynamodb-integrations-troubleshooting-case-sensitive "#zero-etl-dynamodb-integrations-troubleshooting-case-sensitive")
- [Database
  isn't created to activate a zero-ETL integration](#zero-etl-dynamodb-integrations-troubleshooting-db-creation "#zero-etl-dynamodb-integrations-troubleshooting-db-creation")
- [Point-in-time recovery (PITR) is not enabled on source DynamoDB table](#zero-etl-dynamodb-integrations-troubleshooting-pitr-recovery "#zero-etl-dynamodb-integrations-troubleshooting-pitr-recovery")
- [KMS key access
  denied](#zero-etl-dynamodb-integrations-troubleshooting-kms-key "#zero-etl-dynamodb-integrations-troubleshooting-kms-key")
- [Amazon Redshift does
  not have access to DynamoDB table key](#zero-etl-dynamodb-integrations-troubleshooting-ddb-table-key "#zero-etl-dynamodb-integrations-troubleshooting-ddb-table-key")

### Creation of

the integration failed

If the creation of the zero-ETL integration failed, the status of the integration is
`Inactive`. Make sure that the following are correct for your Amazon Redshift data
warehouse and source DynamoDB table:

- Case sensitivity is turned on for your data warehouse. See [Turn on case sensitivity](zero-etl-using.md#zero-etl-setting-up.case-sensitivity "zero-etl-using.md#zero-etl-setting-up.case-sensitivity") in the
  _Amazon Redshift Management Guide_.
- You added the correct authorized principal and integration source for your
  namespace in Amazon Redshift. See [Configure authorization for your Amazon Redshift data warehouse](zero-etl-using.md#zero-etl-using.redshift-iam "zero-etl-using.md#zero-etl-using.redshift-iam") in the
  _Amazon Redshift Management Guide_.
- You added the correct resource-based policy to the source DynamoDB table. See
  [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
  _IAM User Guide_.

### Unsupported data types in tables

DynamoDB numbers are translated to DECIMAL(38,10) in Amazon Redshift. Numbers exceeding this
precision range are automatically transformed to (38,10). Delete the integration and
unify the number precisions, and then re-create the integration.

### Unsupported table and attribute names

Amazon Redshift supports up to 127 character table and attribute names. If a long name, such as
the DynamoDB table name or the partition key or sort key column name fails your
integration, fix it by using a shorter name and re-create the integration.

### Authorization failed

Authorization can fail when the source DynamoDB table is removed as an authorized
integration source for the Amazon Redshift data warehouse.

To resolve this issue, delete the zero-ETL integration, and re-create it using
Amazon DynamoDB.

### Amazon Redshift

can't load data

Amazon Redshift can't load data from a zero-ETL integration.

To resolve this issue, refresh the integration with ALTER DATABASE.

```
ALTER DATABASE `sample_integration_db` INTEGRATION REFRESH ALL TABLES
```

### Workgroup or cluster parameter settings are incorrect

Your workgroup or cluster doesn't have case sensitivity turned on.

To resolve this issue, go to the **Properties** tab on the
integration details page, choose the parameter group, and turn on the case-sensitive
identifier from the **Properties** tab. If you don't have an
existing parameter group, create one with the case-sensitive identifier turned on. Then,
create a new zero-ETL integration on DynamoDB. See [Turn on case sensitivity](zero-etl-using.md#zero-etl-setting-up.case-sensitivity "zero-etl-using.md#zero-etl-setting-up.case-sensitivity") in the _Amazon Redshift Management Guide_.

### Database

isn't created to activate a zero-ETL integration

There isn't a database created for the zero-ETL integration to activate it.

To resolve this issue, create a database for the integration. See [Creating destination databases in Amazon Redshift](zero-etl-using.md "zero-etl-using.md") in the
_Amazon Redshift Management Guide_.

### Point-in-time recovery (PITR) is not enabled on source DynamoDB table

Enabling PITR is required for DynamoDB to export data. Ensure PITR is always enabled.
If you ever turn off PITR while the integration is active, you’ll need to follow
instructions in the error message and refresh the integration using ALTER
DATABASE.

```
ALTER DATABASE `sample_integration_db` INTEGRATION REFRESH ALL TABLES
```

### KMS key access

denied

The KMS key used for the source table or integration must be configured with
sufficient permissions. For information about table encryption and decryption, see
[DynamoDB encryption at
rest](../../../amazondynamodb/latest/developerguide/EncryptionAtRest.md "../../../amazondynamodb/latest/developerguide/EncryptionAtRest.md") in the _Amazon DynamoDB Developer Guide_.

### Amazon Redshift does

not have access to DynamoDB table key

If the source table encryption is an AWS managed key, then switch to an
AWS owned key or customer managed key. If the table is already encrypted with a customer managed key,
ensure that the policy doesn't have any condition keys.

Use the following information to troubleshoot common issues with zero-ETL integrations with
applications, such as, Salesforce, SAP, ServiceNow, and Zendesk.

###### Topics

- [Creation of the integration
  failed](#zero-etl-using.troubleshooting.creation "#zero-etl-using.troubleshooting.creation")
- [Tables aren't replicating
  to Amazon Redshift](#zero-etl-using.troubleshooting.primary-key "#zero-etl-using.troubleshooting.primary-key")
- [Unsupported data types
  in tables](#zero-etl-using.troubleshooting.unsupported-data "#zero-etl-using.troubleshooting.unsupported-data")
- [Workgroup parameter
  settings are incorrect](#zero-etl-using.troubleshooting.case-sensitive "#zero-etl-using.troubleshooting.case-sensitive")
- [Database isn't created
  to activate a zero-ETL integration](#zero-etl-using.troubleshooting.db-creation "#zero-etl-using.troubleshooting.db-creation")
- [Table is in the Resync
  Required or Resync Initiated state](#zero-etl-using.troubleshooting.resync "#zero-etl-using.troubleshooting.resync")

### Creation of the integration

failed

If the creation of the zero-ETL integration failed, the status of the integration is
`Inactive`. Make sure that the following are correct for your Amazon Redshift data
warehouse:

- Case sensitivity is turned on. See [Turn on case sensitivity for your
  data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
- You added the correct authorized principal and integration source for your
  namespace. See [Configure authorization for your Amazon Redshift data
  warehouse](zero-etl-using.md "zero-etl-using.md").

### Tables aren't replicating

to Amazon Redshift

In the destination database, one or more of the tables don't have a primary key
and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
You can add primary keys to the tables and Amazon Redshift will resynchronize the tables. You
can run the following command to resynchronize them. Replace
`dbname` with the name of your Amazon Redshift database. And, replace
`table1` and `table2` with the names
of the tables to be synchronized.

```
ALTER DATABASE `dbname` INTEGRATION REFRESH TABLES `table1`, `table2`;
```

For more information, see [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
_Amazon Redshift Database Developer Guide_.

### Unsupported data types

in tables

In the database that you created from the integration in Amazon Redshift and in which data
is replicated from zero-ETL integrations with applications, one or more of the tables have
unsupported data types and can't be synchronized.

To resolve this issue, go to the **Table statistics** tab on the
integration details page or use SVV_INTEGRATION_TABLE_STATE to view the failed tables.
Then, remove these tables and recreate new tables at the source. For more information,
see see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the _AWS Glue Developer Guide_.

### Workgroup parameter

settings are incorrect

Your workgroup doesn't have case sensitivity turned on.

To resolve this issue, go to the **Properties** tab on the
integration details page, choose the parameter group, and turn on the case-sensitive
identifier from the **Properties** tab. If you don't have an
existing parameter group, create one with the case-sensitive identifier turned on. Then,
create a new zero-ETL integration. For more information, see see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the
_AWS Glue Developer Guide_.

### Database isn't created

to activate a zero-ETL integration

There isn't a database created for the zero-ETL integration to activate it.

To resolve this issue, create a database for the integration. For more information,
see [Creating destination databases in
Amazon Redshift](zero-etl-using.md "zero-etl-using.md").

### Table is in the \*\*Resync

Required** or **Resync Initiated\*\* state

Your table is in the **Resync Required** or **Resync
Initiated** state.

To gather more detailed error information about why your table is in that state, use
the [SYS_LOAD_ERROR_DETAIL](../dg/SYS_LOAD_ERROR_DETAIL.md "../dg/SYS_LOAD_ERROR_DETAIL.md") system view.
