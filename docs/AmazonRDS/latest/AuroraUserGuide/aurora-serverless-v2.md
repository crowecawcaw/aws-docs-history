# Migrating to Aurora Serverless v2

To convert an existing DB cluster to use Aurora Serverless v2, you can do the following:

- Upgrade from a provisioned Aurora DB cluster.
- Upgrade from an Aurora Serverless v1 cluster.
- Migrate from an on-premises database to an Aurora Serverless v2 cluster.
  When your upgraded cluster is running the appropriate engine version as listed in [Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md"), you can begin adding Aurora Serverless v2 DB instances to it. The first DB
  instance that you add to the upgraded cluster must be a provisioned DB instance. Then you can switch over the processing for the
  write workload, the read workload, or both to the Aurora Serverless v2 DB instances.

###### Contents

- [Upgrading or switching existing clusters to use Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.getting-started-general-procedure "aurora-serverless-v2.md#aurora-serverless-v2.getting-started-general-procedure")
  - [Upgrade paths for MySQL-compatible clusters to use Aurora Serverless v2](aurora-serverless-v2.md#serverless-v2-upgrade-paths-ams "aurora-serverless-v2.md#serverless-v2-upgrade-paths-ams")
  - [Upgrade paths for PostgreSQL-compatible clusters to use Aurora Serverless v2](aurora-serverless-v2.md#serverless-v2-upgrade-paths-apg "aurora-serverless-v2.md#serverless-v2-upgrade-paths-apg")

- [Switching from a provisioned cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.switch-from-provisioned "aurora-serverless-v2.md#aurora-serverless-v2.switch-from-provisioned")
- [Comparison of Aurora Serverless v2 and Aurora Serverless v1](aurora-serverless-v2.md#aurora-serverless.comparison "aurora-serverless-v2.md#aurora-serverless.comparison")
  - [Comparison of Aurora Serverless v2 and Aurora Serverless v1 requirements](aurora-serverless-v2.md#aurora-serverless.comparison-requirements "aurora-serverless-v2.md#aurora-serverless.comparison-requirements")
  - [Comparison of Aurora Serverless v2 and Aurora Serverless v1 scaling and availability](aurora-serverless-v2.md#aurora-serverless.comparison-scaling "aurora-serverless-v2.md#aurora-serverless.comparison-scaling")
  - [Comparison of Aurora Serverless v2 and Aurora Serverless v1 feature support](aurora-serverless-v2.md#aurora-serverless.comparison-features "aurora-serverless-v2.md#aurora-serverless.comparison-features")
  - [Adapting Aurora Serverless v1 use cases to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless.comparison-approaches "aurora-serverless-v2.md#aurora-serverless.comparison-approaches")

- [Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure")
  - [Aurora MySQL–compatible DB clusters](aurora-serverless-v2.md#sv1-to-sv2-ams "aurora-serverless-v2.md#sv1-to-sv2-ams")
  - [Aurora PostgreSQL–compatible DB clusters](aurora-serverless-v2.md#sv1-to-sv2-apg "aurora-serverless-v2.md#sv1-to-sv2-apg")

- [Migrating from an on-premises database to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.migrate-from-on-prem "aurora-serverless-v2.md#aurora-serverless-v2.migrate-from-on-prem")

###### Note

These topics describe how to convert an existing DB cluster. For information on creating a new Aurora Serverless v2 DB cluster,
see [Creating a DB cluster that uses Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

## Upgrading or switching existing clusters to use Aurora Serverless v2

If your provisioned cluster has an engine version that supports Aurora Serverless v2, switching to
Aurora Serverless v2 doesn't require an upgrade. In that case, you can add Aurora Serverless v2 DB instances
to your original cluster. You can switch the cluster to use all Aurora Serverless v2 DB instances. You can also
use a combination of Aurora Serverless v2 and provisioned DB instances in the same DB cluster. For the Aurora
engine versions that support Aurora Serverless v2, see
[Supported
Regions and Aurora DB engines for Aurora Serverless v2](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

If you're running a lower engine version that doesn't support Aurora Serverless v2, you take these general steps:

1. Upgrade the cluster.
2. Create a provisioned writer DB instance for the upgraded cluster.
3. Modify the cluster to use Aurora Serverless v2 DB instances.

###### Important

When you perform a major version upgrade to an Aurora Serverless v2-compatible version by using snapshot restore or cloning, the
first DB instance that you add to the new cluster must be a provisioned DB instance. This addition starts the final stage of
the upgrade process.

Until that final stage happens, the cluster doesn't have the infrastructure that's required for Aurora Serverless v2
support. Thus, these upgraded clusters always start with a provisioned writer DB instance. Then you can convert or fail over
the provisioned DB instance to an Aurora Serverless v2 one.

Upgrading from Aurora Serverless v1 to Aurora Serverless v2 involves creating a provisioned cluster as an intermediate step. Then you
perform the same upgrade steps as when you start with a provisioned cluster.

### Upgrade paths for MySQL-compatible clusters to use Aurora Serverless v2

If your original cluster is running Aurora MySQL, choose the appropriate procedure depending on the engine version and engine mode
of your cluster.

| If your original Aurora MySQL cluster is this                                          | Do this to switch to Aurora Serverless v2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Provisioned cluster running Aurora MySQL version 3, compatible with MySQL 8.0          | This is the final stage for all conversions from existing Aurora MySQL clusters.<br>If necessary, perform a minor version upgrade to version 3.02.0 or higher. Use a provisioned DB instance for the writer DB instance.<br>Add one Aurora Serverless v2 reader DB instance. Perform a failover to make that the writer DB instance.<br>(Optional) Convert other provisioned DB instances in the cluster to Aurora Serverless v2. Or add new Aurora Serverless v2 DB instances<br>and remove the provisioned DB instances.<br>For the full procedure and examples, see<br>[Switching from a provisioned cluster to Aurora Serverless v2](#aurora-serverless-v2.switch-from-provisioned "#aurora-serverless-v2.switch-from-provisioned"). |
| Provisioned cluster running Aurora MySQL version 2, compatible with MySQL 5.7          | Perform a major version upgrade to Aurora MySQL version 3.02.0 or higher. Then follow the procedure for Aurora MySQL version 3 to switch the<br>cluster to use Aurora Serverless v2 DB instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Aurora Serverless v1 cluster running Aurora MySQL version 2, compatible with MySQL 5.7 | To help plan your conversion from Aurora Serverless v1, consult [Comparison of Aurora Serverless v2 and Aurora Serverless v1](#aurora-serverless.comparison "#aurora-serverless.comparison") first.<br>Then follow the procedure in<br>[Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").                                                                                                                                                                                                                                                                                                |

### Upgrade paths for PostgreSQL-compatible clusters to use Aurora Serverless v2

If your original cluster is running Aurora PostgreSQL, choose the appropriate procedure depending on the engine version and engine
mode of your cluster.

| If your original Aurora PostgreSQL cluster is this                      | Do this to switch to Aurora Serverless v2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioned cluster running Aurora PostgreSQL version 13                | This is the final stage for all conversions from existing Aurora PostgreSQL clusters.<br>If necessary, perform a minor version upgrade to version 13.6 or higher. Add one provisioned DB instance for the<br>writer DB instance. Add one Aurora Serverless v2 reader DB instance. Perform a failover to make that Aurora Serverless v2<br>instance the writer DB instance.<br>(Optional) Convert other provisioned DB instances in the cluster to Aurora Serverless v2. Or add new Aurora Serverless v2<br>DB instances and remove the provisioned DB instances.<br>For the full procedure and examples, see<br>[Switching from a provisioned cluster to Aurora Serverless v2](#aurora-serverless-v2.switch-from-provisioned "#aurora-serverless-v2.switch-from-provisioned"). |
| Provisioned cluster running Aurora PostgreSQL version 11 or 12          | Perform a major version upgrade to Aurora PostgreSQL version 13.6 or higher. Then follow the procedure for Aurora PostgreSQL<br>version 13 to switch the cluster to use Aurora Serverless v2 DB instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Aurora Serverless v1 cluster running Aurora PostgreSQL version 11 or 13 | To help plan your conversion from Aurora Serverless v1, consult<br>[Comparison of Aurora Serverless v2 and Aurora Serverless v1](#aurora-serverless.comparison "#aurora-serverless.comparison") first.<br>Then follow the procedure in<br>[Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").                                                                                                                                                                                                                                                                                                                                   |

## Switching from a provisioned cluster to Aurora Serverless v2

To switch a provisioned cluster to use Aurora Serverless v2, follow these steps:

1. Check if the provisioned cluster needs to be upgraded to be used with Aurora Serverless v2 DB instances. For the Aurora versions
   that are compatible with Aurora Serverless v2, see [Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

If the provisioned cluster is running an engine version that isn't available for Aurora Serverless v2, upgrade the engine
version of the cluster:

    * If you have a MySQL 5.7–compatible provisioned cluster, follow the upgrade instructions for Aurora MySQL version 3.
     Use the procedures in [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md").
    * If you have a PostgreSQL-compatible provisioned cluster running PostgreSQL version 11 or 12, follow the upgrade
     instructions for Aurora PostgreSQL version 13. Use the procedures in [Performing a major
     version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").

2. Configure any other cluster properties to match the Aurora Serverless v2 requirements from [Requirements and limitations for Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").
3. Configure the scaling configuration for the cluster. Follow the procedure in [Setting the Aurora Serverless v2 capacity range for a cluster](aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus "aurora-serverless-v2-administration.md#aurora-serverless-v2-setting-acus").
4. Add one or more Aurora Serverless v2 DB instances to the cluster. Follow the general procedure in [Adding Aurora Replicas to a DB cluster](aurora-replicas-adding.md "aurora-replicas-adding.md"). For each new DB instance, specify the
   special DB instance class name **Serverless** in the AWS Management Console, or `db.serverless` in the
   AWS CLI or Amazon RDS API.

In some cases, you might already have one or more provisioned reader DB instances in the cluster. If so, you can convert one
of the readers to an Aurora Serverless v2 DB instance instead of creating a new DB instance. To do so, follow the
procedure in [Converting a provisioned writer or reader to Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned "aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned"). 5. Perform a failover operation to make one of the Aurora Serverless v2 DB instances the writer DB instance for the cluster. 6. (Optional) Convert any provisioned DB instances to Aurora Serverless v2, or remove them from the cluster. Follow the general
procedure in [Converting a provisioned writer or reader to Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned "aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned") or [Deleting a DB instance from an Aurora DB cluster](USER_DeleteCluster.md#USER_DeleteInstance "USER_DeleteCluster.md#USER_DeleteInstance").

###### Tip

Removing the provisioned DB instances isn't mandatory. You can set up a cluster containing both Aurora Serverless v2 and
provisioned DB instances. However, until you are familiar with the performance and scaling characteristics of
Aurora Serverless v2 DB instances, we recommend that you configure your clusters with DB instances all of the same
type.

The following AWS CLI example shows the switchover process using a provisioned cluster that's running Aurora MySQL version
3.02.0. The cluster is named `mysql-80`. The cluster starts with two provisioned DB instances named
`provisioned-instance-1` and `provisioned-instance-2`, a writer and a reader. They both use the
`db.r6g.large` DB instance class.

```
$ aws rds describe-db-clusters --db-cluster-identifier mysql-80 \
  --query '*[].[DBClusterIdentifier,DBClusterMembers[*].[DBInstanceIdentifier,IsClusterWriter]]' --output text
mysql-80
provisioned-instance-2     False
provisioned-instance-1     True

$ aws rds describe-db-instances --db-instance-identifier provisioned-instance-1 \
  --output text --query '*[].[DBInstanceIdentifier,DBInstanceClass]'
provisioned-instance-1     db.r6g.large

$ aws rds describe-db-instances --db-instance-identifier provisioned-instance-2 \
  --output text --query '*[].[DBInstanceIdentifier,DBInstanceClass]'
provisioned-instance-2     db.r6g.large

```

We create a table with some data. That way, we can confirm that the data and operation of the cluster are the
same before and after the switchover.

```
mysql> create database serverless_v2_demo;
mysql> create table serverless_v2_demo.demo (s varchar(128));
mysql> insert into serverless_v2_demo.demo values ('This cluster started with a provisioned writer.');
Query OK, 1 row affected (0.02 sec)

```

First, we add a capacity range to the cluster. Otherwise, we get an error when adding any Aurora Serverless v2 DB instances to the
cluster. If we use the AWS Management Console for this procedure, that step is automatic when we add the first Aurora Serverless v2 DB
instance.

```
$ aws rds create-db-instance --db-instance-identifier serverless-v2-instance-1 \
  --db-cluster-identifier mysql-80 --db-instance-class db.serverless --engine aurora-mysql

An error occurred (InvalidDBClusterStateFault) when calling the CreateDBInstance operation:
Set the Serverless v2 scaling configuration on the parent DB cluster before creating a Serverless v2 DB instance.

$ # The blank ServerlessV2ScalingConfiguration attribute confirms that the cluster doesn't have a capacity range set yet.
$ aws rds describe-db-clusters --db-cluster-identifier mysql-80 --query 'DBClusters[*].ServerlessV2ScalingConfiguration'
[]

$ aws rds modify-db-cluster --db-cluster-identifier mysql-80 \
  --serverless-v2-scaling-configuration MinCapacity=0.5,MaxCapacity=16
{
  "DBClusterIdentifier": "mysql-80",
  "ServerlessV2ScalingConfiguration": {
    "MinCapacity": 0.5,
    "MaxCapacity": 16
  }
}
```

We create two Aurora Serverless v2 readers to take the place of the original DB instances. We do so by specifying the
`db.serverless` DB instance class for the new DB instances.

```
$ aws rds create-db-instance --db-instance-identifier serverless-v2-instance-1 --db-cluster-identifier mysql-80 --db-instance-class db.serverless --engine aurora-mysql
{
  "DBInstanceIdentifier": "serverless-v2-instance-1",
  "DBClusterIdentifier": "mysql-80",
  "DBInstanceClass": "db.serverless",
  "DBInstanceStatus": "creating"
}

$ aws rds create-db-instance --db-instance-identifier serverless-v2-instance-2 \
  --db-cluster-identifier mysql-80 --db-instance-class db.serverless --engine aurora-mysql
{
  "DBInstanceIdentifier": "serverless-v2-instance-2",
  "DBClusterIdentifier": "mysql-80",
  "DBInstanceClass": "db.serverless",
  "DBInstanceStatus": "creating"
}

$ # Wait for both DB instances to finish being created before proceeding.
$ aws rds wait db-instance-available --db-instance-identifier serverless-v2-instance-1 && \
  aws rds wait db-instance-available --db-instance-identifier serverless-v2-instance-2
```

We perform a failover to make one of the Aurora Serverless v2 DB instances the new writer for the cluster.

```
$ aws rds failover-db-cluster --db-cluster-identifier mysql-80 \
  --target-db-instance-identifier serverless-v2-instance-1
{
  "DBClusterIdentifier": "mysql-80",
  "DBClusterMembers": [
    {
      "DBInstanceIdentifier": "serverless-v2-instance-1",
      "IsClusterWriter": false,
      "DBClusterParameterGroupStatus": "in-sync",
      "PromotionTier": 1
    },
    {
      "DBInstanceIdentifier": "serverless-v2-instance-2",
      "IsClusterWriter": false,
      "DBClusterParameterGroupStatus": "in-sync",
      "PromotionTier": 1
    },
    {
      "DBInstanceIdentifier": "provisioned-instance-2",
      "IsClusterWriter": false,
      "DBClusterParameterGroupStatus": "in-sync",
      "PromotionTier": 1
    },
    {
      "DBInstanceIdentifier": "provisioned-instance-1",
      "IsClusterWriter": true,
      "DBClusterParameterGroupStatus": "in-sync",
      "PromotionTier": 1
    }
  ],
  "Status": "available"
}
```

It takes a few seconds for that change to take effect. At that point, we have an Aurora Serverless v2 writer and an
Aurora Serverless v2 reader. Thus, we don't need either of the original provisioned DB instances.

```
$ aws rds describe-db-clusters --db-cluster-identifier mysql-80 \
  --query '*[].[DBClusterIdentifier,DBClusterMembers[*].[DBInstanceIdentifier,IsClusterWriter]]' \
  --output text
mysql-80
serverless-v2-instance-1        True
serverless-v2-instance-2        False
provisioned-instance-2          False
provisioned-instance-1          False
```

The last step in the switchover procedure is to delete both of the provisioned DB instances.

```
$ aws rds delete-db-instance --db-instance-identifier provisioned-instance-2 --skip-final-snapshot
{
  "DBInstanceIdentifier": "provisioned-instance-2",
  "DBInstanceStatus": "deleting",
  "Engine": "aurora-mysql",
  "EngineVersion": "8.0.mysql_aurora.3.02.0",
  "DBInstanceClass": "db.r6g.large"
}

$ aws rds delete-db-instance --db-instance-identifier provisioned-instance-1 --skip-final-snapshot
{
  "DBInstanceIdentifier": "provisioned-instance-1",
  "DBInstanceStatus": "deleting",
  "Engine": "aurora-mysql",
  "EngineVersion": "8.0.mysql_aurora.3.02.0",
  "DBInstanceClass": "db.r6g.large"
}
```

As a final check, we confirm that the original table is accessible and writeable from the Aurora Serverless v2 writer DB
instance.

```
mysql> select * from serverless_v2_demo.demo;
+---------------------------------------------------+
| s                                                 |
+---------------------------------------------------+
| This cluster started with a provisioned writer.   |
+---------------------------------------------------+
1 row in set (0.00 sec)

mysql> insert into serverless_v2_demo.demo values ('And it finished with a Serverless v2 writer.');
Query OK, 1 row affected (0.01 sec)

mysql> select * from serverless_v2_demo.demo;
+---------------------------------------------------+
| s                                                 |
+---------------------------------------------------+
| This cluster started with a provisioned writer.   |
| And it finished with a Serverless v2 writer.      |
+---------------------------------------------------+
2 rows in set (0.01 sec)
```

We also connect to the Aurora Serverless v2 reader DB instance and confirm that the newly written data is
available there too.

```
mysql> select * from serverless_v2_demo.demo;
+---------------------------------------------------+
| s                                                 |
+---------------------------------------------------+
| This cluster started with a provisioned writer.   |
| And it finished with a Serverless v2 writer.      |
+---------------------------------------------------+
2 rows in set (0.01 sec)
```

## Comparison of Aurora Serverless v2 and Aurora Serverless v1

If you are already using Aurora Serverless v1, you can learn the major differences between Aurora Serverless v1 and Aurora Serverless v2.
The architectural differences, such as support for reader DB instances, open up new types of use cases.

You can use the following tables to help understand the most important differences between Aurora Serverless v2 and
Aurora Serverless v1.

###### Topics

- [Comparison of Aurora Serverless v2 and Aurora Serverless v1 requirements](#aurora-serverless.comparison-requirements "#aurora-serverless.comparison-requirements")
- [Comparison of Aurora Serverless v2 and Aurora Serverless v1 scaling and availability](#aurora-serverless.comparison-scaling "#aurora-serverless.comparison-scaling")
- [Comparison of Aurora Serverless v2 and Aurora Serverless v1 feature support](#aurora-serverless.comparison-features "#aurora-serverless.comparison-features")
- [Adapting Aurora Serverless v1 use cases to Aurora Serverless v2](#aurora-serverless.comparison-approaches "#aurora-serverless.comparison-approaches")

### Comparison of Aurora Serverless v2 and Aurora Serverless v1 requirements

The following table summarizes the different requirements to run your database using Aurora Serverless v2 or Aurora Serverless v1.
Aurora Serverless v2 offers higher versions of the Aurora MySQL and Aurora PostgreSQL DB engines than Aurora Serverless v1 does.

| Feature                                      | Aurora Serverless v2 requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Aurora Serverless v1 requirement                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DB engines                                   | Aurora MySQL, Aurora PostgreSQL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Aurora MySQL, Aurora PostgreSQL                                                                                                                                                                                                                                                                                                                                                          |
| Supported Aurora MySQL versions              | See [Aurora Serverless v2 with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | See [Aurora Serverless v1 with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy").                                                                                                                     |
| Supported Aurora PostgreSQL versions         | See [Aurora Serverless v2 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | See [Aurora Serverless v1 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg").                                                                                                                |
| Upgrading a DB cluster                       | Similarly to provisioned DB clusters, you can perform upgrades manually without waiting for Aurora to<br>upgrade the DB cluster for you. For more information, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").<br>NoteTo perform a major version upgrade from 13.x to 14.x or 15.x for an Aurora PostgreSQL–compatible DB<br>cluster, the maximum capacity of your cluster must be at least 2 ACUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Minor version upgrades are applied automatically as they become available. For more information, see [Aurora Serverless v1 and Aurora database engine versions](aurora-serverless.md "aurora-serverless.md").<br>You can perform major version upgrades manually. For more information, see [Modifying an Aurora Serverless v1 DB cluster](aurora-serverless.md "aurora-serverless.md"). |
| Converting from provisioned DB cluster       | You can use the following methods:<br>• Add one or more Aurora Serverless v2 reader DB instances to an existing provisioned cluster. To<br>use Aurora Serverless v2 for the writer, perform a failover to one of the Aurora Serverless v2 DB<br>instances. For the entire cluster to use Aurora Serverless v2 DB instances, remove any provisioned<br>writer DB instances after promoting the Aurora Serverless v2 DB instance to the writer.<br>• Create a new cluster with the appropriate DB engine and engine version. Use any of the standard<br>methods. For example, restore a cluster snapshot or create a clone of an existing cluster.<br>Choose Aurora Serverless v2 for some or all of the DB instances in the new cluster.<br>If you create the new cluster through cloning, you can't upgrade the engine version at the<br>same time. Make sure that the original cluster is already running an engine version that's<br>compatible with Aurora Serverless v2. | Restore snapshot of provisioned cluster to create new Aurora Serverless v1 cluster.                                                                                                                                                                                                                                                                                                      |
| Converting from Aurora Serverless v1 cluster | Follow the procedure in [Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Not applicable                                                                                                                                                                                                                                                                                                                                                                           |
| Available DB instance classes                | The special DB instance class `db.serverless`. In the AWS Management Console, it's labeled as<br>**Serverless**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Not applicable. Aurora Serverless v1 uses the `serverless` engine mode.                                                                                                                                                                                                                                                                                                                  |
| Port                                         | Any port that's compatible with MySQL or PostgreSQL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Default MySQL or PostgreSQL port only                                                                                                                                                                                                                                                                                                                                                    |
| Public IP address allowed?                   | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                                                                                                                                                                                                                                                                                                                                                                                       |
| Virtual private cloud (VPC) required?        | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes. Each Aurora Serverless v1 cluster consumes 2 interface and Gateway Load Balancer endpoints<br>allocated to your VPC.                                                                                                                                                                                                                                                                |

### Comparison of Aurora Serverless v2 and Aurora Serverless v1 scaling and availability

The following table summarizes differences between Aurora Serverless v2 and Aurora Serverless v1 for scalability
and availability.

Aurora Serverless v2 scaling is more responsive, more granular, and less disruptive than the scaling in
Aurora Serverless v1. Aurora Serverless v2 can scale both by changing the size of the DB instance and by adding
more DB instances to the DB cluster. It can also scale by adding clusters in other AWS Regions to an Aurora
global database. In contrast, Aurora Serverless v1 only scales by increasing or decreasing the capacity of the
writer. All the compute for an Aurora Serverless v1 cluster runs in a single Availability Zone and a single
AWS Region.

| Scaling and high availability feature                       | Aurora Serverless v2 behavior                                                                                                                                                                                | Aurora Serverless v1 behavior                                                                                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum Aurora capacity units (ACUs) (Aurora MySQL)         | 0.5 when the cluster is running, 0 when the cluster is paused.                                                                                                                                               | 1 when the cluster is running, 0 when the cluster is paused.                                                                                                    |
| Minimum ACUs (Aurora PostgreSQL)                            | 0.5 when the cluster is running, 0 when the cluster is paused.                                                                                                                                               | 2 when the cluster is running, 0 when the cluster is paused.                                                                                                    |
| Maximum ACUs (Aurora MySQL)                                 | 256                                                                                                                                                                                                          | 256                                                                                                                                                             |
| Maximum ACUs (Aurora PostgreSQL)                            | 256                                                                                                                                                                                                          | 384                                                                                                                                                             |
| Stopping a cluster                                          | You can manually stop and start the cluster by using<br>[the same cluster<br>stop and start feature](aurora-cluster-stop-start.md "aurora-cluster-stop-start.md") as provisioned clusters.                   | The cluster pauses automatically after a timeout. It takes some time to become available when activity<br>resumes.                                              |
| Scaling for DB instances                                    | Scale up and down with minimum increment of 0.5 ACUs.                                                                                                                                                        | Scale up and down by doubling or halving the ACUs.                                                                                                              |
| Number of DB instances                                      | Same as a provisioned cluster: 1 writer DB instance, up to 15 reader DB instances.                                                                                                                           | 1 DB instance handling both reads and writes.                                                                                                                   |
| Scaling can happen while SQL statements are running?        | Yes. Aurora Serverless v2 doesn't require waiting for a quiet point.                                                                                                                                         | No. For example, scaling waits for completion of long-running transactions, temporary tables, and<br>table locks.                                               |
| Reader DB instances scale along with writer                 | Optional                                                                                                                                                                                                     | Not applicable                                                                                                                                                  |
| Maximum storage                                             | 128 TiB                                                                                                                                                                                                      | 128 TiB                                                                                                                                                         |
| Buffer cache preserved when scaling                         | Yes. Buffer cache is resized dynamically.                                                                                                                                                                    | No. Buffer cache is rewarmed after scaling.                                                                                                                     |
| Failover                                                    | Yes, same as for provisioned clusters.                                                                                                                                                                       | Best effort only, subject to capacity availability. Slower than in Aurora Serverless v2.                                                                        |
| Multi-AZ capability                                         | Yes, same as for provisioned. A Multi-AZ cluster requires a reader DB instance in a second<br>Availability Zone (AZ). For a Multi-AZ cluster, Aurora performs Multi-AZ failover in case of an AZ<br>failure. | Aurora Serverless v1 clusters run all their compute in a single AZ. Recovery in case of AZ failure is<br>best effort only and subject to capacity availability. |
| Aurora global databases                                     | Yes                                                                                                                                                                                                          | No                                                                                                                                                              |
| Scaling based on memory pressure                            | Yes                                                                                                                                                                                                          | No                                                                                                                                                              |
| Scaling based on CPU load                                   | Yes                                                                                                                                                                                                          | Yes                                                                                                                                                             |
| Scaling based on network traffic                            | Yes, based on memory and CPU overhead of network traffic. The `max_connections` parameter<br>remains constant to avoid dropping connections when scaling down.                                               | Yes, based on number of connections.                                                                                                                            |
| Timeout action for scaling events                           | No                                                                                                                                                                                                           | Yes                                                                                                                                                             |
| Adding new DB instances to cluster through AWS Auto Scaling | Not applicable. You can create Aurora Serverless v2 reader DB instances in promotion tiers 2–15<br>and leave them scaled down to low capacity.                                                               | No. Reader DB instances aren't available.                                                                                                                       |

### Comparison of Aurora Serverless v2 and Aurora Serverless v1 feature support

The following table summarizes these:

- Features that are available in Aurora Serverless v2 but not Aurora Serverless v1
- Features that work differently between Aurora Serverless v1 and Aurora Serverless v2
- Features that aren't currently available in Aurora Serverless v2

Aurora Serverless v2 includes many features from provisioned clusters that aren't available for
Aurora Serverless v1.

| Feature                                              | Aurora Serverless v2 support                                                                                                                                                                                                                                                         | Aurora Serverless v1 support                                                                                                                                                                                                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cluster topology                                     | Aurora Serverless v2 is a property of individual DB instances. A cluster can contain multiple Aurora Serverless v2 DB<br>instances, or a combination of Aurora Serverless v2 and provisioned DB instances.                                                                           | Aurora Serverless v1 clusters don't use the notion of DB instances. You can't change the Aurora Serverless v1<br>property after you create the cluster.                                                                                   |
| Configuration parameters                             | Almost all the same parameters can be modified as in provisioned clusters. For details, see [Working with parameter groups for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups "aurora-serverless-v2.md#aurora-serverless-v2.parameter-groups"). | Only a subset of parameters can be modified.                                                                                                                                                                                              |
| Parameter groups                                     | Cluster parameter group and DB parameter groups. Parameters with `provisioned` value in<br>`SupportedEngineModes` attribute are available. That's many more parameters than in<br>Aurora Serverless v1.                                                                              | Cluster parameter group only. Parameters with `serverless` value in `SupportedEngineModes`<br>attribute are available.                                                                                                                    |
| Encryption for cluster volume                        | Optional                                                                                                                                                                                                                                                                             | Required. The limitations in [Limitations of Amazon Aurora encrypted DB clusters](Overview.md#Overview.Encryption.Limitations "Overview.md#Overview.Encryption.Limitations") apply to all Aurora Serverless v1 clusters.                  |
| Cross-Region snapshots                               | Yes                                                                                                                                                                                                                                                                                  | Snapshot must be encrypted with your own AWS Key Management Service (AWS KMS) key.                                                                                                                                                        |
| Automated backups retained after DB cluster deletion | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| TLS/SSL                                              | Yes. The support is the same as for provisioned clusters. For usage information, see [Using TLS/SSL with Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2.tls "aurora-serverless-v2-administration.md#aurora-serverless-v2.tls").                   | Yes. There are some differences from TLS support for provisioned clusters. For usage information, see [Using TLS/SSL with Aurora Serverless v1](aurora-serverless.md#aurora-serverless.tls "aurora-serverless.md#aurora-serverless.tls"). |
| Cloning                                              | Only from and to DB engine versions that are compatible with Aurora Serverless v2. You can't use cloning to upgrade<br>from Aurora Serverless v1 or from an earlier version of a provisioned cluster.                                                                                | Only from and to DB engine versions that are compatible with Aurora Serverless v1.                                                                                                                                                        |
| Integration with Amazon S3                           | Yes                                                                                                                                                                                                                                                                                  | Yes                                                                                                                                                                                                                                       |
| Integration with AWS Secrets Manager                 | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| Exporting DB cluster snapshots to S3                 | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| Associating an IAM role                              | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| Uploading logs to Amazon CloudWatch                  | Optional. You choose which logs to turn on and which logs to upload to CloudWatch.                                                                                                                                                                                                   | All logs that are turned on are uploaded to CloudWatch automatically.                                                                                                                                                                     |
| Data API available                                   | Yes                                                                                                                                                                                                                                                                                  | Yes                                                                                                                                                                                                                                       |
| Query editor available                               | Yes                                                                                                                                                                                                                                                                                  | Yes                                                                                                                                                                                                                                       |
| Performance Insights                                 | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| Amazon RDS Proxy available                           | Yes                                                                                                                                                                                                                                                                                  | No                                                                                                                                                                                                                                        |
| Babelfish for Aurora PostgreSQL available            | Yes. Supported for Aurora PostgreSQL versions that are compatible with both Babelfish and Aurora Serverless v2.                                                                                                                                                                      | No                                                                                                                                                                                                                                        |

### Adapting Aurora Serverless v1 use cases to Aurora Serverless v2

Depending on your use case for Aurora Serverless v1, you might adapt that approach to take advantage of Aurora Serverless v2
features as follows.

Suppose that you have an Aurora Serverless v1 cluster that is lightly loaded and your priority is maintaining continuous
availability while minimizing costs. With Aurora Serverless v2, you can configure a smaller minimum ACU setting of 0.5, compared
with a minimum of 1 ACU for Aurora Serverless v1. You can increase availability by creating a Multi-AZ configuration, with the
reader DB instance also having a minimum of 0.5 ACUs.

Suppose that you have an Aurora Serverless v1 cluster that you use in a development and test scenario. In this case, cost is
also a high priority but the cluster doesn't need to be available at all times. Aurora Serverless v2 can
automatically pause each instance when it's completely idle. You do so by specifying a minimum capacity of 0 ACUs
for the cluster, as explained in
[Scaling to Zero ACUs with automatic pause and resume for Aurora Serverless v2](aurora-serverless-v2-auto-pause.md "aurora-serverless-v2-auto-pause.md"). You can also
manually stop the cluster when it's not needed,
and start it when it's time for the next test or development cycle.

Suppose that you have an Aurora Serverless v1 cluster with a heavy workload. An equivalent cluster using Aurora Serverless v2 can
scale with more granularity. For example, Aurora Serverless v1 scales by doubling the capacity, for example from 64 to 128 ACUs.
In contrast, your Aurora Serverless v2 DB instance can scale in 0.5-ACU increments.

Suppose that your workload requires a higher total capacity than is available in Aurora Serverless v1. You can use multiple
Aurora Serverless v2 reader DB instances to offload the read-intensive parts of the workload from the writer DB instance. You can
also divide the read-intensive workload among multiple reader DB instances.

For a write-intensive workload, you might configure the cluster with a large provisioned DB instance as the writer. You might
do so alongside one or more Aurora Serverless v2 reader DB instances.

## Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

The process of upgrading a DB cluster from Aurora Serverless v1 to Aurora Serverless v2 has multiple steps. That's because
you can't convert directly from Aurora Serverless v1 to Aurora Serverless v2. There's always an intermediate step that involves
converting the Aurora Serverless v1 DB cluster to a provisioned cluster.

### Aurora MySQL–compatible DB clusters

You can convert your Aurora Serverless v1 DB cluster to a provisioned DB cluster, then use a blue/green deployment to
upgrade it and convert it to an Aurora Serverless v2 DB cluster. We recommend this procedure for production environments. For
more information, see [Using Amazon Aurora Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

###### To use a blue/green deployment to upgrade an Aurora Serverless v1 cluster running Aurora MySQL version 2 (MySQL

5.7–compatible)

1. Convert the Aurora Serverless v1 DB cluster to a provisioned Aurora MySQL version 2 cluster. Follow the procedure in
   [Converting from Aurora Serverless v1 to
   provisioned](aurora-serverless.md#aurora-serverless.modifying.convert "aurora-serverless.md#aurora-serverless.modifying.convert").
2. Create a blue/green deployment. Follow the procedure in [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md "blue-green-deployments-creating.md").
3. Choose an Aurora MySQL version for the green cluster that's compatible with Aurora Serverless v2, for example
   3.04.1.

For compatible versions, see [Aurora Serverless v2 with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy"). 4. Modify the writer DB instance of the green cluster to use the **Serverless v2** (db.serverless)
DB instance class.

For details, see [Converting a provisioned writer or reader to Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned "aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned"). 5. When your upgraded Aurora Serverless v2 DB cluster is available, switch over from the blue cluster to the green
cluster.

### Aurora PostgreSQL–compatible DB clusters

You can convert your Aurora Serverless v1 DB cluster to a provisioned DB cluster, then use a blue/green deployment to
upgrade it and convert it to an Aurora Serverless v2 DB cluster. We recommend this procedure for production environments. For
more information, see [Using Amazon Aurora Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

###### To use a blue/green deployment to upgrade an Aurora Serverless v1 cluster running Aurora PostgreSQL version 11

1. Convert the Aurora Serverless v1 DB cluster to a provisioned Aurora PostgreSQL cluster. Follow the procedure in [Converting from Aurora Serverless v1 to
   provisioned](aurora-serverless.md#aurora-serverless.modifying.convert "aurora-serverless.md#aurora-serverless.modifying.convert").
2. Create a blue/green deployment. Follow the procedure in [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md "blue-green-deployments-creating.md").
3. Choose an Aurora PostgreSQL version for the green cluster that's compatible with Aurora Serverless v2, for example
   15.3.

For compatible versions, see [Aurora Serverless v2 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg"). 4. Modify the writer DB instance of the green cluster to use the **Serverless v2** (db.serverless)
DB instance class.

For details, see [Converting a provisioned writer or reader to Aurora Serverless v2](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned "aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned"). 5. When your upgraded Aurora Serverless v2 DB cluster is available, switch over from the blue cluster to the green
cluster.

You can also upgrade your Aurora Serverless v1 DB cluster directly from Aurora PostgreSQL version 11 to version 13, convert it
to a provisioned DB cluster, and then convert the provisioned cluster to an Aurora Serverless v2 DB cluster.

###### To upgrade, then convert an Aurora Serverless v1 cluster running Aurora PostgreSQL version 11

1. Convert the Aurora Serverless v1 DB cluster to a provisioned Aurora PostgreSQL cluster. Follow the procedure in [Converting from Aurora Serverless v1 to
   provisioned](aurora-serverless.md#aurora-serverless.modifying.convert "aurora-serverless.md#aurora-serverless.modifying.convert").
2. Upgrade the Aurora Serverless v1 cluster to an Aurora PostgreSQL version 13 version that's compatible with
   Aurora Serverless v2, for example, 13.12. Follow the procedure in [Upgrading the major version](aurora-serverless.md#aurora-serverless.modifying.upgrade "aurora-serverless.md#aurora-serverless.modifying.upgrade").

For compatible versions, see [Aurora Serverless v2 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg"). 3. Add an Aurora Serverless v2 reader DB instance to the cluster. For more information, see [Adding an Aurora Serverless v2 reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader "aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader"). 4. Fail over to the Aurora Serverless v2 DB instance:

    1. Select the writer DB instance of the DB cluster.
    2. For **Actions**, choose **Failover**.
    3. On the confirmation page, choose **Failover**.

For Aurora Serverless v1 DB clusters running Aurora PostgreSQL version 13, you convert the Aurora Serverless v1 cluster to a
provisioned DB cluster, and then convert the provisioned cluster to an Aurora Serverless v2 DB cluster.

###### To upgrade an Aurora Serverless v1 cluster running Aurora PostgreSQL version 13

1. Convert the Aurora Serverless v1 DB cluster to a provisioned Aurora PostgreSQL cluster. Follow the procedure in [Converting from Aurora Serverless v1 to
   provisioned](aurora-serverless.md#aurora-serverless.modifying.convert "aurora-serverless.md#aurora-serverless.modifying.convert").
2. Add an Aurora Serverless v2 reader DB instance to the cluster. For more information, see [Adding an Aurora Serverless v2 reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader "aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader").
3. Fail over to the Aurora Serverless v2 DB instance:
   1. Select the writer DB instance of the DB cluster.
   2. For **Actions**, choose **Failover**.
   3. On the confirmation page, choose **Failover**.

4. Remove the reader instance.

## Migrating from an on-premises database to Aurora Serverless v2

You can migrate your on-premises databases to Aurora Serverless v2, just as with provisioned Aurora MySQL and
Aurora PostgreSQL.

- For MySQL databases, you can use the `mysqldump` command. For more information,
  see [Importing data
  to an Amazon RDS for MySQL database with reduced downtime](../UserGuide/mysql-importing-data-reduced-downtime.md "../UserGuide/mysql-importing-data-reduced-downtime.md") in the _Amazon Relational Database Service User
  Guide_.
- For PostgreSQL databases, you can use the `pg_dump` and `pg_restore` commands. For more
  information, see the blog post [Best practices for migrating PostgreSQL databases to Amazon RDS and Amazon Aurora](https://aws.amazon.com/blogs/database/best-practices-for-migrating-postgresql-databases-to-amazon-rds-and-amazon-aurora/ "https://aws.amazon.com/blogs/database/best-practices-for-migrating-postgresql-databases-to-amazon-rds-and-amazon-aurora/").
