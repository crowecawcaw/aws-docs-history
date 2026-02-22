# Creating a blue/green deployment in Amazon RDS

When you create a blue/green deployment, you specify the source DB instance
to copy in the deployment. The DB instance you choose is the production DB instance, and it
becomes the primary DB instance in the blue environment. This DB instance is copied to the green
environment, and RDS configures replication from the DB instance in the blue environment to the
DB instance in the green environment.

RDS copies the blue environment's topology and features to a staging area. If the blue DB instance
has read replicas, they are copied as replicas of the green instance. The allocated storage of
all green replicas matches the green primary instance, while other storage parameters are
inherited from the blue replicas.

If the blue DB instance is a Multi-AZ DB instance deployment, then the green DB instance
is created as a Multi-AZ DB instance deployment.

###### Topics

- [Preparing for a blue/green
  deployment](#blue-green-deployments-creating-preparing "#blue-green-deployments-creating-preparing")
- [Specifying changes when creating a
  blue/green deployment](#blue-green-deployments-creating-changes "#blue-green-deployments-creating-changes")
- [Lazy loading and storage
  initialization for blue/green deployments](#blue-green-deployments-creating-lazy-loading "#blue-green-deployments-creating-lazy-loading")
- [Creating a blue/green
  deployment](#blue-green-deployments-creating-create "#blue-green-deployments-creating-create")
- [Settings for creating blue/green
  deployments](#create-blue-green-settings "#create-blue-green-settings")

## Preparing for a blue/green

deployment

There are certain steps you must take before you create a blue/green deployment, depending
on the engine that your DB instance is running.

###### Topics

- [Preparing an RDS for MySQL or
  RDS for MariaDB DB instance for a blue/green deployment](#blue-green-deployments-creating-preparing-mysql "#blue-green-deployments-creating-preparing-mysql")
- [Preparing an
  RDS for PostgreSQL DB instance for a blue/green deployment with physical replication](#blue-green-deployments-creating-preparing-postgres-physical "#blue-green-deployments-creating-preparing-postgres-physical")
- [Preparing an
  RDS for PostgreSQL DB instance for a blue/green deployment with logical replication](#blue-green-deployments-creating-preparing-postgres-logical "#blue-green-deployments-creating-preparing-postgres-logical")

### Preparing an RDS for MySQL or

RDS for MariaDB DB instance for a blue/green deployment

Before you create a blue/green deployment for an RDS for MySQL or RDS for MariaDB DB instance, you
must enable automated backups. For instructions, see [Enabling automated
backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

### Preparing an

RDS for PostgreSQL DB instance for a blue/green deployment with physical replication

Before you create an RDS for PostgreSQL blue/green deployment that uses physical
replication, make sure to do the following. For a list of versions that use physical
replication versus logical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

- Enable automated backups on the DB instance. For instructions, see [Enabling automated
  backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").
- Confirm that the DB instance isn't the source or target of external replication. For more
  information, see [General limitations for blue/green
  deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-general "blue-green-deployments-considerations.md#blue-green-deployments-limitations-general").

### Preparing an

RDS for PostgreSQL DB instance for a blue/green deployment with logical replication

Before you create an RDS for PostgreSQL blue/green deployment that uses logical
replication, make sure to do the following. For a list of versions that use logical
replication versus physical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

- Associate the instance with a custom DB parameter group with logical replication
  (`rds.logical_replication`) turned on. Logical replication is required for
  replication from the blue environment to the green environment. For instructions, see
  [Modifying parameters in a DB parameter group
  in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Because blue/green deployments require at least one background worker per database,
make sure to tune the following configuration settings according to your workload. For
instructions to tune each setting, see [Configuration Settings](https://www.postgresql.org/docs/current/logical-replication-config.html "https://www.postgresql.org/docs/current/logical-replication-config.html") in the PostgreSQL documentation.

    + `max_replication_slots`
    + `max_wal_senders`
    + `max_logical_replication_workers`
    + `max_worker_processes`

After you enable logical replication and set all configuration options, make sure to
reboot the DB instance so that your changes take effect. Blue/green deployments
_require_ that the DB instance be in sync with the DB parameter group,
otherwise creation fails. For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

- Confirm that the DB instance isn't the source or target of external replication. For more
  information, see [General limitations for blue/green
  deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-general "blue-green-deployments-considerations.md#blue-green-deployments-limitations-general").
- Make sure that all tables in the DB instance have a primary key. PostgreSQL logical
  replication doesn't allow `UPDATE` or `DELETE` operations on tables
  that don't have a primary key.
- RDS for PostgreSQL uses PostgreSQL's native logical replication, storing write-ahead logs
  (WAL) segments on the blue instance until they're replayed on the green environment.
  Before you create a blue/green deployment, verify that the blue instance has adequate
  capacity by checking the following metrics:

      + `FreeStorageSpace`
      + `TransactionLogsGeneration`
      + `TransactionLogsDiskUsage`
      + `OldestReplicationSlotLag`

  To estimate the additional storage required on the blue instance, monitor the
  `TransactionLogsGeneration` CloudWatch metric during peak workload periods. For
  example, if your workload generates 100 GB of WAL data over 24 hours, ensure you have at
  least 100 GB of extra storage to accommodate one day's worth of WAL segments. For more
  information, see [Monitoring metrics in an Amazon RDS instance](CHAP_Monitoring.md "CHAP_Monitoring.md").

## Specifying changes when creating a

blue/green deployment

You can make the following changes to the DB instance
in the green environment when you create the
blue/green deployment.

You can make other modifications to the DB instance
in the green environment after it
is deployed. For example, you might specify a higher engine version or a different parameter
group.

For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### Topics

- [Specify a higher engine
  version](#blue-green-deployments-engine-version "#blue-green-deployments-engine-version")
- [Specify a different DB parameter
  group](#blue-green-deployments-parameters "#blue-green-deployments-parameters")
- [Modify storage and performance
  settings](#blue-green-deployments-resize "#blue-green-deployments-resize")
- [Enable RDS Optimized Writes](#blue-green-deployments-db-instance "#blue-green-deployments-db-instance")
- [Upgrade the storage configuration](#blue-green-deployments-storage "#blue-green-deployments-storage")

### Specify a higher engine

version

You can specify a higher engine version if you want to test a DB engine upgrade. Upon
switchover, the database is upgraded to the major or minor DB engine version that you
specify.

### Specify a different DB parameter

group

You can test how parameter changes affect the DB instances in the
green environment or specify a parameter group for a new major DB engine version in the case
of an upgrade.

If you specify a different DB parameter group, the specified DB
parameter group is associated with all of the DB instances in the green environment. If you
don't specify a different parameter group, each DB instance in the green environment is
associated with the parameter group of its corresponding blue DB instance.

### Modify storage and performance

settings

Adjust storage and performance settings in the green environment to optimize resource
allocation. These settings include allocated storage, provisioned IOPS, storage type, and
storage throughput (for gp3 storage).

You can change the storage type of the green DB instance to gp2, gp3, io1, or io2. For gp3
storage, you can also adjust storage throughput to enhance data transfer performance for
high-demand workloads, or to reduce costs for less intensive applications. For more
information, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

You can also choose to increase or decrease allocated storage in the green environment.
However, a storage reduction only occurs if the target allocated storage is at least 20%
more than the current storage usage. If you decrease the allocated storage, Amazon RDS initiates
a storage configuration upgrade. For more information, see [Upgrade the storage configuration](#blue-green-deployments-storage "#blue-green-deployments-storage"). The minimum target storage is calculated as:

```
Minimum Target Storage = Total Allocated Storage × Current Apparent Utilization × 1.2
```

1. Total Allocated Storage: The storage capacity provisioned for your DB instance, visible in the RDS console.
2. Current Apparent Utilization: The percentage of allocated storage in use. To estimate it, use the `os.fileSys.usedPercent` metric from Performance Insights (Database Insights) or Enhanced Monitoring.

###### Note

Since storage utilization fluctuates over time, we recommend setting the target storage slightly above the calculated minimum to account for potential increases during the reduction process.

If the blue DB instance uses magnetic storage, you must change the green DB instance to a General
Purpose or Provisioned IOPS storage type in order to increase or decrease the allocated
storage.

### Enable RDS Optimized Writes

You can use a blue/green deployment to upgrade to a DB instance class that supports RDS Optimized Writes. You
can only enable RDS Optimized Writes on a database that was _created_ with
a supported DB instance class. Thus, this option creates a green database that uses a supported
DB instance class, which enables you to turn on RDS Optimized Writes on the green DB instance.

If you're upgrading from a DB instance class that doesn't support RDS Optimized Writes
to one that does, you must also upgrade the storage configuration of the green DB instance. For
more information, see [Upgrade the storage configuration](#blue-green-deployments-storage "#blue-green-deployments-storage").

You can only upgrade the DB instance class of the _primary_ green DB instance. By
default, read replicas in the green environment inherit the DB instance settings from the blue
environment. After the green environment is successfully created, you must manually modify
the DB instance class of the read replicas in the green environment.

Some instance class upgrades aren't supported depending on the engine version and
instance class of the blue DB instance. For more information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

### Upgrade the storage configuration

If your blue database isn't on the latest storage configuration, RDS can migrate the
green DB instance from the older storage configuration (32-bit file system) to the preferred
configuration. You can use RDS Blue/Green Deployments to overcome the scaling limitations on
storage and file size for older 32-bit file systems. In addition, this setting changes the
storage configuration to be compatible with RDS Optimized Writes if the specified DB instance class supports
Optimized Writes.

###### Note

Upgrading the storage configuration is an I/O-intensive operation and leads to longer
creation times for blue/green deployments. The storage upgrade process is faster if the
blue DB instance uses Provisioned IOPS SSD (io1 or io2 Block Express) storage, and if you
provisoned the green environment with an instance size of 4xlarge or larger. Storage
upgrades involving General Purpose SSD (gp2) storage can deplete your I/O credit balance,
resulting in longer upgrade times. For more information, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

During the storage upgrade, the green DB instance is temporarily unavailable, while the blue
DB instance remains available. Replication pauses during this time. Monitor storage on the blue
instance, and consider scaling if storage reaches 90%, as the green instance automatically
scales by 10% after the upgrade.

This option is only available if your blue database is _not_ on the
latest storage configuration, or if you're changing the DB instance class within the same request.
You can only upgrade the storage configuration when initially creating a blue/green
deployment.

## Lazy loading and storage

initialization for blue/green deployments

When you create a blue/green deployment, Amazon RDS creates the primary DB instance in the green
environment by restoring from a DB snapshot. After it's created, the green DB instance and its read
replicas continue to load data in the background through a process known as _lazy loading_.

Lazy loading only loads data blocks as applications request them. If you attempt to access
data that hasn't been loaded yet, Amazon EBS immediately retrieves it from Amazon S3, while remaining
data continues to load in the background. For more information, see [Amazon EBS
snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md").

To accelerate full volume performance, Amazon RDS provides storage initialization, which reads
all blocks in the green environment volume. Amazon EBS proactively downloads blocks from Amazon S3,
providing maximum volume performance from the first use. Storage initialization occurs
entirely in the background, ensuring no impact on your DB instance availability or ongoing
activities, such as patching or upgrades.

Storage initialization is available only for instances in blue/green deployments with
`gp2`, `gp3`, `io1`, and `io2` volume types. It
supports all instance classes except the t3 and t4 families. If you modify a green DB instance in a
Single-AZ deployment to a Multi-AZ DB instance deployment, storage initialization includes the
secondary node in the Multi-AZ configuration.

During storage initialization, the instance remains fully available and usable for
database operations, though storage might not reach full performance until initialization
completes. While the storage initialization is underway, the overall instance status changes
to **Storage-initialization**, and the progress indicator
reflects the minimum initialization level across all volumes of the DB instance.

Use the console, AWS CLI, or Amazon RDS API to monitor storage initialization.

Console In the AWS Management Console, you see the progress of storage initialization with the DB instance
status.

![Storage initialization progress indicator for a blue/green deployment](images/storage-initialization-bg.png)

AWS CLIWith the AWS CLI, you can monitor storage initialization with the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
command. The `PercentProgress` field in the response shows what percentage of
data has been retrieved from Amazon S3.

```
aws rds describe-db-instances --db-instance-identifier my-db-instance

{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "my-db-instance",
            "DBInstanceClass": "db.m5.2xlarge",
            "Engine": "postgres",
            "DBInstanceStatus": "**storage-initialization**",
            ...
            "PercentProgress": "**34**"
        }
    ]
}
```

Amazon RDS API With the Amazon RDS API, you retrieve the status of storage initialization by calling the [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md")
action.

The progress indicator updates as the background initialization job advances, allowing you
to track storage readiness before full storage initialization completes. Storage
initialization enables optimized performance as your green DB instance becomes fully
operational.

## Creating a blue/green

deployment

You can create a blue/green deployment using the AWS Management Console, the AWS CLI, or the RDS
API.

###### To create a blue/green deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB
   instance
   that you want to copy to a green environment.
3. Choose **Actions**, **Create blue/green
   deployment**.

The **Create blue/green deployment** page appears.

![Create blue/green deployment](images/blue-green-deployment-create.png) 4. Review the blue database identifiers. Make sure that they match the DB instances that
you expect in the blue environment. If they don't, choose
**Cancel**. 5. For **Blue/green deployment name**, enter a name for your
blue/green deployment. 6. In the remaining sections, specify the settings for the green environment. For
information about each setting, see [Settings for creating blue/green
deployments](#create-blue-green-settings "#create-blue-green-settings").

You can make other modifications to the databases in the green environment after it is deployed. 7. Choose **Create**.
To create a blue/green deployment using the AWS CLI, use the [create-blue-green-deployment](../../../cli/latest/reference/rds/create-blue-green-deployment.md "../../../cli/latest/reference/rds/create-blue-green-deployment.md") command. For information about all available
options, see [Settings for creating blue/green
deployments](#create-blue-green-settings "#create-blue-green-settings").

###### Example

For Linux, macOS, or Unix:

```
aws rds create-blue-green-deployment \
    --blue-green-deployment-name `my-blue-green-deployment` \
    --source arn:aws:rds:`us-east-2`:`123456789012`:db:`mydb1` \
    --target-engine-version `8.0.31` \
    --target-db-parameter-group-name `mydbparametergroup`
```

For Windows:

```
aws rds create-blue-green-deployment ^
    --blue-green-deployment-name `my-blue-green-deployment` ^
    --source arn:aws:rds:`us-east-2`:`123456789012`:db:`mydb1` ^
    --target-engine-version `8.0.31` ^
    --target-db-parameter-group-name `mydbparametergroup`
```

To create a blue/green deployment by using the Amazon RDS API, use the [`CreateBlueGreenDeployment`](../APIReference/API_CreateBlueGreenDeployment.md "../APIReference/API_CreateBlueGreenDeployment.md") operation. For information about each
option, see [Settings for creating blue/green
deployments](#create-blue-green-settings "#create-blue-green-settings").

## Settings for creating blue/green

deployments

The following table explains the settings that you can choose when you create a
blue/green deployment. For more information about the AWS CLI options, see [create-blue-green-deployment](../../../cli/latest/reference/rds/create-blue-green-deployment.md "../../../cli/latest/reference/rds/create-blue-green-deployment.md"). For more information about the RDS API parameters,
see [CreateBlueGreenDeployment](../APIReference/API_CreateBlueGreenDeployment.md "../APIReference/API_CreateBlueGreenDeployment.md").

| Console setting                                | Setting description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | CLI option and RDS API parameter                                                                                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Allocated storage**                          | The amount of storage to allocate for your green DB instance (in gibibytes). You can<br>choose to increase or decrease the allocated storage.<br>If your blue DB instance uses magnetic (`standard`) storage, you must<br>change the green DB instance to a General Purpose or Provisioned IOPS storage type in<br>order to modify the allocated storage in the green environment.<br>For more information, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").                                                                                                                                                                                                                 | **CLI option:**<br>`--target-allocated-storage`<br>**API parameter:**<br>`TargetAllocatedStorage`                                                                                                |
| **Blue/Green Deployment identifier**           | A name for the blue/green deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **CLI option:**<br>`--blue-green-deployment-name`<br>**API parameter:**<br>`BlueGreenDeploymentName`                                                                                             |
| **Blue database identifier**                   | The identifier of the instance<br>that you want to copy to the green<br>environment. When using the CLI or API, specify the instance<br>Amazon Resource Name (ARN).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **CLI option:**<br>`--source`<br>**API parameter:**<br>`Source`                                                                                                                                  |
| **DB parameter group for green databases**     | A parameter group to associate with the databases in the green<br>environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **CLI option:**<br>`--target-db-parameter-group-name`<br>`--target-db-cluster-parameter-group-name`<br>**API parameter:**<br>`TargetDBParameterGroupName`<br>`TargetDBClusterParameterGroupName` |
| **Enable Optimized Writes for green database** | Enable RDS Optimized Writes on the green primary DB instance. For more information, see [Enable RDS Optimized Writes](#blue-green-deployments-db-instance "#blue-green-deployments-db-instance").<br>If you're changing from a DB instance class that doesn't support Optimized Writes to<br>one that does, you also need to perform a storage configuration upgrade. For more<br>information, see [Upgrade the storage configuration](#blue-green-deployments-storage "#blue-green-deployments-storage").                                                                                                                                                                                           | For the CLI and API, specifying a target DB instance class that supports RDS Optimized Writes<br>automatically enables it on the green primary DB instance.                                      |
| **Engine version for green databases**         | Upgrade the databases<br>in the green environment to the<br>specified DB engine version.<br>If not specified, each<br>database in the green<br>environment is created with the same engine version as the corresponding DB instance in<br>the blue environment.<br>If you choose an RDS for PostgreSQL DB instance that uses logical replication,<br>review and acknowledge the logical replication limitations. For more information,<br>see [Logical replication-specific<br>limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres "blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres"). | **CLI option:**<br>`--target-engine-version`<br>**RDS API parameter:**<br>`TargetEngineVersion`                                                                                                  |
| **Green DB instance class**                    | The compute and memory capacity of each DB instance in the green environment, for<br>example `db.m5d.xlarge`.<br>This option is only visible when you enable RDS Optimized Writes for the green database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **CLI option:**<br>`--target-db-instance-class`<br>**RDS API parameter:**<br>`TargetDBInstanceClass`                                                                                             |
| **Provisioned IOPS**                           | The amount of provisioned input/output operations per second (IOPS) to be<br>initially allocated for the green database.<br>This value applies only to the green primary DB instance, not green replicas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **CLI option:**<br>`--target-iops`<br>**RDS API parameter:**<br>`TargetIops`                                                                                                                     |
| **Storage configuration upgrade**              | Choose whether to upgrade your storage file system configuration. If you enable<br>this setting, RDS migrates the green database from the old storage file system to<br>the preferred configuration.<br>This option is only available if your blue database is _not_<br>on the latest storage configuration, or if you're enabling RDS Optimized Writes within the same<br>request. You can only upgrade the storage configuration when initially creating a<br>blue/green deployment.<br>For more information, see [Upgrading the storage file system for a DB<br>instance](USER_PIOPS.md "USER_PIOPS.md").                                                                                         | **CLI option:**<br>`--upgrade-target-storage-config`<br>**RDS API parameter:**<br>`UpgradeTargetStorageConfig`                                                                                   |
| **Storage throughput**                         | The storage throughput value for the green database. This setting is visible<br>only if you choose General Purpose SSD (gp3) for the storage type.<br>This value applies only to the green primary DB instance, not green replicas.<br>For more information, see [gp3 storage (recommended)](CHAP_Storage.md#gp3-storage "CHAP_Storage.md#gp3-storage").                                                                                                                                                                                                                                                                                                                                             | **CLI option:**<br>`--target-storage-throughput`<br>**RDS API parameter:**<br>`TargetStorageThroughput`                                                                                          |
| **Storage type**                               | The storage type for the green database. The following storage types are<br>supported:<br>• General Purpose SSD (gp2)<br>• General Purpose SSD (gp3)<br>• Provisioned IOPS (io1)<br>• Provisioned IOPS SSD (io2)<br>This value applies only to the green primary DB instance, not green replicas.<br>For more information, see [Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage "CHAP_Storage.md#Concepts.Storage").                                                                                                                                                                                                                                                                      | **CLI option:**<br>`--target-storage-type`<br>**RDS API parameter:**<br>`TargetStorageType`                                                                                                      |
