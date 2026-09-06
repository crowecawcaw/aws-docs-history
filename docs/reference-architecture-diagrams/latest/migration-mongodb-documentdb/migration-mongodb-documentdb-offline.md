

# Migration from MongoDB to Amazon DocumentDB: Offline
<a name="migration-mongodb-documentdb-offline"></a>

Publication date: **March 25, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to migrate from MongoDB to [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html) using the offline approach with MongoDB utilities. This is the simplest approach, but it can result in more downtime during the migration.

## Migration from MongoDB to Amazon DocumentDB: Offline Approach
<a name="diagram1"></a>

![Architecture diagram showing the offline migration approach from MongoDB to Amazon DocumentDB using MongoDB utilities.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/migration-mongodb-documentdb/images/migration-mongodb-documentdb-1.png)


The following steps describe the architecture:

1. Before migration to the Amazon DocumentDB cluster, ensure that the MongoDB source and application drivers use version 3.6 or higher. Stop application writes to the source MongoDB to ensure data consistency.

1. Establish connectivity from the Amazon EC2 instance to your MongoDB source, then export the data and indexes to the Amazon EC2 migration instance using the mongodump tool. To reduce the impact on the source deployment, use the MongoDB read preference option to force the dump to connect to a secondary replica set member.

1. Use the Amazon DocumentDB Index Tool to check the dumped indexes for compatibility and to pre-create the indexes on the target Amazon DocumentDB cluster. This improves overall restore time.

1. Restore exported data to your target Amazon DocumentDB cluster using the mongorestore tool. To parallelize imports, use the mongorestore `numInsertionWorkersPerCollection` option.

1. After data restore is complete, switch your application's database connection string to use your new target Amazon DocumentDB cluster.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 25, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.