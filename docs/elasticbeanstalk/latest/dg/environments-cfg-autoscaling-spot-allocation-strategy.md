# Spot Instance

allocation strategy

You can select any one of the allocation strategies listed in this topic for your Elastic Beanstalk
environment. Use the [Elastic Beanstalk
console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"), [namespace
configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace"), or the [AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli"), to set and configure Spot Instance allocation strategy and related
attributes for your environment.

Amazon EC2 applies an _allocation strategy_ to manage and provision Spot
instances for your environment. Each allocation strategy optimizes the allocated instances
based on how it’s defined to handle available capacity, price, and selection of instance
types.

Amazon EC2 Auto Scaling provides the following allocation strategies for Spot Instances.

- **Capacity optimized** (default)
  - Requests Spot Instances from the pool, with _optimal
    capacity_ for the number of instances that are launching.
  - This strategy works well for workloads where the possibility of service
    disruption must be minimized.

- **Price capacity optimized**
  - Requests Spot Instances from the pools that have the _lowest chance of interruption_ and the _lowest
    possible price_.
  - This is the preferable choice for most Spot workloads.

- **Capacity optimized prioritized**
  - Requests Spot Instances based on _capacity availability
    first_, while honoring your choice of _instance
    type prioritization_ on a best-effort basis. You can provide a list of
    instance types, ordered by priority, when you configure Spot Instance options for
    Elastic Beanstalk.
  - This strategy is good for workloads that require minimal service disruption, and
    a specific instance type prioritization matters.

- **Lowest price**

      + Requests Spot Instances from the *lowest priced
       pool* with available instances.
      + It's important to take precaution when using this strategy, since it only
       considers instance price and not capacity availability, which will result in high
       interruption rates.

  For more details about each allocation strategy, see [Allocation strategies for
  multiple instance types](../../../autoscaling/ec2/userguide/allocation-strategies.md "../../../autoscaling/ec2/userguide/allocation-strategies.md") in the _Amazon EC2 Auto Scaling User Guide_.

To help you understand which allocation strategy is best suited to meet your
environment's requirements, see [Choose the appropriate Spot allocation strategy](../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md#ec2-fleet-allocation-use-cases "../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md#ec2-fleet-allocation-use-cases") in the
_Amazon EC2 User Guide_.
