# Amazon ECS service scaling execution block

The ECS service scaling execution block allows you to scale your ECS service in a destination
Region as part of your multi-Region recovery process. You can define a percentage of capacity, relative
to the Region that Region switch fails over from or deactivates.

## Configuration

To configure the ECS service scaling execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Amazon ECS service scaling execution block sample policy](security_iam_region_switch_ecs.md "security_iam_region_switch_ecs.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Resource for _Region_:** For each
   Region, enter the ECS cluster ARN and the ECS service ARN.
4. **Percentage to match the source Region's task count:**
   Enter the desired percentage of running tasks in the source Region to match in the activated Region.
5. **Capacity monitoring approach:** Select one of the following approaches for
   monitoring capacity for Amazon ECS:
   - **Max running capacity sampled over 24 hours**: Choose this option to use
     the **running tasks count** value in your Amazon ECS service. This option does
     not create additional costs, but is potentially less accurate than using the other option, CloudWatch metrics.

   In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

   For more information, see [Automatically scale your Amazon ECS service](../../../AmazonECS/latest/developerguide/service-auto-scaling.md "../../../AmazonECS/latest/developerguide/service-auto-scaling.md")
   in the Amazon Elastic Container Service Developer Guide.
   - **Max running capacity sampled over 24 hours via container insights**: Choose this option to use
     Amazon ECS Container Insights metrics. Using the option can be more accurate, but incurs the additional
     costs of using Container Insights.

   In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

   To use this option, you must first enable Container Insights.
   For more information, see [Set up Container Insights](../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md#set-container-insights-ECS-cluster "../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md#set-container-insights-ECS-cluster") in the Amazon CloudWatch User Guide.

6. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

After you configure the execution block in your plan, Region switch confirms that there is only
one source ECS service and one destination service. If there are multiple services, Region switch returns
a warning for the execution block. Region switch stores this data in all Regions your plan is configured
for. The target capacity is defined as the desired count set on your ECS service.

For an active/passive approach, Region switch calculates the new desired capacity for the ECS service
in the destination (activating) Region.
The new desired capacity is compared against the destination ECS service's desired
capacity. The formula that Region switch uses to calculate desired capacity is the following:
`ceil(percentToMatch * Source Auto Scaling group capacity)`, where ceil() is a
function that rounds up any fractional result. If the current desired count for the destination
ECS service is higher than the calculated new desired capacity for the ECS service, the
plan execution proceeds. Note that Region switch does not scale down ECS service capacity.

If the ECS service has Application Autoscaling enabled, Region switch updates the minimum capacity
in Application Autoscaling, and also updates the desired count in the ECS service.

When Region switch executes an ECS service block, Region switch attempts to scale up the target Region ECS capacity
to match the desired capacity. Then, Region switch waits until the requested ECS service capacity is fulfilled
in the target Region's ECS service before Region switch proceeds to the next step in the plan. If you like,
you can configure the step to complete before fulfillment is complete by setting a timeout limit for
how long Region switch waits for capacity fulfillment.

If you’re using an active/active approach, Region switch uses the other configured Region
as the source. That is, if a Region is being deactivated, Region switch uses the other active Region
as the source to match for the percent to scale.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your ECS service execution block configuration
and permissions. Region switch verifies that ECS services are present in both the source and target Regions, and
checks to make sure that the maximum capacity set for the target Region's ECS service is sufficient to handle the specified
percentage match of the target Region's capacity. Region switch also validates that the plan's IAM role has
the correct permissions for ECS service. For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

In addition, Region switch checks that the `ResourceMonitor` has successfully collected and stored the
necessary monitoring data for the ECS services, and captures a count of the number of running tasks.

If any of the checks fail, Region switch returns warning messages, which you can view in the console. Or, you can receive
the validation warnings through EventBridge or by using API operations.
