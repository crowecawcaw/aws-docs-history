# Release: Elastic Beanstalk added support for Capacity Rebalancing for Amazon EC2 Spot Instances on August 9, 2021

AWS Elastic Beanstalk added support for Capacity Rebalancing for Amazon EC2 Spot Instances.

**Release date:** August 9, 2021

## Changes

_Spot Instances_ are an Amazon EC2 instance purchasing option that can lower your costs significantly. Although they are a
cost-effective option, your requirements must be flexible regarding when your applications run and whether they can be interrupted.

Starting today, Elastic Beanstalk offers the Capacity Rebalancing feature for Amazon EC2 Auto Scaling groups. This feature reduces Spot Instance interruptions to your
applications. With ASG Capacity Rebalancing enabled, Amazon EC2 automatically attempts to replace Spot Instances in an Auto Scaling group before they are
interrupted.

You can enable Capacity Rebalancing on an existing EC2 Auto Scaling Group using the Elastic Beanstalk Console or the [aws:autoscaling:asg](../dg/command-options-general.md#command-options-general-autoscalingasg "../dg/command-options-general.md#command-options-general-autoscalingasg") namespace configuration
option. For more information, see [Auto Scaling group for your Elastic Beanstalk
environment](../dg/using-features.managing.md "../dg/using-features.managing.md") in the _AWS Elastic Beanstalk Developer Guide_.
