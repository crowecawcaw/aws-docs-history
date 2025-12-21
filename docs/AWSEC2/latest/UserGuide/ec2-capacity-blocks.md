# Capacity Blocks for ML

Capacity Blocks for ML allow you to reserve GPU-based accelerated computing instances on a future date to
support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block
are automatically placed close together inside [Amazon EC2 UltraClusters](https://aws.amazon.com/ec2/ultraclusters/ "https://aws.amazon.com/ec2/ultraclusters/"), for low-latency, petabit-scale, non-blocking networking.

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
  Capacity Blocks are availale for select instance types in some AWS Regions. Fore more information,
  see [Supported instance types and Regions](#capacity-blocks-prerequisites "#capacity-blocks-prerequisites").

You can reserve a Capacity Block with a reservation start time up to eight weeks in the future.
Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across
Capacity Blocks.

###### Topics

- [Supported instance types and Regions](#capacity-blocks-prerequisites "#capacity-blocks-prerequisites")
- [Supported platforms](#capacity-blocks-platforms "#capacity-blocks-platforms")
- [Considerations](#capacity-blocks-considerations "#capacity-blocks-considerations")
- [Related resources](#capacity-blocks-related-resources "#capacity-blocks-related-resources")
- [How Amazon EC2 Capacity Blocks work](capacity-blocks-how.md "capacity-blocks-how.md")
- [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md")
- [Find and purchase Capacity Blocks](capacity-blocks-purchase.md "capacity-blocks-purchase.md")
- [Launch instances using Capacity Blocks](capacity-blocks-launch.md "capacity-blocks-launch.md")
- [View Capacity Blocks](capacity-blocks-view.md "capacity-blocks-view.md")
- [Extend Capacity Blocks](capacity-blocks-extend.md "capacity-blocks-extend.md")
- [Create a resource group for UltraServer Capacity Blocks](cb-group.md "cb-group.md")
- [Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md")
- [Logging Capacity Blocks API calls
  with AWS CloudTrail](capacity-blocks-logging-using-cloudtrail.md "capacity-blocks-logging-using-cloudtrail.md")

## Supported instance types and Regions

Instance and UltraServer Capacity Blocks can use be used with the following instance types and AWS regions.

###### Note

Capacity Block sizes of 64 instances are not supported for all instance types in all
AWS Regions.

### Instance Capacity Blocks

- **`p6-b300.48xlarge`**
  - US West (Oregon) — `us-west-2`

- **`p6-b200.48xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (Oregon) — `us-west-2`

- **`p5.4xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (Oregon) — `us-west-2`
  - Europe (London) — `eu-west-2`
  - Asia Pacific (Mumbai) — `ap-south-1`
  - Asia Pacific (Tokyo) — `ap-northeast-1`
  - Asia Pacific (Sydney) — `ap-southeast-2`
  - South America (São Paulo) — `sa-east-1`

- **`p5.48xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (N. California) — `us-west-1`
  - US West (Oregon) — `us-west-2`
  - Europe (Stockholm) — `eu-north-1`
  - Europe (London) — `eu-west-2`
  - South America (São Paulo) — `sa-east-1`
  - Asia Pacific (Tokyo) — `ap-northeast-1`
  - Asia Pacific (Mumbai) — `ap-south-1`
  - Asia Pacific (Sydney) — `ap-southeast-2`
  - Asia Pacific (Jakarta) — `ap-southeast-3`

- **`p5e.48xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (N. California) — `us-west-1`
  - US West (Oregon) — `us-west-2`
  - Europe (Stockholm) — `eu-north-1`
  - Europe (London) — `eu-west-2`
  - Europe (Spain) — `eu-south-2`
  - South America (São Paulo) — `sa-east-1`
  - Asia Pacific (Tokyo) — `ap-northeast-1`
  - Asia Pacific (Seoul) — `ap-northeast-2`
  - Asia Pacific (Mumbai) — `ap-south-1`
  - Asia Pacific (Jakarta) — `ap-southeast-3`

- **`p4d.24xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (Oregon) — `us-west-2`

- **`p4de.24xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US West (Oregon) — `us-west-2`

- **`trn1.32xlarge`**
  - US East (N. Virginia) — `us-east-1`
  - US East (Ohio) — `us-east-2`
  - US West (N. California) — `us-west-1`
  - US West (Oregon) — `us-west-2`
  - Europe (Stockholm) — `eu-north-1`
  - Asia Pacific (Mumbai) — `ap-south-1`
  - Asia Pacific (Sydney) — `ap-southeast-2`
  - Asia Pacific (Melbourne) — `ap-southeast-4`

- **`trn2.3xlarge`**
  - Asia Pacific (Melbourne) — `ap-southeast-4`
  - South America (São Paulo) — `sa-east-1`

- **`trn2.48xlarge`**
  - US East (Ohio) — `us-east-2`

### UltraServer Capacity Blocks

- **`Trn2`**
  - US East (Ohio) — `us-east-2`

- **`P6e-GB200`**
  - Dallas Local Zone (N. Virginia) — `us-east-1-dfw-2a`

## Supported platforms

Capacity Blocks for ML currently support instances and UltraServers with default tenancy only. When you use the AWS Management Console
to purchase a Capacity Block, the default platform option is Linux/UNIX. When you use the AWS Command Line Interface (AWS CLI) or AWS
SDK to purchase a Capacity Block, the following platform options are available:

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
