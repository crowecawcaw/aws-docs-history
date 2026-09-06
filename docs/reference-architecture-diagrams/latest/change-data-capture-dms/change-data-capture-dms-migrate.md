

# Change Data Capture Using AWS DMS: Migrate and Replicate
<a name="change-data-capture-dms-migrate"></a>

Publication date: **August 2, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) (AWS DMS) for change data capture (CDC) to migrate databases using ongoing replication.

## Change Data Capture Using AWS DMS: Migrate and Replicate
<a name="diagram1"></a>

![Architecture diagram showing change data capture using AWS DMS to migrate and replicate databases.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/change-data-capture-dms/images/change-data-capture-dms-1.png)


The following steps describe the architecture:

1. Sources for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html), and Amazon RDS.

1. AWS Schema Conversion Tool makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of code objects to a format compatible with the target database.

1. AWS DMS helps you with one-time data migration of databases and continuous data replication. AWS DMS captures changes on the source database and applies them in a transactionally consistent way to the target.

1. Targets for CDC include Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Amazon Aurora, Amazon DocumentDB, Amazon RDS, and Amazon S3.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 2, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.