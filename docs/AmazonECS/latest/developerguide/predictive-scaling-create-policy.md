# Create a predictive scaling policy for Amazon ECS service

auto scaling

Create a predictive scaling policy to have Amazon ECS increase or decrease the number of tasks that your service runs based on historical data.

###### Note

A new service needs to provide at least 24 hours of data before a forecast can be generated.

1.  In addition to the standard IAM permissions for creating and updating services, you
    need additional permissions. For more information, see [IAM permissions required for Amazon ECS service auto
    scaling](auto-scaling-IAM.md "auto-scaling-IAM.md").
2.  Determine the metrics to use for the policy. The following metrics are available:

        * **ECSServiceAverageCPUUtilization** – The average CPU
         utilization the service should use.
        * **ECSServiceAverageMemoryUtilization** – Average memory
         utilization the service should use.
        * **ALBRequestCountPerTarget** – The average number of
         requests per minute that task should ideally receive.

    You can alternatively use a custom metric. You need to define the following
    values:

        * Load - a metric that accurately represents the full load on your application and
         is the aspect of your application that's most important to scale on.


        * Scaling metric - the best predictor for how much utilization is ideal for your
         application.

3.  Open the console at
    [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
4.  On the **Clusters** page, choose the cluster.
5.  On the cluster details page, in the **Services** section,
    choose the service.

The service details page appears. 6. Choose **Service auto scaling** and then choose **Set the number of tasks**. 7. Under **Amazon ECS service task count**, choose **Use auto
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

The **Create policy** page appears. 9. For **Scaling policy type**, choose **Predictive
Scaling**. 10. For **Policy name**, enter the name of the policy. 11. For **Metric pair**, choose your metrics from the list of options.

If you chose **Application Load Balancer request count per target**, then choose a target
group in **Target group**. **Application Load Balancer request count per
target** is only supported if you have attached an Application Load Balancer target group for your
service.

If you chose **Custom metric pair**, choose individual metrics from the
lists for **Load metric** and **Scaling metric**. 12. For **Target utilization**, enter the target value for the percentage of
tasks that Amazon ECS should maintain. Service auto scaling scales out your capacity until the
average utilization is at the target utilization, or until it reaches the maximum number of
tasks you specified. 13. Choose **Create scaling policy**.
Use the AWS CLI as follows to configure predictive scaling policies for your Amazon ECS service. Replace
each `user input placeholder` with your own information.

For more information about the CloudWatch metrics you can specify, see [PredictiveScalingMetricSpecification](../../../autoscaling/ec2/APIReference/API_PredictiveScalingMetricSpecification.md "../../../autoscaling/ec2/APIReference/API_PredictiveScalingMetricSpecification.md") in the
_Amazon EC2 Auto Scaling API Reference_.

### Example 1: A predictive scaling policy

with predefined memory.

The following is an example policy with a predefined memory configuration.

```
cat policy.json
{
    "MetricSpecifications": [
        {
            "TargetValue": `40`,
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "`ECSServiceMemoryUtilization`"
            }
        }
    ],
    "SchedulingBufferTime": `3600`,
    "MaxCapacityBreachBehavior": "HonorMaxCapacity",
    "Mode": "ForecastOnly"
}
```

The following example illustrates creating the policy by running the [put-scaling-policy](../../../cli/latest/reference/autoscaling/put-scaling-policy.md "../../../cli/latest/reference/autoscaling/put-scaling-policy.md") command with the configuration file specified.

```
aws application-autoscaling put-scaling-policy \
--service-namespace `ecs` \
--region `us-east-1` \
--policy-name `predictive-scaling-policy-example` \
--resource-id `service/MyCluster/test` \
--policy-type PredictiveScaling \
--scalable-dimension ecs:service:DesiredCount \
--predictive-scaling-policy-configuration file://policy.json

```

If successful, this command returns the policy's ARN.

```
{
    "PolicyARN": "arn:aws:autoscaling:us-east-1:012345678912:scalingPolicy:d1d72dfe-5fd3-464f-83cf-824f16cb88b7:resource/ecs/service/MyCluster/test:policyName/predictive-scaling-policy-example",
    "Alarms": []
}
```

### Example 2: A predictive scaling policy

with predefined CPU.

The following is an example policy with a predefined CPU configuration.

```
cat policy.json
{
    "MetricSpecifications": [
        {
            "TargetValue": `0.00000004`,
            "PredefinedMetricPairSpecification": {
                "PredefinedMetricType": "`ECSServiceCPUUtilization`"
            }
        }
    ],
    "SchedulingBufferTime": `3600`,
    "MaxCapacityBreachBehavior": "HonorMaxCapacity",
    "Mode": "ForecastOnly"
}
```

The following example illustrates creating the policy by running the [put-scaling-policy](../../../cli/latest/reference/autoscaling/put-scaling-policy.md "../../../cli/latest/reference/autoscaling/put-scaling-policy.md") command with the configuration file specified.

```
aws aas put-scaling-policy \
--service-namespace `ecs` \
--region `us-east-1` \
--policy-name `predictive-scaling-policy-example` \
--resource-id `service/MyCluster/test` \
--policy-type PredictiveScaling \
--scalable-dimension ecs:service:DesiredCount \
--predictive-scaling-policy-configuration file://policy.json

```

If successful, this command returns the policy's ARN.

```
{
    "PolicyARN": "arn:aws:autoscaling:us-east-1:012345678912:scalingPolicy:d1d72dfe-5fd3-464f-83cf-824f16cb88b7:resource/ecs/service/MyCluster/test:policyName/predictive-scaling-policy-example",
    "Alarms": []
}
```
