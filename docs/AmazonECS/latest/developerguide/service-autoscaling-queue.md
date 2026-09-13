

# Scale Amazon ECS services based on an Amazon SQS queue
<a name="service-autoscaling-queue"></a>

You can scale your Amazon ECS service in response to the load in an Amazon Simple Queue Service (Amazon SQS) queue. This is useful for asynchronous applications in which the tasks in your service act as workers that consume and process messages from a queue. As the rate of incoming messages changes, Amazon ECS Service Auto Scaling adds tasks when the queue builds up and removes tasks when it drains. This keeps latency for messages waiting in the queue at an acceptable level without over-provisioning.

## Use the backlog per task metric
<a name="service-autoscaling-queue-metric"></a>

Amazon SQS publishes the depth of a queue to CloudWatch as the `ApproximateNumberOfMessagesVisible` metric, which reports the number of messages available for retrieval. Queue depth indicates that there is work to be done, but it is not a reliable metric to scale on directly. The number of messages in the queue does not change proportionally to the number of tasks that process it. The number of tasks that you need also depends on other factors, such as how long a task takes to process a message and the acceptable amount of latency (queue delay). A target tracking policy that tracks queue depth interprets a large queue as demand for proportionally more tasks. This can cause your service to scale out far beyond what the workload requires and increase cost.

Instead, scale on the *backlog per task*: the queue depth divided by the number of running tasks. You calculate this value with a CloudWatch metric math expression that divides the queue depth by the running task count. Backlog per task normalizes queue depth by the running task count. This makes it proportional to the load on each task, so it is suitable for scaling.

Set your target value to the *acceptable backlog per task*. To calculate it, divide the latency that your application can accept by the average time that a task takes to process a message.

For example, if the acceptable latency is 10 seconds and a task takes 0.1 seconds to process a message, the acceptable backlog per task is 10 divided by 0.1, which equals 100 messages per task. This is the target value for your policy. If the queue currently holds 1,500 messages and 10 tasks are running, the backlog per task is 150 (1,500 divided by 10), which exceeds the target. Your service scales out by five tasks to bring the backlog per task back in proportion to the target value.

## Use metric math to compute the metric
<a name="service-autoscaling-queue-architecture"></a>

Application Auto Scaling target tracking policies support CloudWatch *metric math*. Metric math lets you query multiple CloudWatch metrics and use math expressions to create a new time series based on those metrics. You use a metric math expression to compute the backlog per task directly in the scaling policy. Application Auto Scaling evaluates the expression and manages the CloudWatch alarms that start scaling activities. For more information, see [Use metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *CloudWatch User Guide*.

To compute the backlog per task, you use the following two CloudWatch metrics:
+ `ApproximateNumberOfMessagesVisible` (the `Sum` statistic) from the `AWS/SQS` namespace, for the number of messages waiting in the queue.
+ `RunningTaskCount` (the `Average` statistic) from the `ECS/ContainerInsights` namespace, for the number of running tasks in your service. To use this metric, you must turn on CloudWatch Container Insights for your cluster. For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](cloudwatch-container-insights.md).

In the following example, `m1` is the queue depth and `m2` is the running task count. The metric math expression `m1 / m2` produces the backlog per task. Application Auto Scaling adjusts the number of tasks in your service to keep this value at your target value.

## Use step scaling for more control
<a name="service-autoscaling-queue-stepscaling"></a>

We recommend target tracking for most queue-based workloads because it is the simplest approach. You set a single target value, and Amazon ECS Service Auto Scaling creates and manages the CloudWatch alarms and the scaling adjustments for you.

Use step scaling when you want full control over the scaling behavior. With step scaling, you create your own CloudWatch alarms and define separate scale-out and scale-in policies, each with its own step adjustments. You put the backlog per task metric math expression in the alarms, and set each alarm's action to the corresponding policy. This gives you control over the following:
+ **The size of each scaling step** – You can define step adjustments that add more tasks as the backlog grows, so that a small breach adds a few tasks and a large breach adds many. You can scale by a percentage of the running task count or by a fixed number of tasks.
+ **How quickly scaling responds** – You control responsiveness through the metric publishing frequency and the alarm evaluation settings. For example, you can publish a high-resolution queue metric every 10 seconds and configure a scale-out alarm to breach on a single data point, so that the service reacts to a growing backlog faster than the default one-minute resolution allows.
+ **Different scale-out and scale-in behavior** – Because scale-out and scale-in are separate policies and alarms, you can react quickly to a rising backlog while scaling in conservatively. For example, you can require the backlog to stay low for several minutes before removing tasks.

For more information, see [Use predefined increments based on CloudWatch alarms to scale Amazon ECS services](service-autoscaling-stepscaling.md).

## Protect tasks that are processing messages
<a name="service-autoscaling-queue-protection"></a>

