# Aurora zero-ETL integrations

An Aurora
zero-ETL integration with Amazon Redshift and Amazon SageMaker AI enables near real-time
analytics and machine learning (ML) using data from Aurora. It's a fully managed solution
for making transactional data available in your analytics destination after it is written to
an Aurora DB cluster. _Extract, transform,_ and _load_ (ETL) is the process of combining data from multiple
sources into a large, central data warehouse.

A zero-ETL integration makes the data in your Aurora DB cluster available in Amazon Redshift or an
Amazon SageMaker AI lakehouse in near real-time. Once that data is in the
target data warehouse or data lake, you can power your analytics, ML, and AI workloads using
the built-in capabilities, such as machine learning, materialized views, data sharing,
federated access to multiple data stores and data lakes, and integrations with Amazon SageMaker AI,
Quick Suite, and other AWS services.

To create a zero-ETL integration, you specify an Aurora DB cluster as the
_source_, and a supported data warehouse or lakehouse as the
_target_. The integration replicates data from the source database into
the target data warehouse or lakehouse.

The following diagram illustrates this functionality for zero-ETL integration with Amazon Redshift:

![A zero-ETL integration](images/zero-etl-integrations.png)
The following diagram illustrates this functionality for zero-ETL integration with an
Amazon SageMaker AI lakehouse:

![A zero-ETL integration with an Amazon SageMaker AI lakehouse](images/zero-etl-aurora-lakehouse.png)
The integration monitors the health of the data pipeline and recovers from issues when
possible. You can create integrations from multiple Aurora DB clusters into a single target data
warehouse or lakehouse enabling you to derive insights across multiple applications.

