# S3 Tables table attributes

The Iceberg table a Channel creates has the following attributes (designed for governance and compliance):

- **Managed table** — The table is read-only from your perspective. You cannot modify the schema or table properties, or write to the table directly outside of the Channel.
- **No manual record deletion** — You cannot issue delete operations against individual records in the table. To remove old data, enable the record-expiration maintenance job, which automatically deletes records older than a specified retention period based on a timestamp column.
- **Access control** — Table buckets and tables are always private. Use IAM policies to control access.
- **S3 Tables quotas** — All S3 Tables service quotas apply to your service-managed tables. For more information, see [S3 Tables Regions and quotas](../../../AmazonS3/latest/userguide/s3-tables-regions-quotas.md "../../../AmazonS3/latest/userguide/s3-tables-regions-quotas.md").
