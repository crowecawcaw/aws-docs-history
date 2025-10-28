# Metadata table limitations and

restrictions

Amazon S3 Metadata has the following limitations and restrictions:

- S3 Metadata is currently available only in certain Regions. For more information, see [S3 Metadata AWS Regions](#metadata-tables-regions "#metadata-tables-regions").
- S3 Metadata supports all storage classes supported by general purpose buckets. For the
  S3 Intelligent-Tiering storage class, the specific tier isn't shown in the metadata table.
- When you create a metadata table configuration, your metadata tables are stored in an AWS
  managed table bucket. You can't store your configuration in a customer-managed table bucket.
- S3 Metadata isn't supported for directory buckets, table buckets, or vector buckets. You can
  create metadata table configurations only for general purpose buckets. The journal table captures
  metadata only for change events (such as uploads, updates, and deletes) that happen after you have
  created your metadata table configuration.
- You can't control the expiration of journal table or inventory table snapshots. For each table,
  Amazon S3 stores a minimum of 1 snapshot for a maximum of 24 hours.

To help minimize your costs, you can configure journal table record expiration. By default,
journal table records don't expire, and journal table records must be retained for a minimum of 7
days. For more information, see [Expiring journal table records](metadata-tables-expire-journal-table-records.md "metadata-tables-expire-journal-table-records.md").

- You can create a metadata table configuration only for an entire general purpose
  bucket. You can't apply a metadata table configuration at the prefix level.
- You can't pause and resume updates to metadata tables. However, you can delete your associated
  metadata configuration for journal or live inventory tables. Deleting your configuration doesn't
  delete the associated journal or inventory table. To re-create your configuration, you must first
  delete the old journal or inventory table, and then Amazon S3 can create a new journal or inventory
  table. When you re-enable the inventory table, Amazon S3 creates a new inventory table, and you're
  charged again for backfilling the new inventory table.
- Metadata tables don't contain all the same metadata as is available through S3 Inventory or
  through the Amazon S3 REST API. For example, the following information isn't available in metadata
  tables:
  - S3 Lifecycle expiration eligibility or transition status
  - Object Lock retention period or governance mode
  - Object access control list (ACL) information
  - Replication
    status

- When you're using Amazon Athena or Amazon Redshift to query your metadata tables, you must surround your
  metadata table namespace names in quotation marks (`"`) or backticks (```),
  otherwise the query might not work. For examples, see [Example metadata table queries](metadata-tables-example-queries.md "metadata-tables-example-queries.md").
- When using Apache Spark on Amazon EMR or other third-party engines to query your
  metadata tables, we recommend that you use the Amazon S3 Tables Iceberg REST endpoint.
  Your query might not run successfully if you don't use this endpoint. For more information, see
  [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").

## S3 Metadata AWS Regions

S3 Metadata is currently available in the following AWS Regions:

| AWS Region name       | AWS Region code  |
| --------------------- | ---------------- |
| US East (N. Virginia) | `us-east-1`      |
| US East (Ohio)        | `us-east-2`      |
| US West (Oregon)      | `us-west-2`      |
| Asia Pacific (Tokyo)  | `ap-northeast-1` |
| Europe (Frankfurt)    | `eu-central-1`   |
| Europe (Ireland)      | `eu-west-1`      |
