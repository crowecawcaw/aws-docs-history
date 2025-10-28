# Placement groups for your Amazon EC2 instances

To meet the needs of your workload, you can launch a group of
_interdependent_ EC2 instances into a _placement
group_ to influence their placement.

Depending on the type of workload, you can create a placement group using one of the
following placement strategies:

- **Cluster** – Packs instances close together inside an
  Availability Zone. This strategy enables workloads to achieve the low-latency
  network performance necessary for tightly-coupled node-to-node communication that is
  typical of high-performance computing (HPC) applications.
- **Partition** – Spreads your instances across logical
  partitions such that groups of instances in one partition do not share the
  underlying hardware with groups of instances in different partitions. This strategy
  is typically used by large distributed and replicated workloads, such as Hadoop,
  Cassandra, and Kafka.
- **Spread** – Strictly places a small group of instances
  across distinct underlying hardware to reduce correlated failures.
  Placement groups are optional. If you don't launch your instances into a placement group,
  EC2 tries to place the instances in such a way that all of your instances are spread out
  across the underlying hardware to minimize correlated failures.

###### Pricing

There is no charge for creating a placement group.

###### Rules and limitations

Before you use placement groups, be aware of the following rules:

- An instance can be placed in one placement group at a time; you can't
  place an instance in multiple placement groups.
- You can't merge placement groups.
- [On-Demand Capacity Reservations](ec2-capacity-reservations.md#capacity-reservations-limits "ec2-capacity-reservations.md#capacity-reservations-limits") and [zonal Reserved Instances](reserved-instances-scope.md "reserved-instances-scope.md") allow you to
  reserve capacity for EC2 instances in Availability Zones. When you launch an
  instance, if the instance attributes match those specified by an On-Demand Capacity Reservation or
  a zonal Reserved Instance, then the reserved capacity is automatically used by the
  instance. This is also true if you launch the instance into a placement
  group.
- You can't launch Dedicated Hosts in placement groups.
- You can't launch a Spot Instance that is configured to stop or hibernate on
  interruption in a placement group.

###### Contents

- [Placement strategies](placement-strategies.md "placement-strategies.md")
- [Create a placement group](create-placement-group.md "create-placement-group.md")
- [Change instance placement](change-instance-placement-group.md "change-instance-placement-group.md")
- [Delete a placement group](delete-placement-group.md "delete-placement-group.md")
- [Shared placement groups](share-placement-group.md "share-placement-group.md")
- [Placement groups on AWS Outposts](placement-groups-outpost.md "placement-groups-outpost.md")
