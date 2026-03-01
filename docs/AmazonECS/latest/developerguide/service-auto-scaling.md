# Automatically scale your Amazon ECS service

_Automatic scaling_ is the ability to increase or
decrease the desired number of tasks in your Amazon ECS service automatically. Amazon ECS leverages
the Application Auto Scaling service to provide this functionality. For more information, see the [Application Auto Scaling User
Guide](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md").

Amazon ECS publishes CloudWatch metrics with your service’s average CPU and memory usage. For
more information, see [Amazon ECS service utilization metrics](service_utilization.md "service_utilization.md"). You can use these and other CloudWatch metrics to
scale out your service (add more tasks) to deal with high demand at peak times, and to
scale in your service (run fewer tasks) to reduce costs during periods of low
utilization.

Amazon ECS Service Auto Scaling supports the following types of automatic scaling:

- [Use a target metric to scale Amazon ECS services](service-autoscaling-targettracking.md "service-autoscaling-targettracking.md")— Increase or
  decrease the number of tasks that your service runs based on a target value for
  a specific metric. This is similar to the way that your thermostat maintains the
  temperature of your home. You select temperature and the thermostat does the
  rest.
- [Use predefined increments based on CloudWatch alarms to scale Amazon ECS services](service-autoscaling-stepscaling.md "service-autoscaling-stepscaling.md")— Increase or
  decrease the number of tasks that your service runs based on a set of scaling
  adjustments, known as step adjustments, that vary based on the size of the alarm
  breach.
- [Use scheduled actions to scale Amazon ECS services](service-autoscaling-schedulescaling.md "service-autoscaling-schedulescaling.md")—Increase or decrease
  the number of tasks that your service runs based on the date and time.
- [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md "predictive-auto-scaling.md")—Increase or decrease
  the number of tasks that your service runs based on historical load data analytics to detect daily or
  weekly patterns in traffic flows.

## Considerations

When using scaling policies, consider the following:

- Amazon ECS sends metrics in 1-minute intervals to CloudWatch. Metrics are not
  available until the clusters and services send the metrics to CloudWatch, and you
  cannot create CloudWatch alarms for metrics that do not exist.
- The scaling policies support a cooldown period. This is the number of
  seconds to wait for a previous scaling activity to take effect.
  - For scale-out events, the intention is to continuously (but not
    excessively) scale out. After Service Auto Scaling successfully scales out
    using a scaling policy, it starts to calculate the cooldown time.
    The scaling policy won't increase the desired capacity again unless
    either a larger scale out is initiated or the cooldown period ends.
    While the scale-out cooldown period is in effect, the capacity added
    by the initiating scale-out activity is calculated as part of the
    desired capacity for the next scale-out activity.
  - For scale-in events, the intention is to scale in conservatively
    to protect your application's availability, so scale-in activities
    are blocked until the cooldown period has expired. However, if
    another alarm initiates a scale-out activity during the scale-in
    cooldown period, Service Auto Scaling scales out the target immediately. In
    this case, the scale-in cooldown period stops and doesn't complete.

- The service scheduler respects the desired count at all times, but as long
  as you have active scaling policies and alarms on a service, Service Auto Scaling
  could change a desired count that was manually set by you.
- If a service's desired count is set below its minimum capacity value, and
  an alarm initiates a scale-out activity, Service Auto Scaling scales the desired count
  up to the minimum capacity value and then continues to scale out as required,
  based on the scaling policy associated with the alarm. However, a scale-in
  activity does not adjust the desired count, because it is already below the
  minimum capacity value.
- If a service's desired count is set above its maximum capacity value, and
  an alarm initiates a scale in activity, Service Auto Scaling scales the desired count
  out to the maximum capacity value and then continues to scale in as required,
  based on the scaling policy associated with the alarm. However, a scale-out
  activity does not adjust the desired count, because it is already above the
  maximum capacity value.
- During scaling activities, the actual running task count in a service is
  the value that Service Auto Scaling uses as its starting point, as opposed to the
  desired count. This is what processing capacity is supposed to be. This
  prevents excessive (runaway) scaling that might not be satisfied, for
  example, if there aren't enough container instance resources to place the
  additional tasks. If the container instance capacity is available later, the
  pending scaling activity may succeed, and then further scaling activities
  can continue after the cooldown period.
- If you want your task count to scale to zero when there's no work to be
  done, set a minimum capacity of 0. With target tracking scaling policies,
  when actual capacity is 0 and the metric indicates that there is workload
  demand, Service Auto Scaling waits for one data point to be sent before scaling out.
  In this case, it scales out by the minimum possible amount as a starting
  point and then resumes scaling based on the actual running task
  count.
- Application Auto Scaling turns off scale-in processes while Amazon ECS deployments are in
  progress. However, scale-out processes continue to occur, unless suspended,
  during a deployment. This behavior does not apply to Amazon ECS services using
  the external deployment controller. For more information, see [Service auto scaling and deployments](#service-auto-scaling-deployments "#service-auto-scaling-deployments").
- You have several Application Auto Scaling options for Amazon ECS tasks. Target tracking is the
  easiest mode to use. With it, all you need to do is set a target value for a
  metric, such as CPU average utilization. Then, the auto scaler automatically
  manages the number of tasks that are needed to attain that value. With step
  scaling you can more quickly react to changes in demand, because you define
  the specific thresholds for your scaling metrics, and how many tasks to add
  or remove when the thresholds are crossed. And, more importantly, you can
  react very quickly to changes in demand by minimizing the amount of time a
  threshold alarm is in breach.

For more information about best practices for service auto scaling, see [Optimizing Amazon ECS service auto scaling](capacity-autoscaling-best-practice.md "capacity-autoscaling-best-practice.md").

## Service auto scaling and deployments

Application Auto Scaling turns off scale-in processes while Amazon ECS deployments are in progress.
However, scale-out processes continue to occur, unless suspended, during a
deployment. This behavior does not apply to Amazon ECS services using the external
deployment controller. If you want to suspend scale-out processes while deployments are in
progress, take the following steps.

1. Call the [describe-scalable-targets](../../../cli/latest/reference/application-autoscaling/describe-scalable-targets.md "../../../cli/latest/reference/application-autoscaling/describe-scalable-targets.md") command, specifying the resource ID
   of the service associated with the scalable target in Application Auto
   Scaling (Example: `service/default/sample-webapp`). Record the
   output. You will need it when you call the next command.
2. Call the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command, specifying the resource ID,
   namespace, and scalable dimension. Specify `true` for both
   `DynamicScalingInSuspended` and
   `DynamicScalingOutSuspended`.
3. After deployment is complete, you can call the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command to resume scaling.

For more information, see [Suspending and resuming scaling for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md").
