# Capacity Reservation Resource Groups

You can use AWS Resource Groups to create logical collections of Capacity Reservations, called
_Capacity Reservation Resource Groups_ (group). A Capacity Reservation Resource Group is a
resource group that contains your Capacity Reservations and enables you to launch instances into
multiple Capacity Reservations by specifying a single Capacity Reservation Resource Group ARN. For more information
about Capacity Reservation Resource Groups, see [What are resource
groups?](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md") in the _AWS Resource Groups User Guide_.

When you specify a group to launch instances, Amazon EC2 matches the instances with
any Capacity Reservation in the group that has matching attributes and available capacity.

You can include Capacity Reservations that you own in your account, and Capacity Reservations that are shared with you
by other AWS accounts in a single group. You can also include Capacity Reservations that have
different attributes (instance type, platform, Availability Zone, tenancy, and
placement group) in a single group.

A group supports all reservation types, including [On-Demand
Capacity Reservations](ec2-capacity-reservations.md "ec2-capacity-reservations.md"), [interruptible
Capacity Reservations](interruptible-capacity-reservations.md "interruptible-capacity-reservations.md"), and [Capacity Blocks for
ML](ec2-capacity-blocks.md "ec2-capacity-blocks.md"). You can add any combination of reservation types to a single
group.

###### Tasks

- [Create a group](cr-groups-create.md "cr-groups-create.md")
- [Add Capacity Reservations to a group](cr-groups-add.md "cr-groups-add.md")
- [Launch instances into Capacity Reservations in
  a group](cr-groups-launch.md "cr-groups-launch.md")
- [Remove Capacity Reservations from a group](cr-groups-remove.md "cr-groups-remove.md")
- [Instance lifecycle in a group](cr-groups-lifecycle.md "cr-groups-lifecycle.md")
- [Delete a group](cr-groups-delete.md "cr-groups-delete.md")
