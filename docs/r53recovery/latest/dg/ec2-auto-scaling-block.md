

# Amazon EC2 Auto Scaling group execution block
<a name="ec2-auto-scaling-block"></a>

The EC2 Auto Scaling group execution block allows you to scale EC2 instances as part of your multi-Region recovery process. You can define a percentage of capacity, relative to the Region you're leaving (source and destination).

## Configuration
<a name="ec2-auto-scaling-block-config"></a>

When you configure the EC2 Auto Scaling group execution block, you enter the EC2 Auto Scaling ARNs for the specific Regions that are associated with your plan. You should enter EC2 Auto Scaling ARNs in each Region that you want to be scaled up during plan execution.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [EC2 Auto Scaling execution block sample policy](security_iam_region_switch_ec2_autoscaling.md).

To configure a EC2 Auto Scaling group execution block, enter the following values:

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **EC2 Auto Scaling group ARN for *Region*: ** Enter the ARN for the EC2 Auto Scaling group in each Region for your plan.

1. **Percentage to match the activated Region's capacity: ** Enter the desired percentage of the number of running instances in the Auto Scaling group to match for the activated Region.

1. **Capacity monitoring approach: **Select one of the following approaches for monitoring capacity for your EC2 Auto Scaling groups:
   + **Max running capacity sampled over 24 hours**: Choose this option to use the **Desired capacity** value specified in your EC2 Auto Scaling group configuration. This option does not create additional costs, but is potentially less accurate than using the other option, CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

     For more information, see [Set scaling limits for your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html) in the Amazon EC2 Auto Scaling User Guide.
   + **Max running capacity sampled over 24 hours with CloudWatch**: Choose this option to use metrics specified in Amazon CloudWatch for EC2 Auto Scaling. Using the option can be more accurate, but incurs the additional costs of using CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

     To use this option, you must first enable group metrics for your Auto Scaling groups. For more information, see [Enable Auto Scaling group metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html#as-enable-group-metrics) in the Amazon EC2 Auto Scaling User Guide.

1. **Wait for target group health: ** Whether Region switch waits for the Auto Scaling group's instances to become healthy in their associated Elastic Load Balancing target groups before completing the step.
   + When enabled, Region switch checks target group health after scaling capacity. Region switch does not proceed to the next step until every associated target group reports the required number of instances as `healthy`. The required number is the desired capacity Region switch calculates for the step, the same capacity it waits for when scaling.
   + When disabled, the step completes as soon as the target Auto Scaling group reaches the desired capacity of `InService` instances, without checking target group health.

   In the Region switch API, this option corresponds to specifying `waitELBTargetGroupHealthy` as either `enabled` or `disabled`.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="ec2-auto-scaling-block-how"></a>

When the block runs, Region switch reads the source Region's maximum running capacity over the last 24 hours, measured by the capacity monitoring approach you selected. It calculates the target capacity with the formula `ceil(percentToMatch * source capacity)`, where ceil() rounds up any fractional result, and measures capacity as the number of instances in the `InService` state. It then scales up the destination group to match this capacity. Region switch scales up the destination group only when its current desired capacity is less than the calculated target. If the current desired capacity is already greater than or equal to the target, the block proceeds without scaling (Region switch never scales down). This calculation applies to both active/passive and active/active plans.

The source capacity is always that of the other Region. In an active/active plan, Region switch uses the other configured Region as the source in both the activate and deactivate workflows.

Region switch waits until the destination group's capacity is fulfilled before proceeding to the next step. When you enable **Wait for target group health**, Region switch checks target group health after the destination group reaches its desired capacity. It reads the Elastic Load Balancing target groups attached to the group and polls their health until every attached target group reports the desired capacity as `healthy`. This check runs whether or not scaling occurred, so even if the group already had the desired capacity, Region switch verifies target group health before completing the step. For ungraceful execution, it instead waits for the minimum percentage of capacity to be `healthy`.

An instance counts toward the healthy total only when it is `InService` in the Auto Scaling group and its matching target group entry is `healthy`. Region switch identifies instances by EC2 instance ID and re-reads the group on each poll, so instances that are still launching, running a lifecycle hook, or held in a warm pool aren't counted until they reach `InService`. The step completes only after all required instances are healthy across every attached target group. If the group has no attached target groups, Region switch skips the check and completes the step. If the required instances don't become healthy before the timeout, the step fails.

**Note**  
The **Wait for target group health** option supports only Application Load Balancer (ALB) and Network Load Balancer (NLB) target groups. It doesn't support Classic Load Balancer. If your Auto Scaling group is associated only with a Classic Load Balancer, enabling this option has no effect.

The block supports both graceful and ungraceful execution. For ungraceful execution, you specify the minimum percentage of compute capacity to match in the destination Region before Region switch proceeds. The percentage of capacity you specify in the execution block, or as the minimum percentage for ungraceful execution, applies to both scaling and waiting for target group health.

**Note**  
Executing this block modifies the minimum and desired capacity settings of your Auto Scaling groups, which can cause configuration drift if you manage these values through infrastructure-as-code or other automation. Make sure your configuration management processes account for these changes to prevent unintended rollbacks.