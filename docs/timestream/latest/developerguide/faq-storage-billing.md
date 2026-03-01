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
