# Best practices for Amazon EC2 Spot

Amazon EC2 provides access to spare EC2 compute capacity in the AWS Cloud through Spot Instances at
savings of up to 90% compared to On-Demand prices. The only difference between On-Demand Instances
and Spot Instances is that Spot Instances can be interrupted by Amazon EC2, with two minutes of notice, if
Amazon EC2 needs to reclaim the capacity. To ensure the best experience with Spot Instances, it's
important to understand and apply best practices for their use.

Spot Instances are recommended for stateless, fault-tolerant, flexible applications. For example,
Spot Instances work well for big data, containerized workloads, CI/CD, stateless web servers,
high performance computing (HPC), and rendering workloads.

While running, Spot Instances are exactly the same as On-Demand Instances. However, Spot does not guarantee that
you can keep your running instances long enough to finish your workloads. Spot also does
not guarantee that you can get immediate availability of the instances that you are
looking for, or that you can always get the aggregate capacity that you requested.
Moreover, Spot Instance interruptions and capacity can change over time because Spot Instance availability
varies based on supply and demand, and past performance isn’t a guarantee of future
results.

Spot Instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or
tightly coupled between instance nodes. We do not recommend Spot Instances for workloads that
are intolerant of occasional periods when the entire target capacity is not completely
available. While following Spot best practices to be flexible about instance types
and Availability Zones provides the best chance for high availability, there are no
guarantees that capacity will be available, because surges in demand for On-Demand Instances can
disrupt workloads on Spot Instances.

We strongly discourage using Spot Instances for these workloads or attempting to fail over to
On-Demand Instances to handle interruptions or periods of unavailability. Failing over to On-Demand Instances
can inadvertently drive interruptions for your other Spot Instances. In addition if Spot Instances
for a combination of instance type and Availability Zone get interrupted, it might
become difficult for you to get On-Demand Instances with that same combination.

Regardless of whether you're an experienced Spot user or new to Spot Instances, if you are currently
experiencing issues with Spot Instance interruptions or availability, we recommend that you
follow these best practices to have the best experience using the Spot service.

###### Spot best practices

