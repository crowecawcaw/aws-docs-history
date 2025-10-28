Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Features that are

implemented differently

Many Amazon Redshift SQL language elements have different performance characteristics and
use syntax and semantics and that are quite different from the equivalent PostgreSQL
implementation.

###### Important

Do not assume that the semantics of elements that Amazon Redshift and PostgreSQL have
in common are identical. Make sure to consult the _Amazon Redshift Developer
Guide_
[SQL commands](c_SQL_commands.md "c_SQL_commands.md") to understand the
often subtle differences.

One example in particular is the [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md") command, which is used to clean up and
reorganize tables. VACUUM functions differently and uses a different set of
parameters than the PostgreSQL version. See [Vacuuming tables](t_Reclaiming_storage_space202.md "t_Reclaiming_storage_space202.md") for more about information about
using VACUUM in Amazon Redshift.

Often, database management and administration features and tools are different as
well. For example, Amazon Redshift maintains a set of system tables and views that provide
information about how the system is functioning. See [SYS monitoring views](serverless_views-monitoring.md "serverless_views-monitoring.md") for more information.

The following list includes some examples of SQL features that are implemented
differently in Amazon Redshift.

- [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md")

Amazon Redshift does not support tablespaces, table partitioning, inheritance, and
certain constraints. The Amazon Redshift implementation of CREATE TABLE enables you to
define the sort and distribution algorithms for tables to optimize parallel
processing.

Amazon Redshift Spectrum supports table partitioning using the [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md "r_CREATE_EXTERNAL_TABLE.md")
command.

- [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md")

Only a subset of ALTER COLUMN actions are supported.

ADD COLUMN supports adding only one column in each ALTER TABLE
statement.

- [COPY](r_COPY.md "r_COPY.md")

The Amazon Redshift COPY command is highly specialized to enable the loading of
data from Amazon S3 buckets and Amazon DynamoDB tables and to facilitate automatic
compression. See the [Loading data in Amazon Redshift](t_Loading_data.md "t_Loading_data.md") section and the COPY command reference for
details.

- [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md")

The parameters for VACUUM are entirely different. For example, the default
VACUUM operation in PostgreSQL simply reclaims space and makes it available for
re-use; however, the default VACUUM operation in Amazon Redshift is VACUUM FULL, which
reclaims disk space and resorts all rows.

- Trailing spaces in VARCHAR values are ignored when string values are
  compared. For more information, see [Significance of trailing blanks](r_Character_types.md#r_Character_types-significance-of-trailing-blanks "r_Character_types.md#r_Character_types-significance-of-trailing-blanks").
