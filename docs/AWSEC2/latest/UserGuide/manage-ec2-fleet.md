# Work with EC2 Fleet

To start using an EC2 Fleet, create a request that includes the total target capacity,
On-Demand capacity, Spot capacity, and a launch template specifying the configuration for
the instances in the fleet. You can optionally specify additional parameters, or let the
fleet use default values. You can also tag the fleet request, and its instances and volumes,
when you create the fleet.

The fleet launches On-Demand Instances when there is available capacity, and launches Spot Instances when your
maximum price exceeds the Spot price and capacity is available.

Once your fleet is launched, you can describe the fleet request, the instances in the
fleet, and any fleet events. You can also assign additional tags as needed.

If you need to change any fleet parameters, such as the total target capacity, you can modify
the fleet, provided it was configured to maintain capacity. You can't modify the capacity
of a one-time request after it's been submitted.

The fleet request remains active until it expires or you delete it. When you delete the
fleet request, you can either terminate the instances or leave them running. If you choose
to leave them running, the On-Demand Instances run until you terminate them, and the Spot Instances run until
they're interrupted or you terminate them.

###### Topics

- [EC2 Fleet request states](EC2-fleet-states.md "EC2-fleet-states.md")
- [EC2 Fleet prerequisites](ec2-fleet-prerequisites.md "ec2-fleet-prerequisites.md")
- [Create an EC2 Fleet](create-ec2-fleet.md "create-ec2-fleet.md")
- [Tag a new or existing EC2 Fleet request and the instances and
  volumes it launches](tag-ec2-fleet.md "tag-ec2-fleet.md")
- [Describe an EC2 Fleet, its instances, and its events](describe-ec2-fleet.md "describe-ec2-fleet.md")
- [Modify an EC2 Fleet](modify-ec2-fleet.md "modify-ec2-fleet.md")
- [Delete an EC2 Fleet request and the instances in the
  fleet](delete-fleet.md "delete-fleet.md")
