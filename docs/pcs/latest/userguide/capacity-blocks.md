# Using Amazon EC2 Capacity Blocks for ML with AWS PCS

Amazon EC2 Capacity Blocks for ML is an Amazon EC2 purchasing option that enables you
to pay in advance to reserve GPU-based accelerated computing instances within
a specific date and time range to support short duration workloads. Instances
that run inside a Capacity Block are automatically placed close together inside
Amazon EC2 UltraClusters, for low-latency, petabit-scale, non-blocking networking.
For more information, see [Capacity Blocks for
ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md") in the _Amazon Elastic Compute Cloud User Guide_.

You can use a launch template to have AWS PCS use a Capacity Block
when it launches instances for a compute node group.

###### Note

AWS PCS introduced support for Capacity Blocks since Slurm version 24.05.

## Limitations

- AWS PCS only supports Capacity Blocks with P5en, P5e, P5, and P4d instance families.
- You can only associate a compute node group with 1 Capacity Block at a time.
- You can't associate a compute node group with a capacity reservation group
  that combines multiple Capacity Blocks.
- Capacity Blocks must be in a `scheduled` or `active`
  state to use with AWS PCS. You can't use Capacity Blocks in other states, such as
  `payment-failed`. For more information, see [View Capacity Blocks](../../../AWSEC2/latest/UserGuide/capacity-blocks-view.md "../../../AWSEC2/latest/UserGuide/capacity-blocks-view.md")
  in the _Amazon Elastic Compute Cloud User Guide_.

## Capacity Block expiration

Capacity Blocks are limited to a specific date and time range. When a Capacity Block expires:

- The compute node group associated with that Capacity Block continues to exist
  and remains associated with the same queues.
- All instances in the compute node group are terminated and active jobs
  might fail, based on your Slurm settings.
- AWS PCS can't launch new instances in the compute node group.
- All queued or newly submitted jobs remain in pending state
  until another compute node group is attached to the queue
  or you update the compute node group to use a new launch template
  that specifies a new Capacity Block.
