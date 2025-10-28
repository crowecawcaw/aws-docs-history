Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for using Amazon Redshift provisioned

clusters

After your cluster is created, you can find information in this section about regions
where features are available, maintenance tasks, node types, and usage limits.

## Region and Availability Zone considerations

Amazon Redshift is available in several AWS Regions. By default, Amazon Redshift provisions your
cluster in a randomly selected Availability Zone (AZ) within the AWS Region that you
choose. All the cluster nodes are provisioned in the same Availability Zone.

You can optionally request a specific Availability Zone if Amazon Redshift is available in
that zone. For example, if you already have an Amazon EC2 instance running in one
Availability Zone, you might want to create your Amazon Redshift cluster in the same zone to
reduce latency. On the other hand, you might want to choose another Availability Zone
for higher availability. Amazon Redshift might not be available in all Availability Zones
within an AWS Region.

For a list of supported AWS Regions where you can provision an Amazon Redshift cluster,
see [Amazon Redshift endpoints](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md") in the
_Amazon Web Services General Reference_.

## Cluster maintenance

Amazon Redshift periodically performs maintenance to apply upgrades to your cluster. During
these updates, your Amazon Redshift cluster isn't available for normal operations. You
have several ways to control how we maintain your cluster. For example, you can control
when we deploy updates to your clusters. You can also choose whether your cluster runs
the most recently released version, or the version released previously to the most
recently released version. Finally, you have the option to defer non-mandatory
maintenance updates for a period of time.

### Maintenance windows

Amazon Redshift assigns a 30-minute maintenance window at random from an 8-hour block of
time per AWS Region, occurring on a random day of the week (Monday through Sunday,
inclusive).

#### Default maintenance

windows

The following list shows the time blocks for each AWS Region from which the
default maintenance windows are assigned:

- US East (N. Virginia) Region: 03:00–11:00 UTC
- US East (Ohio) Region: 03:00–11:00 UTC
- US West (N. California) Region: 06:00–14:00 UTC
- US West (Oregon) Region: 06:00–14:00 UTC
- Africa (Cape Town) Region: 20:00–04:00 UTC
- Asia Pacific (Hong Kong) Region: 13:00–21:00 UTC
- Asia Pacific (Hyderabad) Region: 16:30–00:30 UTC
- Asia Pacific (Jakarta) Region: 15:00–23:00 UTC
- Asia Pacific (Malaysia) Region: 14:00–22:00 UTC
- Asia Pacific (Melbourne) Region: 12:00–20:00 UTC
- Asia Pacific (Mumbai) Region: 16:30–00:30 UTC
- Asia Pacific (New Zealand) Region: 10:00–18:00 UTC
- Asia Pacific (Osaka) Region: 13:00–21:00 UTC
- Asia Pacific (Seoul) Region: 13:00–21:00 UTC
- Asia Pacific (Singapore) Region: 14:00–22:00 UTC
- Asia Pacific (Sydney) Region: 12:00–20:00 UTC
- Asia Pacific (Taipei) Region: 14:00–22:00 UTC
- Asia Pacific (Thailand) Region: 15:00–23:00 UTC
- Asia Pacific (Tokyo) Region: 13:00–21:00 UTC
- Canada (Central) Region: 03:00–11:00 UTC
- Canada West (Calgary) Region: 04:00–12:00 UTC
- China (Beijing) Region: 13:00–21:00 UTC
- China (Ningxia) Region: 13:00–21:00 UTC
- Europe (Frankfurt) Region: 06:00–14:00 UTC
- Europe (Ireland) Region: 22:00–06:00 UTC
- Europe (London) Region: 22:00–06:00 UTC
- Europe (Milan) Region: 21:00–05:00 UTC
- Europe (Paris) Region: 23:00–07:00 UTC
- Europe (Stockholm) Region: 23:00–07:00 UTC
- Europe (Zurich) Region: 20:00–04:00 UTC
- Israel (Tel Aviv) Region: 20:00–04:00 UTC
- Mexico (Central) Region: 04:00–12:00 UTC
- Europe (Spain) Region: 21:00–05:00 UTC
- Middle East (Bahrain) Region: 13:00–21:00 UTC
- Middle East (UAE) Region: 18:00–02:00 UTC
- South America (São Paulo) Region: 19:00–03:00 UTC

If a maintenance event is scheduled for a given week, it starts during the
assigned 30-minute maintenance window. While Amazon Redshift is performing maintenance,
it terminates any queries or other operations that are in progress. Most
maintenance completes during the 30-minute maintenance window, but some
maintenance tasks might continue running after the window closes. If there are
no maintenance tasks to perform during the scheduled maintenance window, your
cluster continues to operate normally until the next scheduled maintenance
window.

You can change the scheduled maintenance window by modifying the cluster,
either programmatically or by using the Amazon Redshift console. You can find the
maintenance window and set the day and time it occurs for the cluster under the
**Maintenance** tab.

It is possible for a cluster to restart outside of a maintenance window. There are
a few reasons this can occur. One more common reason is that an issue has been
detected with the cluster and maintenance operations are being performed to bring it
back to a healthy state. For more information, see the article [Why did my
Amazon Redshift cluster reboot outside of the maintenance window?](https://repost.aws/knowledge-center/redshift-reboot-maintenance-window "https://repost.aws/knowledge-center/redshift-reboot-maintenance-window"), which provides
details regarding why this might occur.

### Deferring maintenance

To reschedule your cluster's maintenance window, you can defer maintenance by
up to 45 days. For example, if your cluster's maintenance window is set to
Wednesday 08:30 – 09:00 UTC and you need to access your cluster at that time, you
can defer the maintenance to a later time period.

If you defer maintenance, Amazon Redshift will still apply hardware updates or other
mandatory security updates to your cluster. Your cluster isn't available during
these updates.

If a hardware update or other mandatory security update is scheduled during the
upcoming maintenance window, Amazon Redshift sends you advance notifications under the
_Pending_ category. To learn more about
_Pending_ event notifications, see [Amazon Redshift provisioned cluster event
notifications](working-with-event-notifications.md "working-with-event-notifications.md").

You can also choose to receive event notifications from Amazon Simple Notification Service (Amazon SNS). For
more information about subscribing to event notifications from Amazon SNS, see [Amazon Redshift cluster event
notification subscriptions](working-with-event-notifications-subscribe.md "working-with-event-notifications-subscribe.md").

If you defer your cluster's maintenance, the maintenance window following the
period of deferment can't be deferred.

###### Note

You can't defer maintenance after it has started.

For more information about cluster maintenance, see the following
documentation:

- [Maintenance windows](#rs-maintenance-windows "#rs-maintenance-windows")
- [Cluster operations](managing-cluster-operations.md "managing-cluster-operations.md")
- [Modifying a cluster](modify-cluster.md "modify-cluster.md")

### Choosing cluster maintenance

tracks

When Amazon Redshift releases a new cluster version, your cluster is updated during its
maintenance window. You can control whether your cluster is updated to the most
recent release or to the previous release.

The track controls which cluster version is applied during a
maintenance window. When Amazon Redshift releases a new cluster version, that version is
assigned to the _current_ track, and the previous
version is assigned to the _trailing_ track.

For information about cluster tracks, see [Tracks for Amazon Redshift provisioned
clusters and serverless workgroups](tracks.md "tracks.md").

### Understanding how RA3 nodes

separate compute and storage

These sections detail tasks available for RA3 node types, showing their applicability
to a collection of use cases and detailing their advantages over previously available
node types.

#### Advantages and availability of RA3 nodes

RA3 nodes provide the following advantages:

- They are flexible to grow your compute capacity without increasing your
  storage costs. And they scale your storage without over-provisioning compute
  capacity.
- They use high performance SSDs for your hot data and Amazon S3 for cold data.
  Thus they provide ease of use, cost-effective storage, and high query
  performance.
- They use high bandwidth networking built on the AWS Nitro System to
  further reduce the time taken for data to be offloaded to and retrieved from
  Amazon S3.

Consider choosing RA3 node types in these cases:

- You need the flexibility to scale and pay for compute separate from
  storage.
- You query a fraction of your total
  data.
- Your data volume is growing rapidly or is expected to grow rapidly.
- You want the flexibility to size the cluster based only on your
  performance needs.

To use RA3 node types, your AWS Region must support RA3. For more information,
see [RA3 node type availability in AWS
Regions](#ra3-regions "#ra3-regions").

###### Important

You can use ra3.xlplus node types only with cluster version 1.0.21262 or
later. You can view the version of an existing cluster with the Amazon Redshift console.
For more information, see [Determining the workgroup or cluster
version](tracks.md#cluster-version "tracks.md#cluster-version").

Make sure that you use the new Amazon Redshift console when working with RA3 node types.

In addition, to use RA3 node types with Amazon Redshift operations that use the
track, the maintenance track value must be set to a cluster version
that supports RA3. For more information about tracks, see [Choosing cluster maintenance
tracks](#rs-mgmt-maintenance-tracks "#rs-mgmt-maintenance-tracks").

Consider the following when using single-node RA3 node types.

- Datasharing producers and consumers are supported.
- To
  change node types, only classic resize is supported. Changing the node type
  with elastic resize or snapshot restore isn't supported. The following
  scenarios are supported:
  - Classic resize of a 1-node dc2.xlarge to a 1-node ra3.xlplus, and
    vice versa.
  - Classic resize of a 1-node dc2.xlarge to a multiple-node
    ra3.xlplus, and vice versa.
  - Classic resize of a multiple-node dc2.xlarge to a 1-node
    ra3.xlplus, and vice versa.

##### Working with Amazon Redshift managed storage

With Amazon Redshift managed storage, you can store and process all your data in Amazon Redshift
while getting more flexibility to scale compute and storage capacity separately.
You continue to ingest data with the COPY or INSERT command. To optimize
performance and manage automatic data placement across tiers of storage, Amazon Redshift
takes advantage of optimizations such as data block temperature, data block age,
and workload patterns. When needed, Amazon Redshift scales storage automatically to Amazon S3
without requiring any manual action.

For information about storage costs, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

##### Managing RA3 node types

To take advantage of separating compute from storage, you can create or
upgrade your cluster with the RA3 node type. To use the RA3 node types, create
your clusters in a virtual private cloud (EC2-VPC).

To change the number of nodes of Amazon Redshift cluster with an RA3 node type, do one of
the following:

- Add or remove nodes with the elastic resize operation. In some
  situations, removing nodes from a RA3 cluster isn't allowed with elastic
  resize. For example, when a 2:1 node count upgrade puts the number of
  slices per node at 32. For more information, see [Resizing a cluster](resizing-cluster.md "resizing-cluster.md").
  If elastic resize isn't available, use
  classic resize.
- Add or remove nodes with the classic resize operation. Choose this
  option when you are resizing to a configuration that isn't available
  through elastic resize. Elastic resize is quicker than classic resize.
  For more information, see [Resizing a cluster](resizing-cluster.md "resizing-cluster.md").

### RA3 node type availability in AWS

Regions

The RA3 node types are available only in the following AWS Regions:

- US East (N. Virginia) Region (us-east-1)
- US East (Ohio) Region (us-east-2)
- US West (N. California) Region (us-west-1)
- US West (Oregon) Region (us-west-2)
- Africa (Cape Town) Region (af-south-1)
- Asia Pacific (Hong Kong) Region (ap-east-1)
- Asia Pacific (Hyderabad) Region (ap-south-2)
- Asia Pacific (Jakarta) Region (ap-southeast-3)
- Asia Pacific (Malaysia) Region (ap-southeast-5)
- Asia Pacific (Melbourne) Region (ap-southeast-4)
- Asia Pacific (Mumbai) Region (ap-south-1)
- Asia Pacific (New Zealand) Region (ap-southeast-6)
- Asia Pacific (Osaka) Region (ap-northeast-3)
- Asia Pacific (Seoul) Region (ap-northeast-2)
- Asia Pacific (Singapore) Region (ap-southeast-1)
- Asia Pacific (Sydney) Region (ap-southeast-2)
- Asia Pacific (Taipei) Region (ap-east-2)
- Asia Pacific (Thailand) Region (ap-southeast-7)
- Asia Pacific (Tokyo) Region (ap-northeast-1)
- Canada (Central) Region (ca-central-1)
- Canada West (Calgary) Region (ca-west-1)
- China (Beijing) Region (cn-north-1)
- China (Ningxia) Region (cn-northwest-1)
- Europe (Frankfurt) Region (eu-central-1)
- Europe (Zurich) Region (eu-central-2)
- Europe (Ireland) Region (eu-west-1)
- Europe (London) Region (eu-west-2)
- Europe (Milan) Region (eu-south-1)
- Europe (Spain) Region (eu-south-2)
- Europe (Paris) Region (eu-west-3)
- Europe (Stockholm) Region (eu-north-1)
- Israel (Tel Aviv) Region (il-central-1)
- Mexico (Central) Region (mx-central-1)
- Middle East (Bahrain) Region (me-south-1)
- Middle East (UAE) Region (me-central-1)
- South America (São Paulo) Region (sa-east-1)
- AWS GovCloud (US-East) (us-gov-east-1)
- AWS GovCloud (US-West) (us-gov-west-1)

### Upgrading to RA3 node types

To upgrade your existing node type to RA3, you have the following options to
change the node type:

- Restore from a snapshot – Amazon Redshift uses the most recent snapshot of
  your cluster and restores it to create a new RA3 cluster. As soon as the
  cluster creation is complete (usually within minutes), RA3 nodes are ready
  to run your full production workload. As compute is separate from storage,
  hot data is brought in to the local cache at fast speeds thanks to a large
  networking bandwidth. If you restore from the latest

DC2 snapshot, RA3 preserves hot block information of the DC2 workload and
populates its local cache with the hottest blocks. For more information, see
[Restoring a cluster
from a snapshot](working-with-snapshot-restore-cluster-from-snapshot.md "working-with-snapshot-restore-cluster-from-snapshot.md").

To keep the same endpoint for your applications and users, you can rename
the new RA3 cluster with the same name as the original DC2 cluster. To
rename the cluster, modify the cluster in the Amazon Redshift console or
`ModifyCluster` API operation. For more information, see
[Renaming a cluster](rs-mgmt-rename-cluster.md "rs-mgmt-rename-cluster.md") or [`ModifyCluster` API operation](../APIReference/API_ModifyCluster.md "../APIReference/API_ModifyCluster.md") in the
_Amazon Redshift API Reference_.

- Elastic resize – resize the cluster using elastic resize. When you
  use elastic resize to change node type, Amazon Redshift automatically creates a
  snapshot, creates a new cluster, deletes the old cluster, and renames the
  new cluster. The elastic resize operation can be run on-demand or can be
  scheduled to run at a future time. You can quickly upgrade your existing

DC2 node type clusters to RA3 with elastic resize. For more information, see
[Elastic resize](resizing-cluster.md#elastic-resize "resizing-cluster.md#elastic-resize").

The following table shows recommendations when upgrading to RA3 node types. (These
recommendations also apply to reserved nodes.)

The recommendations in this table are starting cluster node types and sizes but
depend on the computing requirements of your workload. To better estimate your
requirements, consider conducting a proof of concept (POC) that uses [Test Drive](https://github.com/aws/redshift-test-drive/tree/main "https://github.com/aws/redshift-test-drive/tree/main") to
run potential configurations. Provision a cluster for your POC data warehouse
instead of Redshift Serverless. For more information about conducting a proof of concept, see
[Conduct a proof of
concept (POC) for Amazon Redshift](../dg/proof-of-concept-playbook.md "../dg/proof-of-concept-playbook.md") in the
_Amazon Redshift Database Developer Guide_.

| Existing node type | Existing number of nodes | Recommended new node type | Upgrade action                                                                                                                                                                                                                                                    |
| ------------------ | ------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dc2.8xlarge        | 2–15                     | ra3.4xlarge               | Start with 2 nodes of ra3.4xlarge for every 1 node of dc2.8xlarge1.                                                                                                                                                                                               |
| dc2.8xlarge        | 16–128                   | ra3.16xlarge              | Start with 1 node of ra3.16xlarge for every 2 nodes of dc2.8xlarge1.                                                                                                                                                                                              |
| dc2.large          | 1–4                      | ra3.large                 | Start with 1 node of ra3.large for every 1 node of dc2.large1. Start with 2 nodes of ra3.large for every 2 nodes of dc2.large1. Start with 3 nodes of ra3.large for every 3 nodes of dc2.large1. Start with 3 nodes of ra3.large for every 4 nodes of dc2.large1. |
| dc2.large          | 5–15                     | ra3.xlplus                | Start with 3 nodes of ra3.xlplus for every 8 nodes of dc2.large1.                                                                                                                                                                                                 |
| dc2.large          | 16–32                    | ra3.4xlarge               | Start with 1 node of ra3.4xlarge for every 8 nodes of dc2.large1,2.                                                                                                                                                                                               | 1Extra nodes might be needed depending on workload requirements. Add or remove nodes based on the compute requirements of your required query performance. 2Clusters with the dc2.large node type are limited to 32 nodes. The minimum number of nodes for some RA3 node types is 2 nodes. Take this into consideration when creating an RA3 cluster. ### Networking features supported by RA3 nodes RA3 nodes support a collection of networking features not available to other node types. This section provides brief descriptions of each feature and links to additional documentation: <br>• **Provisioned-cluster VPC endpoint** – When you create or restore an RA3 cluster, Amazon Redshift uses a port within the ranges of 5431-5455 or 8191-8215. When the cluster is set to a port in one of these ranges, Amazon Redshift automatically creates a VPC endpoint in your AWS account for the cluster and attaches a private IP address to it. If you set the cluster to publicly-accessible, Redshift creates an elastic IP address in your AWS account and attaches it to the VPC endpoint. For more information, see [Configuring security group communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup](rs-security-group-public-private.md "rs-security-group-public-private.md"). <br>• **Single-subnet RA3 clusters** – You can create an RA3 cluster with a single subnet, but it can't use disaster-recovery features. An exception occurs if you enable cluster relocation when the subnet doesn't have multiple Availability Zones (AZs). <br>• **Multi-subnet RA3 clusters and subnet groups** – You can create an RA3 cluster with multiple subnets by creating a subnet group when you provision the cluster in your virtual private cloud (VPC). A cluster subnet group allows you to specify a set of subnets in your VPC and Amazon Redshift creates the cluster in one of them. After creating a subnet group, you can remove subnets you previously added, or add more. For more information, see [Amazon Redshift cluster subnet groups](working-with-cluster-subnet-groups.md "working-with-cluster-subnet-groups.md"). <br>• **Cross-account or cross-VPC endpoint access** – You can access a provisioned cluster or Amazon Redshift Serverless workgroup by setting up a Redshift-managed VPC endpoint. You can set it up as a private connection between a VPC that contains a cluster or workgroup and a VPC where you run a client tool, for example. By doing this, you can access the data warehouse without using a public IP address and without routing traffic through the internet. For more information, see [Working with Redshift-managed VPC endpoints](managing-cluster-cross-vpc.md "managing-cluster-cross-vpc.md"). <br>• **Cluster relocation** – You can move a cluster to another Availability Zone (AZ) without any loss of data when there is an interruption of service. You enable it on the console. For more information, see [Relocating a cluster](managing-cluster-recovery.md "managing-cluster-recovery.md"). <br>• **Custom domain name** – You can create a custom domain name, also known as a custom URL, for your Amazon Redshift cluster. It's an easy-to-read DNS record that routes SQL-client connections to your cluster endpoint. For more information, see [Custom domain names for client connections](connecting-connection-CNAME.md "connecting-connection-CNAME.md"). |
