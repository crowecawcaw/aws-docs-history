

# Upgrading Aurora MySQL by modifying the engine version
<a name="AuroraMySQL.Updates.Patching.ModifyEngineVersion"></a>

Upgrading the minor version of an Aurora MySQL DB cluster applies additional fixes and new features to an existing cluster.

This kind of upgrade applies to Aurora MySQL clusters where the original version and the upgraded version both have the same Aurora MySQL major version, either 2 or 3. The process is fast and straightforward because it doesn't involve any conversion for the Aurora MySQL metadata or reorganization of your table data.

You perform this kind of upgrade by modifying the engine version of the DB cluster using the AWS Management Console, AWS CLI, or the RDS API. For example, if your cluster is running Aurora MySQL 3.x, choose a higher 3.x version.

If you're performing a minor upgrade on an Aurora Global Database, upgrade all of the secondary clusters before you upgrade the primary cluster.

**Note**  
To perform a minor version upgrade to Aurora MySQL version 8.4, version 3.04.\* or higher, or version 2.12.\*, use the following process:  
Remove all secondary Regions from the global cluster. Follow the steps in [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md).
Upgrade the engine version of the primary Region to version 8.4, version 3.04.\* or higher, or version 2.12.\*, as applicable. Follow the steps in [To modify the engine version of a DB cluster](#modify-db-cluster-engine-version).
Add secondary Regions to the global cluster. Follow the steps in [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md).

 **To modify the engine version of a DB cluster** 
+ **By using the console** – Modify the properties of your cluster. In the **Modify DB cluster** window, change the Aurora MySQL engine version in the **DB engine version** box. If you aren't familiar with the general procedure for modifying a cluster, follow the instructions at [Modifying the DB cluster by using the console, CLI, and API](Aurora.Modifying.md#Aurora.Modifying.Cluster).
+ **By using the AWS CLI** – Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command, and specify the name of your DB cluster for the `--db-cluster-identifier` option and the engine version for the `--engine-version` option.

  For example, to upgrade to Aurora MySQL version 3.04.1, set the `--engine-version` option to `8.0.mysql_aurora.3.04.1`. Specify the `--apply-immediately` option to immediately update the engine version for your DB cluster.
+ **By using the RDS API** – Call the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) API operation, and specify the name of your DB cluster for the `DBClusterIdentifier` parameter and the engine version for the `EngineVersion` parameter. Set the `ApplyImmediately` parameter to `true` to immediately update the engine version for your DB cluster.