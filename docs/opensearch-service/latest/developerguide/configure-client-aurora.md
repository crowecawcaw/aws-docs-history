# Using an OpenSearch Ingestion pipeline with

Amazon Aurora

You can use an OpenSearch Ingestion pipeline with Amazon Aurora to export existing data and stream changes (such as create,
update, and delete) to Amazon OpenSearch Service domains and collections. The OpenSearch Ingestion pipeline
incorporates change data capture (CDC) infrastructure to provide a high-scale, low-latency
way to continuously stream data from Amazon Aurora. Aurora MySQL and Aurora PostgreSQL are
supported.

There are two ways that you can use Amazon Aurora as a source to process data—with or without
a full initial snapshot. A full initial snapshot is a snapshot of specified tables and this
snapshot is exported to Amazon S3. From there, an OpenSearch Ingestion pipeline sends it to one index
in a domain, or partitions it to multiple indexes in a domain. To keep the data in Amazon Aurora
and OpenSearch consistent, the pipeline syncs all of the create, update, and delete events in
the tables in Amazon Aurora clusters with the documents saved in the OpenSearch index or
indexes.

When you use a full initial snapshot, your OpenSearch Ingestion pipeline first ingests the
snapshot and then starts reading data from Amazon Aurora change streams. It eventually catches
up and maintains near real-time data consistency between Amazon Aurora and OpenSearch.

You can also use the OpenSearch Ingestion integration with Amazon Aurora to track change data
capture and ingest all updates in Aurora to OpenSearch. Choose this option if you already have
a full snapshot from some other mechanism, or if you just want to capture all changes to the
data in Amazon Aurora cluster.

When you choose this option you need to [configure
binary logging for Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.md") or [set up logical replication for Aurora PostgreSQL on the cluster](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.md").

###### Topics

- [Aurora MySQL](aurora-mysql.md "aurora-mysql.md")
- [Aurora PostgreSQL](aurora-PostgreSQL.md "aurora-PostgreSQL.md")
