# Restoring from a snapshot

You can restore the data from a MemoryDB or ElastiCache (Redis OSS) .rdb snapshot file to a new cluster at any time.

The MemoryDB restore process supports the following:

- Migrating from one or more .rdb snapshot files you created from ElastiCache (Redis OSS) to a MemoryDB cluster.

The .rdb files must be put in S3 to perform the restore.

- Specifying a number of shards in the new
  cluster that is different from the number of shards in the cluster that was used
  to create the snapshot file.
- Specifying a different node type for the new cluster—larger or smaller.
  If scaling to a smaller node type,
  be sure that the new node type has sufficient memory for your data and engine overhead.
- Configuring the slots of the new MemoryDB cluster differently than in the cluster that was
  used to create the snapshot file.

###### Important

- MemoryDB clusters do not support multiple databases. Therefore, when
  restoring to MemoryDB your restore fails if the .rdb file references
  more than one database.
- You cannot restore a snapshot from a cluster that uses data tiering (for example, r6gd node type) into a cluster that does not use data tiering (for example, r6g node type).
  Whether you make any changes when restoring a cluster from a snapshot is governed by
  choices that you make. You make these choices in the **Restore
  Cluster** page when using the MemoryDB console to restore. You make
  these choices by setting parameter values when using the AWS CLI or MemoryDB API to
  restore.

During the restore operation, MemoryDB creates the new cluster, and then populates it
with data from the snapshot file. When this process is complete, the
cluster is warmed up and ready to accept requests.

###### Important

Before you proceed, be sure you have created a snapshot of the cluster you want to
restore from. For more information, see [Making manual snapshots](snapshots-manual.md "snapshots-manual.md").

If you want to restore from an externally
created snapshot, see [Seeding a new cluster with an externally created snapshot](snapshots-seeding-redis.md "snapshots-seeding-redis.md").

The following procedures show you how to restore a snapshot to a new cluster using the
MemoryDB console, the AWS CLI, or the MemoryDB API.

###### To restore a snapshot to a new cluster (console)

1.  Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2.  On the navigation pane, choose **Snapshots**.
3.  In the list of snapshots, choose button next to the name of the snapshot name you want to restore from.
4.  Choose **Actions** and then choose **Restore**
5.  Under **Cluster configuration, enter the following:**
    1. **Cluster name** –
       Required.
       The name of the new cluster.
    2. **Description** –
       Optional.
       The description of the new cluster.

6.  Complete the **Subnet groups** section:
    1. For **Subnet groups**, create a new subnet group or choose an existing
       one from the available list that you want to apply to this cluster. If you are creating a new one:
       - Enter a **Name**
       - Enter a **Description**
       - If you enabled Multi-AZ,
         the subnet group must contain at least two subnets that reside in
         different availability zones. For more information, see [Subnets and subnet groups](subnetgroups.md "subnetgroups.md").
       - If you are creating a new subnet group and do not have an existing VPC, you will be asked to create a VPC.
         For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
         _Amazon VPC User Guide._

