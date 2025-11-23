# How Amazon DocumentDB serverless works

###### Topics

- [Overview](#docdb-serverlerss-overviewn "#docdb-serverlerss-overviewn")
- [Configurations for Amazon DocumentDB clusters](#docdb-serverlerss-configuration "#docdb-serverlerss-configuration")
- [Amazon DocumentDB serverless scaling capacity](#docdb-serverless-scaling-capacity "#docdb-serverless-scaling-capacity")
- [Amazon DocumentDB serverless scaling](#docdb-serverless-scaling "#docdb-serverless-scaling")
- [Idle state (0.5 DCUs)](#docdb-serverlerss-idle-state "#docdb-serverlerss-idle-state")

## Overview

Amazon DocumentDB serverless is suitable for the most demanding, highly variable workloads.
For example, your database usage might be heavy for a short period of time, followed by long periods of light activity or no activity at all.
Some examples are retail, gaming, or sports websites with periodic promotional events, and databases that produce reports when needed.
Others are development and testing environments, and new applications where usage might ramp up quickly.
For cases such as these and many others, configuring capacity correctly in advance isn't always possible with the provisioned model.
It can also result in higher costs if you overprovision and have capacity that you don't use.

In contrast, DocumentDB provisioned clusters are suitable for steady workloads.
With provisioned clusters, you choose a instance class that has a predefined amount of memory, CPU power, I/O bandwidth, and so on.
If your workload changes, you manually modify the instance class of your writer and readers.
The provisioned model works well when you can adjust capacity in advance of expected consumption patterns and it's acceptable to have brief outages while you change the instance class of the writer and readers in your cluster.

DocumentDB serverless is architected from the ground up to support serverless clusters that are instantly scalable.
DocumentDB serverless is engineered to provide the same degree of security and isolation as with provisioned writers and readers.
These aspects are crucial in multitenant serverless cloud environments.
The dynamic scaling mechanism has very little overhead so that it can respond quickly to changes in the database workload.
It's also powerful enough to meet dramatic increases in processing demand.

By using DocumentDB serverless, you can create an DocumentDB cluster without being locked into a specific database capacity for each writer and reader.
You specify the minimum and maximum capacity range.
DocumentDB scales each DocumentDB serverless writer or reader in the cluster within that capacity range.
By using a Multi-AZ cluster where each writer or reader can scale dynamically, you can take advantage of dynamic scaling and high availability.

DocumentDB serverless scales the database resources automatically based on your minimum and maximum capacity specifications.
Scaling is fast because most scaling events operations keep the writer or reader on the same host.
In the rare cases that an DocumentDB serverless writer or reader is moved from one host to another, DocumentDB serverless manages the connections automatically.
You don't need to change your database client application code or your database connection strings.

With DocumentDB serverless, as with provisioned clusters, storage capacity and compute capacity are separate.
When we refer to DocumentDB serverless capacity and scaling, it's always compute capacity that's increasing or decreasing.
Thus, your cluster can contain many terabytes of data even when the CPU and memory capacity scale down to low levels.

Instead of provisioning and managing database servers, you specify database capacity.
The actual capacity of each DocumentDB serverless writer or reader varies over time, depending on your workload.
For details about that mechanism, see [Amazon DocumentDB serverless scaling](#docdb-serverless-scaling "#docdb-serverless-scaling").

## Configurations for Amazon DocumentDB clusters

For each of your Amazon DocumentDB clusters, you can choose any combination of DocumentDB serverless capacity, provisioned capacity, or both.

You can set up a cluster that contains both DocumentDB serverless and provisioned capacity, called a mixed-configuration cluster.
For example, suppose that you need more read/write capacity than is available for an DocumentDB serverless writer.
In this case, you can set up the cluster with a very large provisioned writer.
Then you can still use DocumentDB serverless for the readers.
Or suppose that the write workload for your cluster varies but the read workload is steady.
In this case, you can set up your cluster with an DocumentDB serverless writer and one or more provisioned readers.

You can also set up a cluster where all the capacity is managed by DocumentDB serverless.
To do this, you can create a new cluster and use DocumentDB serverless from the start.
Or you can replace all the provisioned capacity in an existing cluster with DocumentDB serverless.
For the procedures to create a new cluster with DocumentDB serverless or to switch an existing cluster to DocumentDB serverless, see [Creating a cluster that uses Amazon DocumentDB serverless](docdb-serverless-create-cluster.md "docdb-serverless-create-cluster.md") and [Migrating to Amazon DocumentDB serverless](docdb-serverless-migrating.md "docdb-serverless-migrating.md").

If you don't use DocumentDB serverless at all in a cluster, all the writers and readers in the cluster are provisioned.
This is the most common kind of cluster that most users are familiar with.
Provisioned capacity is constant.
The charges are relatively easy to forecast.
However, you have to predict in advance how much capacity you need.
In some cases, your predictions might be inaccurate or your capacity needs might change.
In these cases, your cluster can become underprovisioned (slower than you want) or overprovisioned (more expensive than you want).

## Amazon DocumentDB serverless scaling capacity

The unit of measure for Amazon DocumentDB serverless is the DocumentDB Capacity Unit (DCU).
DocumentDB serverless scaling capacity isn't tied to the instance classes that you use for provisioned clusters.

Each DCU is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking.
You specify the database capacity range using this unit of measure.
The `ServerlessDatabaseCapacity` and `DCUUtilization` CloudWatch metrics help you to determine how much capacity your database is actually using and where that capacity falls within the specified range.

At any moment in time, each DocumentDB serverless writer or reader has a capacity.
The capacity is a floating-point number representing DCUs.
The capacity increases or decreases whenever the writer or reader scales.
This value is measured every second.
For each cluster where you intend to use DocumentDB serverless, you define a capacity range: the minimum and maximum capacity values that each DocumentDB serverless writer or reader can scale between.
The capacity range is the same for each DocumentDB serverless writer or reader in a cluster.
Each DocumentDB serverless writer or reader has its own capacity, falling somewhere in that range.

DocumentDB serverless is supported on DocumentDB 5.0.0 and higher with a capacity range of 0.5 - 256 DCUs.

The smallest DocumentDB serverless capacity that you can define is 0.5 DCUs.
You can specify a higher number if it's less than or equal to the maximum supported capacity value.
Setting the minimum capacity to a small number lets lightly loaded clusters consume minimal compute resources.
At the same time, they stay ready to accept connections immediately and scale up when they become busy.

We recommend setting the minimum to a value that allows each writer or reader to hold the working set of the application in the buffer pool.
That way, the contents of the buffer pool aren't discarded during idle periods.
For all the considerations when choosing the scaling capacity range, see [Choosing the scaling capacity range for a DocumentDB serverless cluster](docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing "docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing").

Depending on how you configure the readers in a Multi-AZ deployment, their capacities can be tied to the capacity of the writer or independently.
For details about how to do that, see [Viewing and modifying the promotion tier of serverless readers](docdb-serverless-managing.md#docdb-serverless-promo-tier "docdb-serverless-managing.md#docdb-serverless-promo-tier").

Monitoring DocumentDB serverless involves measuring the capacity values for the writer and readers in your cluster over time.
If your database doesn't scale down to the minimum capacity, you can take actions such as adjusting the minimum and optimizing your database application.
If your database consistently reaches its maximum capacity, you can take actions such as increasing the maximum.
You can also optimize your database application and spread the query load across more readers.

The charges for DocumentDB serverless capacity are measured in terms of DCU-hours.
For information about how DocumentDB serverless charges are calculated, see [Amazon DocumentDB pricing](https://aws.amazon.com//documentdb/pricing "https://aws.amazon.com//documentdb/pricing").
Suppose that the total number of writers and readers in your cluster is n.
In that case, the cluster consumes approximately n x minimum DCUs when you aren't running any database operations.
Amazon DocumentDB itself might run monitoring or maintenance operations that cause some small amount of load.
That cluster consumes no more than n x maximum DCUs when the database is running at full capacity.

For more details about choosing appropriate minimum and maximum DCU values, see [Choosing the scaling capacity range for a DocumentDB serverless cluster](docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing "docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing").
The minimum and maximum DCU values that you specify also affect some Amazon DocumentDB instance limits.
For details about the interaction between the capacity range and instance limits, see [Amazon DocumentDB serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md").

## Amazon DocumentDB serverless scaling

For each DocumentDB serverless writer or reader, Amazon DocumentDB continuously tracks utilization of resources such as CPU, memory, and network.
These measurements collectively are called the load.
The load includes the database operations performed by your application.
It also includes background processing for the database server and Amazon DocumentDB administrative tasks.
When capacity is constrained by any of these, DocumentDB serverless scales up.
DocumentDB serverless also scales up when it detects performance issues that it can resolve by doing so.
You can monitor resource utilization and how it affects DocumentDB serverless scaling by using the procedures in [Monitoring Amazon DocumentDB serverless](docdb-serverless-monitoring.md "docdb-serverless-monitoring.md").

The load can vary across the writer and readers in your cluster.
The writer handles write operations, and performs all the data modifications to the cluster volume.
Readers can process read-only requests.

Scaling is the operation that increases or decreases DocumentDB serverless capacity for your database.
With DocumentDB serverless, each writer and reader has its own current capacity value, measured in DCUs.
DocumentDB serverless scales a writer or reader up to a higher capacity when its current capacity is too low to handle the load.
It scales the writer or reader down to a lower capacity when its current capacity is higher than needed.

DocumentDB serverless can increase capacity incrementally.
When your workload demand begins to reach the current database capacity of a writer or reader, DocumentDB serverless increases the number of DCUs for that writer or reader.
DocumentDB serverless scales capacity in the increments required to provide the best performance for the resources consumed.
Scaling happens in increments as small as 0.5 DCUs.
The larger the current capacity, the larger the scaling increment and thus the faster scaling can happen.

Because DocumentDB serverless scaling is so frequent, granular, and nondisruptive, it doesn't cause discrete events in the AWS Management Console.
Instead, you can measure the Amazon CloudWatch metrics such as `serverlessDatabaseCapacity` and `DCUUtilization`, and track their minimum, maximum, and average values over time.
To learn more about monitoring DocumentDB serverless, see [Monitoring Amazon DocumentDB serverless](docdb-serverless-monitoring.md "docdb-serverless-monitoring.md").

Scaling up or down can be caused by the following:

- Memory utilization
- CPU utilization
- Network utilization
- Storage utilization

You can monitor these causes of scaling up/down on DocumentDB serverless instances.
For more information, see [Monitoring Amazon DocumentDB serverless](docdb-serverless-monitoring.md "docdb-serverless-monitoring.md").

You can choose to make a reader scale at the same time as the associated writer, or independently from the writer.
You do so by specifying the promotion tier for that reader.

- DocumentDB serverless readers, in promotion tiers 0 and 1, scale at the same time as the writer.
  That scaling behavior makes readers in priority tiers 0 and 1 ideal for availability.
  That's because they are always sized to the right capacity to take over the workload from the writer in case of failover.
- Readers in promotion tiers 2–15 scale independently from the writer.
  Each reader remains within the minimum and maximum DCU values that you specified for your cluster.
  When a reader scales independently of the associated writer DB, it can become idle and scale down while the writer continues to process a high volume of transactions.
  It's still available as a failover target, if no other readers are available in lower promotion tiers.
  However, if it's promoted to be the writer, it might need to scale up to handle the full workload of the writer.

For details about viewing and changing promotion tiers of serverless instances, see [Viewing and modifying the promotion tier of serverless readers](docdb-serverless-managing.md#docdb-serverless-promo-tier "docdb-serverless-managing.md#docdb-serverless-promo-tier").

DocumentDB serverless scaling can happen while database connections are open, while transactions are in process, etc.
DocumentDB serverless doesn't wait for a quiet point to begin scaling.
Scaling doesn't disrupt any database operations that are underway.

If your workload requires more read capacity than is available with a single writer and a single reader, you can add multiple DocumentDB serverless readers to the cluster.
Each DocumentDB serverless reader can scale within the range of minimum and maximum capacity values that you specified for your cluster.
You can use the cluster's reader endpoint to direct read-only sessions to the readers and reduce the load on the writer.

Whether DocumentDB serverless performs scaling, and how fast scaling occurs once it starts, also depends on the minimum and maximum DCU settings for the cluster.
In addition, it depends on whether a reader is configured to scale along with the writer or independently from it.
For details about the scaling configuration, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md "docdb-serverless-scaling-config.md").

## Idle state (0.5 DCUs)

When Amazon DocumentDB serverless writers or readers are idle, DocumentDB serverless instances support scaling down to an idle state of 0.5 DCUs if the cluster’s MinCapacity is configured to be 0.5.

In the idle state, the DocumentDB serverless instances do not have sufficient CPU compute capacity to support most production workloads, but are ready to quickly scale up to support a new workload.
In a non-idle state, DocumentDB serverless instances typically require at least 1.0 - 2.5 DCUs.
Therefore, when DocumentDB serverless instances scale up from an idle state to a non-idle state, they will scale up directly to 1.0 - 2.5 DCUs (or the value of MaxCapacity if it is lower).

In order to support scaling down to 0.5 DCUs when idle, instance limits are capped if the MinCapacity is configured to be less than or equal to 1.0 DCUs.
For more information on how the limits are affected by the MinCapacity configuration, see [Amazon DocumentDB serverless instance limits](docdb-serverless-instance-limits.md "docdb-serverless-instance-limits.md").
