# Using Capacity Reservation in cluster placement groups with a Capacity Reservation

group

Amazon EC2 provides different launch methods for you to use Capacity Reservations in a cluster placement group
with a Capacity Reservation group. You can choose one of the following methods to target a Capacity Reservation
group based on your workload requirements:

- _Specifying the ARN of the cluster placement group and Capacity Reservation group_
  – This will use any available Capacity Reservation with matching attributes and available capacity
  in the selected Capacity Reservation group. If the selected group does not have a Capacity Reservation with matching
  attributes and available capacity, the instances launch into On-Demand capacity.

###### Note

When you launch instances using this method, the instances are placed in the
specified cluster placement group.

- _Specifying only a Capacity Reservation group_ – This will use all available
  capacity within the Capacity Reservation group by specifying only the Capacity Reservation group. While
  launching instances, capacity is used in the following order:
  - Capacity Reservations not associated with any cluster placement group.
  - Capacity Reservation in any cluster placement group within the Capacity Reservation group.
  - If the group does not have a Capacity Reservation with matching attributes and available capacity,
    the instances run using On-Demand capacity and they are not
    placed in any cluster placement group.

###### Note

When you launch instances by specifying only a Capacity Reservation group, the instances are
launched into the Capacity Reservations that are created in the cluster placement group, but
the instances are not directly attached to the cluster placement group.
