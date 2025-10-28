For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Migrating data from self-managed

InfluxDB to Timestream for InfluxDB

The [Influx migration script](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/influx-migration "https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/influx-migration") is a Python script that migrates data between InfluxDB OSS
instances, whether those instances are managed by AWS or not.

InfluxDB is a time series database. InfluxDB contains _points_, which
contain a number of key-value pairs and a timestamp. When points are grouped by key-value pairs,
they form a series. A series is grouped by a string identifier called a
_measurement_. InfluxDB is often used for operations monitoring, IOT data,
and analytics. A _bucket_ is a kind of container within InfluxDB to store
data. AWS-managed InfluxDB is InfluxDB within the AWS ecosystem. InfluxDB provides the
InfluxDB v2 API for accessing data and making changes to the database. The InfluxDB v2 API is
what the Influx migration script uses to migrate data.

- The Influx migration script can migrate buckets and their metadata, migrate all buckets from all organizations, or do a full migration, which replaces all data on the destination instance.
- The script backups data from the source instance locally, on whatever system executes the script, then restores
  the data to the destination instance. The data is kept in code>influxdb-backup-<timestamp></timestamp> directories, one for each migration.
- The script provides a number of options and configurations including mounting S3 buckets to limit local storage usage during migration and choosing which organizations to use during migration.

###### Topics

- [Preparation](timestream-for-influx-getting-started-migrating-data-prepare.md "timestream-for-influx-getting-started-migrating-data-prepare.md")
- [How to use scripts](timestream-for-influx-getting-started-migrating-data-using-script.md "timestream-for-influx-getting-started-migrating-data-using-script.md")
- [Migration Overview](timestream-for-influx-getting-started-migrating-data-overview.md "timestream-for-influx-getting-started-migrating-data-overview.md")
