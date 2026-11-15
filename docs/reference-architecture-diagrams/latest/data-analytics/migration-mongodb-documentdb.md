

# Migration from MongoDB to Amazon DocumentDB
<a name="migration-mongodb-documentdb"></a>

Publication date: **March 25, 2022 ([Diagram history](diagram-history.md))**

This architecture shows how to migrate from MongoDB to [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/devguide/) using the offline approach with MongoDB utilities. This is the simplest approach, but it can result in more downtime during the migration.

## Offline approach
<a name="migration-mongodb-documentdb-offline"></a>

![Architecture diagram showing the offline migration approach from MongoDB to Amazon DocumentDB using MongoDB utilities.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/migration-mongodb-documentdb-1.png)


The following steps describe the architecture:

1. Before migration to the Amazon DocumentDB cluster, ensure that the MongoDB source and application drivers use version 3.6 or higher. Stop application writes to the source MongoDB to ensure data consistency.

1. Establish connectivity from the Amazon EC2 instance to your MongoDB source, then export the data and indexes to the Amazon EC2 migration instance using the mongodump tool. To reduce the impact on the source deployment, use the MongoDB read preference option to force the dump to connect to a secondary replica set member.

1. Use the Amazon DocumentDB Index Tool to check the dumped indexes for compatibility and to pre-create the indexes on the target Amazon DocumentDB cluster. This improves overall restore time.

1. Restore exported data to your target Amazon DocumentDB cluster using the mongorestore tool. To parallelize imports, use the mongorestore `numInsertionWorkersPerCollection` option.

1. After data restore is complete, switch your application's database connection string to use your new target Amazon DocumentDB cluster.

## Online approach
<a name="migration-mongodb-documentdb-online"></a>

This architecture shows how to migrate from MongoDB to Amazon DocumentDB using the online approach with [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) (AWS DMS). This approach delivers near-zero downtime with medium complexity.

![Architecture diagram showing the online migration approach from MongoDB to Amazon DocumentDB using AWS DMS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/migration-mongodb-documentdb-2.png)


The following steps describe the architecture:

1. When you use the online method to migrate to Amazon DocumentDB, your application continues to write to the source MongoDB database.

1. Create an Amazon EC2 instance in the same VPC as your Amazon DocumentDB cluster and install the mongo shell. Establish connectivity from the Amazon EC2 instance to your MongoDB source, then export the data indexes to the Amazon EC2 migration instance using the mongodump tool.

1. AWS DMS enables database migration using full data load and change data capture (CDC). The online migration approach uses AWS DMS to perform a full data copy and uses CDC to replicate delta changes to Amazon DocumentDB. To improve the performance of AWS DMS full data load migrations, use the auto segmentation or range segmentation option.

1. Use the Amazon EC2 instance created in step 2 to connect to the Amazon DocumentDB cluster to migrate indexes. Use the Amazon DocumentDB Index Tool to check the dumped indexes for compatibility, and pre-create the indexes on the target Amazon DocumentDB cluster.

1. When the data is in sync, switch your application's database connection string to use the new target Amazon DocumentDB cluster.

## Hybrid approach
<a name="migration-mongodb-documentdb-hybrid"></a>

This architecture shows how to migrate from MongoDB to Amazon DocumentDB using the hybrid approach with MongoDB utilities and AWS DMS. This approach delivers near-zero downtime, and it is the suggested option for source datasets greater than 1 TB.

![Architecture diagram showing the hybrid approach from MongoDB to Amazon DocumentDB using MongoDB utilities and AWS DMS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/migration-mongodb-documentdb-3.png)


The following steps describe the architecture:

1. In the hybrid method to migrate to Amazon DocumentDB, your application continues to write to the source MongoDB database.

1. Create an Amazon EC2 instance in the same VPC as your Amazon DocumentDB cluster and install the mongo shell. Establish connectivity from the Amazon EC2 instance to your MongoDB source. Export the data indexes to the Amazon EC2 migration instance using the Amazon DocumentDB Index Tool.

1. Export the data from your MongoDB replica set to the Amazon EC2 migration instance using the mongodump tool. To reduce the impact of the mongodump on the source, set the `readPreference` option to `secondary` to force the dump to connect to a secondary replica set member.

1. Restore the indexes that you exported in step 2 to your target Amazon DocumentDB cluster by using the Amazon DocumentDB Index Tool.

1. To restore the data that you dumped in your target cluster in step 3, use the mongorestore utility.

1. AWS DMS enables database migration using full data load and CDC. The hybrid migration approach uses CDC to replicate changes to Amazon DocumentDB.

1. When the data is in sync, change your application's database connection string to use Amazon DocumentDB cluster.

## Further reading
<a name="migration-mongodb-documentdb-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)