- [Prepare individual instances for interruptions](#prep-instances-for-interruptions "#prep-instances-for-interruptions")
- [Be flexible about instance types and Availability
  Zones](#be-instance-type-flexible "#be-instance-type-flexible")
- [Use attribute-based instance type selection](#use-attribute-based-instance-type-selection "#use-attribute-based-instance-type-selection")
- [Use Spot placement scores to identify optimal Regions and Availability
  Zones](#use-spot-placement-scores-to-identify-optimal-regions-and-availability-zones "#use-spot-placement-scores-to-identify-optimal-regions-and-availability-zones")
- [Use EC2 Auto Scaling groups or EC2 Fleet to manage your
  aggregate capacity](#use-sf-asg-for-aggregate-capacity "#use-sf-asg-for-aggregate-capacity")
- [Use the price and capacity optimized
  allocation strategy](#use-capacity-optimized-allocation-strategy "#use-capacity-optimized-allocation-strategy")
- [Use integrated AWS services to manage your Spot Instances](#use-integrated-aws-services "#use-integrated-aws-services")
- [Which is the best Spot request method to use?](#which-spot-request-method-to-use "#which-spot-request-method-to-use")

## Prepare individual instances for interruptions

The best way for you to gracefully handle Spot Instance interruptions is to architect your
application to be fault-tolerant. To accomplish this, you can take advantage of EC2
instance rebalance recommendations and Spot Instance interruption notices.

An EC2 Instance rebalance recommendation is a signal that notifies you when a Spot Instance is at an
elevated risk of interruption. The signal gives you the opportunity to proactively
manage the Spot Instance in advance of the two-minute Spot Instance interruption notice. You can
decide to rebalance your workload to new or existing Spot Instances that are not at an
elevated risk of interruption. We've made it easy for you to use this signal by
using the Capacity Rebalancing feature in Auto Scaling groups and EC2 Fleet.

A Spot Instance interruption notice is a warning that is issued two minutes before Amazon EC2 interrupts
a Spot Instance. If your workload is "time-flexible," you can configure your Spot Instances to be
stopped or hibernated, instead of being terminated, when they are interrupted. Amazon EC2
automatically stops or hibernates your Spot Instances on interruption, and automatically
resumes the instances when we have available capacity.

We recommend that you create a rule in [Amazon EventBridge](../../../eventbridge/index.md "../../../eventbridge/index.md") that captures the rebalance
recommendations and interruption notifications, and then triggers a checkpoint for
the progress of your workload or gracefully handles the interruption. For more
information, see [Monitor rebalance recommendation
signals](rebalance-recommendations.md#monitor-rebalance-recommendations "rebalance-recommendations.md#monitor-rebalance-recommendations"). For a detailed example that
walks you through how to create and use event rules, see [Taking Advantage of Amazon EC2 Spot Instance Interruption Notices](https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/ "https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/").

For more information, see [EC2 instance rebalance recommendations](rebalance-recommendations.md "rebalance-recommendations.md") and [Spot Instance interruptions](spot-interruptions.md "spot-interruptions.md").

## Be flexible about instance types and Availability

Zones

A Spot capacity pool is a set of unused EC2 instances with the same instance type (for
example, `m5.large`) and Availability Zone (for example, us-east-1a). You
should be flexible about which instance types you request and in which Availability
Zones you can deploy your workload. This gives Spot a better chance to find and
allocate your required amount of compute capacity. For example, don't just ask for
`c5.large` if you'd be willing to use larges from the c4, m5, and m4
families.

Depending on your specific needs, you can evaluate which instance types you can be
flexible across to fulfill your compute requirements. If a workload can be
vertically scaled, you should include larger instance types (more vCPUs and memory)
in your requests. If you can only scale horizontally, you should include older
generation instance types because they are less in demand from On-Demand
customers.

A good rule of thumb is to be flexible across at least 10 instance types for each workload.
In addition, make sure that all Availability Zones are configured for use in your
VPC and selected for your workload.

## Use attribute-based instance type selection

With attribute-based instance type selection, you can specify instance
attributes—such as vCPUs, memory, and storage—for the workload you
want to run. EC2 Auto Scaling or EC2 Fleet will then automatically identify and launch instances
that match your specified attributes. This removes the effort required to manually
select specific instance types, which requires an in-depth understanding of each
instance type's offering.

Moreover, attribute-based instance type selection enables you to automatically use newly
released instance types as they become available. This ensures seamless access to an
increasingly broad range of Spot Instance capacity.

Attribute-based instance type selection is ideal for workloads and frameworks that can be
flexible about the instance types they run on, such as High Performance Computing
(HPC) and big data workloads.

For more information, see [Create mixed instances group using attribute-based instance type
selection](../../../autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.md "../../../autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.md") in the _Amazon EC2 Auto Scaling User Guide_ and
[Specify attributes for
instance type selection for EC2 Fleet or Spot Fleet](ec2-fleet-attribute-based-instance-type-selection.md "ec2-fleet-attribute-based-instance-type-selection.md") in this
guide.

## Use Spot placement scores to identify optimal Regions and Availability

Zones

Spot Instances are unused EC2 capacity, and this capacity fluctuates based on EC2 supply and demand.
As a result, you might not always get the exact Spot capacity that you require in a
specific location at a specific time. To mitigate this unpredictability, you can use
the Spot placement score feature. This feature provides recommendations for Regions or Availability
Zones that are more likely to have sufficient capacity to meet your Spot capacity
needs without requiring you to launch Spot Instances in those locations first.

Spot placement score is best used for workloads that can be flexible about the instance types and the
Region or Availability Zone they can use. All you need to do is specify the Spot
capacity that you need, your instance type requirements, and whether you want a
recommendations for Regions or Availability Zones. In return, you receive a score
ranging from 1 to 10 for each Region or Availability Zone, indicating the likelihood
of successfully provisioning your requested Spot capacity in that location. A score
of 10 indicates that your Spot request is highly likely to succeed.

It's important to note that a Spot placement score is a point-in-time recommendation, because capacity can
vary over time. It does not guarantee available capacity or predict the risk of
interruption.

You can use the Spot placement score feature in the Amazon EC2 console, AWS CLI, or an SDK. For more information,
see [Spot placement score](spot-placement-score.md "spot-placement-score.md").

## Use EC2 Auto Scaling groups or EC2 Fleet to manage your

aggregate capacity

Spot enables you to think in terms of aggregate capacity—in units that include
vCPUs, memory, storage, or network throughput—rather than thinking in terms
of individual instances. Auto Scaling groups and EC2 Fleet enable you to launch and maintain a
target capacity, and to automatically request resources to replace any that are
disrupted or manually terminated. When you configure an Auto Scaling group or an EC2 Fleet, you
need only specify the instance types and target capacity based on your application
needs. For more information, see [Auto Scaling groups](../../../autoscaling/ec2/userguide/auto-scaling-groups.md "../../../autoscaling/ec2/userguide/auto-scaling-groups.md")
in the _Amazon EC2 Auto Scaling User Guide_ and [Create an EC2 Fleet](create-ec2-fleet.md "create-ec2-fleet.md") in this user guide.

## Use the price and capacity optimized

allocation strategy

Allocation strategies in Auto Scaling groups help you to provision your target capacity without the
need to manually look for the Spot capacity pools with spare capacity. We recommend
using the `price-capacity-optimized` strategy because this strategy
automatically provisions instances from the most-available Spot capacity pools that
also have the lowest possible price. You can also take advantage of the
`price-capacity-optimized` allocation strategy in EC2 Fleet. Because your
Spot Instance capacity is sourced from pools with optimal capacity, this decreases the
possibility that your Spot Instances are reclaimed. For more information, see [Allocation strategies
for multiple instance types](../../../autoscaling/ec2/userguide/allocation-strategies.md "../../../autoscaling/ec2/userguide/allocation-strategies.md") in the _Amazon EC2 Auto Scaling User Guide_ and
[When workloads have a
high cost of interruption](ec2-fleet-allocation-strategy.md#ec2-fleet-strategy-capacity-optimized "ec2-fleet-allocation-strategy.md#ec2-fleet-strategy-capacity-optimized") in this user guide.

## Use integrated AWS services to manage your Spot Instances

Other AWS services integrate with Spot to reduce overall compute costs without the need
to manage the individual instances or fleets. We recommend that you consider the
following solutions for your applicable workloads: Amazon EMR, Amazon Elastic Container Service, AWS Batch,
Amazon Elastic Kubernetes Service, Amazon SageMaker AI, AWS Elastic Beanstalk, and Amazon GameLift Servers. To learn more about Spot best
practices with these services, see the [Amazon EC2 Spot Instances Workshops Website](https://ec2spotworkshops.com/ "https://ec2spotworkshops.com/").

## Which is the best Spot request method to use?

Use the following table to determine which API to use when requesting Spot Instances.

| API                                                                                                                                                                 | When to use?                                                                                                                                                                                                                                                                                          | Use case                                                                                                                                                                                                                                                                                                                                                                     | Should I use this API?                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [CreateAutoScalingGroup](../../../autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.md "../../../autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.md") | • You need multiple instances with either a single configuration or a mixed<br>configuration.<br>• You want to automate the lifecycle management through<br>a configurable API.                                                                                                                       | Create an Auto Scaling group that manages the lifecycle of your instances while<br>maintaining the desired number of instances. Supports horizontal<br>scaling (adding more instances) between specified minimum and<br>maximum limits.                                                                                                                                      | Yes                                                                                  |
| [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md")                                                                              | • You need multiple instances with either a single configuration or a mixed<br>configuration.<br>• You want to self-manage your instance lifecycle.<br>• If you don’t need auto scaling, we recommend that you<br>use an `instant` type fleet.                                                        | Create a fleet of both On-Demand Instances and Spot Instances in a single request, with multiple launch<br>specifications that vary by instance type, AMI, Availability<br>Zone, or subnet. The Spot Instance allocation strategy defaults<br>to `lowest-price` per unit, but you can change it to<br>`price-capacity-optimized`, `capacity-optimized`, or<br>`diversified`. | Yes – in `instant` mode if you don’t need auto scaling                               |
| [RunInstances](../APIReference/API_RunInstances.md "../APIReference/API_RunInstances.md")                                                                           | • You're already using the RunInstances API to launch On-Demand Instances, and you simply want to<br>change to launching Spot Instances by changing a single<br>parameter.<br>• You do not need multiple instances with different<br>instance types.                                                  | Launch a specified number of instances using an AMI and one<br>instance type.                                                                                                                                                                                                                                                                                                | No – because RunInstances does not allow mixed instance types in a single<br>request |
| [RequestSpotFleet](../APIReference/API_RequestSpotFleet.md "../APIReference/API_RequestSpotFleet.md")                                                               | • We strongly discourage using the RequestSpotFleet API<br>because it is a legacy API with no planned<br>investment.<br>• If you want to manage your instance lifecycle, use the<br>CreateFleet API.<br>• If you don't want to manage your instance lifecycle,<br>use the CreateAutoScalingGroup API. | DO NOT USE. RequestSpotFleet is legacy API with no planned investment.                                                                                                                                                                                                                                                                                                       | No                                                                                   |
| [RequestSpotInstances](../APIReference/API_RequestSpotInstances.md "../APIReference/API_RequestSpotInstances.md")                                                   | • We strongly discourage using the RequestSpotInstances API because it is a legacy API<br>with no planned investment.                                                                                                                                                                                 | DO NOT USE. RequestSpotInstances is legacy API with no planned investment.                                                                                                                                                                                                                                                                                                   | No                                                                                   |
