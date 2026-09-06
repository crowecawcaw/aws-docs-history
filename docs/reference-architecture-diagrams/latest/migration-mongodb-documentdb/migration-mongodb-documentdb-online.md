

# Migration from MongoDB to Amazon DocumentDB: Online
<a name="migration-mongodb-documentdb-online"></a>

This architecture shows how to migrate from MongoDB to Amazon DocumentDB using the online approach with [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) (AWS DMS). This approach delivers near-zero downtime with medium complexity.

## Migration from MongoDB to Amazon DocumentDB: Online Approach
<a name="diagram2"></a>

![Architecture diagram showing the online migration approach from MongoDB to Amazon DocumentDB using AWS DMS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/migration-mongodb-documentdb/images/migration-mongodb-documentdb-2.png)


The following steps describe the architecture:

1. When you use the online method to migrate to Amazon DocumentDB, your application continues to write to the source MongoDB database.

1. Create an Amazon EC2 instance in the same VPC as your Amazon DocumentDB cluster and install the mongo shell. Establish connectivity from the Amazon EC2 instance to your MongoDB source, then export the data indexes to the Amazon EC2 migration instance using the mongodump tool.

1. AWS DMS enables database migration using full data load and change data capture (CDC). The online migration approach uses AWS DMS to perform a full data copy and uses CDC to replicate delta changes to Amazon DocumentDB. To improve the performance of AWS DMS full data load migrations, use the auto segmentation or range segmentation option.

1. Use the Amazon EC2 instance created in step 2 to connect to the Amazon DocumentDB cluster to migrate indexes. Use the Amazon DocumentDB Index Tool to check the dumped indexes for compatibility, and pre-create the indexes on the target Amazon DocumentDB cluster.

1. When the data is in sync, switch your application's database connection string to use the new target Amazon DocumentDB cluster.