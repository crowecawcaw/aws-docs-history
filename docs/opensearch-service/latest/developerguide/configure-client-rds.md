# Using an OpenSearch Ingestion pipeline with Amazon RDS

You can use an OpenSearch Ingestion pipeline with Amazon RDS to export existing data and stream
changes (such as create, update, and delete) to Amazon OpenSearch Service domains and collections. The
OpenSearch Ingestion pipeline incorporates change data capture (CDC) infrastructure to provide a
high-scale, low-latency way to continuously stream data from Amazon RDS. RDS for MySQL and
RDS for PostgreSQL are supported.

There are two ways that you can use Amazon RDS as a source to process data—with or without a
full initial snapshot. A full initial snapshot is a snapshot of specified tables and this
snapshot is exported to Amazon S3. From there, an OpenSearch Ingestion pipeline sends it to one index
in a domain, or partitions it to multiple indexes in a domain. To keep the data in Amazon RDS and
OpenSearch consistent, the pipeline syncs all of the create, update, and delete events in the
tables in Amazon RDS instances with the documents saved in the OpenSearch index or indexes.

When you use a full initial snapshot, your OpenSearch Ingestion pipeline first ingests the
snapshot and then starts reading data from Amazon RDS change streams. It eventually catches up
and maintains near real-time data consistency between Amazon RDS and OpenSearch.

You can also use the OpenSearch Ingestion integration with Amazon RDS to track change data capture
and ingest all updates in Aurora to OpenSearch. Choose this option if you already have a full
snapshot from some other mechanism, or if you just want to capture all changes to the data
in an Amazon RDS instance.

When you choose this option you need to [configure Amazon RDS
for MySQL binary logging](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.md "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.md") or [set up logical replication for Amazon RDS for PostgresSQL DB instance](../../../AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.md "../../../AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.md").

###### Topics

- [RDS for MySQL](rds-mysql.md "rds-mysql.md")
- [RDS for PostgreSQL](rds-PostgreSQL.md "rds-PostgreSQL.md")
