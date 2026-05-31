# Getting started with MemoryDB

This exercise leads you through the steps to create, grant access to,
connect to, and finally delete a MemoryDB cluster using the MemoryDB Management
Console.

###### Note

For the purposes of this exercise, we recommend you use the **Easy create** option when creating a cluster and return
to the other two options once you have further explored MemoryDB's features.

###### Topics

- [Step 1: Setting up](#set-up "#set-up")
- [Step 2: Create a cluster](#getting-started.createcluster "#getting-started.createcluster")
- [Step 3: Authorize access to the cluster](#getting-started.authorizeaccess "#getting-started.authorizeaccess")
- [Step 4: Connect to the cluster](#getting-startedclusters.connecttonode "#getting-startedclusters.connecttonode")
- [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete")
- [Next steps](#getting-started.wheregofromhere "#getting-started.wheregofromhere")

## Step 1: Setting up

Following, you can find topics that describe the one-time actions you must take to start
using MemoryDB.

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

### Set up your permissions (new MemoryDB users only)

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

MemoryDB creates and uses service-linked roles to provision resources and access other
AWS resources and services on your behalf. For MemoryDB to create a service-linked role
for you, use the AWS-managed policy named `AmazonMemoryDBFullAccess`. This
role comes preprovisioned with permission that the service requires to create a
service-linked role on your behalf.

You might decide not to use the default policy and instead to use a custom-managed policy.
In this case, make sure that you have either permissions to call
`iam:createServiceLinkedRole` or that you have created the MemoryDB
service-linked role.

For more information, see the following:

- [Creating a New Policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") (IAM)
- [AWS-managed (predefined) policies for MemoryDB](security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies "security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies")
- [Using Service-Linked Roles for MemoryDB](using-service-linked-roles.md "using-service-linked-roles.md")

## Step 2: Create a cluster

Before creating a cluster for production use, you obviously need to consider how you will configure the cluster to meet your business needs. Those issues
are addressed in the [Preparing a cluster](clusters.prepare.md "clusters.prepare.md") section. For the purposes of this Getting Started exercise, you can accept the default configuration values where they apply.

The cluster you create will be live, and not running in a sandbox. You will
incur the standard MemoryDB usage fees for the instance until you delete it. The total
charges will be minimal (typically less than a dollar) if you complete the exercise
described here in one sitting and delete your cluster when you are finished. For more
information about MemoryDB usage rates, see [MemoryDB](https://aws.amazon.com/memorydb/ "https://aws.amazon.com/memorydb/").

Your cluster is launched in a virtual private cloud (VPC) based on the Amazon VPC service.

### Creating a MemoryDB cluster

The following examples show how to create a cluster using the AWS Management Console, AWS CLI and MemoryDB API.

###### To create a cluster using the MemoryDB console

1.  Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2.  Choose **Clusters** In the left navigation pane and then choose **Create**.
    Easy create
3.  Complete the **Configuration** section. This configures the node type and
    default configuration of your cluster. Select the appropriate memory size and network performance you require
    from the following options:
    - Production
    - Dev/Test
    - Demo

4.  Complete the **Cluster info** section.
    1. In **Name**, enter a name for your cluster.

    Cluster naming constraints are as follows:

        * Must contain 1–40 alphanumeric characters or hyphens.
        * Must begin with a letter.
        * Can't contain two consecutive hyphens.
        * Can't end with a hyphen.

    2. In the **Description** box, enter a description for this
       cluster.

5.  Complete the **Subnet groups** section:
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

6.  For **Vector search**, you can **Enable Vector search capability** to store vector embeddings and perform vector searches. Note that this will fix the values
    for engine version compatibility, **Parameter groups** and **Shards**. For more
    information, see [Vector search](vector-search.md "vector-search.md").
7.  **View default settings**:

When using **Easy create**, the remaining cluster settings are set by default. Note that some
of these settings can be changed after creation, as indicated by **Editable after creation**. 6. For **Tags**, you can optionally apply tags to search and filter your clusters or track your AWS costs. 7. Review all your entries and choices, then make any needed corrections. When you're ready,
choose **Create** to launch your cluster, or
**Cancel** to cancel the operation.

As soon as your cluster's status is _available_, you can grant EC2 access to it, connect to it, and begin using it.
For more information, see [Step 3: Authorize access to the cluster](#getting-started.authorizeaccess "#getting-started.authorizeaccess")

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete").

Create new cluster1. Complete the **Cluster info** section.

    1. In **Name**, enter a name for your cluster.


    Cluster naming constraints are as follows:




    	* Must contain 1–40 alphanumeric characters or hyphens.
    	* Must begin with a letter.
    	* Can't contain two consecutive hyphens.
    	* Can't end with a hyphen.
    2. In the **Description** box, enter a description for this
     cluster.

2.  Complete the **Subnet groups** section:
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

3.  Complete the **Cluster settings** section:
    1. For **Enable Vector search capability**, you can enable
       this to store vector embeddings and perform vector searches. Note that this will fix the values
       for engine version compatibility, **Parameter groups** and **Shards**. For more
       information, see [Vector search](vector-search.md "vector-search.md").
    2. For engine version compatibility, accept the default. For example, with Valkey the default is 7.2.6, and with Redis OSS the default is `6.2`.
    3. For **Port**, accept the default port of 6379 or, if you have a reason to use a different port, enter the port number..
    4. For **Parameter group**, if you have enabled vector search, use `default.memorydb-valkey7.search`.
       Otherwise, for Valkey accept the `default.memorydb-valkey7` parameter group.

    Parameter groups control the runtime parameters of your cluster.
    For more information on parameter groups,
    see [Engine specific parameters](parametergroups.redis.md "parametergroups.redis.md"). 5. For **Node type**, choose a value for the node type (along with its associated memory size) that you want.

    If you choose a node type from the r6gd family, you will automatically enable data-tiering, which splits data storage
    between memory and SSD. For more information, see [Data tiering](data-tiering.md "data-tiering.md"). 6. For **Number of shards**, choose the number of shards that you want for this cluster.
    For higher availability of your clusters, we recommend that you add at least 2 shards.

    You can change the
    number of shards in your cluster dynamically. For more
    information, see [Scaling MemoryDB clusters](scaling-cluster.md "scaling-cluster.md"). 7. For **Replicas per shard**, choose the number of read replica nodes
    that you want in each shard.

    The following restrictions exist:

        * If you have Multi-AZ enabled, make sure that you have at least one replica per
         shard.
        * The number of replicas is the same for each shard when creating the cluster using the console.

    8.  Choose **Next**
    9.  Complete the **Advanced settings** section:
        1. For **Security groups**, choose the security groups that you want for
           this cluster. A _security group_
           acts as a firewall to control network access to your cluster. You
           can use the default security group for your VPC or create a new
           one.

        For more information on security groups, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
        _Amazon VPC User Guide._ 2. To encrypt your data, you have the following options:

            * **Encryption at rest** – Enables encryption of data stored
             on disk. For more information, see [Encryption at Rest](at-rest-encryption.md "at-rest-encryption.md").


            ###### Note

            You have the option to supply an encryption key other than default by choosing **Customer
             Managed AWS-owned KMS key** and choosing
             the key.
            * **Encryption in-transit** – Enables encryption of data on the wire. If you select no encryption, then an open Access control list called “open access” will be created with a default user. For more
             information, see [Authenticating users with Access Control Lists (ACLs)](clusters.acls.md "clusters.acls.md").

        3. For **Snapshot**, optionally specify a snapshot retention period and a snapshot window. By default, **Enable automatic snapshots** is pre-selected.
        4. For **Maintenance window** optionally specify a maintenance window. The _maintenance window_ is
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
        information, see [https://aws.amazon.com/sns/](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/"). 6. For **Tags**, you can optionally apply tags to search and filter your clusters or track your AWS costs.

    10. Review all your entries and choices, then make any needed corrections. When you're ready,
        choose **Create** to launch your cluster, or
        **Cancel** to cancel the operation.As soon as your cluster's status is _available_, you can grant EC2 access to it, connect to it, and begin using it.
        For more information, see [Step 3: Authorize access to the cluster](#getting-started.authorizeaccess "#getting-started.authorizeaccess")

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete").

Restore from snapshotsUnder **Snapshot source**, choose the source snapshot from which to migrate data.
For more information, see [Snapshot and restore](snapshots.md "snapshots.md").

###### Note

If you want your new cluster to have vector search enabled, the source snapshot must also
have vector search enabled.

The target cluster defaults to the settings of the source cluster. Optionally, you can change the following settings on the target cluster:

1.  **Cluster info**
    1. In **Name**, enter a name for your cluster.

    Cluster naming constraints are as follows:

        * Must contain 1–40 alphanumeric characters or hyphens.
        * Must begin with a letter.
        * Can't contain two consecutive hyphens.
        * Can't end with a hyphen.

    2. In the **Description** box, enter a description for this
       cluster.

2.  **Subnet groups**
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

3.  **Cluster settings**
    1. For **Enable Vector search capability**, you can enable
       this to store vector embeddings and perform vector searches. Note that this will fix the values
       for engine version compatibility, **Parameter groups** and **Shards**. For more
       information, see [Vector search](vector-search.md "vector-search.md").
    2. For engine version compatibility, accept the default `6.2`.
    3. For **Port**, accept the default port of 6379 or, if you have a reason to use a different port, enter the port number..
    4. For **Parameter group**, if you have enabled vector search, use `default.memorydb-redis7.search.preview`. Otherwise, accept the `default.memorydb-redis7` parameter group.

    Parameter groups control the runtime parameters of your cluster.
    For more information on parameter groups,
    see [Engine specific parameters](parametergroups.redis.md "parametergroups.redis.md"). 5. For **Node type**, choose a value for the node type (along with its associated memory size) that you want.

    If you choose a node type from the r6gd family, you will automatically enable data-tiering, which splits data storage
    between memory and SSD. For more information, see [Data tiering](data-tiering.md "data-tiering.md"). 6. For **Number of shards**, choose the number of shards that you want for this cluster.
    For higher availability of your clusters, we recommend that you add at least 2 shards.

    You can change the
    number of shards in your cluster dynamically. For more
    information, see [Scaling MemoryDB clusters](scaling-cluster.md "scaling-cluster.md"). 7. For **Replicas per shard**, choose the number of read replica nodes
    that you want in each shard.

    The following restrictions exist:

        * If you have Multi-AZ enabled, make sure that you have at least one replica per
         shard.
        * The number of replicas is the same for each shard when creating the cluster using the console.

    8.  Choose **Next**
    9.  **Advanced settings**
        1. For **Security groups**, choose the security groups that you want for
           this cluster. A _security group_
           acts as a firewall to control network access to your cluster. You
           can use the default security group for your VPC or create a new
           one.

        For more information on security groups, see [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
        _Amazon VPC User Guide._ 2. To encrypt your data, you have the following options:

            * **Encryption at rest** – Enables encryption of data stored
             on disk. For more information, see [Encryption at Rest](at-rest-encryption.md "at-rest-encryption.md").


            ###### Note

            You have the option to supply an encryption key other than default by choosing **Customer
             Managed AWS-owned KMS key** and choosing
             the key.
            * **Encryption in-transit** – Enables encryption of data on the wire. If you select no encryption, then an open Access control list called “open access” will be created with a default user. For more
             information, see [Authenticating users with Access Control Lists (ACLs)](clusters.acls.md "clusters.acls.md").

        3. For **Snapshot**, optionally specify a snapshot retention period and a snapshot window. By default, **Enable automatic snapshots** is pre-selected.
        4. For **Maintenance window** optionally specify a maintenance window. The _maintenance window_ is
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
        information, see [https://aws.amazon.com/sns/](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/"). 6. For **Tags**, you can optionally apply tags to search and filter your clusters or track your AWS costs.

    10. Review all your entries and choices, then make any needed corrections. When you're ready,
        choose **Create** to launch your cluster, or
        **Cancel** to cancel the operation.As soon as your cluster's status is _available_, you can grant EC2 access to it, connect to it, and begin using it.
        For more information, see [Step 3: Authorize access to the cluster](#getting-started.authorizeaccess "#getting-started.authorizeaccess")

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete").

To create a cluster using the AWS CLI, see [`create-cluster`](../../../cli/latest/reference/memorydb/create-cluster.md "../../../cli/latest/reference/memorydb/create-cluster.md"). The following is an example:

For Linux, macOS, or Unix:

```
aws memorydb create-cluster \
    --cluster-name my-cluster \
    --node-type db.r6g.large \
    --acl-name my-acl \
    --engine valkey \
    --subnet-group my-sg

```

For Windows:

```
aws memorydb create-cluster ^
   --cluster-name my-cluster ^
   --node-type db.r6g.large ^
   --acl-name my-acl ^
   --engine valkey
   --subnet-group my-sg
```

You should get the following JSON response:

```
{
    "Cluster": {
        "Name": "my-cluster",
        "Status": "creating",
        "NumberOfShards": 1,
        "AvailabilityMode": "MultiAZ",
        "ClusterEndpoint": {
            "Port": 6379
        },
        "NodeType": "db.r6g.large",
        "EngineVersion": "7.2",
        "EnginePatchVersion": "7.2.6",
        "ParameterGroupName": "default.memorydb-valkey7",
        "Engine": "valkey"
        "ParameterGroupStatus": "in-sync",
        "SubnetGroupName": "my-sg",
        "TLSEnabled": true,
        "ARN": `"arn:aws:memorydb:us-east-1:xxxxxxxxxxxxxx:cluster/my-cluster"`,
        "SnapshotRetentionLimit": 0,
        "MaintenanceWindow": "wed:03:00-wed:04:00",
        "SnapshotWindow": "04:30-05:30",
        "ACLName": "my-acl",
        "DataTiering": "false",
        "AutoMinorVersionUpgrade": true
    }
}



```

You can begin using the cluster once its status changes to `available`.

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not actively using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete").

To create a cluster using the MemoryDB API, use the [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") action.

###### Important

As soon as your cluster becomes available,
you're billed for each hour or partial hour that the cluster is active,
even if you're not using it.
To stop incurring charges for this cluster, you must delete it. See [Step 5: Deleting a cluster](#clusters.delete "#clusters.delete").

### Setting up authentication

For information about setting up authentication for your cluster, see [Authenticating with IAM](auth-iam.md "auth-iam.md") and [Authenticating users with Access Control Lists (ACLs)](clusters.acls.md "clusters.acls.md").

## Step 3: Authorize access to the cluster

This section assumes that you are familiar with launching and connecting to Amazon EC2
instances. For more information, see the _[Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/GettingStartedGuide.md "../../../AWSEC2/latest/GettingStartedGuide.md")_.

MemoryDB clusters are designed to be accessed from an Amazon EC2 instance. They can also be accessed by containerized or serverless applications running in Amazon Elastic Container Service or AWS Lambda. The most common
scenario is to access a MemoryDB cluster from an Amazon EC2 instance in the same Amazon Virtual Private Cloud
(Amazon VPC), which will be the case for this exercise.

Before you can connect to a cluster from an EC2 instance,
you must authorize the EC2 instance to access the cluster.

The most common use case is when an application deployed on an EC2 instance needs to connect to a cluster in the same VPC. The simplest way to manage access between EC2 instances and clusters in the same VPC is to do the following:

1. Create a VPC security group for your cluster.
   This security group can be used to restrict access to the clusters.
   For example, you can create a custom rule for this security group that allows
   TCP access using the port you assigned to the cluster when you created it
   and an IP address you will use to access the cluster.

The default port for MemoryDB clusters is `6379`. 2. Create a VPC security group for your EC2 instances (web and application servers).
This security group can, if needed, allow access to the EC2 instance from the Internet via the VPC's routing table.
For example, you can set rules on this security group to allow TCP access to the EC2 instance over port 22. 3. Create custom rules in the security group for your cluster that allow connections
from the security group you created for your EC2 instances. This would allow any member of
the security group to access the clusters.

###### To create a rule in a VPC security group that allows connections from another security group

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the left navigation pane, choose **Security Groups**.
3. Select or create a security group that you will use for your clusters. Under **Inbound Rules**, select **Edit Inbound Rules** and then
   select **Add Rule**. This security group will allow access to
   members of another security group.
4. From **Type** choose **Custom TCP Rule**.
   1. For **Port Range**, specify the port you used when you created your
      cluster.

   The default port for MemoryDB clusters is `6379`. 2. In the **Source** box, start typing the ID of the security group.
   From the list select the security group you will use for your Amazon EC2 instances.

5. Choose **Save** when you finish.

Once you have enabled access, you are now ready to connect to the cluster, as discussed in the next section.

For information on accessing your
MemoryDB cluster from a different Amazon VPC, a different AWS Region, or even your corporate
network, see the following:

- [Access Patterns for Accessing a MemoryDB Cluster in an Amazon VPC](memorydb-vpc-accessing.md "memorydb-vpc-accessing.md")
- [Accessing MemoryDB resources from outside AWS](accessing-memorydb.md#access-from-outside-aws "accessing-memorydb.md#access-from-outside-aws")

## Step 4: Connect to the cluster

Before you continue, complete [Step 3: Authorize access to the cluster](#getting-started.authorizeaccess "#getting-started.authorizeaccess").

This section assumes that you've created an Amazon EC2 instance and can connect to it. For
instructions on how to do this, see the [Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/GettingStartedGuide.md "../../../AWSEC2/latest/GettingStartedGuide.md").

An Amazon EC2 instance can connect to a cluster only if you have authorized it to do so.

### Find your cluster endpoint

When your cluster is in the _available_ state and you've authorized
access to it, you can log in to an Amazon EC2
instance and connect to the cluster. To do so, you must first determine the
endpoint.

To further explore how to find your endpoints, see the following:

- [Finding the Endpoint for a MemoryDB Cluster (AWS Management Console)](endpoints.md#endpoints.find.console "endpoints.md#endpoints.find.console")
- [Finding the Endpoint for a MemoryDB Cluster (AWS CLI)](endpoints.md#endpoints.find.cli "endpoints.md#endpoints.find.cli")
- [Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)](endpoints.md#endpoints.find.api "endpoints.md#endpoints.find.api")

### Connect to a MemoryDB cluster (Linux)

Now that you have the endpoint you need, you can log in to an EC2 instance and connect to the cluster. In the following example, you use the _cli_ utility to connect to a cluster using Ubuntu 22. The latest version of cli also supports SSL/TLS for connecting encryption/authentication enabled clusters.

#### Connecting to MemoryDB nodes using redis-cli

To access data from MemoryDB nodes, you use clients that work with Secure Socket Layer (SSL). You can also use redis-cli with TLS/SSL on Amazon Linux and Amazon Linux 2.

###### To use redis-cli to connect to a MemoryDB cluster on Amazon Linux 2 or Amazon Linux

1. Download and compile the redis-cli utility. This utility is included in the Redis OSS software distribution.
2. At the command prompt of your EC2 instance, type the appropriate commands for the version of Linux you are using.

**Amazon Linux 2023**

If using Amazon Linux 2023, enter this:

```
sudo yum install redis6 -y
```

Then type the following command, substituting the endpoint of your cluster and port for what is shown in this example.

```
redis-cli -h `Primary or Configuration Endpoint` --tls -p 6379
```

For more information on finding the endpoint, see [Find your Node Endpoints](../../../AmazonElastiCache/latest/dg/GettingStarted.ConnectToCacheNode.md#GettingStarted.FindEndpoints "../../../AmazonElastiCache/latest/dg/GettingStarted.ConnectToCacheNode.md#GettingStarted.FindEndpoints").

**Amazon Linux 2**

If using Amazon Linux 2, enter this:

```
sudo yum -y install openssl-devel gcc
wget https://download.redis.io/releases/redis-7.2.5.tar.gz
tar xvzf redis-7.2.5.tar.gz
cd redis-7.2.5
make distclean
make redis-cli BUILD_TLS=yes
sudo install -m 755 src/redis-cli /usr/local/bin/
```

**Amazon Linux**

If using Amazon Linux, enter this:

```
sudo yum install gcc jemalloc-devel openssl-devel tcl tcl-devel clang wget
wget https://download.redis.io/releases/redis-7.2.5.tar.gz
tar xvzf redis-7.2.5.tar.gz
cd redis-7.2.5
make redis-cli CC=clang BUILD_TLS=yes
sudo install -m 755 src/redis-cli /usr/local/bin/
```

On Amazon Linux, you may also need to run the following additional steps:

```
sudo yum install clang
CC=clang make
sudo make install
```

3. After you have downloaded and installed the redis-cli utility, it is recommended that you run the optional `make-test` command.
4. To connect to a cluster with encryption and authentication enabled, enter this command:

```
redis-cli -h `Primary or Configuration Endpoint` --tls -a `'your-password'` -p 6379
```

###### Note

If you install redis6 on Amazon Linux 2023, you can now use the command `redis6-cli` instead of `redis-cli`:

```
redis6-cli -h Primary or Configuration Endpoint --tls -p 6379
```

## Step 5: Deleting a cluster

As long as a cluster is in the _available_ state, you are being charged for it, whether or not
you are actively using it. To stop incurring charges, delete the cluster.

###### Warning

- When you delete a MemoryDB cluster, your manual snapshots are retained.
  You can also create a final snapshot before the cluster is deleted. Automatic snapshots are not retained.
  For more information, see [Snapshot and restore](snapshots.md "snapshots.md").
- `CreateSnapshot` permission is required to create a final snapshot.
  Without this permission, the API call will fail with an `Access Denied` exception.

The following procedure deletes a single cluster from your deployment. To delete multiple
clusters, repeat the procedure for each cluster that you want to delete. You do not
need to wait for one cluster to finish deleting before starting the procedure to
delete another cluster.

###### To delete a cluster

1. Sign in to the AWS Management Console and open the MemoryDB console at
   [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To choose the cluster to delete, choose the radio button next to the cluster's name from the list of
   clusters. In this case, the name of the cluster you created at [Step 2: Create a cluster](#getting-started.createcluster "#getting-started.createcluster").
3. For **Actions**, choose **Delete**.
4. First choose whether to create a snapshot of the cluster before deleting it and then enter
   `delete` in the confirmation box and
   **Delete** to delete the cluster, or choose
   **Cancel** to keep the cluster.

If you chose **Delete**, the status of the cluster changes to _deleting_.
As soon as your cluster is no longer listed in the list of clusters, you stop incurring charges for it.

The following code deletes the cluster `my-cluster`. In this case, substitute `my-cluster` with the
name of the cluster you created at [Step 2: Create a cluster](#getting-started.createcluster "#getting-started.createcluster").

```
aws memorydb delete-cluster --cluster-name `my-cluster`
```

The `delete-cluster` CLI operation only deletes one cluster. To delete
multiple clusters, call `delete-cluster` for each cluster that you want to delete. You do not need to wait for one cluster to
finish deleting before deleting another.

For Linux, macOS, or Unix:

```
aws memorydb delete-cluster \
    --cluster-name `my-cluster` \
    --region `us-east-1`
```

For Windows:

```
aws memorydb delete-cluster ^
    --cluster-name `my-cluster` ^
    --region `us-east-1`
```

For more information, see [`delete-cluster`](../../../cli/latest/reference/memorydb/delete-cluster.md "../../../cli/latest/reference/memorydb/delete-cluster.md").

The following code deletes the cluster `my-cluster`. In this case, substitute `my-cluster` with the
name of the cluster you created at [Step 2: Create a cluster](#getting-started.createcluster "#getting-started.createcluster").

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=DeleteCluster
    &ClusterName=my-cluster
    &Region=us-east-1
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210802T220302Z
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Date=20210802T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20210802T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

The `DeleteCluster` API operation only deletes one cluster. To delete
multiple clusters, call `DeleteCluster` for each cluster
that you want to delete. You do not need to wait for one cluster to finish
deleting before deleting another.

For more information, see [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md").

## Next steps

Now that you have tried the Getting Started exercise, you can explore the following sections
to learn more about MemoryDB and available tools:

- [Getting started with AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/")
- [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/")
- [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")
- [MemoryDB API Reference.](../APIReference/Welcome.md "../APIReference/Welcome.md")
