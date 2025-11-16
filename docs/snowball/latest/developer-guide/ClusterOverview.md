AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using Amazon S3 compatible storage on Snowball Edge with a cluster of Snow devices

A cluster is a collection of three or more Snowball Edge devices used
as a single logical unit for local storage and compute purposes. A cluster offers two primary benefits over a standalone Snowball Edge device for
local storage and computing:

- **Increased durability** – The S3 data
  stored in a cluster of Snowball Edge devices enjoys increased data durability
  over a single device. In addition, the data on the cluster remains safe and
  viable, despite possible hardware outages affecting the
  cluster. Clusters can withstand the loss of one device in clusters of 3 and 4
  devices and up to two devices in clusters of 5 to 16 devices before the data is
  in danger. You can replace unhealthy nodes to maintain the durability and safety of data stored in the cluster.
- **Increased
  storage** – With
  Snowball Edge storage optimized devices, you can create a single, 16 node
  cluster with up to 2.6 PB of usable S3-compatible storage capacity. With
  Snowball Edge compute optimized devices, you can create a single, 16 node
  cluster of up to 501 TB of usable S3-compatible storage capacity.
  A cluster of Snowball Edge devices is made of leaderless nodes. Any node can write
  data to and read data from the entire cluster, and all nodes are capable of performing
  the behind-the-scenes management of the cluster.

Keep the following considerations in mind when planning to use a cluster of
Snowball Edge devices:

- We recommend that you provide a redundant power source for all devices in the cluster to reduce potential
  performance and stability issues for the cluster.
- As with standalone local storage and compute jobs, the data stored in a
  cluster can't be imported into Amazon S3 without ordering additional devices
  as a part of separate import jobs. If you order additional devices as import
  jobs, you can transfer the data from the cluster to the import job devices.
- To get data onto a cluster from Amazon S3, use the Amazon S3 API to create Amazon S3 buckets on the cluster to store and retrieve objects from S3. Also, you can use AWS DataSync to transfer objects between AWS storage services and Amazon S3 compatible storage on Snowball Edge on a Snowball Edge device. For more information, see [Configuring transfers with S3 compatible storage on Snowball Edge](../../../datasync/latest/userguide/s3-compatible-storage-snow.md "../../../datasync/latest/userguide/s3-compatible-storage-snow.md").
- You can create a job to order a cluster of devices from the AWS Snow Family Management Console, the AWS CLI, or one of the
  AWS SDKs. For more information, see
  [Getting started with Snowball Edge](getting-started.md "getting-started.md").
- Each device in the cluster has a node ID. A _node ID_
  is a unique identifier for each device in the cluster, like a job ID for a standalone device. You can get node IDs from the AWS Snow Family Management Console,
  the AWS CLI, the AWS SDKs, and the Snowball Edge client. The Snowball Edge client commands `describe-device` and `describe-cluster` return node IDs with other information about devices or the cluster.
- The lifespan of a cluster is limited by the security certificate granted
  to the cluster devices when the cluster is provisioned. By default,
  Snowball Edge devices can be used for up to 360 days before they need to
  be returned. At the end of that time, the devices stop responding to
  read/write requests. If you need to keep one or more devices for longer than
  360 days, contact AWS Support.
- When AWS receives a returned device that was part of a cluster, we
  perform a complete erasure of the device. This erasure follows the National
  Institute of Standards and Technology (NIST) 800-88 standards.

| Amazon S3 compatible storage on Snowball Edge cluster fault tolerance and storage capacity | Cluster size          | Fault tolerance | Storage capacity of Snowball Edge Compute Optimized (Compute<br>Optimized with AMD EPYC Gen2 and NVMe) devices (in TB) | Storage capacity of Snowball Edge storage optimized 210 TB<br>devices (in TB) |
| ------------------------------------------------------------------------------------------ | --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 3                                                                                          | Loss of up to 1 node  | 38              | 438                                                                                                                    |
| 4                                                                                          | Loss of up to 1 node  | 57              | 657                                                                                                                    |
| 5                                                                                          | Loss of up to 2 nodes | 57              | 657                                                                                                                    |
| 6                                                                                          | Loss of up to 2 nodes | 76              | 904                                                                                                                    |
| 7                                                                                          | Loss of up to 2 nodes | 95              | 1096                                                                                                                   |
| 8                                                                                          | Loss of up to 2 nodes | 114             | 1315                                                                                                                   |
| 9                                                                                          | Loss of up to 2 nodes | 133             | 1534                                                                                                                   |
| 10                                                                                         | Loss of up to 2 nodes | 152             | 1754                                                                                                                   |
| 11                                                                                         | Loss of up to 2 nodes | 165             | 1970                                                                                                                   |
| 12                                                                                         | Loss of up to 2 nodes | 171             | 1973                                                                                                                   |
| 13                                                                                         | Loss of up to 2 nodes | 190             | 2192                                                                                                                   |
| 14                                                                                         | Loss of up to 2 nodes | 209             | 2411                                                                                                                   |
| 15                                                                                         | Loss of up to 2 nodes | 225             | 2625                                                                                                                   |
| 16                                                                                         | Loss of up to 2 nodes | 228             | 2631                                                                                                                   |

After you unlock a cluster, you're ready to store and access data on that
cluster. You can use the Amazon S3 compatible endpoint to read from and write data to
a cluster.

To read from or write data to a cluster, you must have a read/write quorum
with no more than the allowed number of unavailable nodes in your cluster of
devices.

## Snowball Edge cluster quorums

A _quorum_ represents the minimum number of
Snowball Edge devices in a cluster that must be communicating with each other to
maintain a read/write quorum.

When all devices in a cluster are healthy, you have a _read/write quorum_ for
your cluster. If one or two of those devices goes offline, you reduce the operational
capacity of the cluster. However, you can still read and write to the cluster. With all but one or two devices the cluster operating, the cluster still
has a read/write quorum. The number of nodes that can go offline before the
operational capacity of the cluster is affected is found in [this table](#cluster-table "#cluster-table").

Quorom may be lost if a cluster loses more than the number of devices
indicated in [this table](#cluster-table "#cluster-table"). When a
quorom is lost, the cluster is offline and the data in the cluster is
unavailable. You might be able fix this, or the data might be permanently lost,
depending on the severity of the event. If it is a temporary external power event,
and you can power the Snowball Edge devices back on and unlock all the nodes
in the cluster, your data is available again.

###### Important

If a minimum quorum of healthy nodes doesn't exist, contact AWS Support.

You can use the `describe-cluster` command to view the lock state and network reachability of each node. Ensuring that the devices in your
cluster are healthy and connected is an administrative responsibility that you take
on when you using cluster storage. For more information, see [Getting device status](using-client-commands.md#client-status "using-client-commands.md#client-status").

If you determine one or more nodes are unhealthy, you can replace nodes in the cluster to maintain quorom and the health and stability of your data. For more information, see [Replacing a node in a cluster](replacement.md "replacement.md").
