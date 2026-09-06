

# Migration from MongoDB to Amazon DocumentDB: Hybrid
<a name="migration-mongodb-documentdb-hybrid"></a>

This architecture shows how to migrate from MongoDB to Amazon DocumentDB using the hybrid approach with MongoDB utilities and AWS DMS. This approach delivers near-zero downtime, and it is the suggested option for source datasets greater than one terabyte (TB).

## Migration from MongoDB to Amazon DocumentDB: Hybrid Approach
<a name="diagram3"></a>

![Architecture diagram showing the hybrid migration approach from MongoDB to Amazon DocumentDB using MongoDB utilities and AWS DMS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/migration-mongodb-documentdb/images/migration-mongodb-documentdb-3.png)


The following steps describe the architecture:

1. In the hybrid method to migrate to Amazon DocumentDB, your application continues to write to the source MongoDB database.

1. Create an Amazon EC2 instance in the same VPC as your Amazon DocumentDB cluster and install the mongo shell. Establish connectivity from the Amazon EC2 instance to your MongoDB source. Export the data indexes to the Amazon EC2 migration instance using the Amazon DocumentDB Index Tool.

1. Export the data from your MongoDB replica set to the Amazon EC2 migration instance using the mongodump tool. To reduce the impact of the mongodump on the source, set the `readPreference` option to `secondary` to force the dump to connect to a secondary replica set member.

1. Use the Amazon DocumentDB Index Tool to restore the indexes that you exported (step 2) in your target Amazon DocumentDB cluster.

1. To restore the data that you dumped in your target cluster in step 3, use the mongorestore utility.

1. AWS DMS enables database migration using full data load and CDC. The hybrid migration approach uses CDC to replicate changes to Amazon DocumentDB.

1. When the data is in sync, change your application's database connection string to use Amazon DocumentDB cluster.