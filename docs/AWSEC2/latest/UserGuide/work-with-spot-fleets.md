# Work with Spot Fleet

To start using a Spot Fleet, create a request that includes the total target capacity for Spot Instances,
an optional On-Demand portion, and either manually specify an AMI and a key pair, or specify
a launch template that includes the configuration for the instances in the fleet. You can
optionally specify additional parameters, or let the fleet use default values. You can also
tag the fleet request, and its instances and volumes, when you create the fleet.

The fleet launches On-Demand Instances when there is available capacity, and launches Spot Instances when your
maximum price exceeds the Spot price and capacity is available.

Once your fleet is launched, you can describe the fleet request, the instances in the
fleet, and any fleet events. You can also assign additional tags as needed.

If you need to change any fleet parameters, such as the total target capacity, you can
modify the fleet, provided it was configured to maintain capacity. You can't modify the
capacity of a one-time request after it's been submitted.

The fleet request remains active until it expires or you cancel (delete) it. When you
cancel the fleet request, you can either terminate the instances or leave them running. If
you choose to leave them running, the On-Demand Instances run until you terminate them, and the Spot Instances run
until they're interrupted or you terminate them.

###### Topics

- [Spot Fleet request states](spot-fleet-states.md "spot-fleet-states.md")
- [Spot Fleet permissions](spot-fleet-prerequisites.md "spot-fleet-prerequisites.md")
- [Create a Spot Fleet](create-spot-fleet.md "create-spot-fleet.md")
- [Tag a new or existing Spot Fleet request and the instances
  and volumes it launches](tag-spot-fleet.md "tag-spot-fleet.md")
- [Describe a Spot Fleet request, its instances, and event
  history](manage-spot-fleet.md "manage-spot-fleet.md")
- [Modify a Spot Fleet request](modify-spot-fleet.md "modify-spot-fleet.md")
- [Cancel (delete) a Spot Fleet request](cancel-spot-fleet.md "cancel-spot-fleet.md")
- [Understand automatic scaling for
  Spot Fleet](spot-fleet-automatic-scaling.md "spot-fleet-automatic-scaling.md")
