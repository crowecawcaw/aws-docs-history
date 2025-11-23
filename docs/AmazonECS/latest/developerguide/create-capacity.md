# Amazon EC2 container instances for Amazon ECS

An Amazon ECS container instance is an Amazon EC2 instance that run the Amazon ECS container
agent and is registered to a cluster. When you run tasks with Amazon ECS using the
capacity provider, External capacity provider or an Amazon EC2 Auto Scaling group capacity
provider, your tasks are placed on your active container instances. You are
responsible for the container instance management and maintenance.

Although you can create your own Amazon EC2 instance AMI that meets the basic
specifications needed to run your containerized workloads on Amazon ECS, the
Amazon ECS-optimized AMIs are preconfigured and tested on Amazon ECS by AWS engineers. It
is the simplest way for you to get started and to get your containers running on
AWS quickly.

When you create a cluster using the console, Amazon ECS creates a launch template for
your instances with the latest AMI associated with the selected operating system.

When you use CloudFormation to create a cluster, the SSM parameter is part of the Amazon EC2
launch template for the Amazon EC2 Auto Scaling group instances. You can configure the template to use a
dynamic Systems Manager parameter to determine what Amazon ECS Optimized AMI to deploy. This
parameter ensures that each time you deploy the stack it will check to see if there
is available update that needs to be applied to the EC2 instances. For an example of
how to use the Systems Manager parameter, see [Create an Amazon ECS cluster with the Amazon ECS-optimized Amazon Linux 2023 AMI](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.md#aws-resource-ecs-cluster--examples--Create_an_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.md#aws-resource-ecs-cluster--examples--Create_an_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI") in the _AWS CloudFormation User Guide_.

- [Retrieving Amazon ECS-optimized Linux AMI
  metadata](retrieve-ecs-optimized_AMI.md "retrieve-ecs-optimized_AMI.md")
- [Retrieving Amazon ECS-optimized
  Bottlerocket AMI metadata](ecs-bottlerocket-retrieve-ami.md "ecs-bottlerocket-retrieve-ami.md")
- [Retrieving Amazon ECS-optimized Windows
  AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md")
  You can choose from the instance types that are compatible with your application.
  With larger instances, you can launch more tasks at the same time. With smaller
  instances, you can scale out in a more fine-grained way to save costs. You don't
  need to choose a single Amazon EC2 instance type that to fit all the applications in your
  cluster. Instead, you can create multiple Amazon EC2 Auto Scaling groups where each group has a
  different instance type. Then, you can create an Amazon EC2 capacity provider for each
  one of these groups.

Use the following guidelines to determine the instance family types and instance
type to use:

- Eliminate the instance types or instance families that don't meet the
  specific requirements of your application. For example, if your application
  requires a GPU, you can exclude any instance types that don't have a
  GPU.
- Consider requirements including network throughput and storage.
- Consider the CPU and memory. As a general rule, the CPU and memory must be
  large enough to hold at least one replica of the task that you want to run.

## Spot Instances

Spot capacity can provide significant cost savings over on-demand instances. Spot
capacity is excess capacity that's priced significantly lower than on-demand or reserved
capacity. Spot capacity is suitable for batch processing and machine-learning workloads,
and development and staging environments. More generally, it's suitable for any workload
that tolerates temporary downtime.

Understand that the following consequences because Spot capacity might not be
available all the time.

- During periods of extremely high demand, Spot capacity might be unavailable.
  This can cause Amazon EC2 Spot instance launches to be delayed. In these events,
  Amazon ECS services retry launching tasks, and Amazon EC2 Amazon EC2 Auto Scaling groups also retry launching
  instances, until the required capacity becomes available. Amazon EC2 doesn't replace
  Spot capacity with on-demand capacity.
- When the overall demand for capacity increases, Spot Instances and tasks might
  be terminated with only a two-minute warning. After the warning is sent, tasks
  should begin an orderly shutdown if necessary before the instance is fully
  terminated. This helps minimize the possibility of errors. For more information
  about a graceful shutdown, see [Graceful shutdowns with ECS](https://aws.amazon.com/blogs/containers/graceful-shutdowns-with-ecs/ "https://aws.amazon.com/blogs/containers/graceful-shutdowns-with-ecs/").

To help minimize Spot capacity shortages, consider the following recommendations:

- Use multiple Regions and Availability Zones - Spot
  capacity varies by Region and Availability Zone. You can
  improve Spot availability by running your workloads in multiple
  Regions and Availability Zones. If possible, specify
  subnets in all the Availability Zones in the Regions
  where you run your tasks and instances.
- Use multiple Amazon EC2 instance types - When you use Mixed Instance Policies with
  Amazon EC2 Amazon EC2 Auto Scaling, multiple instance types are launched into your Amazon EC2 Auto Scaling Group. This
  ensures that a request for Spot capacity can be fulfilled when needed. To
  maximize reliability and minimize complexity, use instance types with roughly
  the same amount of CPU and memory in your Mixed Instances Policy. These
  instances can be from a different generation, or variants of the same base
  instance type. Note that they might come with additional features that you might
  not require. An example of such a list could include m4.large, m5.large,
  m5a.large, m5d.large, m5n.large, m5dn.large, and m5ad.large. For more
  information, see [Amazon EC2 Auto Scaling groups with multiple instance types and purchase options](../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md") in the
  _Amazon EC2 Auto Scaling User Guide_.
- Use the capacity-optimized Spot allocation strategy - With Amazon EC2 Spot, you can
  choose between the capacity- and cost-optimized allocation strategies. If you
  choose the capacity-optimized strategy when launching a new instance, Amazon EC2 Spot
  selects the instance type with the greatest availability in the selected
  Availability Zone. This helps reduce the possibility that the instance is
  terminated soon after it launches.

For information about how to configure spot termination notices on your container instances, see:

- [Configuring Amazon ECS Linux
  container instances to receive Spot Instance notices](spot-instance-draining-linux-container.md "spot-instance-draining-linux-container.md")
- [Configuring Amazon ECS Windows
  container instances to receive Spot Instance notices](windows-spot-instance-draining-container.md "windows-spot-instance-draining-container.md")