7.  Complete the **Cluster settings** section:
    1. For **Valkey version compatibility** or **Redis OSS version compatibility**, accept the default `6.0`.
    2. For **Port**, accept the default port of 6379 or, if you have a reason to use a different port, enter the port number..
    3. For **Parameter group**, accept the `default.memorydb-redis6` parameter group.

    Parameter groups control the runtime parameters of your cluster.
    For more information on parameter groups,
    see [Engine specific parameters](parametergroups.md "parametergroups.md"). 4. For **Node type**, choose a value for the node type (along with its associated memory size) that you want.

    If you choose a member of the r6gd node type family, you will automatically enable data-tiering in your cluster.
    For more information, see [Data tiering](data-tiering.md "data-tiering.md"). 5. For **Number of shards**, choose the number of shards that you want for this cluster.

    You can change the
    number of shards in your cluster dynamically. For more
    information, see [Scaling MemoryDB clusters](scaling-cluster.md "scaling-cluster.md"). 6. For **Replicas per shard**, choose the number of read replica nodes
    that you want in each shard.

    The following restrictions exist;.

        * If you have Multi-AZ enabled, make sure that you have at least one replica per
         shard.
        * The number of replicas is the same for each shard when creating the cluster using the console.

    7.  Choose **Next**
    8.  Complete the **Advanced settings** section:
        1. For **Security groups**, choose the security groups that you want for
           this cluster. A _security group_
           acts as a firewall to control network access to your cluster. You
           can use the default security group for your VPC or create a new
           one.

        For more information on security groups, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
        _Amazon VPC User Guide._ 2. Data is encrypted in the following ways:

            * **Encryption at rest** – Enables encryption of data stored
             on disk. For more information, see [Encryption at Rest](at-rest-encryption.md "at-rest-encryption.md").


            ###### Note

            You have the option to supply a different encryption key by choosing **Customer
             Managed AWS KMS key** and choosing
             the key.
            * **Encryption in-transit** – Enables encryption of data on the wire. This is enabled by default. For more information, see [encryption in transit](in-transit-encryption.md "in-transit-encryption.md").

        If you select no encryption, then an open Access control list called “open access” will be created with a default user. For more information, see [Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md"). 3. For **Snapshot** optionally specify a snapshot retention period and a snapshot window. By default, the **Enable automatic snapshots** is selected. 4. For **Maintenance window** optionally specify a maintenance window. The _maintenance window_ is
        the time, generally an hour in length, each week when MemoryDB
        schedules system maintenance for your cluster. You can allow MemoryDB
        to choose the day and time for your maintenance window (_No
        preference_), or you can choose the day, time, and
        duration yourself (_Specify maintenance window_).
        If you choose _Specify maintenance window_ from
        the lists, choose the _Start day_,
        _Start time_, and
        _Duration_ (in hours) for your maintenance
        window. All times are UCT times.

        For more information, see [Managing maintenance](maintenance-window.md "maintenance-window.md"). 5. For **Notifications**, choose an existing Amazon Simple Notification Service (Amazon SNS) topic, or
        choose Manual ARN input and enter the topic's Amazon Resource Name
        (ARN). Amazon SNS allows you to push notifications to Internet-connected
        smart devices. The default is to disable notifications. For more
        information, see [https://aws.amazon.com/sns/](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/").

    9.  For **Tags**, you can optionally apply tags to search and filter your clusters or track your AWS costs.
    10. Review all your entries and choices, then make any needed corrections. When you're ready,
        choose **Create cluster** to launch your cluster, or
        **Cancel** to cancel the operation.As soon as your cluster's status is _available_, you can grant EC2 access to it, connect to it, and begin using it.
        For more information, see [Step 3: Authorize access to the cluster](getting-started.md#getting-started.authorizeaccess "getting-started.md#getting-started.authorizeaccess")
        and [Step 4: Connect to the cluster](getting-started.md#getting-startedclusters.connecttonode "getting-started.md#getting-startedclusters.connecttonode").

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](getting-started.md#clusters.delete "getting-started.md#clusters.delete").
When using either the `create-cluster` operation, be sure to include the
parameter `--snapshot-name` or `--snapshot-arns`
to seed the new cluster with the data from the snapshot.

For more information, see the following:

- [Creating a cluster (AWS CLI)](getting-started.md#clusters.create.cli "getting-started.md#clusters.create.cli") in the _MemoryDB User Guide_.
- [create-cluster](../../../cli/latest/reference/memorydb/create-cluster.md "../../../cli/latest/reference/memorydb/create-cluster.md") in the AWS CLI Command Reference.
  You can restore a MemoryDB snapshot using the MemoryDB API operation
  `CreateCluster`.

When using the `CreateCluster` operation, be sure to include the parameter
`SnapshotName` or `SnapshotArns` to seed the new cluster
with the data from the snapshot.

For more information, see the following:

- [Creating a cluster (MemoryDB API)](getting-started.md#clusters.create.api "getting-started.md#clusters.create.api") in the _MemoryDB User Guide_.
- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") in the _MemoryDB API Reference_.