For information about pricing for zero-ETL integrations, see [Amazon Aurora
pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/") and [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

###### Topics

- [Benefits](#zero-etl.benefits "#zero-etl.benefits")
- [Key concepts](#zero-etl.concepts "#zero-etl.concepts")
- [Limitations](#zero-etl.reqs-lims "#zero-etl.reqs-lims")
- [Quotas](#zero-etl.quotas "#zero-etl.quotas")
- [Supported Regions](#zero-etl.regions "#zero-etl.regions")
- [Getting started with Aurora zero-ETL integrations](zero-etl.md "zero-etl.md")
- [Creating Aurora zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md")
- [Creating Aurora zero-ETL integrations with an Amazon SageMaker lakehouse](zero-etl.md "zero-etl.md")
- [Data filtering for Aurora zero-ETL integrations](zero-etl.md "zero-etl.md")
- [Adding data to a source Aurora DB cluster and querying it](zero-etl.md "zero-etl.md")
- [Viewing and monitoring Aurora
  zero-ETL integrations](zero-etl.md "zero-etl.md")
- [Modifying Aurora zero-ETL integrations](zero-etl.md "zero-etl.md")
- [Deleting Aurora zero-ETL integrations](zero-etl.md "zero-etl.md")
- [Troubleshooting Aurora zero-ETL integrations](zero-etl.md "zero-etl.md")

## Benefits

Aurora
zero-ETL integrations have the following benefits:

- Help you derive holistic insights from multiple data sources.
- Eliminate the need to build and maintain complex data pipelines that perform
  extract, transform, and load (ETL) operations. Zero-ETL integrations remove the
  challenges that come with building and managing pipelines by provisioning and
  managing them for you.
- Reduce operational burden and cost, and let you focus on improving your
  applications.
- Let you leverage the target destination's analytics and ML capabilities to
  derive insights from transactional and other data, to respond effectively to
  critical, time-sensitive events.

## Key concepts

As you get started with zero-ETL integrations, consider the following concepts:

**Integration**

A fully managed data pipeline that automatically replicates transactional
data and schemas from an Aurora DB cluster to a data
warehouse or catalog.

**Source DB cluster**

The Aurora DB cluster where data is replicated from.
You can specify a DB cluster that
uses provisioned DB instances or Aurora Serverless v2 DB instances as the
source.

**Target**

The data warehouse or lakehouse where the data is replicated to. There are
two types of data warehouse: a [provisioned
cluster](../../../redshift/latest/mgmt/working-with-clusters.md "../../../redshift/latest/mgmt/working-with-clusters.md") data warehouse and a [serverless](../../../redshift/latest/mgmt/serverless-workgroup-namespace.md "../../../redshift/latest/mgmt/serverless-workgroup-namespace.md") data warehouse. A provisioned cluster data warehouse
is a collection of computing resources called nodes, which are organized
into a group called a _cluster_. A serverless data
warehouse is comprised of a workgroup that stores compute resources, and a
namespace that houses the database objects and users. Both data warehouses
run an analytics engine and contain one or more databases.

A target lakehouse consists of catalogs, databases, tables, and views. For
more information about lakehouse architecture, see [SageMaker Lakehouse components](../../../sagemaker-unified-studio/latest/userguide/lakehouse-components.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-components.md") in the _Amazon SageMaker AI Unified Studio User
Guide_.

Multiple source DB clusters can write to the same target.

For more information, see [Data warehouse
system architecture](../../../redshift/latest/dg/c_high_level_system_architecture.md "../../../redshift/latest/dg/c_high_level_system_architecture.md") in the _Amazon Redshift Developer
Guide_.

## Limitations

The following limitations apply to Aurora zero-ETL integrations.

###### Topics

- [General limitations](#zero-etl.reqs-lims-general "#zero-etl.reqs-lims-general")
- [Aurora MySQL
  limitations](#zero-etl.reqs-lims-mysql "#zero-etl.reqs-lims-mysql")
- [Aurora PostgreSQL limitations](#zero-etl.reqs-lims-apg "#zero-etl.reqs-lims-apg")
- [Amazon Redshift limitations](#zero-etl.reqs-lims-redshift "#zero-etl.reqs-lims-redshift")
- [Amazon SageMaker AI lakehouse
  limitations](#zero-etl.reqs-lims-sagemaker- "#zero-etl.reqs-lims-sagemaker-")

### General limitations

- The source DB cluster must be in the same
  Region as the target.
- You can't rename a DB cluster or any of its instances if it has
  existing integrations.
- You can't create multiple integrations between the same source and target
  databases.
- You can't delete a DB cluster that has existing integrations. You must
  delete all associated integrations first.
- If you stop the source DB cluster, the last
  few transactions might not be replicated to the target until you resume the
  cluster.
- If your cluster is the source of a blue/green
  deployment, the blue and green environments can't have existing
  zero-ETL integrations during switchover. You must delete the integration first and
  switch over, then recreate it.
- A DB cluster must contain at least one DB instance in order to be the source of an
  integration.
- You can't create an integration for a source DB cluster that is a cross-account
  clone, such as those shared using AWS Resource Access Manager (AWS RAM).
- If your source cluster is the primary DB cluster in an Aurora global database
  and it fails over to one of its secondary clusters, the integration becomes
  inactive. You must delete and recreate the integration.
- You can't create an integration for a source database that has another
  integration being actively created.
- When you initially create an integration, or when a table is being
  resynchronized, data seeding from the source to the target can take 20-25
  minutes or more depending on the size of the source database. This delay can
  lead to increased replica lag.
- Some data types aren't supported. For more information, see [Data type differences between Aurora and
  Amazon Redshift databases](zero-etl.md#zero-etl.data-type-mapping "zero-etl.md#zero-etl.data-type-mapping").
- System tables, temporary tables, and views aren't replicated to target
  warehouses.
- Performing DDL commands (for example `ALTER TABLE`) on a source
  table can trigger a table resynchronization, making the table unavailable
  for querying while it's resynchronizing. For more information, see [One or more of my Amazon Redshift tables
  requires a resync](zero-etl.md#zero-etl.troubleshooting.resync "zero-etl.md#zero-etl.troubleshooting.resync").

### Aurora MySQL

limitations

- Your source DB cluster must be running a supported version of Aurora MySQL. For a
  list of supported versions, see [Supported
  Regions and Aurora DB engines for zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").
- Zero-ETL integrations rely on MySQL binary logging (binlog) to capture ongoing
  data changes. Don't use binlog-based data filtering, as it can cause data
  inconsistencies between the source and target databases.
- Zero-ETL integrations are supported only for databases configured to use the
  InnoDB storage engine.
- Foreign key references with predefined table updates aren't supported.
  Specifically, `ON DELETE` and `ON UPDATE` rules aren't
  supported with `CASCADE`, `SET NULL`, and `SET
DEFAULT` actions. Attempting to create or update a table with such
  references to another table will put the table into a failed state.
- [XA
  transactions](https://dev.mysql.com/doc/refman/8.0/en/xa.html "https://dev.mysql.com/doc/refman/8.0/en/xa.html") performed on the source DB cluster cause the integration
  to enter a state of `Syncing`.

### Aurora PostgreSQL limitations

- Your source DB cluster must be running a supported version of Aurora PostgreSQL.
  For a list of supported versions, see [Supported
  Regions and Aurora DB engines for zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").
- If you select an Aurora PostgreSQL source DB cluster, you must specify at least one
  data filter pattern. At minimum, the pattern must include a single database
  (``database-name`._._`) for
  replication to the target warehouse. For more information, see [Data filtering for Aurora zero-ETL integrations](zero-etl.md "zero-etl.md").
- All databases created within the source Aurora PostgreSQL DB cluster must use UTF-8
  encoding.
- When using declarative partitioning, the table partitions will be replicated to Amazon Redshift.
  However, the partitioned table itself isn't replicated to Amazon Redshift.
- [Two-phase transactions](https://www.postgresql.org/docs/current/two-phase.html "https://www.postgresql.org/docs/current/two-phase.html") aren't supported.
- If you delete all DB instances from a DB cluster that is the source of an integration
  and then re-add a DB instance, replication breaks between the source and the
  target clusters.
- The source DB cluster can't use Aurora Limitless Database.
- Primary keys are required on all tables present in the data filter.
  Any tables without a primary key will be put into the failed state.

### Amazon Redshift limitations

For a list of Amazon Redshift limitations related to zero-ETL integrations, see [Considerations when using zero-ETL integrations with Amazon Redshift](../../../redshift/latest/mgmt/zero-etl.md "../../../redshift/latest/mgmt/zero-etl.md") in
the _Amazon Redshift Management Guide_.

### Amazon SageMaker AI lakehouse

limitations

Following is a limitation for Amazon SageMaker AI lakehouse
zero-ETL integrations.

- Catalog names are limited to 19 characters in length.

## Quotas

Your account has the following quotas related to Aurora zero-ETL integrations. Each quota
is per-Region unless otherwise specified.

| Name                            | Default | Description                                                                                |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| Integrations                    | 100     | The total number of integrations within an AWS account.                                    |
| Integrations per target         | 50      | The number of integrations sending data to a single target data<br>warehouse or lakehouse. |
| Integrations per source cluster | 5       | The number of integrations sending data from a single source DB cluster.                   |

In addition, the target warehouse places certain limits on the number of tables
allowed in each DB instance or cluster node. For more information about Amazon Redshift quotas and
limits, see [Quotas and limits in
Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-limits.md "../../../redshift/latest/mgmt/amazon-redshift-limits.md") in the _Amazon Redshift Management
Guide_.

## Supported Regions

Aurora
zero-ETL integrations are available in a subset of AWS Regions. For a list of supported
Regions, see [Supported
Regions and Aurora DB engines for zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").
