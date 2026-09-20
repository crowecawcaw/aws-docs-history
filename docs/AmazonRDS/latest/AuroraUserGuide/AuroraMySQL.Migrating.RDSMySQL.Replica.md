

# Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster by using an Aurora read replica
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica"></a>

Aurora uses the MySQL DB engines' binary log replication functionality to create a special type of DB cluster called an Aurora read replica for a source RDS for MySQL DB instance. Updates made to the source RDS for MySQL DB instance are asynchronously replicated to the Aurora read replica.

We recommend using this functionality to migrate from a RDS for MySQL DB instance to an Aurora MySQL DB cluster by creating an Aurora read replica of your source RDS for MySQL DB instance. When the replica lag between the RDS for MySQL DB instance and the Aurora read replica is 0, you can direct your client applications to the Aurora read replica and then stop replication to make the Aurora read replica a standalone Aurora MySQL DB cluster. Be prepared for migration to take a while, roughly several hours per tebibyte (TiB) of data.

For a list of regions where Aurora is available, see [Amazon Aurora](https://docs.aws.amazon.com/general/latest/gr/rande.html#aurora) in the *AWS General Reference*.

When you create an Aurora read replica of an RDS for MySQL DB instance, Amazon RDS creates a DB snapshot of your source RDS for MySQL DB instance (private to Amazon RDS, and incurring no charges). Amazon RDS then migrates the data from the DB snapshot to the Aurora read replica. After the data from the DB snapshot has been migrated to the new Aurora MySQL DB cluster, Amazon RDS starts replication between your RDS for MySQL DB instance and the Aurora MySQL DB cluster. If your RDS for MySQL DB instance contains tables that use storage engines other than InnoDB, or that use compressed row format, you can speed up the process of creating an Aurora read replica by altering those tables to use the InnoDB storage engine and dynamic row format before you create your Aurora read replica. For more information about the process of copying a MySQL DB snapshot to an Aurora MySQL DB cluster, see [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster](AuroraMySQL.Migrating.RDSMySQL.md).

You can have only one Aurora read replica for an RDS for MySQL DB instance.

**Note**  
Replication issues can arise due to feature differences between Aurora MySQL and the MySQL database engine version of your RDS for MySQL DB instance that is the replication primary. If you encounter an error, you can find help in the [Amazon RDS community forum](https://forums.aws.amazon.com/forum.jspa?forumID=60) or by contacting AWS Support.  
You can't create an Aurora read replica if your RDS for MySQL DB instance is already the source for a cross-Region read replica.  
You can't migrate to Aurora MySQL version 3.05 and higher from some older RDS for MySQL 8.0 versions, including 8.0.11, 8.0.13, and 8.0.15. We recommend that you upgrade to RDS for MySQL version 8.0.28 before migrating.

For more information on MySQL read replicas, see [ Working with read replicas of MariaDB, MySQL, and PostgreSQL DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

## Creating an Aurora read replica
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Create"></a>

You can create an Aurora read replica for an RDS for MySQL DB instance by using the console, the AWS CLI, or the RDS API.

### Console
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Create.Console"></a>

**To create an Aurora read replica from a source RDS for MySQL DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**. 

1. Choose the MySQL DB instance that you want to use as the source for your Aurora read replica.

1. For **Actions**, choose **Create Aurora read replica**.

1. Choose the DB cluster specifications you want to use for the Aurora read replica, as described in the following table. 

<a name="aurora_read_replica_param_advice"></a>
<table>
<thead>
  <tr><th>Option</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>DB instance class</b> </td><td>Choose a DB instance class that defines the processing and memory requirements for the primary instance in the DB cluster. For more information about DB instance class options, see <a href="Concepts.DBInstanceClass.md">Amazon AuroraDB instance classes</a>.</td></tr>
  <tr><td> <b>Multi-AZ deployment</b> </td><td>Choose <b>Create Replica in Different Zone</b> to create a standby replica of the new DB cluster in another Availability Zone in the target AWS Region for failover support. For more information about multiple Availability Zones, see <a href="Concepts.RegionsAndAvailabilityZones.md">Regions and Availability Zones</a>. </td></tr>
  <tr><td> <b>DB instance identifier</b> </td><td>Type a name for the primary instance in your Aurora read replica DB cluster. This identifier is used in the endpoint address for the primary instance of the new DB cluster. <br />The DB instance identifier has the following constraints: <ul><li> It must contain from 1 to 63 alphanumeric characters or hyphens. </li><li> Its first character must be a letter. </li><li> It cannot end with a hyphen or contain two consecutive hyphens. </li><li> It must be unique for all DB instances for each AWS account, for each AWS Region. </li></ul><br />Because the Aurora read replica DB cluster is created from a snapshot of the source DB instance, the master user name and master password for the Aurora read replica are the same as the master user name and master password for the source DB instance.</td></tr>
  <tr><td> <b>Virtual Private Cloud (VPC)</b> </td><td>Select the VPC to host the DB cluster. Select <b>Create new VPC</b> to have Aurora create a VPC for you. For more information, see <a href="Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites">DB cluster prerequisites</a>.</td></tr>
  <tr><td> <b>DB subnet group</b> </td><td>Select the DB subnet group to use for the DB cluster. Select <b>Create new DB subnet group</b> to have Aurora create a DB subnet group for you. For more information, see <a href="Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites">DB cluster prerequisites</a>.</td></tr>
  <tr><td> <b>Public accessibility</b> </td><td>Select <code>Yes</code> to give the DB cluster a public IP address; otherwise, select <code>No</code>. The instances in your DB cluster can be a mix of both public and private DB instances. For more information about hiding instances from public access, see <a href="USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Hiding">Hiding a DB cluster in a VPC from the internet</a>.</td></tr>
  <tr><td> <b>Availability zone</b> </td><td>Determine if you want to specify a particular Availability Zone. For more information about Availability Zones, see <a href="Concepts.RegionsAndAvailabilityZones.md">Regions and Availability Zones</a>.</td></tr>
  <tr><td> <b>VPC security group (firewall)</b> </td><td>Select <b>Create new VPC security group</b> to have Aurora create a VPC security group for you. Select <b>Select existing VPC security groups</b> to specify one or more VPC security groups to secure network access to the DB cluster. For more information, see <a href="Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites">DB cluster prerequisites</a>.</td></tr>
  <tr><td> <b>Database port</b> </td><td>Specify the port for applications and utilities to use to access the database. Aurora MySQL DB clusters default to the default MySQL port, 3306. Firewalls at some companies block connections to this port. If your company firewall blocks the default port, choose another port for the new DB cluster.</td></tr>
  <tr><td> <b>DB parameter group</b> </td><td>Select a DB parameter group for the Aurora MySQL DB cluster. Aurora has a default DB parameter group you can use, or you can create your own DB parameter group. For more information about DB parameter groups, see <a href="USER_WorkingWithParamGroups.md">Parameter groups for Amazon Aurora</a>.</td></tr>
  <tr><td> <b>DB cluster parameter group</b> </td><td>Select a DB cluster parameter group for the Aurora MySQL DB cluster. Aurora has a default DB cluster parameter group you can use, or you can create your own DB cluster parameter group. For more information about DB cluster parameter groups, see <a href="USER_WorkingWithParamGroups.md">Parameter groups for Amazon Aurora</a>.</td></tr>
  <tr><td> <b>Encryption</b> </td><td>Choose <b>Disable encryption</b> if you don't want your new Aurora DB cluster to be encrypted. Choose <b>Enable encryption</b> for your new Aurora DB cluster to be encrypted at rest. If you choose <b>Enable encryption</b>, you must choose a KMS key as the <b>AWS KMS key</b> value.<br />If your MySQL DB instance isn't encrypted, specify an encryption key to have your DB cluster encrypted at rest.<br />If your MySQL DB instance is encrypted, specify an encryption key to have your DB cluster encrypted at rest using the specified encryption key. You can specify the encryption key used by the MySQL DB instance or a different key. You can't create an unencrypted DB cluster from an encrypted MySQL DB instance.</td></tr>
  <tr><td> <b>Priority</b> </td><td>Choose a failover priority for the DB cluster. If you don't select a value, the default is <b>tier-1</b>. This priority determines the order in which Aurora Replicas are promoted when recovering from a primary instance failure. For more information, see <a href="Concepts.AuroraHighAvailability.md#Aurora.Managing.FaultTolerance">Fault tolerance for an Aurora DB cluster</a>.</td></tr>
  <tr><td> <b>Backup retention period</b> </td><td>Select the length of time, from 1 to 35 days, that Aurora retains backup copies of the database. Backup copies can be used for point-in-time restores (PITR) of your database down to the second.</td></tr>
  <tr><td><b>Enhanced Monitoring</b></td><td>Choose <b>Enable enhanced monitoring</b> to enable gathering metrics in real time for the operating system that your DB cluster runs on. For more information, see <a href="USER_Monitoring.OS.md">Monitoring OS metrics with Enhanced Monitoring</a>. </td></tr>
  <tr><td><b>Monitoring Role</b></td><td>Only available if <b>Enhanced Monitoring</b> is set to <b>Enable enhanced monitoring</b>. Choose the IAM role that you created to permit Aurora to communicate with Amazon CloudWatch Logs for you, or choose <b>Default</b> to have Aurora create a role for you named <code>rds-monitoring-role</code>. For more information, see <a href="USER_Monitoring.OS.md">Monitoring OS metrics with Enhanced Monitoring</a>. </td></tr>
  <tr><td><b>Granularity</b></td><td>Only available if <b>Enhanced Monitoring</b> is set to <b>Enable enhanced monitoring</b>. Set the interval, in seconds, between when metrics are collected for your DB cluster.</td></tr>
  <tr><td> <b>Auto minor version upgrade</b> </td><td>This setting doesn't apply to Aurora MySQL DB clusters.<br />For more information about engine updates for Aurora MySQL, see <a href="AuroraMySQL.Updates.md">Database engine updates for Amazon Aurora MySQL</a>.</td></tr>
  <tr><td> <b>Maintenance window</b> </td><td>Select <b>Select window</b> and specify the weekly time range during which system maintenance can occur. Or, select <b>No preference</b> for Aurora to assign a period randomly.</td></tr>
</tbody>
</table>


1. Choose **Create read replica**.

### AWS CLI
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Create.CLI"></a>

To create an Aurora read replica from a source RDS for MySQL DB instance, use the [`create-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) and [`create-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI commands to create a new Aurora MySQL DB cluster. When you call the `create-db-cluster` command, include the `--replication-source-identifier` parameter to identify the Amazon Resource Name (ARN) for the source MySQL DB instance. For more information about Amazon RDS ARNs, see [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-rds).

Don't specify the master username, master password, or database name as the Aurora read replica uses the same master username, master password, and database name as the source MySQL DB instance. 

For Linux, macOS, or Unix:

```
aws rds create-db-cluster --db-cluster-identifier sample-replica-cluster --engine aurora \
    --db-subnet-group-name mysubnetgroup --vpc-security-group-ids sg-c7e5b0d2 \
    --replication-source-identifier arn:aws:rds:us-west-2:123456789012:db:primary-mysql-instance
```

For Windows:

```
aws rds create-db-cluster --db-cluster-identifier sample-replica-cluster --engine aurora ^
    --db-subnet-group-name mysubnetgroup --vpc-security-group-ids sg-c7e5b0d2 ^
    --replication-source-identifier arn:aws:rds:us-west-2:123456789012:db:primary-mysql-instance
```

If you use the console to create an Aurora read replica, then Aurora automatically creates the primary instance for your DB cluster Aurora read replica. If you use the AWS CLI to create an Aurora read replica, you must explicitly create the primary instance for your DB cluster. The primary instance is the first instance that is created in a DB cluster.

You can create a primary instance for your DB cluster by using the [`create-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command with the following parameters.
+ `--db-cluster-identifier`

  The name of your DB cluster.
+ `--db-instance-class`

  The name of the DB instance class to use for your primary instance.
+ `--db-instance-identifier`

  The name of your primary instance.
+ `--engine aurora`

In this example, you create a primary instance named {{myreadreplicainstance}} for the DB cluster named {{myreadreplicacluster}}, using the DB instance class specified in {{myinstanceclass}}.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds create-db-instance \
    --db-cluster-identifier {{myreadreplicacluster}} \
    --db-instance-class {{myinstanceclass}} \
    --db-instance-identifier {{myreadreplicainstance}} \
    --engine aurora
```
For Windows:  

```
aws rds create-db-instance ^
    --db-cluster-identifier {{myreadreplicacluster}} ^
    --db-instance-class {{myinstanceclass}} ^
    --db-instance-identifier {{myreadreplicainstance}} ^
    --engine aurora
```

### RDS API
<a name="Aurora.Migration.RDSMySQL.Create.API"></a>

To create an Aurora read replica from a source RDS for MySQL DB instance, use the [`CreateDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) and [`CreateDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) Amazon RDS API commands to create a new Aurora DB cluster and primary instance. Do not specify the master username, master password, or database name as the Aurora read replica uses the same master username, master password, and database name as the source RDS for MySQL DB instance. 

You can create a new Aurora DB cluster for an Aurora read replica from a source RDS for MySQL DB instance by using the [`CreateDBCluster`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) Amazon RDS API command with the following parameters:
+ `DBClusterIdentifier`

  The name of the DB cluster to create.
+ `DBSubnetGroupName`

  The name of the DB subnet group to associate with this DB cluster.
+ `Engine=aurora`
+ `KmsKeyId`

  The AWS KMS key to optionally encrypt the DB cluster with, depending on whether your MySQL DB instance is encrypted.
  + If your MySQL DB instance isn't encrypted, specify an encryption key to have your DB cluster encrypted at rest. Otherwise, your DB cluster is encrypted at rest using the default encryption key for your account.
  + If your MySQL DB instance is encrypted, specify an encryption key to have your DB cluster encrypted at rest using the specified encryption key. Otherwise, your DB cluster is encrypted at rest using the encryption key for the MySQL DB instance.
**Note**  
You can't create an unencrypted DB cluster from an encrypted MySQL DB instance.
+ `ReplicationSourceIdentifier`

  The Amazon Resource Name (ARN) for the source MySQL DB instance. For more information about Amazon RDS ARNs, see [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-rds). 
+ `VpcSecurityGroupIds`

  The list of EC2 VPC security groups to associate with this DB cluster.

In this example, you create a DB cluster named {{myreadreplicacluster}} from a source MySQL DB instance with an ARN set to {{mysqlprimaryARN}}, associated with a DB subnet group named {{mysubnetgroup}} and a VPC security group named {{mysecuritygroup}}.

**Example**  

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CreateDBCluster
    &DBClusterIdentifier={{myreadreplicacluster}}
    &DBSubnetGroupName={{mysubnetgroup}}
    &Engine=aurora
    &ReplicationSourceIdentifier={{mysqlprimaryARN}}
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &VpcSecurityGroupIds={{mysecuritygroup}}
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20150927/us-east-1/rds/aws4_request
    &X-Amz-Date=20150927T164851Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=6a8f4bd6a98f649c75ea04a6b3929ecc75ac09739588391cd7250f5280e716db
```

If you use the console to create an Aurora read replica, then Aurora automatically creates the primary instance for your DB cluster Aurora read replica. If you use the AWS CLI to create an Aurora read replica, you must explicitly create the primary instance for your DB cluster. The primary instance is the first instance that is created in a DB cluster.

You can create a primary instance for your DB cluster by using the [`CreateDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) Amazon RDS API command with the following parameters:
+ `DBClusterIdentifier`

  The name of your DB cluster.
+ `DBInstanceClass`

  The name of the DB instance class to use for your primary instance.
+ `DBInstanceIdentifier`

  The name of your primary instance.
+ `Engine=aurora`

In this example, you create a primary instance named {{myreadreplicainstance}} for the DB cluster named {{myreadreplicacluster}}, using the DB instance class specified in {{myinstanceclass}}.

**Example**  

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CreateDBInstance
    &DBClusterIdentifier={{myreadreplicacluster}}
    &DBInstanceClass={{myinstanceclass}}
    &DBInstanceIdentifier={{myreadreplicainstance}}
    &Engine=aurora
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-09-01
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140424/us-east-1/rds/aws4_request
    &X-Amz-Date=20140424T194844Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=bee4aabc750bf7dad0cd9e22b952bd6089d91e2a16592c2293e532eeaab8bc77
```

## Viewing an Aurora read replica
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.View"></a>

You can view the MySQL to Aurora MySQL replication relationships for your Aurora MySQL DB clusters by using the AWS Management Console or the AWS CLI.

### Console
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.View.Console"></a>

**To view the primary MySQL DB instance for an Aurora read replica**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**. 

1. Choose the DB cluster for the Aurora read replica to display its details. The primary MySQL DB instance information is in the **Replication source** field.  
![View MySQL primary.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-repl6.png)

### AWS CLI
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.View.CLI"></a>

To view the MySQL to Aurora MySQL replication relationships for your Aurora MySQL DB clusters by using the AWS CLI, use the [`describe-db-clusters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) and [`describe-db-instances`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) commands. 

To determine which MySQL DB instance is the primary, use the [`describe-db-clusters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) and specify the cluster identifier of the Aurora read replica for the `--db-cluster-identifier` option. Refer to the `ReplicationSourceIdentifier` element in the output for the ARN of the DB instance that is the replication primary. 

To determine which DB cluster is the Aurora read replica, use the [`describe-db-instances`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) and specify the instance identifier of the MySQL DB instance for the `--db-instance-identifier` option. Refer to the `ReadReplicaDBClusterIdentifiers` element in the output for the DB cluster identifier of the Aurora read replica. 

**Example**  
For Linux, macOS, or Unix:  

```
aws rds describe-db-clusters \
    --db-cluster-identifier {{myreadreplicacluster}}
```

```
aws rds describe-db-instances \
    --db-instance-identifier {{mysqlprimary}}
```
For Windows:  

```
aws rds describe-db-clusters ^
    --db-cluster-identifier {{myreadreplicacluster}}
```

```
aws rds describe-db-instances ^
    --db-instance-identifier {{mysqlprimary}}
```

## Promoting an Aurora read replica
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Promote"></a>

After migration completes, you can promote the Aurora read replica to a stand-alone DB cluster using the AWS Management Console or AWS CLI.

Then you can direct your client applications to the endpoint for the Aurora read replica. For more information on the Aurora endpoints, see [Amazon Aurora endpoint connections](Aurora.Overview.Endpoints.md). Promotion should complete fairly quickly, and you can read from and write to the Aurora read replica during promotion. However, you can't delete the primary MySQL DB instance or unlink the DB Instance and the Aurora read replica during this time.

Before you promote your Aurora read replica, stop any transactions from being written to the source MySQL DB instance, and then wait for the replica lag on the Aurora read replica to reach 0. You can view the replica lag for an Aurora read replica by calling the `SHOW SLAVE STATUS` (Aurora MySQL version 2) or `SHOW REPLICA STATUS` (Aurora MySQL version 3) command on your Aurora read replica. Check the **Seconds behind master** value. 

You can start writing to the Aurora read replica after write transactions to the primary have stopped and replica lag is 0. If you write to the Aurora read replica before this and you modify tables that are also being modified on the MySQL primary, you risk breaking replication to Aurora. If this happens, you must delete and recreate your Aurora read replica.

### Console
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Promote.Console"></a>

**To promote an Aurora read replica to an Aurora DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the DB cluster for the Aurora read replica.

1. For **Actions**, choose **Promote**.

1. Choose **Promote read replica**.

After you promote, confirm that the promotion has completed by using the following procedure.

**To confirm that the Aurora read replica was promoted**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Events**.

1. On the **Events** page, verify that there is a `Promoted Read Replica cluster to a stand-alone database cluster` event for the cluster that you promoted.

After promotion is complete, the primary MySQL DB instance and the Aurora read replica are unlinked, and you can safely delete the DB instance if you want.

### AWS CLI
<a name="AuroraMySQL.Migrating.RDSMySQL.Replica.Promote.CLI"></a>

To promote an Aurora read replica to a stand-alone DB cluster, use the [`promote-read-replica-db-cluster`](https://docs.aws.amazon.com/cli/latest/reference/rds/promote-read-replica-db-cluster.html) AWS CLI command. 

**Example**  
For Linux, macOS, or Unix:  

```
aws rds promote-read-replica-db-cluster \
    --db-cluster-identifier {{myreadreplicacluster}}
```
For Windows:  

```
aws rds promote-read-replica-db-cluster ^
    --db-cluster-identifier {{myreadreplicacluster}}
```