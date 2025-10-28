# Capacity Reservation groups

You can use AWS Resource Groups to create logical collections of Capacity Reservations, called
_resource groups_. A resource group is a logical grouping of
AWS resources that are all in the same AWS Region. For more information about
resource groups, see [What are resource groups?](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md") in
the _AWS Resource Groups User Guide_.

You can include Capacity Reservations that you own in your account, and Capacity Reservations that are shared with you
by other AWS accounts in a single resource group. You can also include Capacity Reservations that have
different attributes (instance type, platform, Availability Zone, and tenancy) in a
single resource group.

When you create resource groups for Capacity Reservations, you can target instances to a group of
Capacity Reservations instead of an individual Capacity Reservation. Instances that target a group of Capacity Reservations match with
any Capacity Reservation in the group that has matching attributes (instance type, platform,
Availability Zone, and tenancy) and available capacity. If the group does not have a
Capacity Reservation with matching attributes and available capacity, the instances run using On-Demand
capacity. If a matching Capacity Reservation is added to the targeted group at a later stage, the
instance is automatically matched with and moved into its reserved capacity.

To prevent unintended use of Capacity Reservations in a group, configure the Capacity Reservations in the group to
accept only instances that explicitly target the capacity reservation. To do this, set
**Instance eligibility** to **Only instances that specify
this reservation** when creating the Capacity Reservation using the Amazon EC2 console. When
using the AWS CLI, specify `--instance-match-criteria targeted` when creating
the Capacity Reservation. Doing this ensures that only instances that explicitly target the group, or a
Capacity Reservation in the group, can run in the group.

If a Capacity Reservation in a group is canceled or expires while it has running instances, the
instances are automatically moved to another Capacity Reservation in the group that has matching
attributes and available capacity. If there are no remaining Capacity Reservations in the group that
have matching attributes and available capacity, the instances run in On-Demand
capacity. If a matching Capacity Reservation is added to the targeted group at a later stage, the
instance is automatically moved into its reserved capacity.

###### Tasks

- [Create a group](create-group.md "create-group.md")
- [Add Capacity Reservation to group](add-to-group.md "add-to-group.md")
- [Remove Capacity Reservation from group](remove-from-group.md "remove-from-group.md")
- [Delete group](delete-group.md "delete-group.md")
- [Using Capacity Reservation in cluster placement groups
  with a Capacity Reservation group](using-cpg-odcr-crg.md "using-cpg-odcr-crg.md")
