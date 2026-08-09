For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Storage and billing FAQ for Amazon Timestream for InfluxDB 3

Questions about how Amazon Timestream for InfluxDB 3 stores data, manages backups, and handles billing. For pricing details, see [DB Cluster Billing for Amazon Timestream for InfluxDB 3](influxdb3.md#db-cluster-billing-for-amazon-timestream-for-influxdb-3 "influxdb3.md#db-cluster-billing-for-amazon-timestream-for-influxdb-3").

**How does storage work in InfluxDB 3?**

InfluxDB 3 decouples compute from storage. Data is persisted in Apache Parquet format on Amazon S3 object storage, providing virtually unlimited and cost-effective storage. The compute nodes handle query processing and data ingestion while Amazon S3 handles durable storage.

**How is Amazon Timestream for InfluxDB 3 billed?**

Billing is based on compute node hours (per instance type), Amazon S3 object storage volume (GB/month), and data transfer. I/O operations are bundled into compute pricing for the `db.influxIOIncluded` instance classes, providing predictable costs regardless of I/O patterns.

**Does Amazon Timestream for InfluxDB 3 support automatic backups?**

Yes. Amazon Timestream for InfluxDB 3 automatically backs up your database and keeps your database software up to date with the latest version. Because data is stored on Amazon S3, it benefits from built-in durability and redundancy.

**What are customer-managed backups?**

Customer-managed backups let you create, manage, and restore database backups on demand or on a schedule—without opening an AWS support ticket. The first backup takes a complete copy of your database, and subsequent backups are incremental (only changed data). You can also enable continuous backups for point-in-time restore. For details, see [Customer-managed backup and restore](influxdb3-customer-managed-backup-restore.md "influxdb3-customer-managed-backup-restore.md").

**What is the difference between service-managed backups and customer-managed backups?**

Service-managed backups are automatic, managed by AWS, and require a support ticket to restore. Customer-managed backups give you self-service control—you choose when to back up, how long to keep them, and can restore directly from the console or CLI.

**Can I restore a backup to the same cluster?**

Yes. You can restore using `REPLACE_EXISTING` mode, which replaces the data on your existing cluster with data from the backup. This is a destructive operation—existing data is deleted and the cluster is unavailable during the restore. You can also restore to a new cluster using `NEW_RESOURCE` mode (recommended).

**Does a backup include my most recently written data?**

Data written within the last 15 minutes might not be included in the backup. To recover the most recent data, use point-in-time restore with a timestamp at least 15 minutes in the past. Point-in-time restore requires a `CONTINUOUS` backup configuration.

**Are there additional charges for customer-managed backups?**

No feature charge. You pay only for the Amazon S3 storage consumed by your backups. Incremental backups reduce costs by storing only changed data.
