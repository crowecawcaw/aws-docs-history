

# Spot Instance allocation strategy
<a name="environments-cfg-autoscaling-spot-allocation-strategy"></a>

You can select any one of the allocation strategies listed in this topic for your Elastic Beanstalk environment. Use the [Elastic Beanstalk console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console), [namespace configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace), or the [AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli), to set and configure Spot Instance allocation strategy and related attributes for your environment. 

Amazon EC2 applies an *allocation strategy* to manage and provision Spot instances for your environment. Each allocation strategy optimizes the allocated instances based on how it’s defined to handle available capacity, price, and selection of instance types. 

Amazon EC2 Auto Scaling provides the following allocation strategies for Spot Instances. 
+ **Capacity optimized** (default)
  + Requests Spot Instances from the pool, with *optimal capacity* for the number of instances that are launching.
  + This strategy works well for workloads where the possibility of service disruption must be minimized.
+ **Price capacity optimized**
  + Requests Spot Instances from the pools that have the *lowest chance of interruption* and the *lowest possible price*.
  + This is the preferable choice for most Spot workloads.
+ **Capacity optimized prioritized**
  + Requests Spot Instances based on *capacity availability first*, while honoring your choice of *instance type prioritization* on a best-effort basis. You can provide a list of instance types, ordered by priority, when you configure Spot Instance options for Elastic Beanstalk.
  + This strategy is good for workloads that require minimal service disruption, and a specific instance type prioritization matters.
+ **Lowest price** 
  + Requests Spot Instances from the *lowest priced pool* with available instances.
  + It's important to take precaution when using this strategy, since it only considers instance price and not capacity availability, which will result in high interruption rates.

For more details about each allocation strategy, see [ Allocation strategies for multiple instance types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html) in the *Amazon EC2 Auto Scaling User Guide*. 

To help you understand which allocation strategy is best suited to meet your environment's requirements, see [ Choose the appropriate Spot allocation strategy ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html#ec2-fleet-allocation-use-cases) in the *Amazon EC2 User Guide*.