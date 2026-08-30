# Instance lifecycle in a group

When a Capacity Reservation in a group changes state, the impact on your running instances
depends on the reservation type.

## On-Demand Capacity Reservations

When an On-Demand Capacity Reservation in a group is canceled, expires, or has its
capacity reduced, instances that target the group match with any other
On-Demand Capacity Reservation in the group that has matching attributes (instance type,
platform, Availability Zone, and tenancy) and available capacity. If the
group does not have an On-Demand Capacity Reservation with matching attributes and
available capacity, the instances run using On-Demand capacity. If you
add a matching On-Demand Capacity Reservation to the group later, Amazon EC2 automatically
moves the instances into its reserved capacity.

## Interruptible Capacity Reservations

When the capacity of an interruptible Capacity Reservation is reclaimed, instances
receive an interruption notice 2 minutes before termination. For more
information, see [Interruption experience](interruptible-capacity-reservations.md#interruption-experience "interruptible-capacity-reservations.md#interruption-experience").

## Capacity Blocks

Instances running in a Capacity Block in a Capacity Reservation Resource Group are
terminated before the Capacity Block ends, the same as for a Capacity Block that you
target directly. For more information, see [How Amazon EC2 Capacity Blocks work](capacity-blocks-how.md "capacity-blocks-how.md").
