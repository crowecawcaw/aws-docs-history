Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Cluster versions for Amazon Redshift

Amazon Redshift regularly releases cluster versions. Your Amazon Redshift clusters are patched during your system maintenance window.
The timing of the patch depends on your AWS Region and maintenance window settings.
You can view or change your maintenance window settings from the Amazon Redshift console.
For more information about maintenance, see
[Cluster maintenance](managing-cluster-considerations.md#rs-cluster-maintenance "managing-cluster-considerations.md#rs-cluster-maintenance").

You can view the cluster version of your cluster on the Amazon Redshift console on the **Maintenance** tab of the cluster details.
Or you can see the cluster version in the output of the SQL command:

```
SELECT version();
```

###### Note

Critical updates that affect Amazon Redshift behavior are introduced as Amazon Redshift evolves. To keep up with these changes, take actions,
and avoid potential disruptions to your workloads, see
[Behavior changes in Amazon Redshift](behavior-changes.md "behavior-changes.md").

###### Topics

- [Amazon Redshift patch 197](#cluster-version-197 "#cluster-version-197")
- [Amazon Redshift patch 196](#cluster-version-196 "#cluster-version-196")
- [Amazon Redshift patch 195](#cluster-version-195 "#cluster-version-195")
- [Amazon Redshift patch 194](#cluster-version-194 "#cluster-version-194")
- [Amazon Redshift patch 193](#cluster-version-193 "#cluster-version-193")
- [Amazon Redshift patch 192](#cluster-version-192 "#cluster-version-192")
- [Amazon Redshift patch 191](#cluster-version-191 "#cluster-version-191")
- [Amazon Redshift patch 190](#cluster-version-190 "#cluster-version-190")
- [Amazon Redshift patch 189](#cluster-version-189 "#cluster-version-189")
- [Amazon Redshift patch 188](#cluster-version-188 "#cluster-version-188")
- [Amazon Redshift patch 187](#cluster-version-187 "#cluster-version-187")
- [Amazon Redshift patch 186](#cluster-version-186 "#cluster-version-186")
- [Amazon Redshift patch 185](#cluster-version-185 "#cluster-version-185")
- [Amazon Redshift patch 184](#cluster-version-184 "#cluster-version-184")
- [Amazon Redshift patch 183](#cluster-version-183 "#cluster-version-183")
- [Amazon Redshift patch 182](#cluster-version-182 "#cluster-version-182")
- [Amazon Redshift patch 181](#cluster-version-181 "#cluster-version-181")
- [Amazon Redshift patch 180](#cluster-version-180 "#cluster-version-180")
- [Amazon Redshift patch 179](#cluster-version-179 "#cluster-version-179")
- [Amazon Redshift patch 178](#cluster-version-178 "#cluster-version-178")
- [Amazon Redshift patch 177](#cluster-version-177 "#cluster-version-177")
- [Amazon Redshift patch 176](#cluster-version-176 "#cluster-version-176")
- [Amazon Redshift patch 175](#cluster-version-175 "#cluster-version-175")
- [Amazon Redshift patch 174](#cluster-version-174 "#cluster-version-174")
- [Amazon Redshift patch 173](#cluster-version-173 "#cluster-version-173")
- [Amazon Redshift patch 172](#cluster-version-172 "#cluster-version-172")
- [Amazon Redshift patch 171](#cluster-version-171 "#cluster-version-171")
- [Amazon Redshift patch 170](#cluster-version-170 "#cluster-version-170")
- [Amazon Redshift patch 169](#cluster-version-169 "#cluster-version-169")
- [Amazon Redshift patch 168](#cluster-version-168 "#cluster-version-168")

## Amazon Redshift patch 197

Cluster versions in this patch:

- 1.0.166219 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on November 21, 2025

### New features and improvements in this patch

- Added support to store strings literals up to 16,000,000 bytes within the SUPER data types
- Added GET_NUMBER_ATTRIBUTES(super_object) function that returns the total number of attributes contained within a SUPER object.
- Release patch compatibility restrictions are enforced for table restore operations. When attempting to restore a table, the backup can only be used on clusters running the same patch version as when the backup was created, one patch version lower than the backup, or any patch version higher than the backup.
- Enhanced the LIKE operator to properly handle trailing whitespaces in patterns when using CHAR datatype.
- Introduced 4 new spatial H3 functions operating on cell hierarchies: H3_Resolution, H3_ToParent, H3_ToChildren and H3_IsValid.
- Enables Amazon Redshift Federated Permissions that simplifies permissions management across multiple Redshift data warehouses by enabling you to define data permissions once and automatically enforce them across all warehouses in your AWS account.
- Enables object-level grants, fine-grained column-level access control, scoped permissions grants and database-level grants on Amazon Redshift Federated Permissions Catalog objects.
- Enables CREATE, ALTER, ATTACH, DETACH and DROP RLS policy operations on Amazon Redshift Federated Permissions Catalog.
- Enables the ability to turn on or off row-level security for relations in Amazon Redshift Federated Permissions Catalog.
- Enable CREATE, ALTER, ATTACH, DETACH and DROP masking policy operations on Amazon Redshift Federated Permissions Catalog objects.
- Enables SHOW POLICIES to show RLS and Masking policies on a connected database and attachments on relations in Amazon Redshift Federated Permissions Catalog objects.
- Enables database users to assume an IAM role to query on an Amazon Redshift Federated Permissions Catalog objects.
- Enhanced SHOW GRANTS command to support cross-database grant visibility within the same Redshift cluster.
- Added support for SHOW COLUMN GRANTS command to simplify discovery of column-level access controls.
- Added support for SHOW PROCEDURES command to simplify discovery of stored procedure metadata discovery.
- Added support for SHOW FUNCTIONS command to simplify discovery of user-defined function metadata.
- Introduced SHOW PARAMETERS command to display parameter metadata for functions and stored procedures.
- Introduced SHOW CONSTRAINTS command to display constraint metadata for functions and stored procedures.
- Added support for CREATE/CREATE OR REPLACE/DROP VIEW operations on Amazon Redshift Federated Permissions Catalog and on cross-database within the same Redshift cluster.
- Improved constant strings collation handling in some INTERSECT or EXCEPT queries.
- Enhanced SHOW TABLES to display a warning message instead of failing when FAS credentials are missing for AWS Glue Data Catalog access.
- Enhanced SHOW COLUMNS command with additional metadata columns for sort keys, distribution style, encoding, and collation information.
- Added grantor_name column to SHOW GRANTS output and standardized database_name inclusion across all SHOW GRANTS result sets.
- Enhanced SHOW TABLES command with additional columns: table_owner, last_altered_time, last_modified_time, dist_style, and table_sub_type.

## Amazon Redshift patch 196

Cluster versions in this patch:

- 1.0.163480 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on November 19, 2025
- 1.0.160807 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on November 13, 2025
- 1.0.155905 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on November 10, 2025

### New features and improvements in this patch

- Optimized the plans for correlated IN and EXISTS subqueries by decorrelating them into semi joins.
- Extended the SHOW TABLE command to include collation information for every column.

## Amazon Redshift patch 195

Cluster versions in this patch:

- 1.0.162991 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on November 17, 2025
- 1.0.160706 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on November 13, 2025
- 1.0.151179 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on November 4, 2025
- 1.0.148180 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on November 3, 2025
- 1.0.142459 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on October 18, 2025

### New features and improvements in this patch

- Adds support for writing to Iceberg tables using CREATE TABLE , CREATE TABLE AS SELECT, INSERT INTO, SQL commands.
- Adds support for the SUPER data type in databases with case-insensitive collation.
- Updates the IANA Time Zone Database database version to 2025b.
- Adds support for the TZDB_VERSION function. This
  function displays the current IANA Time Zone Database version in use.
- Amazon Redshift now enforces patch compatibility restrictions.
  Backups created on patch versions that are more than one patch version
  ahead of the current cluster are no longer permitted to perform
  table restore operations.
- Extends UNNEST functionality to support JOIN expressions.
  Previously, UNNEST was limited to single-table references.
- Adds support for the JIT (Just In Time) ANALYZE feature.
  JIT ANALYZE automatically, intelligently, and efficiently collects the minimal set
  of statistics that Amazon Redshift's query optimizer needs to generate efficient query
  execution plans, allowing customers to achieve best price-performance
  for Apache Iceberg out-of-box (OOB) queries and workloads.

## Amazon Redshift patch 194

Cluster versions in this patch:

- 1.0.148169 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on October 29, 2025
- 1.0.138443 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on October 17, 2025
- 1.0.129791 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on October 1, 2025

### New features and improvements in this patch

- Amazon Redshift will no longer fail a query that accesses an
  AWS Lake Formation-governed relation where the `AuthorizedColumns`
  field includes a backslash.
- Added support for the NULL AS option in COPY command for SUPER columns,
  letting you specify a custom string to represent NULL values.
- Added support for the ISOWEEK and ISOYEAR date parts in EXTRACT
  and DATE_PART functions when used with dates and timestamps.
- Fixed PartiQL navigation on grouped variables to ensure correct
  parsing and evaluation of nested field access in
  GROUP BY queries.
- Added support to view primary key and foreign key
  constraints using the SHOW CONSTRAINTS command.
- Added support for local materialized views created from
  data sharing materialized views.
- Improves the performance of queries that retrieve data from different tables and invoke Lambda User Defined Functions in join conditions.
- Add support for MVs on Datasharing MVs
- The DROP DATABASE command now uses a background worker
  to remove leader node catalog directories after commit.
  Using a worker avoids rare bugs related to catalog
  directory cleanup.

## Amazon Redshift patch 193

Cluster versions in this patch:

- 1.0.136890 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on October 13, 2025
- 1.0.127211 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on September 29, 2025
- 1.0.125329 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on September 24, 2025
- 1.0.121010 – Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup
  version – Released on August 26, 2025

### New features and improvements in this patch

- Added support for creating tables using CREATE TABLE LIKE to clone one parent
  table from remote databases (both within the same cluster and between different
  clusters).
- Added ST_GeomFromGeoJSON overload that creates a geometry from the SUPER
  datatype in GeoJSON format, with support for geometries up to 1 MB.
- Changed the default fallback option in case of misconfigurations in automatic
  workload management (WLM). The default fallback option is now automatic WLM
  instead of manual WLM.
- Updated time zone calculation by adopting the latest IANA Time Zone Database
  patches. This change alters how date and time conversions function for certain
  time zones and time periods. For more information, see [Amazon Redshift uses up-to-date IANA Time Zone Database](behavior-changes.md#timezone-changes-aug2025 "behavior-changes.md#timezone-changes-aug2025").
- Added support for multidimensional data layout (MDDL) sorting.
  MDDL sort keys dynamically sort data based on actual query filters,
  accelerating query performance. For more information, see
  [Multidimensional data layout storing](../dg/t_Sorting_mutidimensional-sort-key.md "../dg/t_Sorting_mutidimensional-sort-key.md") in the _Amazon Redshift Database Developer Guide_.

## Amazon Redshift patch 192

Cluster versions in this patch:

- 1.0.124422 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on September 22, 2025
- 1.0.122914 – Trailing Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on September 16, 2025
- 1.0.121035 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on August 22, 2025
- 1.0.119650 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on August 7, 2025
- 1.0.118447 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on July 24, 2025

### New features and improvements in this patch

- Fixes an issue when JOIN on a collated case-insensitive column and a constant
  string column selects a mismatching hash function.

## Amazon Redshift patch 191

Cluster versions in this patch:

- 1.0.117891 – Trailing Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on July 29, 2025
- 1.0.117891 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on July 22, 2025
- 1.0.117458 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on July 15, 2025
- 1.0.116415 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on June 26, 2025
- 1.0.116263 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on June 25, 2025
- 1.0.115865 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on June 18, 2025

### New features and improvements in this patch

- Adds support for the UNNEST operation in the SELECT statement's FROM clause,
  enabling customers to convert array elements into individual rows.
- Improves error handling for PartiQL unnesting syntax when
  using SUPER data type within Common Table Expressions (CTEs) and recursive CTEs,
  particularly when resolving table aliases with identical names.
- Improves performance for automatic analyze by
  adding support for incremental automatic analyze for large tables.
- Amazon Redshift now supports Cascading Refresh of nested Materialized
  Views (MVs).
- Amazon Redshift now supports Auto Refresh of Materialized Views (MVs)
  defined on Apache Iceberg tables.
- Adds support for Amazon RDS for Oracle zero-ETL integrations with Amazon Redshift.
- Adds support for Amazon RDS for PostgreSQL zero-ETL integrations with Amazon Redshift.

## Amazon Redshift patch 190

Cluster versions in this patch:

- 1.0.115140 – Trailing Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on June 16, 2025
- 1.0.115564 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on June 14, 2025
- 1.0.113436 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on May 15, 2025
- 1.0.112895 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on May 7, 2025

### New features and improvements in this patch

- Adds improved models for Amazon Redshift Serverless AI-driven scaling and optimizations.
- Adds support for auto-copy when using Amazon Redshift with enhanced VPC routing
  enabled.
- Adds support for multiple automatic table optimization operations to run
  concurrently across different tables.
- Fixes a rare condition in streaming ingestion where queued autorefresh queries
  trigger UNDO queries that also queue, leading to lock contention.
- Adds support for Oracle Database@AWS zero-ETL integrations with Amazon Redshift.

## Amazon Redshift patch 189

Cluster versions in this patch:

- 1.0.112790 – Trailing Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on May 14, 2025
- 1.0.112790 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on May 6, 2025
- 1.0.112086 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on April 29, 2025
- 1.0.111040 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on April 16, 2025
- 1.0.109768 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 22, 2025
- 1.0.109284 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 13, 2025
- 1.0.108971 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 7, 2025

### New features and improvements in this patch

- Adds support for concurrency scaling for write queries using the SUPER, GEOMETRY, and GEOGRAPHY data types.
- Fixes an issue that allowed SUPER, GEOMETRY, or GEOGRAPHY columns to be set as
  DISTKEY or SORTKEY columns during table creation with CREATE TABLE AS.
- Adds support for the TRY_CAST function.
- Enables support for running multiple vacuum commands concurrently across
  different tables.

## Amazon Redshift patch 188

Cluster versions in this patch:

- 1.0.109616 – Trailing Amazon Redshift Serverless
  workgroup version – Released on March 27, 2025
- 1.0.109616 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 24, 2025
- 1.0.108470 – Trailing Amazon Redshift Serverless
  workgroup version – Released on March 13, 2025
- 1.0.108470 – Current Amazon Redshift Serverless
  workgroup version – Released on March 11, 2025
- 1.0.108950 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 10, 2025
- 1.0.108790 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 9, 2025
- 1.0.108470 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on March 4, 2025
- 1.0.107910 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on February 20, 2025
- 1.0.107360 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless
  workgroup version – Released on February 13, 2025
- 1.0.106767 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on February 5, 2025

### New features and improvements in this patch

- Adds support for automatic mounting of an Amazon S3 Tables catalog, making it easier for
  you to run queries on Apache Iceberg tables managed in Amazon S3 Tables. See
  [Prerequisites for managing Amazon Redshift namespaces in the AWS Glue Data Catalog](../../../lake-formation/latest/dg/redshift-ns-prereqs.md "../../../lake-formation/latest/dg/redshift-ns-prereqs.md") in the _AWS Lake Formation Developer Guide_ for required permissions.
- You can now bypass the data masking check and add a table with a dynamic data
  masking (DDM) attachment to a datashare.
- Disallows the use of correlation references that skip a query block, also known as "skip-level correlation references".
  For more information, see
  [Correlated subquery patterns that are not supported](../dg/r_correlated_subqueries.md#r_correlated_subqueries-correlated-subquery-patterns-that-are-not-supported "../dg/r_correlated_subqueries.md#r_correlated_subqueries-correlated-subquery-patterns-that-are-not-supported") in the _Amazon Redshift Database Developer Guide_.
- Adds support for correlated SUPER data type queries with data sharing and 3-part notation.
- Adds support for the EXCLUDE SQL keyword.
- Adds support for new GROUP BY ALL SQL keyword.
- Improves performance for workload management (WLM) queues configured with roles, resulting in lower lock contention.
- Adds support for automatically refreshed materialize views on zero-ETL tables with history mode turned on.
- Adds support for null characters embedded in strings during zero-ETL replication.
- Improves models for AI driven scaling and optimizations.
- Adds the `username` column to the `sys_query_history` view.

## Amazon Redshift patch 187

Cluster versions in this patch:

- 1.0.107351 – Amazon Redshift provisioned cluster trailing track version and Amazon Redshift Serverless workgroup version – Released on February 13, 2025
- 1.0.106452 – Amazon Redshift provisioned cluster trailing track version – Released on February 5, 2025
- 1.0.106980 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on February 3, 2025
- 1.0.106452 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on January 24, 2025
- 1.0.106073 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on January 21, 2025
- 1.0.105722 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on January 10, 2025
- 1.0.105373 – Current Amazon Redshift provisioned cluster version and Amazon Redshift Serverless workgroup version – Released on January 8, 2025
- 1.0.104930 – Amazon Redshift Serverless workgroup version – Released on December 20, 2024

### New features and improvements in this patch

- Introduces two new spatial H3 functions (H3_center and H3_boundary).
- Enables dynamic disk cache on concurrency scaling clusters.
- Fixes an inefficiency in memory usage during the ingestion of sorted tables that could impact performance.
- Fixes an issue where certain queries with a subquery inside the SELECT clause, such as `SELECT ARRAY_FLATTEN((SELECT FROM ...))`,
  would incorrectly trigger a `size >= min_partiql_size` XCHECK error in specific scenarios involving a single SUPER value.
- Fixes an issue where non-nullable SUPER expressions (`json_serialize()`, `json_size()`, `json_typeof()`, `is_object()`, and several others)
  would sometimes produce erroneous results when combined with argument expressions such as `CASE ... END` or `COALESCE()`.
- Fixes an issue where SELECT from late binding views would raise an ERROR after enabling row-level security on the view.
- Fixes an issue where CDC on a zero-ETL integration lead to a high leader node CPU consumption.
- Adds the capability to zero-ETL integrations to query tables in all states, including during updates.
- Adds the capability to zero-ETL integrations to truncate large texts/strings for mapping to the max varchar size on Amazon Redshift.
- Adds the capability to zero-ETL integrations to replace invalid UTF-8 characters with a specified character of your choice.
- Fixes an issue on 'refresh interval' for zero-ETL integration with Amazon RDS for MySQL.
- Adds support for JSON/JSONB data type for zero-ETL integration with Aurora PostgreSQL.
- Fixes an issue where queries containing expressions with `IS [NOT] {TRUE|FALSE|UNKNOWN}`
  would encounter an assertion error.
- Fixes an issue where the `json_extract_path_text()` and `json_extract_array_element_text()`
  functions would produce an empty string `''` instead of `NULL` or vice versa in cases like accessing a
  non-existent array element or attribute, the JSON `'null'` value, or an empty JSON string.
- Improves performance of INSERT/COPY statements in concurrent transactions writing to the same table by allowing them
  to share a lock and make progress until they need to write data to the table.

## Amazon Redshift patch 186

Cluster versions in this patch:

- 1.0.82096 – Trailing track version – Released on January 10, 2025
- 1.0.82000 – Amazon Redshift Serverless version – Released on January 10, 2025
- 1.0.81981 – Current track version – Released on January 10, 2025
- 1.0.81475 – Trailing track version – Released on January 6, 2025
- 1.0.81473 – Amazon Redshift Serverless version – Released on January 6, 2025
- 1.0.81462 – Current track version – Released on January 6, 2025
- 1.0.80643 – Trailing track version – Released on December 17, 2024
- 1.0.80583 – Amazon Redshift Serverless version – Released on December 17, 2024
- 1.0.80560 – Current track version – Released on December 17, 2024
- 1.0.80498 – Amazon Redshift Serverless version – Released on December 13, 2024
- 1.0.80491 – Current track version – Released on December 13,
  2024
- 1.0.80036 – Amazon Redshift Serverless version – Released on December 6, 2024
- 1.0.80009 – Current track version – Released on December 6,
  2024
- 1.0.79372 – Amazon Redshift Serverless version – Released on November 26, 2024
- 1.0.79237 – Amazon Redshift Serverless version – Released on November 24, 2024
- 1.0.79229 – Current track version – Released on November 24,
  2024
- 1.0.79003 – Amazon Redshift Serverless version – Released on November 19, 2024
- 1.0.78987 – Current track version – Released on November 19,
  2024
- 1.0.78890 – Amazon Redshift Serverless version – Released on November 18, 2024
- 1.0.78881 – Current track version – Released on November 18,
  2024
- 1.0.78646 – Amazon Redshift Serverless version – Released on November 14, 2024
- 1.0.78641 – Current track version – Released on November 14,
  2024
- 1.0.78178 – Amazon Redshift Serverless version – Released on November 12, 2024
- 1.0.78160 – Current track version – Released on November 12,
  2024
- 1.0.77809 – Amazon Redshift Serverless version – Released on October 31, 2024
- 1.0.77777 – Current track version – Released on October 31,
  2024
- 1.0.77292 – Amazon Redshift Serverless version – Released on October 24, 2024
- 1.0.77272 – Current track version – Released on October 24,
  2024
- 1.0.77040 – Amazon Redshift Serverless version – Released on October 22, 2024
- 1.0.77028 – Current track version – Released on October 22,
  2024

### New features and improvements in this patch

- Adds support for automatic and incremental refresh of materialized views on tables from zero-ETL integrations with Amazon Aurora MySQL, Amazon Aurora PostgreSQL, Amazon RDS for MySQL, and Amazon DynamoDB.
- Improves how Amazon Redshift rewrites queries with correlated single-row subqueries, such as `SELECT … WHERE key = (SELECT … correlated subquery)`.
  Note that such queries are only valid if the subquery yields a single row.
  Due to the improved rewrite, certain queries that violate this condition might now fail with
  **`ERROR: single-row subquery returns more than one row`** in cases where they were previously permitted.
  To avoid this, such subqueries might need to be corrected so that they are guaranteed to return a single row,
  for example, by adding a MIN() or MAX() aggregate.
- Adds a SQL Identifier 'KAFKA' in Amazon Redshift to support streaming from external Kafka sources into Amazon Redshift with direct streaming ingestion.
  These sources include external Kafka sources such as Confluent Managed Cloud and Apache Kafka.
- Adds support for multi-warehouse writes using data sharing so that you can
  scale your write workloads and achieve better performance for extract,
  transform, and load (ETL) workloads by using different warehouses of various
  types and sizes, based on your workload needs.
- You can now run `SELECT` queries on Apache Iceberg tables managed in Amazon S3 Tables using Amazon Redshift
  For more information, see [Accessing Amazon S3 tables with Amazon Redshift](../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md") in the _Amazon Simple Storage Service User Guide_.
- Adds support for cross-database write queries in Amazon Redshift, so that you can
  write across multiple databases in an Amazon Redshift cluster. For more information,
  see [Cross-database queries](../dg/cross-database-overview.md "../dg/cross-database-overview.md").

## Amazon Redshift patch 185

Cluster versions in this patch:

- 1.0.79878 – Trailing track version – Released on December 3,
  2024
- 1.0.79868 – Amazon Redshift Serverless version – Released on December 3, 2024
- 1.0.79845 – Current track version – Released on December 3,
  2024
- 1.0.78946 – Trailing track version – Released on November 19,
  2024
- 1.0.78354 – Trailing track version – Released on November 12, 2024
- 1.0.78130 – Amazon Redshift Serverless version – Released on November 12, 2024
- 1.0.78125 – Current track version – Released on November 12, 2024
- 1.0.78016 – Amazon Redshift Serverless version – Released on November 5, 2024
- 1.0.78014 – Current track version – Released on November 5, 2024
- 1.0.77707 – Amazon Redshift Serverless version – Released on November 4, 2024
- 1.0.77687 – Current track version – Released on November 4, 2024
- 1.0.77467 – Amazon Redshift Serverless version – Released on November 4, 2024
- 1.0.77433 – Current track version – Released on November 4, 2024
- 1.0.77467 – Amazon Redshift Serverless version – Released on October 29, 2024
- 1.0.77433 – Current track version – Released on October 29, 2024
- 1.0.76991 – Amazon Redshift Serverless version – Released on October 21, 2024
- 1.0.76913 – Current track version – Released on October 21, 2024
- 1.0.76645 – Amazon Redshift Serverless version – Released on October 14, 2024
- 1.0.76642 – Current track version – Released on October 14, 2024
- 1.0.76242 – Amazon Redshift Serverless version – Released on October 10, 2024
- 1.0.76230 – Current track version – Released on October 10, 2024

### New features and improvements in this patch

- Adds support for incremental refresh of materialized views (MVs) created on
  data lake tables.
- Introduces support to alter the distribution key and sort key for materialized
  views.
- Adds support for the integration of Amazon Redshift machine learning (ML) with Amazon
  Bedrock to leverage large language models (LLMs) from simple SQL commands along
  with the data in Amazon Redshift.
- Fixes a bug that allowed the processing of empty shapefiles in Amazon Redshift spatial
  data without throwing errors.
- Fixes a bug that allowed varbit and varbinary datatypes to ingest an empty
  string value as "", rather than NULL, in a zero-ETL integration.
- Fixes a race condition with a result cache, which caused cross-database
  queries to return stale results in a zero-ETL integration.
- Optimizes the zero-ETL integration resync process, resulting in shorter resync
  times.
- Improves zero-ETL bootstrap time after recovery and system mainteanance
  operations. Now the system can recover the CDC after the last query operation,
  instead of being able to recover up until the latest available CDC point.
- Improves observability for zero-ETL integration with a new system table,
  `sys_integration_table_activity`. This table tracks zero-ETL
  integration table inserts, updates, and deletes.
- Improves the auto-creation of federated roles experience. Amazon Redshift administrators
  now have more control over the auto-creation of federated roles during federated
  user login. You can now to enable, disable, apply filters to, and configure
  auto-creation settings for each identity provider.
- IAM Identity Center users can run COPY, UNLOAD, and CREATE LIBRARY with IAM Identity Center credentials
  using S3 access grants.
- Auto-copy (COPY JOB) that enables continuous ingestion of files from Amazon S3, is now generally available.

## Amazon Redshift patch 184

Cluster versions in this patch:

- 1.0.77706 – Trailing track version – Released on November 12, 2024
- 1.0.76832 – Trailing track version – Released on October 17, 2024
- 1.0.76169 – Amazon Redshift Serverless version – Released on October 10, 2024
- 1.0.76142 – Current track version – Released on October 10, 2024
- 1.0.75677 – Amazon Redshift Serverless version – Released on September 27, 2024
- 1.0.75672 – Current track version – Released on September 27, 2024
- 1.0.75504 – Amazon Redshift Serverless version – Released on September 23, 2024
- 1.0.75449 – Current track version – Released on September 24, 2024
- 1.0.74765 – Amazon Redshift Serverless version – Released on September 12, 2024
- 1.0.74754 – Current track version – Released on September 12, 2024

### New features and improvements in this patch

- Amazon Redshift streaming materialized views (MVs) for streaming data ingestion have increased VARBYTE column sizes up from 1,024,000 bytes.
  Amazon Redshift can now ingest records from Amazon Kinesis Data Streams up to 1,048,576 bytes, or 1MiB. Redshift can ingest records from Amazon Managed Streaming for Apache Kafka up to
  16,777,216 bytes, or 16 MiB.
  If you're using the ATA SQL command `ALTER TABLE <target_tbl> APPEND FROM <streaming_mv>`,
  please drop and recreate your <target_tbl> to have the corresponding larger VARBYTE column sizes.
- Amazon Redshift datashares now can include Amazon S3 data lake tables and views that reference AWS Glue Data Catalog including tables governed by Lake Formation.
- Adds support for automatic and incremental refresh of materialized views on tables from zero-ETL integration with DynamoDB.
- Adds support to configure the 'refresh interval' on zero-ETL integration tables to specify the replication refresh rate on Amazon Redshift.
  You can set it at the time of creating a database for a new integration or alter the database of an existing integration.
- Adds support for Mutual Transport Layer Security (mTLS) authentication in Amazon Redshift streaming ingestion for Amazon Managed Streaming for Apache Kafka.
- Adds support for query hash, a unique identifier for a SQL query based on the textual representation of the query and the values of its parameters.
  It can be used to identify, group, and analyze similar queries. Query hash can now be found in SYS_QUERY_HISTORY view,
  with the addition of two new columns:
  - `user_query_hash` – The hash as submitted by the user including the query literals.
  - `generic_query_hash` - The hash as submitted by the user without any query literals.

- Fixes system deadlock in a rare case where zero-ETL was running CDC replication and scan, performing table queries with result cache.
- Addresses an issue in Workload Management (WLM) where a Python User Defined Function (UDF) queries would preempt other queries
  when WLM resources for Python UDF queries were unavailable.
- Addresses an issue where Workload Management (WLM) would fail to route queries to the queue mapped to a newly created user role.
- Improves disk utilization on smaller data sharing consumers querying large producer tables.
- Improves performance of INSERT statements for provisioned clusters elastically resized to a higher size.

## Amazon Redshift patch 183

Cluster versions in this patch:

- 1.0.75655 – Trailing track version – Released on September 30, 2024
- 1.0.75388 – Amazon Redshift Serverless version – Released on September 25, 2024
- 1.0.75379 – Current track version – Released on September 25, 2024
- 1.0.74967 – Amazon Redshift Serverless version – Released on September 17, 2024
- 1.0.74927 – Current track version – Released on September 17, 2024
- 1.0.74518 – Amazon Redshift Serverless version – Released on September 11, 2024
- 1.0.74503 – Current track version – Released on September 11, 2024
- 1.0.74223 – Amazon Redshift Serverless version – Released on September 5, 2024
- 1.0.74159 – Current track version – Released on September 5, 2024
- 1.0.74126 – Amazon Redshift Serverless version – Released on August 30, 2024
- 1.0.74097 – Current track version – Released on August 30, 2024
- 1.0.73016 – Amazon Redshift Serverless version – Released on August 8, 2024
- 1.0.72982 – Current track version – Released on August 8, 2024

### New features and improvements in this patch

- Adds support for discovery of Scoped Permissions via SVV_DATABASE_PRIVILEGES and SVV_SCHEMA_PRIVILEGES. Also introduces the column privilege_scope to SVV_DATABASE_PRIVILEGES and SVV_SCHEMA_PRIVILEGES.
- Improves performance of queries that execute distinct aggregation operations when grouping columns have a low number of distinct values (NDV).
- Improves performance of INSERT/COPY statements for provisioned data warehouses
  elastically resized by 2x or higher in size.
- Supports session context variables inside a Dynamic Data Masking policy.
- Adds support for subqueries and views as the source for the MERGE statement.
- Supports stored procedures containing a MERGE statement on provisioned concurrency scaling and serverless autoscaling compute.
- Improves query performance with better resource prediction in workload management for COPY commands and for warehouses which undergo resizes.
- Improves resilience to out of memory errors in clusters with limited memory available
- Adds support for non-ASCII characters as field delimiters to the COPY command.
- Adds support for ingesting data encoded in the ISO-8859-1 character set using the COPY command.
- Removes requirement to specify CLUSTER_ARN in MSK external schema definition if specifying URI.
- Supports applying range scan filters during scans on zero-ETL integration tables.
- Supports adding sort keys to zero-ETL integration tables.
- Supports database options like `serializable` and `collation` to be specified with CREATE DATABASE statement when creating a zero-ETL integration database.
- Fixed the issue that was causing the cluster to restart when the data filter exceeded 2 KB in a zero-ETL integration.

## Amazon Redshift patch 182

Cluster versions in this patch:

- 1.0.73589 – Trailing track version – Released on August 22, 2024
- 1.0.73359 – Amazon Redshift Serverless version – Released on August 15, 2024
- 1.0.73348 – Current track version – Released on August 15, 2024
- 1.0.72917 – Amazon Redshift Serverless version – Released on August 12, 2024
- 1.0.72899 – Current track version – Released on August 12, 2024
- 1.0.72528 – Amazon Redshift Serverless version – Released on August 7, 2024
- 1.0.72503 – Current track version – Released on August 8, 2024
- 1.0.72239 – Amazon Redshift Serverless version – Released on August 1, 2024
- 1.0.71714 – Amazon Redshift Serverless version – Released on July 24, 2024
- 1.0.71629 – Current track version – Released on July 24, 2024
- 1.0.70953 – Amazon Redshift Serverless version – Released on July 11, 2024
- 1.0.70890 – Current track version – Released on July 11, 2024
- 1.0.70716 – Amazon Redshift Serverless version – Released on July 8, 2024
- 1.0.70695 – Current track version – Released on July 8, 2024
- 1.0.69945 – Amazon Redshift Serverless version – Released on June 27, 2024
- 1.0.69938 – Current track version – Released on June 27, 2024

### New features and improvements in this patch

- Updates LISTAGG, MEDIAN, PERCENTILE_CONT and PERCENTILE_DISC to no longer require user-defined tables. Queries that reference catalog tables
  or that don't reference any tables can also use these functions.
- Reduces query-planning time for datasharing read queries by consolidating temp tables across multiple queries within
  a single session, for high-concurrency workloads.
- Provides general availability of Redshift machine learning (ML) integration with Amazon SageMaker AI Jumpstart, for bringing
  your own large-language models.
- Introduces support for the SUPER input and output data type in Redshift ML.
- Enables support for an UPDATE statement with a JOIN clause when the target table is protected by a
  dynamic data-masking policy and referenced in the JOIN clause.
- Allows querying of a zero-ETL database on Redshift, even after the integration is deleted from source.
- Fixes a replication error that could cause zero-ETL integration to fail. This
  makes an integration more resilient.
- Allows users other than the user who created a zero-ETL integration to query the data, after GRANT permissions.
- Fixes an out-of-memory issue that could cause cluster restarts in an Amazon Redshift provisioned cluster with zero-ETL integration enabled.
- Enables creation of an RDS for MySQL zero-ETL integration with Redshift, from a source RDS Multi-AZ DB cluster. A Multi-AZ DB cluster is a
  semisynchronous, high-availability deployment mode of Amazon RDS with two readable replica DB instances.
- Enables a user to connect to an Amazon MSK cluster from an Amazon Redshift streaming consumer client by
  specifying the Amazon MSK cluster's broker URI in the external schema definition needed to associate an Amazon Redshift streaming materialized view with an Amazon MSK topic.
  This feature removes the need to obtain the Amazon MSK bootstrap broker node name by calling the GetBootStrapBroker API
  on the Amazon MSK cluster over an internet gateway.
- Resolves the issue with resuming Amazon Redshift Serverless instances, enabling an existing database user to resume a Serverless instance
  when connecting to databases in Amazon Redshift query editor v2, using the IAM Identity Center authentication method.
- Optimizes CDC replication and reduced resource utilization on Redshift compute by moving to
  table-based sharding.
- Improves query performance using enhanced resource prediction in workload management (WLM).
- Fixes queries failing on concurrency scaling clusters with the message: **`ran out of WLM queues for restart`**.
- Fixes a workload management (WLM) issue where Amazon Redshift falls back to manual WLM when customers try to apply an invalid WLM configuration.
- Allows data sharing consumers to run read queries even when the producer is down due to planned maintenance or an unplanned outage.
- Fixes a rare cluster restart issue that occurs when the ANY_VALUE function is used in queries that aggregate data, for example, the COUNT(DISTINCT) aggregation function.

## Amazon Redshift patch 181

Cluster versions in this patch:

- 1.0.72031 – Current track version – Released on August 1, 2024
- 1.0.71912 – Trailing track version – Released on August 1, 2024
- 1.0.70665 – Amazon Redshift Serverless version – Released on July 8, 2024
- 1.0.70634 – Current track version – Released on July 8, 2024
- 1.0.69954 – Amazon Redshift Serverless version – Released on June 26, 2024
- 1.0.69952 – Current track version – Released on June 26, 2024
- 1.0.69497 – Amazon Redshift Serverless version – Released on June 18, 2024
- 1.0.69451 – Current track version – Released on June 18, 2024
- 1.0.69076 – Amazon Redshift Serverless version – Released on June 14, 2024
- 1.0.69065 – Current track version – Released on June 14, 2024
- 1.0.68555 – Amazon Redshift Serverless version – Released on May 31, 2024
- 1.0.68540 – Current track version – Released on May 31, 2024
- 1.0.68328 – Amazon Redshift Serverless version – Released on May 23, 2024
- 1.0.68205 – Current track version – Released on May 23, 2024
- 1.0.67796 – Amazon Redshift Serverless version – Released on May 15, 2024
- 1.0.67788 – Current track version – Released on May 15, 2024
- 1.0.67308 – Amazon Redshift Serverless version – Released on May 1, 2024
- 1.0.67305 – Current track version – Released on May 1, 2024

### New features and improvements in this patch

- Introduces support for the 'lower_attribute_names()' and 'upper_attribute_names()' functions which modify the case of attribute names for SUPER object values.
- Fixes an issue in CREATE TABLE LIKE when using an identity column. Previously, the new table would inherit the identifier from the source table.
  This caused problems if the source table was later dropped, since the identifier would become invalid in the new table.
- Fixes an issue preventing some external tables from showing in SVV_ALL_TABLES.
- Improves cluster bootstrap time, and speeds up query initialization for high concurrent workloads.
- Fixes an issue with federated query that caused errors when passing split_part() functions to the federated source to RDS and Aurora MySQL
- Supports user initiated changes to the distribution key through ALTER TABLE...ALTER DISTSTYLE KEY DISTKEY commands on provisioned concurrency scaling clusters and serverless autoscaling compute.
- Supports manually refreshed materialized views that involve aggregation on provisioned concurrency scaling and serverless autoscaling compute.
- Adds support for zero-ETL to handle records up to 16 MB in size and for supporting SUPER values up to 16 MB.
- Enhances error messages during initial sync in zero-ETL from Aurora MySQL by providing additional details like schema and table name.
- Introduces support for tagging with Amazon Redshift ML CREATE MODEL. With this improvement, you can now tag Amazon SageMaker AI resources used by Amazon Redshift ML.
  Tagging helps you manage, identify, organize, search for, and filter resources.
- Improves the performance of queries involving Lambda user-defined functions (UDFs) by optimizing the data processing with the AWS Lambda.
- Reduces memory utilization during data ingestion in sorted tables of elastically resized and serverless clusters.
- Adds support for newlines (\n) in column `query_text` in view SYS_QUERY_HISTORY and for column `text` in view SYS_QUERY_TEXT.

## Amazon Redshift patch 180

Cluster versions in this patch:

- 1.0.68520 – Trailing track version – Released on May 28, 2024
- 1.0.67699 – Trailing track version – Released on May 15, 2024
- 1.0.66960 – Trailing track version – Released on April 21, 2024
- 1.0.66954 – Current track version – Released on April 21, 2024
- 1.0.66276 – Current track version – Released on April 12, 2024
- 1.0.66290 – Amazon Redshift Serverless version – Released on April 10, 2024
- 1.0.63590 – Current track version – Released on February 19, 2024
- 1.0.63567 – Amazon Redshift Serverless version – Released on February 16, 2024
- 1.0.63282 – Amazon Redshift Serverless version – Released on February 13, 2024
- 1.0.63269 – Current track version – Released on February 13, 2024
- 1.0.63215 – Amazon Redshift Serverless version – Released on February 12, 2024
- 1.0.63205 – Current track version – Released on February 12, 2024
- 1.0.63030 – Amazon Redshift Serverless version – Released on February 7, 2024
- 1.0.62913 – Current track version – Released on February 7, 2024
- 1.0.62922 – Amazon Redshift Serverless version – Released on February 5, 2024
- 1.0.62878 – Current track version – Released on February 5, 2024
- 1.0.62698 – Amazon Redshift Serverless version – Released on January 31, 2024
- 1.0.62614 – Current track version – Released on January 31, 2024
- 1.0.61687 – Amazon Redshift Serverless version – Released on January 5, 2024
- 1.0.61678 – Current track version – Released on January 5, 2024
- 1.0.61567 – Amazon Redshift Serverless version – Released on December 31, 2023
- 1.0.61559 – Current track version – Released on December 31, 2023
- 1.0.61430 – Amazon Redshift Serverless version – Released on December 29, 2023
- 1.0.61395 – Current track version – Released on December 29, 2023

### New features and improvements in this patch

- Changes CURRENT_USER to no longer truncate the returned username to 64 characters.
- Adds the ability to apply data masking policies on standard views and late binding views.
- Adds the ability to apply dynamic data masking (DDM) to scalar attributes in SUPER data type columns.
- Adds OBJECT_TRANSFORM SQL function.
  For more information, see
  [OBJECT_TRANSFORM function](../dg/r_object_transform_function.md "../dg/r_object_transform_function.md")
  in the _Amazon Redshift Database Developer Guide_.
- Adds the ability to apply AWS Lake Formation fine-grained access control to your nested data, and query with Amazon Redshift data lake analytics.
- Adds the INTERVAL data type.
- Adds CONTINUE_HANDLER, which is a type of exception handler that controls the flow of a stored procedure.
  Using it, you can catch and handle exceptions without ending the existing statement block.
- Adds the ability to define permissions on a scope (schema or database) in addition to individual objects.
  This allows users and roles to be granted a permission on all current and future objects within the scope.
- Adds the ability to create a database from a datashare with permissions that let consumer-side administrators
  grant individual permissions on shared database objects to consumer-side users and roles.
- Adds support for the SUPER return data type from remote BYOM models.
  This expands the range of accepted SageMaker AI models to include those with more complex return formats.
- Changes external functions to now implicitly cast numbers with or without fractional parts to the numeric data type of the column.
  For int2, int4, and int8 columns, numbers with fractional digits are accepted by truncating unless the number is out of range.
  For float4 and float8 columns, numbers are accepted without fractional digits.
- Adds three spatial functions that work with the H3 hierarchical geospatial indexing grid system: H3_FromLongLat, H3_FromPoint, and H3_Polyfill.

## Amazon Redshift patch 179

Cluster versions in this patch:

- 1.0.62317 – Amazon Redshift Serverless version – Released on January 29, 2024
- 1.0.62312 – Trailing track version – Released on January 29, 2024
- 1.0.61631 – Amazon Redshift Serverless version – Released on January 5, 2024
- 1.0.61626 – Current track version – Released on January 5, 2024
- 1.0.61191 – Current track version – Released on December 16, 2023
- 1.0.61150 – Amazon Redshift Serverless version – Released on December 16, 2023
- 1.0.60982 – Amazon Redshift Serverless version – Released on December 13, 2023
- 1.0.60854 – Current track version – Released on December 10, 2023
- 1.0.60354 – Amazon Redshift Serverless version – Released on November 22nd, 2023
- 1.0.60353 – Current track version – Released on November 21st, 2023
- 1.0.60293 – Amazon Redshift Serverless version – Released on November 21st, 2023
- 1.0.60292 – Current track version – Released on November 22nd, 2023
- 1.0.60161 – Amazon Redshift Serverless version – Released on November 18th, 2023
- 1.0.60140 – Current track version – Released on November 18th, 2023
- 1.0.60139 – Amazon Redshift Serverless version – Released on November 18th, 2023
- 1.0.59947 – Amazon Redshift Serverless version – Released on November 16th, 2023
- 1.0.59945 – Current track version – Released on November 16th, 2023
- 1.0.59118 – Amazon Redshift Serverless version – Released on November 9th, 2023
- 1.0.59117 – Current track version – Released on November 9th, 2023

### New features and improvements in this patch

- Adds support so that federated users
  with appropriate permissions can view row-level
  security and dynamic data masking system views, including:
  - SVV_ATTACHED_MASKING_POLICY
  - SVV_MASKING_POLICY
  - SVV_RLS_ATTACHED_POLICY
  - SVV_RLS_POLICY
  - SVV_RLS_RELATION

- Adds functionality such that a query that contains only scalar
  functions in the FROM clause now results in an error.
- Adds CREATE TABLE AS (CTAS) statements with permanent
  target tables functionality to concurrency scaling clusters.
  Concurrency scaling clusters now support more queries.
- Adds the following system tables to track table
  redistribution status after running classic resize on
  RA3 clusters:
  - The SYS_RESTORE_STATE system table
    shows table level redistribution progress.
  - The SYS_RESTORE_LOG system table
    shows historical throughput of data redistribution.

- Improves slice skew minimizing on EVEN tables after running
  classic resize on RA3 node types. This is also applicable
  to patch 178 clusters that ran classic resize.
- Adds support for UNLOAD with EXTENSION on
  concurrency scaling clusters.
- Improves performance for queries that
  contain Λ UDFs in HashJoins and NestLoop joins.
- Improves performance of Elastic Resize on RA3 node types.
- Improves performance for data sharing queries.
- Improves performance of manually initiated analyze
  queries in elastic-resized provisioned clusters
  and serverless workgroup.
- Improves auto WLM query performance with better
  resource prediction in workload management.
- Removes the functionality of launching clusters
  into dedicated tenancy VPCs. This change doesn't affect
  tenancy of any EC2 instances in the VPC. You can modify
  tenancy of your VPC to default with the
  `modify-vpc-tenancy` AWS CLI command.
- Materialized view manual refresh is now supported on
  provisioned concurrency scaling clusters and
  serverless autoscaling compute.
- Adds support for INTERVAL literals to the EXTRACT function.
  For example, `EXTRACT('hours' from Interval '50 hours')` returns `2` because 50 hours is interpreted as 2 days and 2 hours,
  and the hour component of 2 is extracted.

## Amazon Redshift patch 178

Cluster versions in this patch:

- 1.0.63327 - Current track version – Released on February 9, 2024
- 1.0.63313 - Trailing track version – Released on February 9, 2024
- 1.0.60977 - Trailing track version – Released on December 15, 2023
- 1.0.59596 - Current track version – Released on November 9th, 2023
- 1.0.58593 - Amazon Redshift Serverless version – Released on October 23rd, 2023
- 1.0.58558 - Current track version – Released on October 23rd, 2023
- 1.0.57864 - Current track version – Released on October 12th, 2023
- 1.0.57850 - Amazon Redshift Serverless version – Released on October 12th, 2023
- 1.0.56952 - Current track version – Released on September 25th, 2023
- 1.0.56970 - Amazon Redshift Serverless version – Released on September 25th, 2023

### New features and improvements in this patch

- Amazon Redshift now has improved data sharing query performance by speeding up metadata
  refresh on consumer instances while concurrent data changes are happening on the producer instance.
- Adds support for automatic and incremental refresh of materialized
  views on Amazon Redshift data sharing consumer instances when the base tables of the
  materialized view refer to the shared data.
- Adds support for storing large objects up to 16 MB in size in the SUPER data type.
  When ingesting from JSON, PARQUET, TEXT, and CSV source files, you can load semi-structured data
  or documents as values in the SUPER data type, up to 16 MB.
- Adds support for elastic resize for scaling to and from a single-node Amazon Redshift RA3 cluster.
- Single-node Amazon Redshift RA3 clusters now can now benefit from encryption enhancements,
  reducing the overall encryption time and improving the availability of the data warehouse during the encryption process.
- Improves support for queries when unnesting and unpivoting data stored in the SUPER data type.
- Improves performance of refreshing materialized views with SUPER data types.
- Adds support for aggregating INTERVAL literals with the ANY_VALUE function.
- Streaming ingestion now supports the following new SQL command to purge streaming data:
  `DELETE FROM streaming_materialized_views WHERE <where filter clause>`.
- The DECODE function replaces a specific value with either another specific value or a default value,
  depending on the result of an equality condition. DECODE now requires the following three parameters:
  - expression
  - search
  - result

- Adds functionality to stored procedures to allow for catching data overflow
  data type conversion errors, and handling inside an exception-handling block.
- You'll now receive an error when querying row-level security or dynamic data
  masking-protected relations if you change enable_case_sensitive_identifier to be
  different from the session default setting. Additionally, the following configuration is blocked when
  row-level security or dynamic data masking policies are applied in your provisioned cluster or serverless
  namespace:

`ALTER USER <current_user> SET case-sensitive identifier`.

- The MERGE command now supports a simplified syntax that only requires the target and
  source table. For more information, see
  [MERGE](../dg/r_MERGE.md "../dg/r_MERGE.md")
  in the _Amazon Redshift Database Developer Guide_.
- Adds support for attaching identical dynamic data masking policies
  to multiple users or roles with the same priority, or without specifying the priority.
- You can now specify a COLLATION when adding a new column through ALTER TABLE ADD COLUMN.
- Fixes issue that delays the enforcement of QMR rules
  on concurrency scaling clusters and Amazon Redshift Serverless.
- Amazon Redshift Federated Query has expanded pushdown support for timezone with timestamp on Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL.
- You can now use Amazon RDS for MySQL and Aurora MySQL database names starting with digits with federated queries.
- Adds the SYS_ANALYZE_HISTORY view, which contains record details for ANALYZE operations.
- Adds the SYS_ANALYZE_COMPRESSION_HISTORY view, which contains record
  details for compression analysis operations during COPY or ANALYZE COMPRESSION commands.
- Adds the SYS_SESSION_HISTORY view, which contains record details related
  to active, historical, and restarted sessions.
- Adds the SYS_TRANSACTION_HISTORY view, which contains record details
  related to transaction level analysis that provides the time spent on commit, datasha
  number of blocks committed, and isolation level.
- Adds the SVV_REDSHIFT_SCHEMA_QUOTA view, which contains records related to
  quotas and the current disk usage for each schema in a database.
- Adds the SYS_PROCEDURE_CALL view, which contains records
  related to stored procedure calls, including start time, end time,
  status of the stored procedure call, and call hierarchy for
  nested stored procedure calls.
- Adds the SYS_CROSS_REGION_DATASHARING_USAGE view, which contains
  records related to tracking cross-Region data sharing usage.
- Adds the SYS_PROCEDURE_MESSAGES view, which contains records related to tracking
  information about logged stored procedure messages.
- Adds the SYS_UDF_LOG view, which contains records related to tracking system log messages
  from user-defined function calls, errors, warnings, or traces when applicable.
- Adds the new columns IS_RECURSIVE, IS_NESTED, S3LIST_TIME, and GET_PARTITION_TIME to
  SYS_EXTERNAL_QUERY_DETAIL.
- Adds MaxRPU, a new compute cost control setting for Redshift Serverless.
  With MaxRPU, you can optionally specify an upper compute threshold to control data warehouse costs at different points in time by selecting
  the maximum compute level that Redshift Serverless can scale per workgroup.
- Corrects the output of the INTERVAL literal with numeric interval strings.
  For example, an interval that specifies as `INTERVAL '1' YEAR` now returns `1 YEAR` instead of `"00:00:00`.
  In addition, the output of the INTERVAL literal is truncated to the smallest INTERVAL component specified.
  For example, `INTERVAL '1 day 1 hour 1 minute 1.123 seconds' HOUR TO MINUTE` is truncated to `1 day 01:01:00`.

## Amazon Redshift patch 177

Cluster versions in this patch:

- 1.0.57922 - Trailing track version – Released on October 12th, 2023
- 1.0.57799 - Amazon Redshift Serverless version – Released on October 10th, 2023
- 1.0.57798 - Current track version – Released on October 10th, 2023
- 1.0.57085 - Trailing track version – Released on September 26th, 2023
- 1.0.56899 - Amazon Redshift Serverless version – Released on September 21st, 2023
- 1.0.56754 - Current track version – Released on September 21st, 2023
- 1.0.56242 - Current track version – Released on September 11th, 2023
- 1.0.55539 - Amazon Redshift Serverless version – Released on August 28th, 2023
- 1.0.55524 - Current track version – Released on August 28th, 2023
- 1.0.54899 - Current track version – Released on August 15th, 2023
- 1.0.54899 - Current track version – Released on August 14th, 2023
- 1.0.54899 - Current track version – Released on August 15th, 2023
- 1.0.54239 - Current track version – Released on August 3rd, 2023
- 1.0.54321 - Amazon Redshift Serverless version – Released on August 3rd, 2023

### New features and improvements in this patch

- Adds the SYS_MV_STATE view, which contains a row for every state transition of a materialized view.
  SYS_MV_STATE can be used for MV refresh monitoring for Amazon Redshift Serverless and Amazon Redshift
  provisioned instances.
- Adds the SYS_USERLOG view, which records details for the changes to a database user for Create user,
  Drop user, Alter user (rename), Alter user (alter properties).
- Adds the SYS_COPY_REPLACEMENTS view, which displays a log that records when invalid UTF-8 characters were
  replaced by the COPY command with the ACCEPTINVCHARS option.
- Adds the SYS_SPATIAL_SIMPLIFY view, which contains information about simplified
  spatial geometry objects using the COPY command.
- Adds the SYS_VACUUM_HISTORY view, which you can use to see the details and results of VACUUM operations.
- Adds the SYS_SCHEMA_QUOTA_VIOLATIONS view to record the occurrence, timestamp, XID, and other
  useful information when a schema quota is exceeded.
- Adds the SYS_RESTORE_STATE view, which you can use monitor the redistribution progress of each table in the
  cluster during asynchronous classic resize.
- Adds the SYS_EXTERNAL_QUERY_ERROR view that return information about Redshift Spectrum scan errors.
- Adds the tag parameter to the CREATE MODEL command, so you can now track training costs with
  autopilot training jobs.
- Adds custom domain names (CNAME) for Amazon Redshift clusters.
- Adds preview support for Apache Iceberg, enabling customers to run analytics queries on Apache Iceberg tables within Amazon Redshift.
- Adds support for using user roles with parameter groups in workload management (WLM).
- Adds support for automatic mounting of AWS Glue Data Catalog, making it easier for
  customers to run queries in their data lakes.
- Adds functionality such that using grouping functions without a GROUP BY clause or using grouping operations in
  a WHERE clause results in an error.
- Adds functionality to stored procedures to allow for catching divide by zero errors and handling inside
  a exception-handling block.
- Fixes a bug that prevented queries from using concurrency scaling to write data to
  tables when the source table is a data sharing table.
- Fixes the case-sensitive identifier documented at enable_case_sensitive_identifier to now work with MERGE statements.
- Fixes the bug that a query on the function pg_get_late_binding_view_cols() might get ignored occasionally.
  You can now always cancel such queries.
- Improves performance for data sharing queries running on consumers when running vacuum
  jobs on the producer.
- Improves performance for data sharing and concurrency scaling queries, especially
  with concurrent data changes on the producer or when offloading to a concurrency scaling instance
  attached to the consumer.

## Amazon Redshift patch 176

Cluster versions in this patch:

- 1.0.56738 - Trailing track version – released on September 21st, 2023
- 1.0.55837 - Trailing track version – released on September 11th, 2023
- 1.0.54776 - Current track version – released on August 15th, 2023
- 1.0.54052 - Current track version – Released on July 26th, 2023
- 1.0.53642 - Amazon Redshift Serverless version – Released on July 20th, 2023
- 1.0.53301 - Current track version – Released on July 20th, 2023
- 1.0.52943 - Amazon Redshift Serverless version – Released on July 7, 2023
- 1.0.52931 - Current track version – Released on July 7, 2023
- 1.0.52194 - Amazon Redshift Serverless version – Released on June 21, 2023
- 1.0.51986 - Current track version – Released on June 16, 2023
- 1.0.51594 - Current track version – Released on June 9, 2023

### New features and improvements in this patch

- Improved error handling when writing GROUP BY () for an empty grouping set. This was ignored previously and now returns a parser error.
- Performance enhancements for incrementally refreshing
  materialized views with SUPER columns.
- ALTER TABLE <target_tbl> APPEND FROM <streaming_mv> – (ATA) SQL command now supports moving all records from a
  streaming materialized view (MV) as a source, in addition to tables as a source, to a target table. The support for ATA on streaming
  MVs allows users to rapidly purge all records in a streaming MV by moving them to another table to manage data growth.
- TRUNCATE <streaming_mv> – SQL command now supports truncating all records in a streaming materialized
  view (MV), in addition to tables. TRUNCATE deletes all records in the streaming MV, while leaving the streaming MV structure intact. Running
  TRUNCATE on streaming MVs allows customers to rapidly purge all records in a streaming
  MV to manage data growth.
- Added functionality for the QUALIFY clause to the SELECT command.
- Redshift machine-learning support for time series forecasting by integrating with Amazon Forecast.
- AWS Glue Data Catalog auto mounting is supported to simplify querying a data lake without extra steps
  to create external schema references.
- Altering an RLS policy is now supported. Refer to the documentation for more
  details at [ALTER RLS POLICY](../dg/r_ALTER_RLS_POLICY.md "../dg/r_ALTER_RLS_POLICY.md").
- Lambda UDFs now support the STABLE function-volatility parameter in the CREATE FUNCTION statement. When the STABLE
  parameter is used in the CREATE FUNCTION statement and the Lambda UDF is called multiple times, with the same arguments, the expected
  number of Lambda UDF function invocations is decreased. The STABLE function volatility category is explained in
  more detail in the [CREATE FUNCTION parameters](../dg/r_CREATE_FUNCTION.md#r_CREATE_FUNCTION-parameters "../dg/r_CREATE_FUNCTION.md#r_CREATE_FUNCTION-parameters").
- Multiple Lambda UDF performance improvements. Specifically, improved record batching support when querying a
  table protected by a row-level security (RLS) policy.
- Reduction in the overall encryption time for Amazon Redshift RA3 clusters and improvement in the availability of the data warehouse during encryption. For more
  information, see [Amazon Redshift database encryption](working-with-db-encryption.md "working-with-db-encryption.md").
- A new system view SYS_MV_REFRESH_HISTORY has been added to Redshift. The SYS_MV_REFRESH_HISTORY view contains a
  row for the refresh activity of materialized views. Using SYS_MV_REFRESH_HISTORY, you can check the refresh history of materialized
  views. SYS_MV_REFRESH_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data.

A new column SPILLED_BLOCK_LOCAL_DISK has been added to system view SYS_QUERY_DETAIL. The new column SPILLED_BLOCK_LOCAL_DISK helps customers
to determine blocks spilled to local disk. You can use SYS_QUERY_DETAIL to view details for queries at a step level. SYS_QUERY_DETAIL is
visible to all users. Superusers can see all rows; regular users can see only metadata to which they have access.

- A new system view, SYS_QUERY_TEXT, has been added to Amazon Redshift Serverless and Amazon Redshift provisioned. The SYS_QUERY_TEXT view is similar
  to [SVL_STATEMENTTEXT](../dg/r_SVL_STATEMENTTEXT.md "../dg/r_SVL_STATEMENTTEXT.md") for provisioned clusters. Use the `sequence`
  column in the SYS_QUERY_TEXT view to get complete SQL statement text.

## Amazon Redshift patch 175

Cluster versions in this patch:

- 1.0.53064 - Current track version – Released on July 7, 2023
- 1.0.51973 - Current track version – Released on June 16, 2023
- 1.0.51781 - Current track version – Released on June 10, 2023
- 1.0.51314 - Amazon Redshift Serverless version – Released on June 3, 2023
- 1.0.51304 - Current track version – Released on June 2, 2023
- 1.0.50708 - Current Track version – Released on May 19, 2023
- 1.0.50300 - Current track version – Released on May 8, 2023
- 1.0.49710 - Amazon Redshift Serverless version – Released on April 28, 2023
- 1.0.49676 - Current track version – Released on April 28, 2023

### New features and improvements in this patch

- Minor bug fixes.
- Amazon Redshift streaming ingestion now supports cross-region streaming ingestion where your
  source Amazon Kinesis Data Streams (KDS) or Amazon Managed Streaming for Apache Kafka (MSK) topic can be located in an AWS region that is different from
  the AWS region where your Amazon Redshift data warehouse is located. The documentation
  at [Getting started with streaming
  ingestion from Amazon Kinesis Data Streams](../dg/materialized-view-streaming-ingestion-getting-started.md "../dg/materialized-view-streaming-ingestion-getting-started.md") has been revised and explains how the REGION keyword is used.
- Egypt daylight saving adjustment.
- Improved overall times for encryption of RA3 clusters.

## Amazon Redshift patch 174

### 1.0.51296 – Released on June 2, 2023

Release to trailing track. No release notes.

### 1.0.50468 – Released on May 12, 2023

Maintenance release. No release notes.

### 1.0.49780, 1.0.49868, and 1.0.49997 – Released on April 28, 2023

Release notes for this version:

- Improved batching support for Lambda UDF.
- Incremental batching for Lambda UDF.
- New MERGE SQL command to apply source data changes to Amazon Redshift tables.
- New dynamic data masking capability to simplify the process of protecting sensitive data in an Amazon Redshift data warehouse.
- New centralized access control for data sharing with Lake Formation that allows managing permission grants, viewing access controls, and auditing permissions on the tables and views
  in the Amazon Redshift datashares using Lake Formation APIs and the AWS Console.
- Egypt daylight saving adjustment.

### 1.0.49087 – Released on April 12, 2023

Maintenance release. No release notes.

### 1.0.48805 – Released on April 5, 2023

Release notes for this version:

- Amazon Redshift introduced additional performance enhancements to string-heavy queries using BYTEDICT,
  a new compression encoding in Amazon Redshift that speeds up string-based data processing between 5x to
  63x compared to alternative compression encodings such as LZO or ZSTD. For more information on this
  feature, see [Compression encodings](../dg/c_Compression_encodings.md "../dg/c_Compression_encodings.md") in the _Amazon Redshift Database Developer Guide_.

### 1.0.48004 – Released on March 17, 2023

Maintenance release. No release notes.

### 1.0.47470 – Released on March 11, 2023

Release notes for this version:

- Improves query performance on `pg_catalog.svv_table_info`. Also
  adds new column `create_time`. When creating a table, this column stores the date/time stamp in UTC.
- Adds support for specifying session level timeout on federated query.

## Amazon Redshift patch 173

### 1.0.49788 – Released on April 28, 2023

Release notes for this version:

- Egypt daylight saving adjustment.

### 1.0.49074 – Released on April 12, 2023

Release notes for this version:

- Timezone configuration updated to IANA library release 2022g.

### 1.0.48766 – Released on April 5, 2023

Maintenance release. No release notes.

### 1.0.48714 – Released on April 5, 2023

Maintenance release. No release notes.

### 1.0.48022 – Released on March 17, 2023

Maintenance release. No release notes.

### 1.0.47357 – Released on March 7, 2023

Maintenance release. No release notes.

### 1.0.46987 – Released on February 24, 2023

Maintenance release. No release notes.

### 1.0.46806 – Released on February 18, 2023

Maintenance release. No release notes.

### 1.0.46607 – Released on February 13, 2023

Release notes for this version:

- We now automatically convert tables with manually set interleaved sort keys to compound sort keys if
  their distribution style has been set to **DISTSTYLE KEY**, to improve
  the performance of these tables. This is done at the time of restoring a snapshot
  into Amazon Redshift Serverless.

### 1.0.45698 – Released on January 20, 2023

Release notes for this version:

- Adds a file extension parameter to the UNLOAD command, so file extensions are automatically added to filenames.
- Supports protecting RLS-protected objects by default when adding them to a datashare or if they're already part of a datashare.
  Administrators can now turn off RLS for datashares to allow consumers access to the protected object.
- Adds new system tables for monitoring: `SVV_ML_MODEL_INFO`, `SVV_MV_DEPENDENCY`, and `SYS_LOAD_DETAIL`. Also adds
  the columns `data_skewness` and `time_skewness` to the system table `SYS_QUERY_DETAIL`.

## Amazon Redshift patch 172

Cluster versions in this patch:

- 1.0.46534 – Released on February 18, 2023
- 1.0.46523 – Released on February 13, 2023
- 1.0.46206 – Released on February 1, 2023
- 1.0.45603 – Released on January 20, 2023
- 1.0.44924 – Released on December 19, 2022
- 1.0.44903 – Released on December 18, 2022
- 1.0.44540 – Released on December 13, 2022
- 1.0.44126 – Released on November 23, 2022
- 1.0.43980 – Released on November 17, 2022

### New features and improvements in this patch

- Tables created by CTAS are AUTO by default.
- Adds support for row-level security (RLS) on materialized views.
- Increases the S3 timeout to improve cross-Region data sharing.
- Adds new spatial function `ST_GeomFromGeohash`.
- Improves automatic selection of distribution key from composite primary keys to improve out-of-the-box performance.
- Adds automatic primary key to distribution key for tables with composite primary keys, improving out-of-the-box performance.
- Improves concurrency scaling to allow more queries to scale even as data changes.
- Improves data sharing query performance.
- Adds Machine Learning probability metrics for classification models.
- Adds new system tables for monitoring: `SVV_USER_INFO`, `SVV_MV_INFO`, `SYS_CONNECTION_LOG`,
  `SYS_DATASHARE_USAGE_PRODUCER`, `SYS_DATASHARE_USAGE_CONSUMER`, and `SYS_DATASHARE_CHANGE_LOG`.
- Adds support for querying VARBYTE columns in external tables for Parquet and ORC file types.

## Amazon Redshift patch 171

Cluster versions in this patch:

- 1.0.43931 – Released on November 16, 2022
- 1.0.43551 – Released on November 5, 2022
- 1.0.43331 – Released on September 29, 2022
- 1.0.43029 – Released on September 26, 2022

### New features and improvements in this patch

- CONNECT BY support: Adds support for the CONNECT BY SQL construct,
  letting you recursively query the hierarchical data in your data warehouse
  based on parent-child relationship within that data set.

## Amazon Redshift patch 170

Cluster versions in this patch:

- 1.0.43922 – Released on November 21, 2022
- 1.0.43573 – Released on November 7, 2022
- 1.0.41881 – Released on September 20, 2022
- 1.0.41465 – Released on September 7, 2022
- 1.0.40325 – Released on July 27, 2022

### New features and improvements in this patch

- ST_GeomfromGeoJSON: Constructs an Amazon Redshift spatial geometry object from VARCHAR in GeoJSON representation.

## Amazon Redshift patch 169

Cluster versions in this patch:

- 1.0.41050 – Released on September 7, 2022
- 1.0.40083 – Released on July 16, 2022
- 1.0.39734 – Released on July 7, 2022
- 1.0.39380 – Released on June 23, 2022
- 1.0.39251 – Released on June 15, 2022
- 1.0.39009 – Released on June 8, 2022

### New features and improvements in this patch

- Adds role as a parameter for the Alter Default Privileges command to support Role-based Access Control.
- Adds ACCEPTINVCHARS parameter to support replacing invalid UTF-8 characters when copying from Parquet and ORC files.
- Adds OBJECT(k,v) function to construct SUPER objects from key and value pairs.

## Amazon Redshift patch 168

Cluster versions in this patch:

- 1.0.38698 – Released on May 25, 2022
- 1.0.38551 – Released on May 20, 2022
- 1.0.38463 – Released on May 18, 2022
- 1.0.38361 – Released on May 13, 2022
- 1.0.38199 – Released on May 9, 2022
- 1.0.38112 – Released on May 6, 2022
- 1.0.37684 – Released on April 20, 2022

### New features and improvements in this patch

- Adds support for the Linear Learner model type in Amazon Redshift ML.
- Adds SNAPSHOT option for SQL transaction isolation level.
- Adds `farmhashFingerprint64` as new hashing algorithm for `VARBYTE` and `VARCHAR` data.
- Supports the AVG function in incremental refresh of materialized views.
- Supports correlated sub-queries on external tables in Redshift Spectrum.
- To improve the out-of-the-box query performance, Amazon Redshift automatically chooses a single column primary key for specific tables as a distribution key.
