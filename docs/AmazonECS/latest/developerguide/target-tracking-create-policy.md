# Create a target tracking scaling policy for Amazon ECS service auto scaling

Create a target tracking scaling policy to have Amazon ECS increase or decrease the desired
task count in your service automatically. Target tracking works off of a target metric
value.

1. In addition to the standard IAM permissions for creating and updating
   services, you need additional permissions. For more information, see [IAM permissions required for Amazon ECS service auto scaling](auto-scaling-IAM.md "auto-scaling-IAM.md").
2. Determine the metrics to use for the policy. The following metrics
   are available:
   - **ECSServiceAverageCPUUtilization** – The average CPU
     utilization the service should use.
   - **ECSServiceAverageMemoryUtilization** – Average
     memory utilization the service should use.
   - **ALBRequestCountPerTarget** – The average number of
     requests per minute that task should ideally receive.

3. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
4. On the **Clusters** page, choose the cluster.
5. On the cluster details page, in the **Services** section, and then
   choose the service.

The service details page appears. 6. Choose **Set the number of tasks**. 7. Under **Amazon ECS service task count**, choose **Use auto
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

8. Choose **Create scaling policy**.

The **Create policy** page appears. 9. For **Scaling policy type**, choose **Target
tracking**. 10. For **Policy name**, enter
the name of the policy. 11. For **Metric type**, choose your metrics from the list of options. 12. For **Target utilization**, enter the target value for the
percentage of tasks that Amazon ECS should maintain. Service auto scaling scales out
your capacity until the average utilization is at the target utilization, or
until it reaches the maximum number of tasks you specified. 13. Under **Additional Settings**, do the following

    1. For **Scale-in cooldown period**, enter the amount of time in seconds after a scale-in activity completes before another scale-in activity can start.
    2. For **Scale-out cooldown period**, enter the amount of time in seconds to wait for a previous scale-out activity to take effect.
    3. To create only a scale-out policy, select **Disable scale-in**.

14. Choose **Create scaling policy**.
1. Register your Amazon ECS service as a scalable target using the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command.
1. Create a scaling policy using the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command.
