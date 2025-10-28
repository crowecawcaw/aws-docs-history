# Create a step scaling policy

for Amazon ECS service auto scaling

Create a step scaling policy to have Amazon ECS increase or decrease the desired
number of tasks in your service automatically. Step scaling runs based on a set of scaling
adjustments, known as step adjustments, that vary based on the size of the alarm breach.

1. In addition to the standard IAM permissions for creating and updating
   services, you need additional permissions. For more information, see [IAM permissions required for Amazon ECS service auto
   scaling](auto-scaling-IAM.md "auto-scaling-IAM.md").
2. Determine the metrics to use for the policy. The following metrics
   are available:
   - **ECSServiceAverageCPUUtilization** – The average CPU
     utilization the service should use.
   - **ECSServiceAverageMemoryUtilization** – Average
     memory utilization the service should use.
   - **ALBRequestCountPerTarget** – The average number of
     requests per minute that task should ideally receive.

3. Create the CloudWatch alarms for the metrics. For more information, see [Create a
   CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the _Amazon CloudWatch User Guide_.
4. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
5. On the **Clusters** page, choose the cluster.
6. On the cluster details page, in the **Services** section, and then
   choose the service.

The service details page appears. 7. Choose **Set the number of tasks**. 8. Under **Amazon ECS service task count**, choose **Use auto
scaling**.

The **Task count section** appears.

    1. For **Minimum number of tasks**, enter the lower limit of the
     number of tasks for service auto scaling to use. The desired count will not go
     below this count.
    2. For **Maximum**, enter the upper limit of the
     number of tasks for service auto scaling to use. The desired count will not go
     above this count.
    3. Choose **Save**.


    The policies page appears.

9. Choose **Create scaling policy**.

The **Create policy** page appears. 10. For **Scaling policy type**, choose **Step
Scaling**. 11. Configure the scaling-out properties. Under **Steps to add
tasks** do the following:

    1. For **Policy name**, enter
     the name of the policy.
    2. For **CloudWatch alarm name**, choose the CloudWatch alarm.
    3. For **Metric aggregation type**, choose how to compare the selected metric to
     the defined threshold.
    4. For A**djustment types**, choose whether the adjustment is based on a change
     in the number of tasks, or a change in the percentage of tasks.
    5. For **Actions to take**, enter the values for what action to take.


    Choose **Add step** to add additional actions.

12. Configure the scaling-in properties. Under **Steps to remove
    tasks**, do the following:
    1.  For **Policy name**, enter the name of the
        policy.
    2.  For **CloudWatch alarm name**, choose the CloudWatch
        alarm.
    3.  For **Metric aggregation type**, choose how to
        compare the selected metric to the defined threshold.
    4.  For **Adjustment types**, choose whether the
        adjustment is based on a change in the number of tasks, or a change in
        the percentage of tasks.
    5.  For **Actions to take**, enter the values for what
        action to take.

    Choose **Add step** to add additional actions.

13. For **Cooldown period**, enter the amount of time, in
    seconds, to wait for a previous scaling activity to take effect. For an add
    policy, this is the time after a scale-out activity that the scaling policy
    blocks scale-in activities and limits how many tasks can be scale out at a time.
    For a remove policy, this is the time after a scale-in activity that must pass
    before another scale-in activity can start.
14. Choose **Create scaling policy**.
15. Register your Amazon ECS service as a scalable target using the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command.
16. Create a scaling policy using the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command.
