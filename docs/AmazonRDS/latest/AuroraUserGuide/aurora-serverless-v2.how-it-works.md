

# How Aurora serverless works
<a name="aurora-serverless-v2.how-it-works"></a>

The following overview describes how Aurora serverless works.

**Topics**
+ [Overview](#aurora-serverless-v2.architecture)
+ [Cluster configurations](#aurora-serverless-v2.how-it-works.cluster_topology)
+ [Capacity](#aurora-serverless-v2.how-it-works.capacity)
+ [Scaling](#aurora-serverless-v2.how-it-works.scaling)
+ [High availability](#aurora-serverless.ha)
+ [Storage](#aurora-serverless.storage)
+ [Configuration parameters](#aurora-serverless-v2.parameters)

## Aurora serverless overview
<a name="aurora-serverless-v2.architecture"></a>

*Amazon Aurora serverless* is suitable for the most demanding, highly variable workloads. For example, your database usage might be heavy for a short period of time, followed by long periods of light activity or no activity at all. Some examples are retail, gaming, or sports websites with periodic promotional events, and databases that produce reports when needed. Others are development and testing environments, and new applications where usage might ramp up quickly. For cases such as these and many others, configuring capacity correctly in advance isn't always possible with the provisioned model. It can also result in higher costs if you overprovision and have capacity that you don't use.

In contrast, *Aurora provisioned clusters* are suitable for steady workloads. With provisioned clusters, you choose a DB instance class that has a predefined amount of memory, CPU power, I/O bandwidth, and so on. If your workload changes, you manually modify the instance class of your writer and readers. The provisioned model works well when you can adjust capacity in advance of expected consumption patterns and it's acceptable to have brief outages while you change the instance class of the writer and readers in your cluster.

Aurora serverless is architected from the ground up to support serverless DB clusters that are instantly scalable. Aurora serverless is engineered to provide the same degree of security and isolation as with provisioned writers and readers. These aspects are crucial in multitenant serverless cloud environments. The dynamic scaling mechanism has very little overhead so that it can respond quickly to changes in the database workload. It's also powerful enough to meet dramatic increases in processing demand.

By using Aurora serverless, you can create an Aurora DB cluster without being locked into a specific database capacity for each writer and reader. You specify the minimum and maximum capacity range. Aurora scales each Aurora serverless writer or reader in the cluster within that capacity range. By using a Multi-AZ cluster where each writer or reader can scale dynamically, you can take advantage of dynamic scaling and high availability.

Aurora serverless scales the database resources automatically based on your minimum and maximum capacity specifications. Scaling is fast because most scaling events operations keep the writer or reader on the same host. In the rare cases that an Aurora serverless writer or reader is moved from one host to another, Aurora serverless manages the connections automatically. You don't need to change your database client application code or your database connection strings.

With Aurora serverless, as with provisioned clusters, storage capacity and compute capacity are separate. When we refer to Aurora serverless capacity and scaling, it's always compute capacity that's increasing or decreasing. Thus, your cluster can contain many terabytes of data even when the CPU and memory capacity scale down to low levels.

Instead of provisioning and managing database servers, you specify database capacity. For details about Aurora serverless capacity, see [Aurora serverless capacity](#aurora-serverless-v2.how-it-works.capacity). The actual capacity of each Aurora serverless writer or reader varies over time, depending on your workload. For details about that mechanism, see [Aurora serverless scaling](#aurora-serverless-v2.how-it-works.scaling).

**Important**  
With Aurora serverless, your cluster can contain readers in addition to the writer. Each Aurora serverless writer and reader can scale between the minimum and maximum capacity values. Thus, the total capacity of your Aurora serverless cluster depends on both the capacity range that you define for your DB cluster and the number of writers and readers in the cluster. At any specific time, you are only charged for the Aurora serverless capacity that is being actively used in your Aurora DB cluster.

## Configurations for Aurora DB clusters
<a name="aurora-serverless-v2.how-it-works.cluster_topology"></a>

For each of your Aurora DB clusters, you can choose any combination of Aurora serverless capacity, provisioned capacity, or both.

You can set up a cluster that contains both Aurora serverless and provisioned capacity, called a *mixed-configuration cluster*. For example, suppose that you need more read/write capacity than is available for an Aurora serverless writer. In this case, you can set up the cluster with a very large provisioned writer. In that case, you can still use Aurora serverless for the readers. Or suppose that the write workload for your cluster varies but the read workload is steady. In this case, you can set up your cluster with an Aurora serverless writer and one or more provisioned readers.

You can also set up a DB cluster where all the capacity is managed by Aurora serverless. To do this, you can create a new cluster and use Aurora serverless from the start. Or you can replace all the provisioned capacity in an existing cluster with Aurora serverless. For example, some of the upgrade paths from older engine versions require starting with a provisioned writer and replacing it with a Aurora serverless writer. For the procedures to create a new DB cluster with Aurora serverless or to switch an existing DB cluster to Aurora serverless, see [Creating an Aurora serverless DB cluster](aurora-serverless-v2.create.md#aurora-serverless-v2.create-cluster) and [Converting a provisioned writer or reader to Aurora serverless](aurora-serverless-v2-administration.md#aurora-serverless-v2-converting-from-provisioned).

If you don't use Aurora serverless at all in a DB cluster, all the writers and readers in the DB cluster are *provisioned*. This is the oldest and most common kind of DB cluster that most users are familiar with. In fact, before Aurora Serverless, there wasn't a special name for this kind of Aurora DB cluster. Provisioned capacity is constant. The charges are relatively easy to forecast. However, you have to predict in advance how much capacity you need. In some cases, your predictions might be inaccurate or your capacity needs might change. In these cases, your DB cluster can become underprovisioned (slower than you want) or overprovisioned (more expensive than you want).

## Aurora serverless capacity
<a name="aurora-serverless-v2.how-it-works.capacity"></a>

The unit of measure for Aurora serverless is the *Aurora capacity unit (ACU)*. Aurora serverless capacity isn't tied to the DB instance classes that you use for provisioned clusters.

Each ACU is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking. You specify the database capacity range (minimum and maximum) using this unit of measure. Aurora serverless offers capacity from 0 ACUs to 256 ACUs. With the minimum capacity of 0 ACUs, the cluster will scale to 0 when there is no workload running.The `ServerlessDatabaseCapacity` and `ACUUtilization` metrics help you to determine how much capacity your database is actually using and where that capacity falls within the specified range.

At any moment in time, each Aurora serverless DB writer or reader has a *capacity*. The capacity is represented as a floating-point number representing ACUs. The capacity increases or decreases whenever the writer or reader scales. This value is measured every second. For each DB cluster where you intend to use Aurora serverless, you define a *capacity range*: the minimum and maximum capacity values that each Aurora serverless writer or reader can scale between. The capacity range is the same for each Aurora serverless writer or reader in a DB cluster. Each Aurora serverless writer or reader has its own capacity, falling somewhere in that range.

The following table shows the Aurora serverless capacity ranges and engine version support for Aurora MySQL and Aurora PostgreSQL.


| Capacity range (ACUs) | Aurora MySQL supported versions | Aurora PostgreSQL supported versions | 
| --- | --- | --- | 
| 0.5–128 | 3.02.0 and higher | 13.6 and higher, 14.3 and higher, 15.2 and higher, 16.1 and higher | 
| 0.5–256 | 3.06.0 and higher | 13.13 and higher, 14.10 and higher, 15.5 and higher, 16.1 and higher | 
| 0–256 | 3.08.0 and higher | 13.15 and higher, 14.12 and higher, 15.7 and higher, 16.3 and higher | 

Platform versions in Aurora serverless represent improvements in performance, scaling capabilities or features. Amazon Aurora automatically manages platform version assignments at the cluster level. All new clusters, database restores, and new clones launch with the latest platform version available in your AWS Region. When a new platform version becomes available, existing clusters on previous platform versions can be upgraded directly to the latest platform version by applying the pending maintenance, stopping and restarting the cluster, or by using blue/green deployments. Amazon Aurora recommends upgrading to the latest platform version to benefit from all the latest improvements.

The following table shows the Aurora serverless platform versions with their ACU ranges and performance characteristics.


| Aurora serverless platform version | ACU range | Performance | 
| --- | --- | --- | 
| 1 | 0–128 | Baseline performance | 
| 2 | 0–256 | Baseline performance | 
| 3 | 0–256 | Up to 30% improved performance compared to platform version 2 | 
| 4 | 0-256 | Up to 30% improved performance compared to platform version 3 | 

**Note**  
The available scaling range for a given cluster is determined by both engine version and platform version. It is possible to have a more capable engine version running on a less capable platform version and vice-versa. The scaling range is determined by the lowest capable engine or platform version. Platform versions should not be confused with Aurora Serverless v1, which is a deprecated product with a different architecture.

Platform version 1, 2, and 3 are available in all regions where Aurora serverless is supported. Platform Version 4 is available in the following regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), South America (São Paulo), AWS GovCloud (US-East), and AWS GovCloud (US-West).

You can determine what platform version your cluster is running on in the Instance Configuration section of the AWS Management Console or through the API by viewing the `ServerlessV2PlatformVersion` for a [DBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBCluster.html).

The smallest Aurora serverless capacity that you can define is 0 ACUs, for Aurora serverless versions that support the auto-pause feature. You can specify a higher number if it's less than or equal to the maximum capacity value. Setting the minimum capacity to a small number lets lightly loaded DB clusters consume minimal compute resources. At the same time, they stay ready to accept connections immediately and scale up when they become busy.

We recommend setting the minimum to a value that allows each DB writer or reader to hold the working set of the application in the buffer pool. That way, the contents of the buffer pool aren't discarded during idle periods. For all the considerations when choosing the minimum capacity value, see [Choosing the minimum Aurora serverless capacity setting for a cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.min_capacity_considerations). For all the considerations when choosing the maximum capacity value, see [Choosing the maximum Aurora serverless capacity setting for a cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.max_capacity_considerations).

Depending on how you configure the readers in a Multi-AZ deployment, their capacities can be tied to the capacity of the writer or independently. For details about how to do that, see [Aurora serverless scaling](#aurora-serverless-v2.how-it-works.scaling).

Monitoring Aurora serverless involves measuring the capacity values for the writer and readers in your DB cluster over time. If your database doesn't scale down to the minimum capacity, you can take actions such as adjusting the minimum and optimizing your database application. If your database consistently reaches its maximum capacity, you can take actions such as increasing the maximum. You can also optimize your database application and spread the query load across more readers.

The charges for Aurora serverless capacity are measured in terms of ACU-hours. For information about how Aurora serverless charges are calculated, see the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/).

Suppose that the total number of writers and readers in your cluster is {{n}}. In that case, the cluster consumes approximately `n x {{minimum ACUs}}` when you aren't running any database operations. Aurora itself might run monitoring or maintenance operations that cause some small amount of load. That cluster consumes no more than `n x {{maximum ACUs}}` when the database is running at full capacity.

For more details about choosing appropriate minimum and maximum ACU values, see [Choosing the Aurora serverless capacity range for an Aurora cluster](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2-examples-setting-capacity-range-for-cluster). The minimum and maximum ACU values that you specify also affect the way some of the Aurora configuration parameters work for Aurora serverless. For details about the interaction between the capacity range and configuration parameters, see [Working with parameter groups for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.parameter-groups).

## Aurora serverless scaling
<a name="aurora-serverless-v2.how-it-works.scaling"></a>

For each Aurora serverless writer or reader, Aurora continuously tracks utilization of resources such as CPU, memory, and network. These measurements collectively are called the *load*. The load includes the database operations performed by your application. It also includes background processing for the database server and Aurora administrative tasks. When capacity is constrained by any of these, Aurora serverless scales up. Aurora serverless also scales up when it detects performance issues that it can resolve by doing so. You can monitor resource utilization and how it affects Aurora serverless scaling by using the procedures in [Important Amazon CloudWatch metrics for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.monitoring) and [Monitoring Aurora serverless performance with Performance Insights](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.performance-insights).

The load can vary across the writer and readers in your DB cluster. The writer handles all data definition language (DDL) statements, such as `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`. The writer also handles all data manipulation language (DML) statements, such as `INSERT` and `UPDATE`. Readers can process read-only statements, such as `SELECT` queries.

*Scaling* is the operation that increases or decreases Aurora serverless capacity for your database. With Aurora serverless, each writer and reader has its own current capacity value, measured in ACUs. Aurora serverless scales a writer or reader up to a higher capacity when its current capacity is too low to handle the load. It scales the writer or reader down to a lower capacity when its current capacity is higher than needed.

 Aurora serverless can increase capacity incrementally. When your workload demand begins to reach the current database capacity of a writer or reader, Aurora serverless increases the number of ACUs for that writer or reader. Aurora serverless scales capacity in the increments required to provide the best performance for the resources consumed. Scaling happens in increments as small as 0.5 ACUs. The larger the current capacity, the larger the scaling increment and thus the faster scaling can happen.

Because Aurora serverless scaling is so frequent, granular, and nondisruptive, it doesn't cause discrete events in the AWS Management Console. Instead, you can measure the Amazon CloudWatch metrics such as `ServerlessDatabaseCapacity` and `ACUUtilization` and track their minimum, maximum, and average values over time. To learn more about Aurora metrics, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md). For tips about monitoring Aurora serverless, see [Important Amazon CloudWatch metrics for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.viewing.monitoring).

You can choose to make a reader follow the capacity of the associated writer, or scale independently from the writer. You do so by specifying the promotion tier for that reader.
+ For readers in promotion tiers 0 and 1, the minimum capacity is defined by the current writer capacity and the maximum capacity is the maximum ACU value specified for the cluster. That scaling behavior makes readers in priority tiers 0 and 1 ideal for availability. That's because they are at least as large as the writer, so they can take over the workload from the writer in case of a failover. If the writer is a provisioned instance, the serverless reader's minimum capacity is the ACU equivalent of the writer's memory size.
+ Readers in promotion tiers 2–15 scale independently from the writer. Each reader remains within the minimum and maximum ACU values that you specified for your cluster. When a reader scales independently of the associated writer DB, it can become idle and scale down while the writer continues to process a high volume of transactions. It's still available as a failover target, if no other readers are available in lower promotion tiers. However, if it's promoted to be the writer, it might need to scale up to handle the full workload of the writer.

For details about promotion tiers, see [Choosing the promotion tier for an Aurora serverless reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-choosing-promotion-tier).

Aurora serverless scaling can happen while database connections are open, while SQL transactions are in process, while tables are locked, and while temporary tables are in use. Aurora serverless doesn't wait for a quiet point to begin scaling. Scaling doesn't disrupt any database operations that are underway.

If your workload requires more read capacity than is available with a single writer and a single reader, you can add multiple Aurora serverless readers to the cluster. Each Aurora serverless reader can scale within the range of minimum and maximum capacity values that you specified for your DB cluster. You can use the cluster's reader endpoint to direct read-only sessions to the readers and reduce the load on the writer.

Whether Aurora serverless performs scaling, and how fast scaling occurs once it starts, also depends on the minimum and maximum ACU settings for the cluster. In addition, it depends on whether a reader is configured to scale along with the writer or independently from it. For details about the factors that affect Aurora serverless scaling, see [Performance and scaling for Aurora serverless](aurora-serverless-v2.setting-capacity.md).

### Scaling to Zero
<a name="aurora-serverless-v2-scaling-to-zero"></a>

 In recent Aurora MySQL and Aurora PostgreSQL versions, Aurora serverless writers and readers can scale all the way down to zero ACUs. We refer to this capability as automatic pause and resume, or auto-pause. You can choose whether to allow this behavior by specifying a zero or nonzero value for the minimum capacity. You can also choose how long to wait before an Aurora serverless instance pauses. For information about which versions have this capability, see [Aurora serverless capacity](#aurora-serverless-v2.how-it-works.capacity). For information about how to use it effectively, see [Scaling to Zero ACUs with automatic pause and resume for Aurora serverless](aurora-serverless-v2-auto-pause.md). 

 In older Aurora MySQL and Aurora PostgreSQL versions, idle Aurora serverless writers and readers can scale down to the minimum ACU value that you specified for the cluster, but not all the way to zero ACUs. In that case, zero ACUs isn't available as a choice when you set the capacity range. 

 When your DB cluster with Aurora serverless capacity isn't needed for some time, you can also stop and start the entire cluster, the same as with provisioned DB clusters. This technique is most appropriate for development and test systems, where they might not be needed for many hours at a time, and the speed of resuming the cluster isn't crucial. The stop/start cluster feature is available for all Aurora serverless versions. For more information about that feature, see [Stopping and starting an Amazon Aurora DB cluster](aurora-cluster-stop-start.md). 

## Aurora serverless and high availability
<a name="aurora-serverless.ha"></a>

The way to establish high availability for an Aurora DB cluster is to make it a Multi-AZ DB cluster. A *Multi-AZ Aurora DB cluster* has compute capacity available at all times in more than one Availability Zone (AZ). That configuration keeps your database up and running even in case of a significant outage. Aurora performs an automatic failover in case of an issue that affects the writer or even the entire AZ. With Aurora serverless, you can choose for the standby compute capacity to scale up and down along with the capacity of the writer. That way, the compute capacity in the second AZ is ready to take over the current workload at any time. At the same time, the compute capacity in all AZs can scale down when the database is idle. For details about how Aurora works with AWS Regions and Availability Zones, see [High availability for Aurora DB instances](Concepts.AuroraHighAvailability.md#Concepts.AuroraHighAvailability.Instances).

The Aurora serverless Multi-AZ capability uses *readers* in addition to the writer. Support for readers is new for Aurora serverless. You can add up to 15 Aurora serverless readers spread across 3 AZs to an Aurora DB cluster.

For business-critical applications that must remain available even in case of an issue that affects your entire cluster or the whole AWS Region, you can set up an Aurora global database. You can use Aurora serverless capacity in the secondary clusters so they're ready to take over during disaster recovery. They can also scale down when the database isn't busy. For details about Aurora global databases, see [Using Amazon Aurora Global Database](aurora-global-database.md).

Aurora serverless works like provisioned for failover and other high availability features. For more information, see [High availability for Amazon Aurora](Concepts.AuroraHighAvailability.md).

Suppose that you want to ensure maximum availability for your Aurora serverless cluster. You can create a reader in addition to the writer. If you assign the reader to promotion tier 0 or 1, the reader's minimum capacity will match the current writer capacity (or writer's memory size, for provisioned writers). That way, a reader is always ready to take over for the writer in case of a failover.

Suppose that you want to run quarterly reports for your business at the same time as your cluster continues to process transactions. If you add an Aurora serverless reader to the cluster and assign it to a promotion tier from 2 through 15, you can connect directly to that reader to run the reports. Depending on how memory-intensive and CPU-intensive the reporting queries are, that reader can scale up to accommodate the workload. It can then scale down again when the reports are finished.

## Aurora serverless and storage
<a name="aurora-serverless.storage"></a>

The storage for each Aurora DB cluster consists of six copies of all your data, spread across three AZs. This built-in data replication applies regardless of whether your DB cluster includes any readers in addition to the writer. That way, your data is safe, even from issues that affect the compute capacity of the cluster.

Aurora serverless storage has the same reliability and durability characteristics as described in [Amazon Aurora storage](Aurora.Overview.StorageReliability.md). That's because the storage for Aurora DB clusters works the same whether the compute capacity uses Aurora serverless or provisioned.

## Configuration parameters for Aurora clusters
<a name="aurora-serverless-v2.parameters"></a>

You can adjust all the same cluster and database configuration parameters for clusters with Aurora serverless capacity as for provisioned DB clusters. However, some capacity-related parameters are handled differently for Aurora serverless. In a mixed-configuration cluster, the parameter values that you specify for those capacity-related parameters still apply to any provisioned writers and readers.

Almost all of the parameters work the same way for Aurora serverless writers and readers as for provisioned ones. The exceptions are some parameters that Aurora automatically adjusts during scaling, and some parameters that Aurora keeps at fixed values that depend on the maximum capacity setting.

For example, the amount of memory reserved for the buffer cache increases as a writer or reader scales up, and decreases as it scales down. That way, memory can be released when your database isn't busy. Conversely, Aurora automatically sets the maximum number of connections to a value that's appropriate based on the maximum capacity setting. That way, active connections aren't dropped if the load drops and Aurora serverless scales down. For information about how Aurora serverless handles specific parameters, see [Working with parameter groups for Aurora serverless](aurora-serverless-v2.setting-capacity.md#aurora-serverless-v2.parameter-groups).