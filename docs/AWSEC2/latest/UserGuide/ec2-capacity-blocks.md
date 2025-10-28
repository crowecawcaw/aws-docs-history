# Capacity Blocks for ML

Capacity Blocks for ML allow you to reserve GPU-based accelerated computing instances on a future date to
support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block
are automatically placed close together inside [Amazon EC2 UltraClusters](https://aws.amazon.com/ec2/ultraclusters/ "https://aws.amazon.com/ec2/ultraclusters/"), for low-latency, petabit-scale,
non-blocking networking.

You can also use Capacity Blocks to reserve capacity for Amazon EC2 UltraServers. UltraServers connect multiple
Amazon EC2 instances within a low-latency, high-bandwidth accelerator interconnect. You can use
UltraServers to handle the most compute and memory intensive AI/ML workloads in training,
fine-tuning, and inference. For more information, see [Amazon EC2 UltraServers](https://aws.amazon.com/ec2/ultraservers/ "https://aws.amazon.com/ec2/ultraservers/").

With Capacity Blocks, you can see when GPU instance capacity is available on future dates, and
you can schedule a Capacity Block to start at a time that works best for you. When you reserve a
Capacity Block, you get predictable capacity assurance for GPU instances while paying only for the
amount of time that you need. We recommend Capacity Blocks when you need GPUs to support your ML
workloads for days or weeks at a time and don't want to pay for a reservation while your GPU
instances aren't in use.

The following are some common use cases for Capacity Blocks.

- **ML model training and fine-tuning** – Get
  uninterrupted access to the GPU instances that you reserved to complete ML model
  training and fine-tuning.
- **ML experiments and prototypes** – Run
  experiments and build prototypes that require GPU instances for short
  durations.
  You can reserve a Capacity Block with the following specifications:

- Reserve a start time up to 8 weeks in advance
- Set a reservation duration of one to 14 days or a multiple of 7 days, up to 182
  days (Examples: 21 days, 28 days)
- Configure up to 64 instances per Capacity Block
- Configure up to 256 instances across multiple Capacity Blocks
  For Amazon EC2 UltraServers, each UltraServer corresponds to one Capacity Block. You can request multiple
  UltraServers through a single request.

You can use Capacity Blocks to reserve `p6-b200`, `p5`, `p5e`,
`p5en`, `p4d`, `p4de`, `trn1`, and
`trn2` instances. You can purchase the following UltraServer types through
Capacity Blocks: `P6e-GB200` and `Trn2` (in preview).

To reserve a Capacity Block, you start by specifying your capacity needs, including the instance
type or UltraServer type, the number of instances or UltraServers, amount of time, earliest start date,
and latest end date that you need. Then, you can see an available Capacity Block offering that meets
your specifications. The Capacity Block offering includes details such as start time, Availability
Zone, and reservation price. The price of a Capacity Block offering depends on available supply and
demand at the time the offering was delivered. After you reserve a Capacity Block, the price doesn't
change. For more information, see [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md").

When you purchase a Capacity Block offering, your reservation is created for the date and number
of instances that you selected. When your Capacity Block reservation begins, you can target
instance launches by specifying the reservation ID in your launch requests.

You can use all the instances you reserved until 30 minutes (for instance types) or 60
minutes (for UltraServer type) before the end time of the Capacity Block. With 30 minutes (for instance
types) or 60 minutes (for UltraServer types) left in your Capacity Block reservation, we begin
terminating any instances that are running in the Capacity Block. We use this time to clean up
your instances before delivering the Capacity Block to the next customer. We emit an event through
EventBridge 10 minutes before the termination process begins. For more information, see [Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md").

###### Topics

- [Supported platforms](#capacity-blocks-platforms "#capacity-blocks-platforms")
- [Considerations](#capacity-blocks-considerations "#capacity-blocks-considerations")
- [Related resources](#capacity-blocks-related-resources "#capacity-blocks-related-resources")
- [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md")
- [Prerequisites for Capacity Blocks](capacity-blocks-prerequisites.md "capacity-blocks-prerequisites.md")
- [Find and purchase Capacity Blocks](capacity-blocks-purchase.md "capacity-blocks-purchase.md")
- [Launch instances using Capacity Blocks](capacity-blocks-launch.md "capacity-blocks-launch.md")
- [View Capacity Blocks](capacity-blocks-view.md "capacity-blocks-view.md")
- [Extend Capacity Blocks](capacity-blocks-extend.md "capacity-blocks-extend.md")
- [Create a resource group for UltraServer Capacity Blocks](cb-group.md "cb-group.md")
- [Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md")
- [Logging Capacity Blocks API calls
  with AWS CloudTrail](capacity-blocks-logging-using-cloudtrail.md "capacity-blocks-logging-using-cloudtrail.md")

## Supported platforms

Capacity Blocks for ML currently support instances and UltraServers with default tenancy only. When you use the AWS Management Console
to purchase a Capacity Block, the default platform option is Linux/UNIX. When you use the AWS Command Line Interface (AWS CLI) or
AWS SDK to purchase a Capacity Block, the following platform options are available:

- Linux/Unix
- Red Hat Enterprise Linux
- RHEL with HA
- SUSE Linux
- Ubuntu Pro

## Considerations

Before you use Capacity Blocks, consider the following details and limitations.

- If we detect impairment impacting an UltraServer Capacity Block, we will notify you but generally
  will not take action to terminate your instances on the Capacity Block. This is to minimize
  unintended disruption to your workloads. You can continue using the UltraServer Capacity Block as
  is after receiving this notification or request remediation by terminating all instances
  on the capacity block and submitting an AWS support case. After we receive your support
  case, we will notify you when we have completed remediation and you can relaunch instances
  onto your UltraServer Capacity Block.
- For `P6e-GB200` UltraServer Capacity Blocks, you must terminate your instances
  at least 60 minutes before the Capacity Block end time.
- To use `P6e-GB200` UltraServer Capacity Blocks, you must be opted in to the
  Dallas Local Zone (N. Virginia) Local Zone.
- Each Capacity Block can have up to 64 instances, and you can have up to 256
  instances across Capacity Blocks.
- You can describe Capacity Block offerings that can start in as soon as 30
  minutes.
- Capacity Blocks end at 11:30AM Coordinated Universal Time (UTC).
- The termination process for instances running in a Capacity Block begins at 11:00AM
  Coordinated Universal Time (UTC) on the final day of the reservation.
- Capacity Blocks can be reserved with a start time up to 8 weeks in the
  future.
- Capacity Block cancellations aren't allowed.
- Capacity Block can't be [moved](capacity-reservations-move.md "capacity-reservations-move.md") or
  [split](capacity-reservations-split.md "capacity-reservations-split.md").
- Capacity Blocks can't be shared across AWS accounts or within your AWS
  Organization.
- Only UltraServer Capacity Blocks can be used with resource groups. Instance Capacity Blocks
  can't be used with resource groups. For more information, see [Create a resource group for UltraServer Capacity Blocks](cb-group.md "cb-group.md").
- The total number of instances that can be reserved in Capacity Blocks across all
  accounts in your AWS Organization can't exceed 256 instances on a particular
  date.
- To use a Capacity Block, instances must specifically target the reservation
  ID.
- Instances in a Capacity Block don't count against your On-Demand Instances
  limits.
- For P5 instances using a custom AMI, ensure that you have the
  [required software and configuration
  for EFA](gpu-instances-started.md "gpu-instances-started.md").
- For Amazon EKS managed node groups, see [Create a managed node
  group with Amazon EC2 Capacity Blocks for ML](../../../eks/latest/userguide/capacity-blocks-mng.md "../../../eks/latest/userguide/capacity-blocks-mng.md"). For Amazon EKS self-managed node groups, see
  [Use Capacity Blocks for ML with self-managed nodes](../../../eks/latest/userguide/capacity-blocks.md "../../../eks/latest/userguide/capacity-blocks.md").

## Related resources

After you create a Capacity Block, you can do the following with the Capacity Block:

- Launch instances into the Capacity Block. For more information, see [Launch instances using Capacity Blocks](capacity-blocks-launch.md "capacity-blocks-launch.md").
- Create an Amazon EC2 Auto Scaling group. For more information, see [Use
  Capacity Blocks for machine learning workloads](../../../autoscaling/ec2/userguide/launch-template-capacity-blocks.md "../../../autoscaling/ec2/userguide/launch-template-capacity-blocks.md") in the
  _Amazon EC2 Auto Scaling User Guide_.

###### Note

If you use Amazon EC2 Auto Scaling or Amazon EKS, you can schedule scaling to run at the start
of the Capacity Block reservation. With scheduled scaling, AWS automatically
handles retries for you, so you don't need to worry about implementing retry
logic to handle transient failures.

- Enhance ML workflows with AWS ParallelCluster. For more information, see
  [Enhancing ML workflows with AWS ParallelCluster and Amazon EC2
  Capacity Blocks for ML](https://aws.amazon.com/blogs/hpc/enhancing-ml-workflows-with-aws-parallelcluster-and-amazon-ec2-capacity-blocks-for-ml/ "https://aws.amazon.com/blogs/hpc/enhancing-ml-workflows-with-aws-parallelcluster-and-amazon-ec2-capacity-blocks-for-ml/").

For more information about AWS ParallelCluster, see [What is
AWS ParallelCluster](../../../parallelcluster/latest/ug/what-is-aws-parallelcluster.md "../../../parallelcluster/latest/ug/what-is-aws-parallelcluster.md").

###### Note

Capacity Block sizes of 64 instances are not supported for all instance types in all
AWS Regions.
