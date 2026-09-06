

# Work with Spot Fleet
<a name="work-with-spot-fleets"></a>

**Important**  
We strongly discourage using Spot Fleet because it uses a legacy API with no planned investment. If you want to manage your instance lifecycle, use EC2 Fleet instead. If you don't want to manage your instance lifecycle, use an Auto Scaling group instead. Use Spot Fleet only if you need console support for a use case where you would use EC2 Fleet. For more information, see [Which is the best fleet method to use?](which-fleet-method-to-use.md).

To start using a Spot Fleet, create a request that includes the total target capacity for Spot Instances, an optional On-Demand portion, and either manually specify an AMI and a key pair, or specify a launch template that includes the configuration for the instances in the fleet. You can optionally specify additional parameters, or let the fleet use default values. You can also tag the fleet request, and its instances and volumes, when you create the fleet.

The fleet launches On-Demand Instances when there is available capacity, and launches Spot Instances when your maximum price exceeds the Spot price and capacity is available.

After your fleet is launched, you can describe the fleet request, the instances in the fleet, and any fleet events. You can also assign additional tags as needed.

If you need to change any fleet parameters, such as the total target capacity, you can modify the fleet, provided it was configured to maintain capacity. You can't modify the capacity of a one-time request after it's been submitted.

The fleet request remains active until it expires or you cancel (delete) it. When you cancel the fleet request, you can either terminate the instances or leave them running. If you choose to leave them running, the On-Demand Instances run until you terminate them, and the Spot Instances run until they're interrupted or you terminate them.

**Topics**
+ [Spot Fleet request states](spot-fleet-states.md)
+ [Spot Fleet permissions](spot-fleet-prerequisites.md)
+ [Create a Spot Fleet](create-spot-fleet.md)
+ [Tag a new or existing Spot Fleet request and the instances and volumes it launches](tag-spot-fleet.md)
+ [Describe a Spot Fleet request, its instances, and event history](manage-spot-fleet.md)
+ [Modify a Spot Fleet request](modify-spot-fleet.md)
+ [Cancel (delete) a Spot Fleet request](cancel-spot-fleet.md)
+ [Understand automatic scaling for Spot Fleet](spot-fleet-automatic-scaling.md)