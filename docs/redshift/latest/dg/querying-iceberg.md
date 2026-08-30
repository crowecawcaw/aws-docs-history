Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Using Apache Iceberg tables with Amazon Redshift

###### Note

To achieve the best performance when using Apache Iceberg tables with Amazon Redshift, you must
generate column statistics for the tables using AWS Glue. For more information, see
[Generating column statistics for Iceberg tables](../../../glue/latest/dg/iceberg-generate-column-stats.md "../../../glue/latest/dg/iceberg-generate-column-stats.md")
in the _AWS Glue Developer Guide_.

This topic describes how to use tables in Apache Iceberg format with Amazon Redshift. Apache
Iceberg is a high-performance open-source table format for data lakes. For more information, see [Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/") in the Apache Iceberg documentation.

You can query Apache Iceberg tables cataloged in the AWS Glue Data Catalog with Amazon Redshift. RG instance types and Redshift Serverless use their own compute to process data lake queries, while RA3 instance types use Redshift Spectrum. For more information, see [Querying your Data Lake](../gsg/data-lake.md "../gsg/data-lake.md").

Amazon Redshift provides transactional consistency for querying Apache Iceberg tables.
You can manipulate the data in your tables using ACID (atomicity, consistency, isolation, durability) compliant services such as Amazon Athena and Amazon EMR while running queries using Amazon Redshift.
Amazon Redshift can use the table statistics stored in Apache Iceberg metadata to optimize query plans and reduce file scans during query processing.
With Amazon Redshift SQL, you can join Redshift tables with data lake tables.

To get started using Iceberg tables with Amazon Redshift:

1. Create an Apache Iceberg table on an AWS Glue Data Catalog database using a compatible service such as Amazon Athena or Amazon EMR.
   To create an Iceberg table using Athena, see
   [Using Apache Iceberg tables](../../../athena/latest/ug/querying-iceberg.md "../../../athena/latest/ug/querying-iceberg.md") in the _Amazon Athena User Guide_.
2. Create an Amazon Redshift cluster or Redshift Serverless workgroup with an associated IAM role that allows access to your data lake. For information on how to create clusters or workgroups, see
   [Get started with Amazon Redshift provisioned data warehouses](../gsg/new-user.md "../gsg/new-user.md")
   and [Get started with Redshift Serverless data warehouses](../gsg/new-user-serverless.md "../gsg/new-user-serverless.md")
   in the _Amazon Redshift Getting Started Guide_.
3. Connect to your cluster or workgroup using query editor v2 or a third-party SQL client. For information about how to connect using query editor v2, see
   [Connecting to an Amazon Redshift data warehouse using SQL client tools](../mgmt/connecting-to-cluster.md "../mgmt/connecting-to-cluster.md")
   in the _Amazon Redshift Management Guide_.
4. Create an external schema in your Amazon Redshift database for a specific Data Catalog database that includes your Iceberg tables. For information about creating an external schema, see
   [External schemas in Amazon Redshift Spectrum](c-spectrum-external-schemas.md "c-spectrum-external-schemas.md").
5. Run SQL queries to access the Iceberg tables in the external schema you created.

## Considerations when using Apache Iceberg tables with Amazon Redshift

Consider the following when using Amazon Redshift with Iceberg tables:

- Iceberg version support – Amazon Redshift supports
  running queries against the following versions of Iceberg tables:

  - Version 1 defines how large analytic tables are managed using
    immutable data files.
  - Version 2 adds the ability to support row-level updates and deletes
    while keeping the existing data files unchanged, and handling table data
    changes using delete files.
  - Version 3 introduces default column values, row lineage
    tracking, and deletion vectors. Default values let you
    define initial values for columns that are applied when
    values are not explicitly provided. Row lineage provides
    pseudo-columns that track row identity and modification
    history. Deletion vectors offer a more compact
    representation of row-level deletes, enabling faster reads
    and writes compared to Iceberg v2 delete files. For more
    information, see [Apache Iceberg v3 features in Amazon Redshift](iceberg-v3-features.md "iceberg-v3-features.md").
    For the differences between version 1, version 2, and version 3
    tables, see [Format version changes](https://iceberg.apache.org/spec/#appendix-e-format-version-changes "https://iceberg.apache.org/spec/#appendix-e-format-version-changes") in the Apache Iceberg documentation.

For more information about the Iceberg v3 features that Amazon Redshift
supports, and current limitations, see [Apache Iceberg v3 features in Amazon Redshift](iceberg-v3-features.md "iceberg-v3-features.md").

- Adding partitions – You don't need to
  manually add partitions for your Apache Iceberg tables. New partitions in Apache
  Iceberg tables are automatically detected by Amazon Redshift and no manual operation is
  needed to update partitions in the table definition. Any changes in partition
  specification are also automatically applied to your queries without any user
  intervention.
- Ingesting Iceberg data into Amazon Redshift – You
  can use INSERT INTO or CREATE TABLE AS commands to import data from your Iceberg
  table into a local Amazon Redshift table. You currently cannot use the COPY command to
  ingest the contents of an Apache Iceberg table into a local Amazon Redshift table.
- Materialized views – You can create
  materialized views on Apache Iceberg tables like any other external table in
  Amazon Redshift. The same considerations for other data lake table formats apply to Apache
  Iceberg tables. Automatic query rewriting and automatic
  materialized views on data lake tables are currently not supported.
- AWS Lake Formation fine-grained access control –
  Amazon Redshift supports AWS Lake Formation fine-grained access control on Apache Iceberg
  tables.
- User-defined data handling parameters –
  Amazon Redshift supports user-defined data handling parameters on Apache Iceberg tables.
  You use user-defined data handling parameters on existing files to tailor the
  data being queried in external tables to avoid scan errors. These parameters
  provide capabilities to handle mismatches between the table schema and the
  actual data on files. You can use user-defined data handling parameters on
  Apache Iceberg tables as well.
- Time travel queries – Time travel
  queries are currently not supported with Apache Iceberg tables.
- Pricing – When you access Iceberg tables from an RG cluster or a Redshift Serverless workgroup, data lake queries run on the cluster's or workgroup's own compute resources, so there is no separate charge for data lake queries. When you access Iceberg tables from a DC2 or RA3 cluster, you are charged Redshift Spectrum pricing. For information about pricing, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").
- Metadata caching – Metadata caching
  assumes metadata files are immutable based on the [Iceberg
  specification](https://iceberg.apache.org/spec/#file-system-operations "https://iceberg.apache.org/spec/#file-system-operations"). Metadata file immutability is a requirement for data
  integrity in Amazon Redshift.
- Federated identity – Federated identity is not supported when writing to Apache Iceberg tables. This includes using the SESSION keyword for the IAM\_ROLE parameter when creating external schemas. For more information about IAM\_ROLE parameters, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").
