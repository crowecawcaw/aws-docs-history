# Adding a DB shard group to an existing Aurora PostgreSQL Limitless Database DB cluster

You can create a DB shard group in an existing DB cluster, for example if you're restoring a DB cluster or you had deleted the DB shard
group.

For more information on primary DB cluster and DB shard group requirements, see [Aurora PostgreSQL Limitless Database requirements and considerations](limitless-reqs-limits.md "limitless-reqs-limits.md").

###### Note

You can have only one DB shard group per cluster.

The Limitless Database DB cluster must be in the `available` state before you can create a DB shard group.

You can use the AWS Management Console to add a DB shard group to an existing DB cluster.

###### To add a DB shard group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Navigate to the **Databases** page.
3. Select the Limitless Database DB cluster to which you want to add a DB shard group.
4. For **Actions**, choose **Add a DB shard group**.

![Add a DB shard group.](images/limitless_add_shard_group.png) 5. Enter a **DB shard group identifier**.

###### Important

After you create the DB shard group, you can't change the DB cluster identifier or the DB shard group identifier. 6. Enter the **Minimum capacity (ACUs)**. Use a value of at least 16 ACUs. 7. Enter the **Maximum capacity (ACUs)**. Use a value from 16–6144 ACUs.

For more information, see [Correlating DB shard group maximum capacity with the number of routers and shards created](limitless-cluster.md#limitless-capacity-mapping "limitless-cluster.md#limitless-capacity-mapping"). 8. For **DB shard group deployment**, choose whether to create standbys for the DB shard group:

    * **No compute redundancy** – Creates a DB shard group without standbys for each shard. This is the
     default value.
    * **Compute redundancy with a single failover target** – Creates a DB shard group with one compute
     standby in a different Availability Zone (AZ).
    * **Compute redundancy with two failover targets** – Creates a DB shard group with two compute
     standbys in two different AZs.

9. Choose whether to make the DB shard group publicly accessible.

###### Note

You can't modify this setting after you create the DB shard group. 10. Choose **Add a DB shard group**.
Use the `create-db-shard-group` AWS CLI command to create a DB shard group.

The following parameters are required:

- `--db-cluster-identifier` – The DB cluster to which the DB shard group belongs.
- `--db-shard-group-identifier` – The name of the DB shard group.

The DB shard group identifier has the following constraints:

    + It must be unique in the AWS account and AWS Region where you create it.
    + It must contain 1–63 letters, numbers, or hyphens.
    + The first character must be a letter.
    + It can't end with a hyphen or contain two consecutive hyphens.

###### Important

After you create the DB shard group, you can't change the DB cluster identifier or the DB shard group identifier.

- `--max-acu` – The maximum capacity of the DB shard group. Use a value from 16–6144 ACUs.
  The following parameters are optional:

- `--compute-redundancy` – Whether to create standbys for the DB shard group. This parameter can have the
  following values:
  - `0` – Creates a DB shard group without standbys for each shard. This is the default value.
  - `1` – Creates a DB shard group with one compute standby in a different Availability Zone (AZ).
  - `2` – Creates a DB shard group with two compute standbys in two different AZs.

###### Note

If you set the compute redundancy to a nonzero value, the total number of nodes will be doubled or tripled. This will incur
extra costs.

- `--min-acu` – The minimum capacity of your DB shard group. It must be at least 16 ACUs, which is the default
  value.
- `--publicly-accessible|--no-publicly-accessible` – Whether to assign publicly accessible IP addresses to the DB
  shard group. Access to the DB shard group is controlled by the security groups used by the cluster.

The default is `--no-publicly-accessible`.

###### Note

You can't modify this setting after you create the DB shard group.
The following example creates a DB shard group in an Aurora PostgreSQL DB cluster.

```
aws rds create-db-shard-group \
    --db-cluster-identifier `my-db-cluster` \
    --db-shard-group-identifier `my-new-shard-group` \
    --max-acu `1000`
```

The output resembles the following example.

```
{
    "Status": "CREATING",
    "Endpoint": "my-db-cluster.limitless-ckifpdyyyxxx.us-east-1.rds.amazonaws.com",
    "PubliclyAccessible": false,
    "DBClusterIdentifier": "my-db-cluster",
    "MaxACU": 1000.0,
    "DBShardGroupIdentifier": "my-new-shard-group",
    "DBShardGroupResourceId": "shardgroup-8986d309a93c4da1b1455add17abcdef",
    "ComputeRedundancy": 0
}
```
