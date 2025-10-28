# Creating your DB cluster

Use the following procedures to create an Aurora PostgreSQL DB cluster that uses Aurora PostgreSQL Limitless Database.

You can use either the AWS Management Console or the AWS CLI to create your DB cluster that uses Aurora PostgreSQL Limitless Database. You create the primary DB cluster and the DB shard
group.

When you use the AWS Management Console to create the primary DB cluster, the DB shard group is also created in the same procedure.

###### To create the DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Create database**.

The **Create database** page displays. 3. For **Engine type**, choose **Aurora (PostgreSQL Compatible)**. 4. For **Version**, choose one of the following:

    * **Aurora PostgreSQL with Limitless Database (Compatible with PostgreSQL 16.4)**
    * **Aurora PostgreSQL with Limitless Database (Compatible with PostgreSQL 16.6)**

5. For **Aurora PostgreSQL Limitless Database**:

![Aurora PostgreSQL Limitless Database console settings with configuration options for sharding and distribution parameters.](images/limitless_create_database.png)

    1. Enter a **DB shard group identifier**.


    ###### Important

    After you create the DB shard group, you can't change the DB cluster identifier or the DB shard group
     identifier.
    2. For **DB shard group capacity range**:


    	1. Enter the **Minimum capacity (ACUs)**. Use a value of at least 16 ACUs.


    	For a development environment, the default value is 16 ACUs. For a production environment, the default value is 24
    	 ACUs.
    	2. Enter the **Maximum capacity (ACUs)**. Use a value of at least 16 ACUs or at most 6144 ACUs.


    	For a development environment, the default value is 64 ACUs. For a production environment, the default value is
    	 384 ACUs.For more information, see [Correlating DB shard group maximum capacity with the number of routers and shards created](limitless-cluster.md#limitless-capacity-mapping "limitless-cluster.md#limitless-capacity-mapping").
    3. For **DB shard group deployment**, choose whether to create standbys for the DB shard group:




    	* **No compute redundancy** – Creates a DB shard group without standbys for each shard. This
    	 is the default value.
    	* **Compute redundancy with a single failover target** – Creates a DB shard group with one
    	 compute standby in a different Availability Zone (AZ).
    	* **Compute redundancy with two failover targets** – Creates a DB shard group with two
    	 compute standbys in two different AZs.
    ###### Note

    If you set the compute redundancy to a nonzero value, the total number of shards DB instances will be doubled or tripled.
     These extra DB instances are compute standbys, scaled up and down to the same capacity as the writer instance.
     You don't set the capacity range separately for the standbys.
     Therefore, ACU usage and bill correspondingly doubles and triples.
     To know the exact ACU usage incurred from compute redundancy, refer to the `DBShardGroupComputeRedundancyCapacity` metric in
     [DBShardGroup metrics](limitless-monitoring.md#limitless-monitoring.cw.DBShardGroup "limitless-monitoring.md#limitless-monitoring.cw.DBShardGroup").
    4. Choose whether to make the DB shard group publicly accessible.


    ###### Note

    You can't modify this setting after you create the DB shard group.

6. For **Connectivity**:
   1. (Optional) Select **Connect to an EC2 compute resource**, then choose an existing EC2 instance or create
      a new one.

   ###### Note

   If you connect to an EC2 instance, you can't make the DB shard group publicly accessible. 2. For **Network type**, choose either **IPv4** or **Dual-stack
   mode**. 3. Choose the **Virtual private cloud (VPC)** and **DB subnet group**, or use the default
   settings.

   ###### Note

   If you create your Limitless Database DB cluster in the US East (N. Virginia) Region, don't include the
   `us-east-1e` Availability Zone (AZ) in your DB subnet group. Because of resource limitations,
   Aurora Serverless v2—and therefore Limitless Database—isn't supported in the `us-east-1e` AZ. 4. Choose the **VPC security group (firewall)**, or use the default setting.

7. For **Database authentication**, choose either **Password authentication** or **Password
   and IAM database authentication**.
8. For **Monitoring**, make sure that the **Turn on Performance Insights** and **Enable Enhanced Monitoring**
   check boxes are selected.

For Performance Insights, choose a retention time of at least 1 month. 9. Expand the last **Additional configuration** on the page. 10. For **Log exports**, make sure that the **PostgreSQL log** check box is selected. 11. Specify other settings as needed. For more information, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings"). 12. Choose **Create database**.
After the primary DB cluster and DB shard group are created, they're displayed on the **Databases** page.

![Aurora PostgreSQL Limitless Database primary DB cluster and DB shard group.](images/limitless_cluster_164.png)
When you use the AWS CLI to create a DB cluster that uses Aurora PostgreSQL Limitless Database, you perform the following tasks:

1. [Create the primary DB cluster](#limitless-create-CLI.cluster "#limitless-create-CLI.cluster").
2. [Create the DB shard group](#limitless-create-CLI.shard-group "#limitless-create-CLI.shard-group").

### Create the primary DB cluster

The following parameters are required to create the DB cluster:

- `--db-cluster-identifier` – The name of your DB cluster.
- `--engine` – The DB cluster must use the `aurora-postgresql` DB engine.
- `--engine-version` – The DB cluster must use one of the DB engine versions:
  - `16.4-limitless`
  - `16.6-limitless`

- `--storage-type` – The DB cluster must use the `aurora-iopt1` DB cluster storage
  configuration.
- `--cluster-scalability-type` – Specifies the scalability mode of the Aurora DB cluster. When set to
  `limitless`, the cluster operates as an Aurora PostgreSQL Limitless Database. When set to `standard` (the default), the cluster
  uses normal DB instance creation.

###### Note

You can't modify this setting after you create the DB cluster.

- `--master-username` – The name of the master user for the DB cluster.
- `--master-user-password` – The password for the master user.
- `--enable-performance-insights` – You must enable Performance Insights.
- `--performance-insights-retention-period` – The Performance Insights retention period must be at least 31 days.
- `--monitoring-interval` – The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the
  DB cluster. This value can't be `0`.
- `--monitoring-role-arn` – The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring
  metrics to Amazon CloudWatch Logs.
- `--enable-cloudwatch-logs-exports` – You must export `postgresql` logs to CloudWatch Logs.

The following parameters are optional:

- `--db-subnet-group-name` – The DB subnet group to associate with the DB cluster. This also determines the
  VPC associated with the DB cluster.

###### Note

If you create your Limitless Database DB cluster in the US East (N. Virginia) Region, don't include the `us-east-1e`
Availability Zone (AZ) in your DB subnet group. Because of resource limitations, Aurora Serverless v2—and therefore
Limitless Database—isn't supported in the `us-east-1e` AZ.

- `--vpc-security-group-ids` – A list of VPC security groups to associate with the DB cluster.
- `--performance-insights-kms-key-id` – The AWS KMS key identifier for encryption of Performance Insights data. If you
  don't specify a KMS key, the default key for your AWS account is used.
- `--region` – The AWS Region where you create the DB cluster. It must be one that supports Aurora PostgreSQL Limitless Database.

To use the default VPC and VPC security group, omit the `--db-subnet-group-name` and `--vpc-security-group-ids`
options.

###### To create the primary DB cluster

- ```
  aws rds create-db-cluster \
      --db-cluster-identifier `my-limitless-cluster` \
      --engine aurora-postgresql \
      --engine-version 16.6-limitless \
      --storage-type aurora-iopt1 \
      --cluster-scalability-type limitless \
      --master-username `myuser` \
      --master-user-password `mypassword` \
      --db-subnet-group-name `mysubnetgroup` \
      --vpc-security-group-ids `sg-c7e5b0d2` \
      --enable-performance-insights \
      --performance-insights-retention-period `31` \
      --monitoring-interval `5` \
      --monitoring-role-arn arn:aws:iam::`123456789012`:role/`EMrole` \
      --enable-cloudwatch-logs-exports postgresql
  ```

````

For more information, see [create-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html").


### Create the DB shard group


Next you create the DB shard group in the DB cluster that you just created. The following parameters are required:



* `--db-shard-group-identifier` – The name of your DB shard group.


The DB shard group identifier has the following constraints:




	+ It must be unique in the AWS account and AWS Region where you create it.
	+ It must contain 1–63 letters, numbers, or hyphens.
	+ The first character must be a letter.
	+ It can't end with a hyphen or contain two consecutive hyphens.
	+ ###### Important

	After you create the DB shard group, you can't change the DB cluster identifier or the DB shard group
	 identifier.
* `--db-cluster-identifier` – The name of the DB cluster in which you're creating the DB shard group.
* `--max-acu` – The maximum capacity of your DB shard group. It must be from 16–6144 ACUs. For capacity limits higher than 6144 ACUs, contact AWS.


The initial number of routers and shards is determined by the maximum capacity that you set when you create the DB shard
 group. The higher the maximum capacity, the greater the number of routers and shards that are created in the DB shard group. For
 more information, see [Correlating DB shard group maximum capacity with the number of routers and shards created](limitless-cluster.md#limitless-capacity-mapping "limitless-cluster.md#limitless-capacity-mapping").

The following parameters are optional:



* `--compute-redundancy` – Whether to create standbys for the DB shard group. This parameter can have the
 following values:




	+ `0` – Creates a DB shard group without standbys for each shard. This is the default value.
	+ `1` – Creates a DB shard group with one compute standby in a different Availability Zone
	 (AZ).
	+ `2` – Creates a DB shard group with two compute standbys in two different AZs.
###### Note

If you set the compute redundancy to a nonzero value, the total number of shards will be doubled or tripled. This will incur extra costs.

The nodes in compute standbys are scaled up and down to the same capacity as the writer. You don't set the capacity range separately for the standbys.
* `--min-acu` – The minimum capacity of your DB shard group. It must be at least 16 ACUs, which is the default
 value.
* `--publicly-accessible|--no-publicly-accessible` – Whether to assign publicly accessible IP addresses to the
 DB shard group. Access to the DB shard group is controlled by the security groups used by the cluster.


The default is `--no-publicly-accessible`.


###### Note

You can't modify this setting after you create the DB shard group.

###### To create the DB shard group

* ```
aws rds create-db-shard-group \
    --db-shard-group-identifier `my-db-shard-group` \
    --db-cluster-identifier my-limitless-cluster \
    --max-acu `1000`
````
