# Placement strategies for your placement groups

You can create a placement group for your EC2 instances using one of the following
placement strategies.

###### Placement strategies

- [Cluster placement groups](#placement-groups-cluster "#placement-groups-cluster")
- [Partition placement groups](#placement-groups-partition "#placement-groups-partition")
- [Spread placement groups](#placement-groups-spread "#placement-groups-spread")

## Cluster placement groups

A cluster placement group is a logical grouping of instances within a single
Availability Zone. Instances are not isolated to a single rack. A cluster placement
group can span peered virtual private networks (VPCs) in the same Region. Instances
in the same cluster placement group enjoy a higher per-flow throughput limit for
TCP/IP traffic and are placed in the same high-bisection bandwidth segment of the
network.

The following image shows instances that are placed into a cluster placement
group.

![A cluster placement group.](images/placement-group-cluster.png)

Cluster placement groups are recommended for applications that benefit from low
network latency, high network throughput, or both. They are also recommended when
the majority of the network traffic is between the instances in the group. To
provide the lowest latency and the highest packet-per-second network performance for
your placement group, choose an instance type that supports enhanced networking. For
more information, see [Enhanced
Networking](enhanced-networking.md "enhanced-networking.md").

We recommend that you launch your instances in the following way:

- Use a single launch request to launch the number of instances that you
  need in the placement group.
- Use the same instance type for all instances in the placement group.

If you try to add more instances to the placement group later, or if you try to
launch more than one instance type in the placement group, you increase your chances
of getting an insufficient capacity error.

If you stop an instance in a placement group and then start it again, it still
runs in the placement group. However, the start fails if there isn't enough capacity
for the instance.

If you receive a capacity error when launching an instance in a placement group
that already has running instances, stop and start all of the instances in the
placement group, and try the launch again. Starting the instances may migrate them
to hardware that has capacity for all of the requested instances.

###### Rules and limitations

The following rules apply to cluster placement groups:

- The following instance types are supported:
  - Current generation instances, except for [burstable performance](burstable-performance-instances.md "burstable-performance-instances.md") instances
    (for example, T2), [Mac1 instances](ec2-mac-instances.md "ec2-mac-instances.md"),
    and M7i-flex instances.
  - The following previous generation instances: A1, C3, C4, I2, M4, R3, and R4.

- A cluster placement group can't span multiple Availability Zones.
- The maximum network throughput speed of traffic between two instances in a
  cluster placement group is limited by the slower of the two instances. For
  applications with high-throughput requirements, choose an instance type with
  network connectivity that meets your requirements.
- For instances that are enabled for enhanced networking, the following
  rules apply:
  - Instances within a cluster placement group can use up to 10 Gbps
    for single-flow traffic. Instances that are not within a cluster
    placement group can use up to 5 Gbps for single-flow traffic.
  - Traffic to and from Amazon S3 buckets within the same Region over the
    public IP address space or through a VPC endpoint can use all
    available instance aggregate bandwidth.

- You can launch multiple instance types into a cluster placement group.
  However, this reduces the likelihood that the required capacity will be
  available for your launch to succeed. We recommend using the same instance
  type for all instances in a cluster placement group.
- We recommend that you reserve capacity explicitly in the cluster placement
  group by creating an [On-Demand Capacity Reservation in the cluster placement
  group](cr-cpg.md "cr-cpg.md"). Note that you can't reserve capacity using zonal Reserved Instances, as
  they can't reserve capacity explicitly in a placement group.
- Network traffic to the internet and over an Direct Connect connection to
  on-premises resources is limited to 5 Gbps for cluster placement
  groups.

## Partition placement groups

Partition placement groups help reduce the likelihood of correlated hardware
failures for your application. When using partition placement groups, Amazon EC2 divides
each group into logical segments called partitions. Amazon EC2 ensures that each
partition within a placement group has its own set of racks. Each rack has its own
network and power source. No two partitions within a placement group share the same
racks, allowing you to isolate the impact of hardware failure within your
application.

The following image is a simple visual representation of a partition placement
group in a single Availability Zone. It shows instances that are placed into a
partition placement group with three partitions—**Partition
1**, **Partition 2**, and **Partition
3**. Each partition comprises multiple instances. The instances in a
partition do not share racks with the instances in the other partitions, allowing
you to contain the impact of a single hardware failure to only the associated
partition.

![A partition placement group with three partitions.](images/placement-group-partition.png)

Partition placement groups can be used to deploy large distributed and replicated
workloads, such as HDFS, HBase, and Cassandra, across distinct racks. When you
launch instances into a partition placement group, Amazon EC2 tries to distribute the
instances evenly across the number of partitions that you specify. You can also
launch instances into a specific partition to have more control over where the
instances are placed.

A partition placement group can have partitions in multiple Availability Zones in
the same Region. A partition placement group can have a maximum of seven partitions
per Availability Zone. The number of instances that can be launched into a partition
placement group is limited only by the limits of your account.

In addition, partition placement groups offer visibility into the partitions
— you can see which instances are in which partitions. You can share this
information with topology-aware applications, such as HDFS, HBase, and Cassandra.
These applications use this information to make intelligent data replication
decisions for increasing data availability and durability.

If you start or launch an instance in a partition placement group and there is
insufficient unique hardware to fulfill the request, the request fails. Amazon EC2 makes
more distinct hardware available over time, so you can try your request again
later.

###### Rules and limitations

The following rules apply to partition placement groups:

- A partition placement group supports a maximum of seven partitions per
  Availability Zone. The number of instances that you can launch in a
  partition placement group is limited only by your account limits.
- When instances are launched into a partition placement group, Amazon EC2 tries
  to evenly distribute the instances across all partitions. Amazon EC2 doesn’t
  guarantee an even distribution of instances across all partitions.
- A partition placement group with Dedicated Instances can have a maximum of two
  partitions.
- Capacity Reservations do not reserve capacity in a partition placement group.

## Spread placement groups

A spread placement group is a group of instances that are each placed on distinct
hardware.

Spread placement groups are recommended for applications that have a small number
of critical instances that should be kept separate from each other. Launching
instances in a spread level placement group reduces the risk of simultaneous
failures that might occur when instances share the same equipment. Spread level
placement groups provide access to distinct hardware, and are therefore suitable for
mixing instance types or launching instances over time.

If you start or launch an instance in a spread placement group and there is
insufficient unique hardware to fulfill the request, the request fails. Amazon EC2 makes
more distinct hardware available over time, so you can try your request again later.
Placement groups can spread instances across racks or hosts. Rack level spread placement
groups can be used in AWS Regions and on AWS Outposts. Host level spread placement groups
can be used with AWS Outposts only.

###### Rack level spread placement groups

The following image shows seven instances in a single Availability Zone that
are placed into a spread placement group. The seven instances are placed on
seven different racks, each rack has its own network and power source.

![A spread placement group.](images/placement-group-spread.png)

A rack level spread placement group can span multiple Availability Zones in the same
Region. In a Region, a rack level spread placement group can have a maximum of seven
running instances per Availability Zone per group. With Outposts, a rack level spread
placement group can hold as many instances as you have racks in your Outpost
deployment.

###### Host level spread placement groups

Host level spread placement groups are only available with AWS Outposts. A host spread
level placement group can hold as many instances as you have hosts in your Outpost
deployment. For more information, see [Placement groups on AWS Outposts](placement-groups-outpost.md "placement-groups-outpost.md").

###### Rules and limitations

The following rules apply to spread placement groups:

- A rack spread placement group supports a maximum of seven running
  instances per Availability Zone. For example, in a Region with three
  Availability Zones, you can run a total of 21 instances in the group, with
  seven instances in each Availability Zone. If you try to start an eighth
  instance in the same Availability Zone and in the same spread placement
  group, the instance will not launch. If you need more than seven instances
  in an Availability Zone, we recommend that you use multiple spread placement
  groups. Using multiple spread placement groups does not provide guarantees
  about the spread of instances between groups, but it does help ensure the
  spread for each group, thus limiting the impact from certain classes of
  failures.
- Spread placement groups are not supported for Dedicated Instances.
- Host level spread placement groups are only supported for placement groups
  on AWS Outposts. A host level spread placement group can hold as many instances as
  you have hosts in your Outpost deployment.
- In a Region, a rack level spread placement group can have a maximum of seven
  running instances per Availability Zone per group. With AWS Outposts, a rack level
  spread placement group can hold as many instances as you have racks in your
  Outpost deployment.
- Capacity Reservations do not reserve capacity in a spread placement group.
