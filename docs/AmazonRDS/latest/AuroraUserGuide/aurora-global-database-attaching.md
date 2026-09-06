

# Adding an AWS Region to an Amazon Aurora global database
<a name="aurora-global-database-attaching"></a>

 You can use the following procedure to add an additional secondary cluster to an existing global database. You can also create a global database from a standalone Aurora DB cluster by using this procedure to add the first secondary AWS Region. 

An Aurora global database needs at least one secondary Aurora DB cluster in a different AWS Region than the primary Aurora DB cluster. You can attach up to 10 secondary DB clusters to your Aurora global database. Repeat the following procedure for each new secondary DB cluster. For each secondary DB cluster that you add to your Aurora global database, reduce the number of Aurora Replicas allowed to the primary DB cluster by one.

For example, if your Aurora global database has 10 secondary Regions, your primary DB cluster can have only 5 (rather than 15) Aurora Replicas. For more information, see [Configuration requirements of an Amazon Aurora global database](aurora-global-database.configuration.requirements.md).

The number of Aurora Replicas (reader instances) in the primary DB cluster determines the number of secondary DB clusters you can add. The total number of reader instances in the primary DB cluster plus the number of secondary clusters can't exceed 15. For example, if you have 14 reader instances in the primary DB cluster and 1 secondary cluster, you can't add another secondary cluster to the global database.

**Note**  
For Aurora MySQL version 3, when you create a secondary cluster, make sure that the value of `lower_case_table_names` matches the value in the primary cluster. This setting is a database parameter that affects how the server handles identifier case sensitivity. For more information about database parameters, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).  
We recommend that when you create a secondary cluster, you use the same DB engine version for the primary and secondary. If necessary, upgrade the primary to be the same version as the secondary. For more information, see [Patch level compatibility for managed cross-Region switchovers and failovers](aurora-global-database-upgrade.md#aurora-global-database-upgrade.minor.incompatibility).

## Console
<a name="aurora-global-database-attach.console"></a>

**To add an AWS Region to an Aurora global database**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane of the AWS Management Console, choose **Databases**. 

1. Choose the Aurora global database that needs a secondary Aurora DB cluster. Ensure that the primary Aurora DB cluster is `Available`.

1.  For **Actions**, choose **Add AWS Region**.   
![Provisioned DB cluster with Add AWS Region chosen from the Actions menu.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-db-create-apg-5-add-region.png)

1. On the **Add a region** page, choose the secondary AWS Region. 

   You can't choose an AWS Region that already has a secondary Aurora DB cluster for the same Aurora global database. Also, it can't be the same Region as the primary Aurora DB cluster.
**Note**  
Babelfish for Aurora PostgreSQL global databases works in secondary regions only if the parameters that control Babelfish preferences are turned on in those regions. For more information, see [DB cluster parameter group settings for Babelfish](babelfish-configuration.md)  
![The Add a region page for an Aurora global database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-db-create-apg-6-add-region.png)

1. Complete the remaining fields for the secondary Aurora cluster in the new AWS Region. These are the same configuration options as for any Aurora DB cluster instance, except for the following option for Aurora MySQL–based Aurora global databases only:
   + Enable read replica write forwarding – This optional setting let's your Aurora global database's secondary DB clusters forward write operations to the primary cluster. For more information, see [Using write forwarding in an Amazon Aurora global database](aurora-global-database-write-forwarding.md).   
![the secondary cluster is now part of the Aurora global database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-database-enable-write-forwarding.png)

1. Choose **Add AWS Region**. 

After you finish adding the Region to your Aurora global database, you can see it in the list of **Databases** in the AWS Management Console as shown in the screenshot. 

![the secondary cluster is now part of the Aurora global database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-db-apg-complete.png)


## AWS CLI
<a name="aurora-global-database-attach.cli"></a>

**To add a secondary AWS Region to an Aurora global database**

 To add a secondary cluster to your global database using the CLI, you must already have the global cluster container object. If you haven't already run the `create-global-cluster` command, see the CLI procedure in [Creating an Amazon Aurora global database](aurora-global-database-creating.md). 

1. Use the `[create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html)` CLI command with the name (`--global-cluster-identifier`) of your Aurora global database. For other parameters, do the following: 

1. For `--region`, choose a different AWS Region than that of your Aurora primary Region.

1. Choose specific values for the `--engine` and `--engine-version` parameters. These values are the same as those for the primary Aurora DB cluster in your Aurora global database. 

1. For an encrypted cluster, specify your primary AWS Region as the `--source-region` for encryption.

The following example creates a new Aurora DB cluster and attaches it to an Aurora global database as a read-only secondary Aurora DB cluster. In the last step, an Aurora DB instance is added to the new Aurora DB cluster.

For Linux, macOS, or Unix:

```
aws rds --region {{secondary_region}} \
  create-db-cluster \
    --db-cluster-identifier {{secondary_cluster_id}} \
    --global-cluster-identifier {{global_database_id}} \
    --engine {{aurora-mysql | aurora-postgresql}} \
    --engine-version {{version}}

aws rds --region {{secondary_region}} \
  create-db-instance \
    --db-instance-class {{instance_class}} \
    --db-cluster-identifier {{secondary_cluster_id}} \
    --db-instance-identifier {{db_instance_id}} \
    --engine {{aurora-mysql | aurora-postgresql}}
```

For Windows:

```
aws rds --region {{secondary_region}} ^
  create-db-cluster ^
    --db-cluster-identifier {{secondary_cluster_id}} ^
    --global-cluster-identifier {{global_database_id_id}} ^
    --engine {{aurora-mysql | aurora-postgresql}} ^
    --engine-version {{version}}

aws rds --region {{secondary_region}} ^
  create-db-instance ^
    --db-instance-class {{instance_class}} ^
    --db-cluster-identifier {{secondary_cluster_id}} ^
    --db-instance-identifier {{db_instance_id}} ^
    --engine {{aurora-mysql | aurora-postgresql}}
```

## RDS API
<a name="aurora-global-database-attach.api"></a>

 To add a new AWS Region to an Aurora global database with the RDS API, run the [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) operation. Specify the identifier of the existing global database using the `GlobalClusterIdentifier` parameter. 