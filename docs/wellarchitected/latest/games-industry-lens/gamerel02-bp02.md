# GAMEREL02-BP02 Support the use of multiple EC2 instance types

for your game

When hosting your game using EC2 instances, or if you use
containers hosted on EC2 instances in your AWS account, use
multiple instance types in your hosting strategy. By using
multiple instance types, you can increase the number of compute
options that can be used when your game is scaling to add more
servers to support player growth, which improves reliability in
case your preferred instance type is unavailable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When hosting your game using Spot Instances, use multiple instance
types since the availability of Spot Instances fluctuates based on
customer demand.

Test your game on multiple instance types to meet your cost and
performance requirements and determine a prioritized ranking of
instance types. Amazon EC2 Auto Scaling supports using multiple
instance types and sizes as well
as [assigning
weights to each instance type](../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md") in your configuration so that
you can implement prioritized ranking of compute options.

When hosting your game using Amazon GameLift managed hosting,
decide what type of instances your game needs and how to run game
server processes on them (using a runtime configuration). When
choosing resources for a fleet, consider several factors,
including game operating system, instance type (the computing
hardware), and whether to use On-Demand Instances, Spot Instances,
or both. Hosting costs with Amazon GameLift primarily depend on
the type of instances you use. For more information,
see [Choose
compute resources for a managed fleet](../../../gamelift/latest/developerguide/gamelift-compute.md "../../../gamelift/latest/developerguide/gamelift-compute.md").

### Implementation steps

- Use multiple EC2 instance types to improve reliability and
  scaling options when hosting your game on EC2 or containers.
- Configure Amazon EC2 Auto Scaling or GameLift fleets with
  prioritized instance types and weights to optimize cost and
  performance.
- Test your game on various instance types to verify that
  performance meets requirements and adjust your hosting
  strategy
  accordingly***.***
