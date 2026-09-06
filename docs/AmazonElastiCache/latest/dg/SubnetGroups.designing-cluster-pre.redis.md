

# Creating a node-based ElastiCache cluster for Redis OSS
<a name="SubnetGroups.designing-cluster-pre.redis"></a>

Following are the one-time actions you must take in order to create a node-based ElastiCache cluster for Redis OSS. 

For further information on setting up ElastiCache see [Setting up ElastiCache](set-up.md).

**Topics**
+ [Step 1: Create a subnet group](#SubnetGroups.Creating-gs.redis)
+ [Step 2: Create a cluster](#GettingStarted.CreateCluster.redis)
+ [Step 3: Authorize access to the cluster](#GettingStarted.AuthorizeAccess.redis)
+ [Step 4: Connect to the cluster's node](#GettingStarted.ConnectToCacheNode.redis)

## Step 1: Create a subnet group
<a name="SubnetGroups.Creating-gs.redis"></a>

Before you create a cluster, you first create a subnet group. A *cache subnet group* is a collection of subnets that you may want to designate for your clusters in a VPC. When launching a cluster in a VPC, you need to select a cache subnet group. Then ElastiCache uses that cache subnet group to assign IP addresses within that subnet to each cache node in the cluster.

When you create a new subnet group, note the number of available IP addresses. If the subnet has very few free IP addresses, you might be constrained as to how many more nodes you can add to the cluster. To resolve this issue, you can assign one or more subnets to a subnet group so that you have a sufficient number of IP addresses in your cluster's Availability Zone. After that, you can add more nodes to your cluster.

The following procedures show you how to create a subnet group called `mysubnetgroup` (console) and the AWS CLI.

### Creating a subnet group (Console)
<a name="SubnetGroups.Creating.CON.redis"></a>

The following procedure shows how to create a subnet group (console).

**To create a subnet group (Console)**

1. Sign in to the AWS Management Console, and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the navigation list, choose **Subnet Groups**.

1. Choose **Create Subnet Group**.

1. In the **Create Subnet Group** wizard, do the following. When all the settings are as you want them, choose **Yes, Create**.

   1. In the **Name** box, type a name for your subnet group.

   1. In the **Description** box, type a description for your subnet group.

   1. In the **VPC ID** box, choose the Amazon VPC that you created.

   1. In the **Availability Zone** and **Subnet ID** lists, choose the Availability Zone or [Local Zone](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Local_zones.html) and ID of your private subnet, and then choose **Add**.  
![Image: Create Subnet VPC screen](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/vpc-03.png)

1. In the confirmation message that appears, choose **Close**.

Your new subnet group appears in the **Subnet Groups** list of the ElastiCache console. At the bottom of the window you can choose the subnet group to see details, such as all of the subnets associated with this group.

### Create a subnet group (AWS CLI)
<a name="SubnetGroups.Creating.redis.CLI"></a>

At a command prompt, use the command `create-cache-subnet-group` to create a subnet group.

For Linux, macOS, or Unix:

```
aws elasticache create-cache-subnet-group \
    --cache-subnet-group-name {{mysubnetgroup}} \
    --cache-subnet-group-description {{"Testing"}} \
    --subnet-ids {{subnet-53df9c3a}}
```

For Windows:

```
aws elasticache create-cache-subnet-group ^
    --cache-subnet-group-name {{mysubnetgroup}} ^
    --cache-subnet-group-description {{"Testing"}} ^
    --subnet-ids {{subnet-53df9c3a}}
```

This command should produce output similar to the following:

```
{
    "CacheSubnetGroup": {
        "VpcId": "vpc-37c3cd17", 
        "CacheSubnetGroupDescription": "Testing", 
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-53df9c3a", 
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            }
        ], 
        "CacheSubnetGroupName": "mysubnetgroup"
    }
}
```

For more information, see the AWS CLI topic [create-cache-subnet-group](https://docs.aws.amazon.com/cli/latest/reference/elasticache/create-cache-subnet-group.html).

## Step 2: Create a cluster
<a name="GettingStarted.CreateCluster.redis"></a>

Before creating a cluster for production use, you obviously need to consider how you will configure the cluster to meet your business needs. Those issues are addressed in the [Preparing a cluster in ElastiCache](Clusters.Prepare.md) section. For the purposes of this Getting Started exercise, you will create a cluster with cluster mode disabled and you can accept the default configuration values where they apply.

The cluster you create will be live, and not running in a sandbox. You will incur the standard ElastiCache usage fees for the instance until you delete it. The total charges will be minimal (typically less than a dollar) if you complete the exercise described here in one sitting and delete your cluster when you are finished. For more information about ElastiCache usage rates, see [Amazon ElastiCache](https://aws.amazon.com/elasticache/).

Your cluster is launched in a virtual private cloud (VPC) based on the Amazon VPC service. 

### Creating a Redis OSS (cluster mode disabled) cluster (Console)
<a name="Clusters.Create.CON.Redis-gs"></a>

**To create a Redis OSS (cluster mode disabled) cluster using the ElastiCache console**

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the list in the upper-right corner, choose the AWS Region that you want to launch this cluster in.

1. Choose **Get started** from the navigation pane.

1. Choose **Create VPC** and follow the steps outlined at [Creating a Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VPCs.CreatingVPC.html).

1. On the ElastiCache dashboard page, choose **Valkey cache** or **Redis OSS cache**. For this exercise we will choose **Redis OSS cache**, and then choose **Create Redis OSS cache**.

1. Under **Cluster settings**, do the following:

   1. Choose **Configure and create a new cluster**.

   1. For **Cluster mode**, choose **Disabled**.

   1. For **Cluster info** enter a value for **Name**. 

   1. (Optional) Enter a value for **Description**.

1. Under **Location**:

------
#### [ AWS Cloud  ]

   1. For **AWS Cloud**, we recommend you accept the default settings for **Multi-AZ** and **Auto-failover**. For more information, see [Minimizing downtime in ElastiCache for Redis OSS with Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html).

   1. Under **Cluster settings**

      1. For **Engine version**, choose an available version.

      1. For **Port**, use the default port, 6379. If you have a reason to use a different port, enter the port number.

      1. For **Parameter group**, choose a parameter group or create a new one. Parameter groups control the runtime parameters of your cluster. For more information on parameter groups, see [Valkey and Redis OSS parameters](ParameterGroups.Engine.md#ParameterGroups.Redis) and [Creating an ElastiCache parameter group](ParameterGroups.Creating.md).
**Note**  
When you select a parameter group to set the engine configuration values, that parameter group is applied to all clusters in the global datastore. On the **Parameter Groups** page, the yes/no **Global** attribute indicates whether a parameter group is part of a global datastore.

      1. For **Node type**, choose the down arrow (![Downward-pointing triangle icon, typically used to indicate a dropdown menu.](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/ElastiCache-DnArrow.png)). In the **Change node type** dialog box, choose a value for **Instance family** for the node type that you want. Then choose the node type that you want to use for this cluster, and then choose **Save**.

         For more information, see [Choosing your node size](CacheNodes.SelectSize.md).

         If you choose an r6gd node type, data-tiering is automatically enabled. For more information, see [Data tiering in ElastiCache](data-tiering.md).

      1. For **Number of replicas**, choose the number of read replicas you want. If you enabled Multi-AZ, the number must be between 1-5.

   1. Under **Connectivity**

      1. For **Network type**, choose the IP version(s) this cluster will support. 

      1. For **Subnet groups**, choose the subnet that you want to apply to this cluster. ElastiCache uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. ElastiCache clusters require a dual-stack subnet with both IPv4 and IPv6 addresses assigned to them to operate in dual-stack mode and an IPv6-only subnet to operate as IPv6-only.

         When creating a new subnet group, enter the **VPC ID** to which it belongs.

         For more information, see:
         + [Choosing a network type in ElastiCache](network-type.md).
         + [Create a subnet in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet).

         If you are [Using local zones with ElastiCache](Local_zones.md), you must create or choose a subnet that is in the local zone. 

         For more information, see [Subnets and subnet groups](SubnetGroups.md).

   1. For **Availability zone placements**, you have two options:
      + **No preference** – ElastiCache chooses the Availability Zone.
      + **Specify availability zones** – You specify the Availability Zone for each cluster.

        If you chose to specify the Availability Zones, for each cluster in each shard, choose the Availability Zone from the list.

      For more information, see [Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md).

   1. Choose **Next**

   1. Under **Advanced Redis OSS settings**

      1. For **Security**: 

        1. To encrypt your data, you have the following options:
           + **Encryption at rest** – Enables encryption of data stored on disk. For more information, see [Encryption at Rest](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/at-rest-encryption.html).
**Note**  
You have the option to supply a different encryption key by choosing **Customer Managed AWS KMS key** and choosing the key. For more information, see [Using customer managed keys from AWS KMS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/at-rest-encryption.html#using-customer-managed-keys-for-elasticache-security).
           + **Encryption in-transit** – Enables encryption of data on the wire. For more information, see [encryption in transit](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption.html). For ElastiCache engine version 6.0 for Redis OSS and above, if you enable encryption in-transit you will be prompted to specify one of the following **Access Control** options:
             + **No Access Control** – This is the default setting. This indicates no restrictions on user access to the cluster.
             + **User Group Access Control List** – Select a user group with a defined set of users that can access the cluster. For more information, see [Managing User Groups with the Console and CLI](Clusters.RBAC.md#User-Groups).
             + **AUTH Default User** – An authentication mechanism for Valkey and Redis OSS server. For more information, see [AUTH](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html).
           + **AUTH** – An authentication mechanism for Redis OSS server. For more information, see [AUTH](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html).
**Note**  
RBAC is available on Valkey, and on Redis OSS version 6.0 and later. On earlier Redis OSS versions, AUTH is the sole option.

        1. For **Security groups**, choose the security groups that you want for this cluster. A *security group* acts as a firewall to control network access to your cluster. You can use the default security group for your VPC or create a new one.

           For more information on security groups, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide.*

   1. For regularly scheduled automatic backups, select **Enable automatic backups** and then enter the number of days that you want each automatic backup retained before it is automatically deleted. If you don't want regularly scheduled automatic backups, clear the **Enable automatic backups** check box. In either case, you always have the option to create manual backups.

      For more information on backup and restore, see [Snapshot and restore](backups.md).

   1. (Optional) Specify a maintenance window. The *maintenance window* is the time, generally an hour in length, each week when ElastiCache schedules system maintenance for your cluster. You can allow ElastiCache to choose the day and time for your maintenance window (*No preference*), or you can choose the day, time, and duration yourself (*Specify maintenance window*). If you choose *Specify maintenance window* from the lists, choose the *Start day*, *Start time*, and *Duration* (in hours) for your maintenance window. All times are UCT times.

      For more information, see [Managing ElastiCache cluster maintenance](maintenance-window.md).

   1. (Optional) For **Logs**:
      + Under **Log format**, choose either **Text** or **JSON**.
      + Under **Destination Type**, choose either **CloudWatch Logs** or **Kinesis Firehose**.
      + Under **Log destination**, choose either **Create new** and enter either your CloudWatch Logs log group name or your Firehose stream name, or choose **Select existing** and then choose either your CloudWatch Logs log group name or your Firehose stream name,

   1. For **Tags**, to help you manage your clusters and other ElastiCache resources, you can assign your own metadata to each resource in the form of tags. For mor information, see [Tagging your ElastiCache resources](Tagging-Resources.md).

   1. Choose **Next**.

   1. Review all your entries and choices, then make any needed corrections. When you're ready, choose **Create**.

------
#### [ On premises ]

   1. For **On premises**, we recommend you leave **Auto-failover** enabled. For more information, see [Minimizing downtime in ElastiCache for Redis OSS with Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)

   1. To finish creating the cluster, follow the steps at [Using Outposts](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ElastiCache-Outposts.html).

------

As soon as your cluster's status is *available*, you can grant Amazon EC2 access to it, connect to it, and begin using it. For more information, see [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.valkey.md#GettingStarted.AuthorizeAccess.valkey) and [Step 4. Connect to the cluster's node](SubnetGroups.designing-cluster-pre.valkey.md#GettingStarted.ConnectToCacheNode.valkey).

**Important**  
Once your cluster is available, you're billed for each hour or partial hour that the cluster is active, even if you're not actively using it. To stop incurring charges for this cluster, you must delete it. See [Deleting a cluster in ElastiCache](Clusters.Delete.md). 

### Creating a Redis OSS (cluster mode disabled) cluster (AWS CLI)
<a name="Clusters.Create.CLI.Redis-gs"></a>

**Example**  
The following CLI code creates a Redis OSS (cluster mode disabled) cluster with no replicas.  
For Linux, macOS, or Unix:  

```
aws elasticache create-cache-cluster \
--cache-cluster-id {{my-cluster}} \
--cache-node-type {{cache.r4.large}} \
--engine {{redis}} \
--num-cache-nodes {{1}} \
--snapshot-arns {{arn:aws:s3:::my_bucket/snapshot.rdb}}
```
For Windows:  

```
aws elasticache create-cache-cluster ^
--cache-cluster-id {{my-cluster}} ^
--cache-node-type {{cache.r4.large}} ^
--engine {{redis}} ^
--num-cache-nodes {{1}} ^
--snapshot-arns {{arn:aws:s3:::my_bucket/snapshot.rdb}}
```

To work with cluster mode enabled, see the following topics:
+ To use the console, see [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.Create.md#Clusters.Create.CON.RedisCluster).
+ To use the AWS CLI, see [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (AWS CLI)](Clusters.Create.md#Clusters.Create.CLI.RedisCluster).

## Step 3: Authorize access to the cluster
<a name="GettingStarted.AuthorizeAccess.redis"></a>

 This section assumes that you are familiar with launching and connecting to Amazon EC2 instances. For more information, see the *[Amazon EC2 Getting Started Guide](https://docs.aws.amazon.com/AWSEC2/latest/GettingStartedGuide/)*. 

All ElastiCache clusters are designed to be accessed from an Amazon EC2 instance. The most common scenario is to access an ElastiCache cluster from an Amazon EC2 instance in the same Amazon Virtual Private Cloud (Amazon VPC), which will be the case for this exercise. 

By default, network access to your cluster is limited to the account that was used to create it. Before you can connect to a cluster from an EC2 instance, you must authorize the EC2 instance to access the cluster. The steps required depend upon whether you launched your cluster into EC2-VPC or EC2-Classic.

The most common use case is when an application deployed on an EC2 instance needs to connect to a cluster in the same VPC. The simplest way to manage access between EC2 instances and clusters in the same VPC is to do the following:

1. Create a VPC security group for your cluster. This security group can be used to restrict access to the cluster instances. For example, you can create a custom rule for this security group that allows TCP access using the port you assigned to the cluster when you created it and an IP address you will use to access the cluster. 

   The default port for Redis OSS clusters and replication groups is `6379`.
**Important**  
Amazon ElastiCache security groups are only applicable to clusters that are *not* running in an Amazon Virtual Private Cloud environment (VPC). If you are running in an Amazon Virtual Private Cloud, ** Security Groups** is not available in the console navigation pane.  
If you are running your ElastiCache nodes in an Amazon VPC, you control access to your clusters with Amazon VPC security groups, which are different from ElastiCache security groups. For more information about using ElastiCache in an Amazon VPC, see [Amazon VPCs and ElastiCache security](VPCs.md)

1. Create a VPC security group for your EC2 instances (web and application servers). This security group can, if needed, allow access to the EC2 instance from the Internet via the VPC's routing table. For example, you can set rules on this security group to allow TCP access to the EC2 instance over port 22.

1. Create custom rules in the security group for your Cluster that allow connections from the security group you created for your EC2 instances. This would allow any member of the security group to access the clusters.

**Note**  
If you are planning to use [Using local zones with ElastiCache](Local_zones.md), ensure that you have enabled them. When you create a subnet group in that local zone, your VPC is extended to that Local Zone and your VPC will treat the subnet as any subnet in any other Availability Zone. All relevant gateways and route tables will be automatically adjusted.

**To create a rule in a VPC security group that allows connections from another security group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Security Groups**.

1. Select or create a security group that you will use for your Cluster instances. Under **Inbound Rules**, select **Edit Inbound Rules** and then select **Add Rule**. This security group will allow access to members of another security group.

1. From **Type** choose **Custom TCP Rule**.

   1. For **Port Range**, specify the port you used when you created your cluster.

      The default port for Redis OSS clusters and replication groups is `6379`.

   1. In the **Source** box, start typing the ID of the security group. From the list select the security group you will use for your Amazon EC2 instances.

1. Choose **Save** when you finish.  
![Image: Screen for editing an inbound VPC rule](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/VPC-Rules.png)

Once you have enabled access, you are now ready to connect to the node, as discussed in the next section.

For information on accessing your ElastiCache cluster from a different Amazon VPC, a different AWS Region, or even your corporate network, see the following:
+ [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md)
+ [Accessing ElastiCache resources from outside AWS](accessing-elasticache.md#access-from-outside-aws)

## Step 4: Connect to the cluster's node
<a name="GettingStarted.ConnectToCacheNode.redis"></a>

Before you continue, complete [Step 3: Authorize access to the cluster](#GettingStarted.AuthorizeAccess.redis).

This section assumes that you've created an Amazon EC2 instance and can connect to it. For instructions on how to do this, see the [Amazon EC2 Getting Started Guide](https://docs.aws.amazon.com/AWSEC2/latest/GettingStartedGuide/). 

An Amazon EC2 instance can connect to a cluster node only if you have authorized it to do so. 

### Find your node endpoints
<a name="GettingStarted.FindEndpoints.redis"></a>

When your cluster is in the *available* state and you've authorized access to it, you can log in to an Amazon EC2 instance and connect to the cluster. To do so, you must first determine the endpoint.

#### Finding a Valkey or Redis OSS (Cluster Mode Disabled) Cluster's Endpoints (Console)
<a name="Endpoints.Find.Redis-gs"></a>

If a Redis OSS (cluster mode disabled) cluster has only one node, the node's endpoint is used for both reads and writes. If the cluster has multiple nodes, there are three types of endpoints; the *primary endpoint*, the *reader endpoint* and the *node endpoints*.

The primary endpoint is a DNS name that always resolves to the primary node in the cluster. The primary endpoint is immune to changes to your cluster, such as promoting a read replica to the primary role. For write activity, we recommend that your applications connect to the primary endpoint.

A reader endpoint will evenly split incoming connections to the endpoint between all read replicas in a ElastiCache for Redis OSS cluster. Additional factors such as when the application creates the connections or how the application (re)-uses the connections will determine the traffic distribution. Reader endpoints keep up with cluster changes in real-time as replicas are added or removed. You can place your ElastiCache for Redis OSS cluster’s multiple read replicas in different AWS Availability Zones (AZ) to ensure high availability of reader endpoints. 

**Note**  
A reader endpoint is not a load balancer. It is a DNS record that will resolve to an IP address of one of the replica nodes in a round robin fashion.

For read activity, applications can also connect to any node in the cluster. Unlike the primary endpoint, node endpoints resolve to specific endpoints. If you make a change in your cluster, such as adding or deleting a replica, you must update the node endpoints in your application.

**To find a Redis OSS (cluster mode disabled) cluster's endpoints**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Redis OSS caches**.

   The clusters screen will appear with a list that will include any existing Valkey or Redis OSS serverless caches, Redis OSS (cluster mode disabled) clusters and Redis OSS (cluster mode enabled) clusters. Choose the cluster you created in the [Creating a Redis OSS (cluster mode disabled) cluster (Console)](#Clusters.Create.CON.Redis-gs) section.

1. To find the cluster's Primary and/or Reader endpoints, choose the cluster's name (not the radio button).  
![Image: Primary endpoint for a Redis OSS (cluster mode disabled) cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/Reader-Endpoint.png)

   *Primary and Reader endpoints for a Redis OSS (cluster mode disabled) cluster*

   If there is only one node in the cluster, there is no primary endpoint and you can continue at the next step.

1. If the Redis OSS (cluster mode disabled) cluster has replica nodes, you can find the cluster's replica node endpoints by choosing the cluster's name and then choosing the **Nodes** tab.

   The nodes screen appears with each node in the cluster, primary and replicas, listed with its endpoint.  
![Image: Node endpoints for a Redis OSS (cluster mode disabled) cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/ElastiCache-Endpoints-Redis-Node.png)

   *Node endpoints for a Redis OSS (cluster mode disabled) cluster*

1. To copy an endpoint to your clipboard:

   1. One endpoint at a time, find the endpoint you want to copy.

   1. Choose the copy icon directly in front of the endpoint.

   The endpoint is now copied to your clipboard. For information on using the endpoint to connect to a node, see [Connecting to nodes](nodes-connecting.md).

A Redis OSS (cluster mode disabled) primary endpoint looks something like the following. There is a difference depending upon whether or not In-Transit encryption is enabled.

**In-transit encryption not enabled**

```
{{clusterName.xxxxxx}}.{{nodeId}}.{{regionAndAz}}.cache.amazonaws.com:{{port}}
			
redis-01.7abc2d.0001.usw2.cache.amazonaws.com:6379
```

**In-transit encryption enabled**

```
master.{{clusterName}}.{{xxxxxx}}.{{regionAndAz}}.cache.amazonaws.com:{{port}}

master.ncit.ameaqx.use1.cache.amazonaws.com:6379
```

To further explore how to find your endpoints, see the relevant topics for the engine and cluster type you're running. 
+ [Finding connection endpoints in ElastiCache](Endpoints.md)
+ [Finding Endpoints for a Valkey or Redis OSS (Cluster Mode Enabled) Cluster (Console)](Endpoints.md#Endpoints.Find.RedisCluster)—You need the cluster's Configuration endpoint.
+ [Finding Endpoints (AWS CLI)](Endpoints.md#Endpoints.Find.CLI)
+ [Finding Endpoints (ElastiCache API)](Endpoints.md#Endpoints.Find.API)

### Connect to a Valkey or Redis OSS cluster or replication group (Linux)
<a name="GettingStarted.ConnectToCacheNode.Redis.Linux"></a>

Now that you have the endpoint you need, you can log in to an EC2 instance and connect to the cluster or replication group. In the following example, you use the *valkey-cli* utility to connect to a cluster. The latest version of valkey-cli also supports SSL/TLS for connecting encryption/authentication enabled clusters.

The following example uses Amazon EC2 instances running Amazon Linux and Amazon Linux 2. For details on installing and compiling valkey-cli with other Linux distributions, see the documentation for your specific operating system..

**Note**  
This process covers testing a connection using valkey-cli utility for unplanned use only. For a list of supported clients, see the [Valkey documentation](https://valkey.io/). For examples of using the AWS SDKs with ElastiCache, see [Tutorials: Getting started with Python and ElastiCache](ElastiCache-Getting-Started-Tutorials.md).

#### Connecting to a cluster mode disabled unencrypted-cluster
<a name="Connecting-to-a-cluster-mode-disabled-unencrypted-cluster.redis"></a>

1. Run the following command to connect to the cluster and replace {{primary-endpoint}} and {{port number}} with the endpoint of your cluster and your port number. (The default port for Valkey and Redis OSS is 6379.)

   ```
   src/valkey-cli -h {{primary-endpoint}} -p {{port number}}
   ```

   The result in a command prompt looks similar to the following:

   ```
   {{primary-endpoint}}:{{port number}}
   ```

1. You can now run Valkey and Redis OSS commands.

   ```
   set x Hello
   OK
   
   get x
   "Hello"
   ```

#### Connecting to a cluster mode enabled unencrypted-cluster
<a name="Connecting-to-a-cluster-mode-enabled-unencrypted-cluster.redis"></a>

1. Run the following command to connect to the cluster and replace {{configuration-endpoint}} and {{port number}} with the endpoint of your cluster and your port number. (The default port for Valkey and Redis OSS is 6379.)

   ```
   src/valkey-cli -h {{configuration-endpoint}} -c -p {{port number}}
   ```
**Note**  
In the preceding command, option -c enables cluster mode following [-ASK and -MOVED redirections](https://redis.io/topics/cluster-spec).

   The result in a command prompt looks similar to the following:

   ```
   {{configuration-endpoint}}:{{port number}}
   ```

1. You can now run Valkey and Redis OSS commands. Note that redirection occurs because you enabled it using the -c option. If redirection isn't enabled, the command returns the MOVED error. For more information on the MOVED error, see [cluster specification](https://valkey.io/topics/cluster-spec).

   ```
   set x Hi
   -> Redirected to slot [16287] located at 172.31.28.122:6379
   OK
   set y Hello
   OK
   get y
   "Hello"
   set z Bye
   -> Redirected to slot [8157] located at 172.31.9.201:6379
   OK
   get z
   "Bye"
   get x
   -> Redirected to slot [16287] located at 172.31.28.122:6379
   "Hi"
   ```

#### Connecting to an Encryption/Authentication enabled cluster
<a name="Connecting-to-an-Encryption-Authentication-enabled-cluster.redis"></a>

By default, valkey-cli uses an unencrypted TCP connection when connecting to Valkey and Redis OSS. The option `BUILD_TLS=yes` enables SSL/TLS at the time of valkey-cli compilation as shown in the preceding [Download and set up command line access](set-up.md#Download-and-install-cli) section. Enabling AUTH is optional. However, you must enable encryption in-transit in order to enable AUTH. For more details on ElastiCache encryption and authentication, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md).

**Note**  
You can use the option `--tls` with valkey-cli to connect to both cluster mode enabled and disabled encrypted clusters. If a cluster has an AUTH token set, then you can use the option `-a` to provide an AUTH password.

In the following examples, be sure to replace {{cluster-endpoint}} and {{port number}} with the endpoint of your cluster and your port number. (The default port for Redis OSS is 6379.)

**Connect to cluster mode disabled encrypted clusters** 

The following example connects to an encryption and authentication enabled cluster:

```
src/valkey-cli -h {{cluster-endpoint}} --tls -a {{your-password}} -p {{port number}}
```

The following example connects to a cluster that has only encryption enabled:

```
src/valkey-cli -h {{cluster-endpoint}} --tls -p {{port number}}
```

**Connect to cluster mode enabled encrypted clusters** 

The following example connects to an encryption and authentication enabled cluster:

```
src/valkey-cli -c -h {{cluster-endpoint}} --tls -a {{your-password}} -p {{port number}}
```

The following example connects to a cluster that has only encryption enabled:

```
src/valkey-cli -c -h {{cluster-endpoint}} --tls -p {{port number}}
```

After you connect to the cluster, you can run the Valkey or Redis OSS commands as shown in the preceding examples for unencrypted clusters.

#### An alternative to valkey-cli or Redis-cli
<a name="Redis-cli-alternative"></a>

If the cluster isn't cluster mode enabled and you need to make a connection to the cluster for a short test but without going through the valkey-cli or redis-cli compilation, you can use telnet or openssl. In the following example commands, be sure to replace {{cluster-endpoint}} and {{port number}} with the endpoint of your cluster and your port number. (The default port for Redis OSS is 6379.)

The following example connects to an encryption and/or authentication enabled cluster mode disabled cluster:

```
openssl s_client -connect {{cluster-endpoint}}:{{port number}}
```

If the cluster has a password set, first connect to the cluster. After connecting, authenticate the cluster using the following command, then press the `Enter` key. In the following example, replace {{your-password}} with the password for your cluster.

```
Auth {{your-password}}
```

The following example connects to a cluster mode disabled cluster that doesn't have encryption or authentication enabled:

```
telnet {{cluster-endpoint}} {{port number}}
```

### Connect to a Valkey or Redis OSS cluster or replication group (Windows)
<a name="GettingStarted.ConnectToCacheNode.Redis.Windows"></a>

In order to connect to the cluster from an EC2 Windows instance using the Valkey or Redis OSS CLI, you must download the *valkey-cli* package and use *valkey-cli.exe* to connect to the Valkey or Redis OSS cluster from an EC2 Windows instance.

In the following example, you use the *valkey-cli* utility to connect to a cluster that is not encryption enabled and running Valkey or Redis OSS. For more information about Valkey and available commands, see [Valkey commands](http://valkey.io/commands) on the Valkey website.

**To connect to a Valkey or Redis OSS cluster that is not encryption-enabled using *valkey-cli***

1. Connect to your Amazon EC2 instance using the connection utility of your choice. For instructions on how to connect to an Amazon EC2 instance, see the [Amazon EC2 Getting Started Guide](https://docs.aws.amazon.com/AWSEC2/latest/GettingStartedGuide/). 

1. Copy and paste the link [https://github.com/microsoftarchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.zip](https://github.com/microsoftarchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.zip) in an Internet browser to download the zip file for the Redis OSS client from the available release at GitHub [https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504](https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504)

   Extract the zip file to you desired folder/path.

   Open the Command Prompt and change to the Valkey directory and run the command `c:\Valkey>valkey-cli -h {{Valkey_Cluster_Endpoint}} -p 6379`.

   For example:

   ```
   c:\Valkey>valkey-cli -h cmd.xxxxxxx.ng.0001.usw2.cache.amazonaws.com -p 6379
   ```

1. Run Valkey or Redis OSS commands.

    You are now connected to the cluster and can run Valkey or Redis OSS commands like the following.

   ```
   set a "hello"          // Set key "a" with a string value and no expiration
   OK
   get a                  // Get value for key "a"
   "hello"
   get b                  // Get value for key "b" results in miss
   (nil)				
   set b "Good-bye" EX 5  // Set key "b" with a string value and a 5 second expiration
   "Good-bye"
   get b                  // Get value for key "b"
   "Good-bye"
                          // wait >= 5 seconds
   get b
   (nil)                  // key has expired, nothing returned
   quit                   // Exit from valkey-cli
   ```