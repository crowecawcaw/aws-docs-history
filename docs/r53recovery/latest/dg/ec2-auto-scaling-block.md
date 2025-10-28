# Amazon EC2 Auto Scaling group execution block

The EC2 Auto Scaling group execution block allows you to scale EC2 instances as part of your multi-Region
recovery process. You can define a percentage of capacity, relative to the Region you're leaving (source and destination).

## Configuration

When you configure the EC2 Auto Scaling group execution block, you enter the EC2 Auto Scaling
ARNs for the specific Regions that are associated with your plan. You should
enter EC2 Auto Scaling ARNs in each Region that you want to be scaled up during plan
execution.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [EC2 Auto Scaling execution block sample policy](security_iam_region_switch_ec2_autoscaling.md "security_iam_region_switch_ec2_autoscaling.md").

To configure a EC2 Auto Scaling group execution block, enter the following values:

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **EC2 Auto Scaling group ARN for _Region_:**
   Enter the ARN for the EC2 Auto Scaling group in each Region for your plan.
4. **Percentage to match the activated Region's capacity:**
   Enter the desired percentage of the number of running instances in the Auto Scaling group
   to match for the activated Region.
5. **Capacity monitoring approach:** Select one of the following approaches for monitoring capacity for your EC2 Auto Scaling groups:
   - **Max running capacity sampled over 24 hours**: Choose this option to use
     the **Desired capacity** value specified in your EC2 Auto Scaling group configuration. This option does not create additional
     costs, but is potentially less accurate than using the other option, CloudWatch metrics.

   In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

   For more information, see [Set scaling limits for your Auto Scaling group](../../../autoscaling/ec2/userguide/asg-capacity-limits.md "../../../autoscaling/ec2/userguide/asg-capacity-limits.md")
   in the Amazon EC2 Auto Scaling User Guide.
   - **Max running capacity sampled over 24 hours with CloudWatch**: Choose this option to use
     metrics specified in Amazon CloudWatch for EC2 Auto Scaling. Using the option can be more accurate, but incurs the additional
     costs of using CloudWatch metrics.

   In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

   To use this option, you must first enable group metrics for your Auto Scaling groups.
   For more information, see [Enable Auto Scaling group metrics](../../../autoscaling/ec2/userguide/ec2-auto-scaling-metrics.md#as-enable-group-metrics "../../../autoscaling/ec2/userguide/ec2-auto-scaling-metrics.md#as-enable-group-metrics")
   in the Amazon EC2 Auto Scaling User Guide.

6. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

After you configure an EC2 Auto Scaling execution block, Region switch confirms that there
is only one source Auto Scaling group and one destination Auto Scaling group. If
there are multiple Auto Scaling groups, the execution block fails during plan evaluation.
The target capacity is defined as the number
of instances have a state that is set to `InService`. For more information, see
[EC2 Auto Scaling instance lifecycle](../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md").

Based on the value that you specify (when you configure the Auto Scaling execution block)
for a matching percentage, Region switch calculates the new desired capacity for the destination Auto Scaling group.
The new desired capacity is compared against the destination Auto Scaling group's desired
capacity. The formula that Region switch uses to calculate desired capacity is the following:
`ceil(percentToMatch * Source Auto Scaling group capacity)`, where ceil() is a
function that rounds up any fractional result. If the current desired capacity of the destination
Auto Scaling group is greater than or equal to the desired capacity of the new Auto Scaling group that Region switch
calculates, the execution block proceeds. Note that Region switch does not scale down Auto Scaling group capacity.

When Region switch executes an Auto Scaling block, Region switch attempts to scale up the target Region Auto Scaling group capacity
to match the desired capacity. Then, Region switch waits until the requested Auto Scaling group capacity is fulfilled
in the target Region's Auto Scaling group before Region switch proceeds to the next step in the plan.

If you’re using an active/active approach, Region switch uses the other configured Region
as the source. That is, if a Region is being deactivated, Region switch uses the other active Region
as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. You can configure ungraceful
execution by specifying the minimum percentage of compute capacity to be matched in the target Region
before Region switch proceeds to the next step in the plan.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several critical checks on your EC2 Auto Scaling group execution block configuration
and permissions. Region switch evaluation verifies that Auto Scaling groups are present in both Regions, ensures that they are properly configured
and accessible, and notes the number of running instances in each Region. It also
confirms that the maximum capacity in the target Region's Auto Scaling group is sufficient to handle the specified
percentage match of scale for the required capacity.

Region switch also validates that the plan's IAM role has
the correct permissions for Auto Scaling. For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

If any of the checks fail, Region switch returns warning messages, which you can view in the console. Or, you can receive
the validation warnings through EventBridge or by using API operations.
