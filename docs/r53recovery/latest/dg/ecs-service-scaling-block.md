

# Amazon ECS service scaling execution block
<a name="ecs-service-scaling-block"></a>

The ECS service scaling execution block allows you to scale your ECS service in a destination Region as part of your multi-Region recovery process. You can define a percentage of capacity, relative to the Region that Region switch fails over from or deactivates.

## Configuration
<a name="ecs-service-scaling-block-config"></a>

To configure the ECS service scaling execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon ECS service scaling execution block sample policy](security_iam_region_switch_ecs.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Resource for *Region*: **For each Region, enter the ECS cluster ARN and the ECS service ARN.

1. **Percentage to match the source Region's task count: ** Enter the desired percentage of running tasks in the source Region to match in the activated Region.

1. **Capacity monitoring approach: **Select one of the following approaches for monitoring capacity for Amazon ECS:
   + **Max running capacity sampled over 24 hours**: Choose this option to use the **running tasks count** value in your Amazon ECS service. This option does not create additional costs, but is potentially less accurate than using the other option, CloudWatch metrics.

     In the Region switch API, this option corresponds to specifying `sampledMaxInLast24Hours`.

     For more information, see [Automatically scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) in the Amazon Elastic Container Service Developer Guide.
   + **Max running capacity sampled over 24 hours via container insights**: Choose this option to use Amazon ECS Container Insights metrics. Using the option can be more accurate, but incurs the additional costs of using Container Insights.

     In the Region switch API, this option corresponds to specifying `autoscalingMaxInLast24Hours`.

     To use this option, you must first enable Container Insights. For more information, see [ Set up Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html#set-container-insights-ECS-cluster) in the Amazon CloudWatch User Guide.

1. **Wait for target group health: ** Choose whether Region switch waits for the ECS service's tasks to become healthy in their associated Elastic Load Balancing target groups before completing the step.
   + When enabled, Region switch checks target group health after it scales capacity. Region switch does not proceed to the next step until every associated target group reports the required number of tasks as `healthy`. The required number of tasks is the desired count Region switch calculates for the step, the same count it waits for when scaling.
   + When disabled, the step completes as soon as the target service reaches its desired running task count, without checking target group health.

   In the Region switch API, this option corresponds to specifying `waitELBTargetGroupHealthy` as either `enabled` or `disabled`.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="ecs-service-scaling-block-how"></a>

When the block runs, Region switch reads the source Region's maximum running task count over the last 24 hours, measured by the capacity monitoring approach you selected. It calculates the target with the formula `ceil(percentToMatch * source task count)`, where ceil() rounds up any fractional result, using the service's desired count as the capacity. It then scales up the destination service to match this count. Region switch scales up the destination service only when its current desired count is less than the calculated target. If the current desired count is already greater than or equal to the target, the execution proceeds without scaling (Region switch never scales down). If the service has Application Auto Scaling enabled, Region switch updates the minimum capacity in Application Auto Scaling as well as the desired count. This calculation applies to both active/passive and active/active plans.

The source capacity is always that of the other Region. In an active/active plan, Region switch uses the other configured Region as the source in both the activate and deactivate workflows.

Region switch waits until the destination service's desired count is fulfilled before proceeding to the next step. When you enable **Wait for target group health**, Region switch checks target group health after the destination service reaches its desired count. It reads the Elastic Load Balancing target groups attached to the service and polls their health until every attached target group reports the desired count of tasks as `healthy`. This check runs whether or not scaling occurred, so even if the service already had the desired count, Region switch verifies target group health before completing the step. For ungraceful execution, it instead waits for the minimum percentage of the task count to be `healthy`.

A task counts toward the healthy total only when it belongs to this service and its matching target group entry is `healthy`. How Region switch identifies the service's tasks depends on the network mode:
+ In `awsvpc` mode, Amazon ECS registers each task by its task ENI IP address. Region switch matches each task by its IPv4 or IPv6 address, according to the target group's address type.
+ In `bridge` or `host` mode, Amazon ECS registers each task by its container instance and the host port mapped for the container. Region switch matches the container instance's EC2 instance ID together with that host port.

The step completes only after all required tasks are healthy across every associated target group. If the service has no load balancers, Region switch skips the check and completes the step. If the required tasks don't become healthy before the timeout, the step fails.

**Note**  
The **Wait for target group health** option supports only Application Load Balancer (ALB) and Network Load Balancer (NLB) target groups. It doesn't support Classic Load Balancer. If your ECS service uses only a Classic Load Balancer, enabling this option has no effect.

The block supports both graceful and ungraceful execution. For ungraceful execution, you specify the minimum percentage of the source Region's task count to match in the destination Region before Region switch proceeds. The percentage you specify in the execution block, or as the minimum percentage for ungraceful execution, applies to both scaling and waiting for target group health.