# Limitations of fine-grained permission mode

Permission mode is a configuration available to Spark compute resources such as Glue ETL or
EMR Serverless. It configures Spark to access different types of data based on the permissions
configured for that data. There are two configuration options for permission mode:

- Compatibility mode. This is a configuration for data managed using full-table access,
  meaning the compute engine can access all rows and columns in the data.
  Choosing this option enables your compute to work with data assets from AWS and from external systems.
- Fine-grained mode. This is a configuration for data managed using fine-grained access controls,
  meaning the compute engine can only access specific rows and columns from the full dataset.
  Choosing this option enables your Glue ETL
  to work with data asset subscriptions from Amazon SageMaker Catalog.
  Consider the following considerations and limitations when you use fine-grained mode.

- Fine-grained mode supports fine-grained access control via AWS Lake Formation
  only for Apache Hive and Apache Iceberg tables. Apache Hive formats include Parquet, ORC, and CSV.
- When fine-grained mode is enabled, a minimum of four workers are required because it requires
  one system driver, system executors, one user driver, and optionally user executors (required
  if you use UDFs or spark.createDataFrame).
- Fine-grained mode supports cross-account table queries shared through resource links.
  The resource link needs to be named identically to the source account's resource.
- The following components aren't supported:
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Write with AWS Lake Formation granted permissions
  - Access control for nested columns
  - Access data stored on Amazon Redshift Managed Storage (RMS), including through lakehouse architecture.

- Fine-grained mode blocks functionalities that might undermine the complete isolation of the system driver,
  including the following:
  - UDTs, HiveUDFs, and any user-defined function that involves custom classes
  - Custom data sources
  - Supply of additional JARs for Spark extension, connector, or metastore
  - `ANALYZE TABLE` command

- To enforce access controls, `EXPLAIN PLAN` and DDL operations such as `DESCRIBE TABLE`
  don't expose restricted information.
- Fine-Grained mode restricts access to system driver Spark logs on Lake Formation-enabled applications.
  Since the system driver runs with more access, events and logs that the system driver generates
  can include sensitive information. To prevent unauthorized users or code from accessing this sensitive data,
  access to system driver logs is disabled. For troubleshooting, contact AWS support.
- The following are considerations and limitations when using Apache Iceberg:
  - You can only use Apache Iceberg with session catalog and not arbitrarily named catalogs.
  - Iceberg tables that are registered in AWS Lake Formation only support
    the metadata tables `history`, `metadata_log_entries`, `snapshots`,
    `files`, `manifests`, and `refs`.
    AWS Glue hides the columns that might have sensitive data, such as `partitions`, `path`,
    and `summaries`. This limitation doesn't apply to Iceberg tables
    that aren't registered in AWS Lake Formation.
  - Tables that you don't register in AWS Lake Formation support all Iceberg stored procedures except for
    the `register_table` and `migrate` procedures, which aren't supported for any tables.
