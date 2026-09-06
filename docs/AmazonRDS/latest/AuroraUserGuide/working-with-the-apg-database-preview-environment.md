

# Working with the database preview environment
<a name="working-with-the-apg-database-preview-environment"></a>

 The PostgreSQL community releases new major version of PostgreSQL annually. Similarly, Amazon Aurora makes PostgreSQL major versions available as Preview releases. This allows you to create DB cluster using the Preview version and test out its features in the Database Preview Environment. 

Aurora PostgreSQL DB clusters in the Database Preview Environment are functionally similar to other Aurora PostgreSQL DB clusters. However, you can't use a Preview version for production.

Keep in mind the following important limitations:
+ All DB instances and DB clusters are deleted 60 days after you create them, along with any backups and snapshots.
+ You can only create a DB instance in a virtual private cloud (VPC) based on the Amazon VPC service.
+ You can't copy a snapshot of a DB instance to a production environment.

The following options are supported by the Preview.
+ You can create DB instances using r5, r6g, r6i, r7g, r7i, r8g, x2g, t3 and t4g instance types only. For more information about instance classes, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md). 
+ You can use both single-AZ and multi-AZ deployments.
+ You can use standard PostgreSQL dump and load functions to export databases from or import databases to the Database Preview Environment.

## Supported DB instance class types
<a name="apg-preview-environment-supported"></a>

Amazon Aurora PostgreSQL supports the following DB instance classes in the preview region:

**Memory Optimized Classes**
+ db.r5 – memory-optimized instance classes
+ db.r6g – memory-optimized instance classes powered by AWS Graviton2 processors
+ db.r6i – memory-optimized instance classes
+ db.r7g – memory-optimized instance classes powered by AWS Graviton3 processors
+ db.r7i – memory-optimized instance classes
+ db.r8g – memory-optimized instance classes powered by AWS Graviton4 processors
+ db.x2g – memory-optimized instance classes powered by AWS Graviton2 processors

**Note**  
For more information on the list of instance classes, see [DB instance class types](Concepts.DBInstanceClass.Types.md).

**Burstable classes**
+ db.t3.medium
+ db.t3.large
+ db.t4g.medium
+ db.t4g.large

## Unsupported features in the preview environment
<a name="apg-preview-environment-exclusions"></a>

The following features aren't available in the preview environment:
+ Aurora Serverless v1 and v2
+ Major version upgrades (MVU)
+ No new minor versions will be released in preview region
+ RDS for PostgreSQL to Aurora PostgreSQL inbound replication
+ Amazon RDS Blue/Green deployment
+ Cross-Region snapshot copy 
+ Aurora global database
+ Database activity streams (DAS), RDS Proxy, and AWS DMS
+ Auto scaling read replicas
+ AWS Bedrock
+ RDS export
+ Performance Insights
+ Custom endpoints
+ Snapshot copy
+ Zero-ETL
+ Babelfish
+ All extensions

## Creating a new DB cluster in the preview environment
<a name="apg-create-db-instance-in-preview-environment"></a>

Use the following procedure to create a DB cluster in the preview environment.

**To create a DB cluster in the preview environment**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Dashboard** from the navigation pane.

1. In the Dashboard page, locate the **Database Preview Environment** section on the Dashboard page, as shown in the following image.  
![Preview environment section with link displayed in RDS Console, Dashboard.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/preview-environment-dashboard.png)

   You can navigate directly to the [Database preview environment](https://us-east-2.console.aws.amazon.com/rds-preview/home?region=us-east-2#). Before you can proceed, you must acknowledge and accept the limitations.   
![Preview environment limitations dialog.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/preview-environment-console.png)

1. To create the Aurora PostgreSQL DB cluster, follow the same process as that for creating any Aurora DB cluster. For more information, see [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md).

To create an instance in the Database Preview Environment using the Aurora API or the AWS CLI, use the following endpoint.

```
rds-preview.us-east-2.amazonaws.com
```

## PostgreSQL version 17 in the Database Preview environment
<a name="PostgreSQL.Concepts.General.version17"></a>

****  
***This is preview documentation for Aurora PostgreSQL version 17. It is subject to change.***

PostgreSQL version 17.0 is now available in the Amazon RDS Database Preview environment. PostgreSQL version 17 contains several improvements that are described in the following PostgreSQL documentation:
+ [ PostgreSQL 17 Released](https://www.postgresql.org/about/news/postgresql-17-released-2936/)

For information on the Database Preview Environment, see [Working with the database preview environment](#working-with-the-apg-database-preview-environment). To access the Preview Environment from the console, select [https://console.aws.amazon.com/rds-preview/](https://console.aws.amazon.com/rds-preview/).