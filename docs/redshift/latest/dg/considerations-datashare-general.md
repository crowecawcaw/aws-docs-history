Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# General considerations for data

sharing in Amazon Redshift

The following are general considerations when working with datashares in
Amazon Redshift:

- _Default database_ – When you read data from a
  datashare, you remain connected to your local cluster database. For more
  information about setting up and reading from a database created from a datashare,
  see [Querying datashare objects](../mgmt/query-editor-v2-datashare-using.md#query-editor-v2-datashare-consumer "../mgmt/query-editor-v2-datashare-using.md#query-editor-v2-datashare-consumer") and [Materialized views on external data
  lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md "materialized-view-external-table.md").
- _Connections_ – You must be connected directly to a
  datashare database or run the USE command to write to datashares. You can also use
  three-part notation. The USE command is not supported on external tables.
- _Performance_ – The performance of the queries on
  shared data depends on the compute capacity of the consumer clusters.
- _Data transfer charges_ – Cross-Region data sharing
  includes additional cross-Region data-transfer charges.
  - These data-transfer charges don't apply within the same Region, only
    across Regions. For more information, see [Managing cost control for cross-Region data
    sharing](cross-region-billing.md "cross-region-billing.md").
  - The consumer is charged for all compute and cross-region data transfer
    fees required to query the producer's data. The producer is charged for
    the underlying storage of data in their provisioned cluster or serverless
    namespace.

- _Data sharing within and between clusters_ – You only
  need datashares when you are sharing data between different Amazon Redshift provisioned
  clusters or serverless workgroups. Within the same cluster, you can query another
  database using simple three-part notation `database.schema.table` as
  long as you have the required permissions on the objects in the other
  database.
- _Metadata Discovery_ – When you're a consumer
  connected directly to a datashare database through the Redshift JDBC, ODBC, or
  Python drivers, you can view catalog data in the following ways:
  - SQL [SHOW](r_SHOW.md "r_SHOW.md") commands.
  - Querying information_schema tables and views.
  - Querying [SVV metadata
    views](svv_views.md "svv_views.md").

- _Permissions visibility_ – Consumers can see the
  permissions granted to the datashares through the SHOW GRANTS SQL command.
- _Cluster encryption management for data sharing_ – To
  share data across an AWS account, both the producer and consumer cluster must be
  encrypted.
  - If both the producer and consumer clusters and serverless namespaces are
    in the same account, they must have the same encryption type (either both
    unencrypted, or both encrypted). In every other case, including Lake Formation managed
    datashares, both the consumer and producer must be encrypted. This is for
    security purposes. However, they don't need to share the same
    encryption key.
  - To protect data in transit, all data is encrypted in transit through the
    encryption schema of the producer cluster. The consumer cluster adopts this
    encryption schema when data is loaded. The consumer cluster then operates as
    a normal encrypted cluster. Communications between the producer and consumer
    are also encrypted using a shared key schema. For more information about
    encryption in transit, [Encryption in
    transit](../mgmt/security-encryption-in-transit.md "../mgmt/security-encryption-in-transit.md").