When your service scales in, Amazon ECS Service Auto Scaling can stop a task that is still processing a message. For long-running or non-idempotent work, this can cause the message to be reprocessed or its progress to be lost. To prevent this, use task scale-in protection to mark a task as protected while it is doing active work.

For queue workers, we recommend that the task protect itself through the Amazon ECS container agent endpoint. When the task starts processing a message, it sets the `ProtectionEnabled` attribute to `true` so that Amazon ECS does not stop it during a scale-in event. After the task finishes the message, it sets `ProtectionEnabled` to `false` so that the task is again eligible for termination. For more information, see [Protect your Amazon ECS tasks from being terminated by scale-in events](task-scale-in-protection.md).

## Considerations
<a name="service-autoscaling-queue-considerations"></a>

Consider the following when you configure queue-based scaling for your Amazon ECS service:
+ Because Application Auto Scaling evaluates the metric math expression for you, you do not need to publish a custom metric or run any additional code to compute backlog per task.
+ The `RunningTaskCount` metric is available only when CloudWatch Container Insights is turned on for your cluster. If it is not, the metric math expression has no data for the divisor and scaling does not occur.
+ Choose a target value based on the latency that your application's service level agreement (SLA) allows. A lower target value keeps queue delay shorter but runs more tasks. A higher target value reduces cost but increases the time that messages wait in the queue.
+ Messages that have not finished processing when a task is stopped return to the Amazon SQS queue. Another running task can process them if you configure the visibility timeout appropriately. To keep a task from being stopped while it is processing a message, use task scale-in protection, as described in [Protect tasks that are processing messages](#service-autoscaling-queue-protection).
+ The general considerations for Amazon ECS Service Auto Scaling and target tracking also apply to queue-based scaling.

## Configure queue-based scaling
<a name="service-autoscaling-queue-configure"></a>

The following steps show how to create a target tracking scaling policy that uses a metric math expression to scale your Amazon ECS service on backlog per task. You use the AWS CLI for these tasks.

1. Confirm that you have the IAM permissions required to create and update services and to register scalable targets and scaling policies. For more information, see [IAM permissions required for Amazon ECS service auto scaling](auto-scaling-IAM.md).

1. Turn on CloudWatch Container Insights for your cluster so that the `RunningTaskCount` metric is available. For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](cloudwatch-container-insights.md).

1. Register your Amazon ECS service as a scalable target by using the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command. The scalable dimension is `ecs:service:DesiredCount`.

   ```
   aws application-autoscaling register-scalable-target \
       --service-namespace ecs \
       --scalable-dimension ecs:service:DesiredCount \
       --resource-id service/my-cluster/my-service \
       --min-capacity 1 \
       --max-capacity 10
   ```

1. Store the metric math expression in a customized metric specification in a JSON file named `config.json`. Replace the queue name, cluster name, and service name with your own values, and set `TargetValue` to the acceptable backlog per task that you calculated.

   ```
   {
       "CustomizedMetricSpecification": {
           "Metrics": [
               {
                   "Label": "Get the queue depth",
                   "Id": "m1",
                   "MetricStat": {
                       "Metric": {
                           "MetricName": "ApproximateNumberOfMessagesVisible",
                           "Namespace": "AWS/SQS",
                           "Dimensions": [
                               { "Name": "QueueName", "Value": "my-queue" }
                           ]
                       },
                       "Stat": "Sum"
                   },
                   "ReturnData": false
               },
               {
                   "Label": "Get the running task count",
                   "Id": "m2",
                   "MetricStat": {
                       "Metric": {
                           "MetricName": "RunningTaskCount",
                           "Namespace": "ECS/ContainerInsights",
                           "Dimensions": [
                               { "Name": "ClusterName", "Value": "my-cluster" },
                               { "Name": "ServiceName", "Value": "my-service" }
                           ]
                       },
                       "Stat": "Average"
                   },
                   "ReturnData": false
               },
               {
                   "Label": "Calculate the backlog per task",
                   "Id": "e1",
                   "Expression": "m1 / m2",
                   "ReturnData": true
               }
           ]
       },
       "TargetValue": 100
   }
   ```

1. Create the target tracking scaling policy by using the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command with the JSON file as input. Application Auto Scaling creates and manages the two CloudWatch alarms (one for scale-out and one for scale-in) that invoke the policy.

   ```
   aws application-autoscaling put-scaling-policy \
       --policy-name sqs-backlog-target-tracking-policy \
       --service-namespace ecs \
       --resource-id service/my-cluster/my-service \
       --scalable-dimension ecs:service:DesiredCount \
       --policy-type TargetTrackingScaling \
       --target-tracking-scaling-policy-configuration file://config.json
   ```

For more information about target tracking scaling policies, see [Target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*.