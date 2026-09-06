

# Capacity Reservation Resource Groups
<a name="cr-groups"></a>

You can use AWS Resource Groups to create logical collections of Capacity Reservations, called *Capacity Reservation Resource Groups* (group). A Capacity Reservation Resource Group is a resource group that contains your Capacity Reservations and enables you to launch instances into multiple Capacity Reservations by specifying a single Capacity Reservation Resource Group ARN. For more information about Capacity Reservation Resource Groups, see [What are resource groups?](https://docs.aws.amazon.com/ARG/latest/userguide/) in the *AWS Resource Groups User Guide*.

When you specify a group to launch instances, Amazon EC2 matches the instances with any Capacity Reservation in the group that has matching attributes and available capacity.

You can include Capacity Reservations that you own in your account, and Capacity Reservations that are shared with you by other AWS accounts in a single group. You can also include Capacity Reservations that have different attributes (instance type, platform, Availability Zone, tenancy, and placement group) in a single group.

A group supports all reservation types, including [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html), [interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html), and [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html). You can add any combination of reservation types to a single group.

**Topics**
+ [Create a group](cr-groups-create.md)
+ [Add Capacity Reservations to a group](cr-groups-add.md)
+ [Launch instances into Capacity Reservations in a group](cr-groups-launch.md)
+ [Remove Capacity Reservations from a group](cr-groups-remove.md)
+ [Instance lifecycle in a group](cr-groups-lifecycle.md)
+ [Delete a group](cr-groups-delete.md)