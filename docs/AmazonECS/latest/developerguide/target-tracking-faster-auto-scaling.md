

# Faster auto scaling with high-resolution metrics
<a name="target-tracking-faster-auto-scaling"></a>

By default, Amazon ECS publishes `CPUUtilization` and `MemoryUtilization` metrics at 60-second resolution. You can configure 20-second resolution to drive faster service auto scaling.

The following high-resolution predefined metrics are available for target tracking scaling policies:


| PredefinedMetricType | Description | 
| --- | --- | 
| ECSServiceAverageCPUUtilizationHighResolution | Average CPU utilization at 20-second resolution | 
| ECSServiceAverageMemoryUtilizationHighResolution | Average memory utilization at 20-second resolution | 

## Create a new service with high-resolution metrics for faster auto scaling
<a name="faster-auto-scaling-create-service"></a>

### Console
<a name="faster-auto-scaling-create-service-console"></a>

1. On the **Clusters** page, choose the cluster you want to create the service in.

1. In the **Services** section, choose **Create**.

1. In the Create Service form, in the **Monitoring configuration** section, choose **Add metric configuration**.

1. For **Metric name**, select the metric you want to collect at high resolution. Choose `CPUUtilization` or `MemoryUtilization`.

1. For **Resolution (seconds)**, select **20**.

1. (Optional) To add both metrics at high resolution, choose **Add metric configuration** again and repeat the previous two steps for the other metric.

1. In the **Service auto scaling** section, choose **Use service auto scaling**.

1. For **Minimum number of tasks**, enter the lower limit of the number of tasks for service auto scaling to use. The desired count will not go below this count.

1. For **Maximum number of tasks**, enter the upper limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.

1. For **Scaling policy type**, choose **Target tracking**.

1. For **Metric type**, select the corresponding high-resolution metric. For example, choose `ECSServiceAverageCPUUtilizationHighResolution` if you configured `CPUUtilization` at 20-second resolution, or `ECSServiceAverageMemoryUtilizationHighResolution` if you configured `MemoryUtilization` at 20-second resolution.

1. For **Target value**, enter the target utilization percentage. Service auto scaling scales out your capacity until the average utilization is at the target value, or until it reaches the maximum number of tasks you specified.

1. Under **Additional Settings**, configure the following:

   1. For **Scale-out cooldown period**, enter the amount of time in seconds to wait for a previous scale-out activity to take effect.

   1. For **Scale-in cooldown period**, enter the amount of time in seconds after a scale-in activity completes before another scale-in activity can start.

1. Choose **Create** to create the service.

### AWS CLI
<a name="faster-auto-scaling-create-service-cli"></a>

1. Create the service with monitoring configuration using the [create-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html) command.

   ```
   aws ecs create-service --region {{us-east-1}} \
       --cluster {{my-cluster}} \
       --service-name {{my-service}} \
       --task-definition {{my-app:1}} \
       --desired-count 2 \
       --monitoring "metricConfigurations=[{metricNames=[CPUUtilization,MemoryUtilization],resolutionSeconds=20}]"
   ```

1. Register the service as a scalable target using the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command.

   ```
   aws application-autoscaling register-scalable-target \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --min-capacity {{1}} \
       --max-capacity {{10}} \
       --region {{us-east-1}}
   ```

1. Create a target tracking scaling policy with a high-resolution predefined metric using the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command.

   ```
   aws application-autoscaling put-scaling-policy \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --policy-name {{my-highres-cpu-policy}} \
       --policy-type TargetTrackingScaling \
       --target-tracking-scaling-policy-configuration '{
           "TargetValue": {{50.0}},
           "PredefinedMetricSpecification": {
               "PredefinedMetricType": "ECSServiceAverageCPUUtilizationHighResolution"
           }
       }' \
       --region {{us-east-1}}
   ```

1. Verify the policy was created using the [describe-scaling-policies](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-policies.html) command.

   ```
   aws application-autoscaling describe-scaling-policies \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --region {{us-east-1}}
   ```

## Update an existing service to use high-resolution metrics for faster auto scaling
<a name="faster-auto-scaling-update-service"></a>

Updating an existing service to use high-resolution metrics for faster service auto scaling is a two-step process. You must first update the monitoring resolution, which triggers a service deployment. After the deployment completes successfully and all tasks are emitting metrics at 20-second resolution, you can then configure a high-resolution scaling policy.

**Important**  
If your service was previously using 60-second metric resolution, high-resolution metrics for scaling policy will only be available on the Amazon ECS console after you have updated your service to use 20-second metric resolution and the service deployment completes.

### Console
<a name="faster-auto-scaling-update-service-console"></a>

**Step 1: Update monitoring resolution**  


1. On the **Clusters** page, choose the cluster that contains the service you want to update.

1. In the **Services** section, select the service and choose **Update**.

1. In the Update Service form, in the **Monitoring configuration** section, choose **Add metric configuration**.

1. For **Metric name**, select the metric you want to collect at high resolution. Choose `CPUUtilization` or `MemoryUtilization`.

1. For **Resolution (seconds)**, select **20**.

1. (Optional) To add both metrics at high resolution, choose **Add metric configuration** again and repeat the previous two steps for the other metric.

1. Choose **Update** to submit the change. This triggers a service deployment.

1. Wait for the deployment to complete. You can monitor progress on the service details page in the **Deployments** tab.
**Note**  
The high-resolution scaling metric options are greyed out in the service auto scaling section until the deployment succeeds and all tasks are emitting at 20-second resolution.

**Step 2: Configure high-resolution scaling policy**  


After the deployment completes, configure the scaling policy using one of the following methods:

Option A: Service details page  

1. On the service details page, choose the **Service auto scaling** tab.

1. Choose **Create scaling policy** (or edit an existing policy).

1. For **Scaling policy type**, choose **Target tracking**.

1. For **Metric type**, select the high-resolution metric. For example, `ECSServiceAverageCPUUtilizationHighResolution` or `ECSServiceAverageMemoryUtilizationHighResolution`.

1. For **Target value**, enter the target utilization percentage.

1. Under **Additional Settings**, configure the following:

   1. For **Scale-out cooldown period**, enter the amount of time in seconds to wait for a previous scale-out activity to take effect.

   1. For **Scale-in cooldown period**, enter the amount of time in seconds after a scale-in activity completes before another scale-in activity can start.

1. Choose **Create scaling policy**.

Option B: Update Service form  

1. On the service details page, choose **Update**.

1. In the **Service auto scaling** section, choose **Use service auto scaling** (if not already enabled).

1. For **Minimum number of tasks**, enter the lower limit.

1. For **Maximum number of tasks**, enter the upper limit.

1. For **Scaling policy type**, choose **Target tracking**.

1. For **Metric type**, select the high-resolution metric (now enabled after the deployment completed).

1. For **Target value**, enter the target utilization percentage.

1. Under **Additional Settings**, set the **Scale-out cooldown period** and **Scale-in cooldown period**.

1. Choose **Update** to submit the change.

### AWS CLI
<a name="faster-auto-scaling-update-service-cli"></a>

**Step 1: Update monitoring resolution**  


1. Update the service with monitoring configuration using the [update-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-service.html) command.

   ```
   aws ecs update-service --region {{us-east-1}} \
       --cluster {{my-cluster}} \
       --service {{my-service}} \
       --monitoring "metricConfigurations=[{metricNames=[CPUUtilization,MemoryUtilization],resolutionSeconds=20}]"
   ```

1. Wait for the deployment to complete. You can monitor progress using the [describe-services](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-services.html) command and checking the deployment status.

   ```
   aws ecs describe-services --region {{us-east-1}} \
       --cluster {{my-cluster}} \
       --services {{my-service}}
   ```

1. After the deployment completes, verify the monitoring configuration is active by describing the service revision. Get the active service revision ARN from the `describe-services` output, then run:

   ```
   aws ecs describe-service-revisions --region {{us-east-1}} \
       --service-revision-arns {{arn:aws:ecs:us-east-1:012345678910:service-revision/my-cluster/my-service/1234567890123456789}}
   ```

   Confirm the monitoring configuration appears in the response:

   ```
   {
       "serviceRevisions": [
           {
               ...
               "monitoring": {
                   "metricConfigurations": [
                       {
                           "metricNames": ["CPUUtilization", "MemoryUtilization"],
                           "resolutionSeconds": 20
                       }
                   ]
               }
           }
       ]
   }
   ```

**Step 2: Configure high-resolution scaling policy**  


1. Register the service as a scalable target if not already registered, using the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command.

   ```
   aws application-autoscaling register-scalable-target \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --min-capacity {{1}} \
       --max-capacity {{10}} \
       --region {{us-east-1}}
   ```

1. Create a target tracking scaling policy with a high-resolution predefined metric using the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) command. The following example targets 50% CPU utilization:

   ```
   aws application-autoscaling put-scaling-policy \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --policy-name {{my-highres-cpu-policy}} \
       --policy-type TargetTrackingScaling \
       --target-tracking-scaling-policy-configuration '{
           "TargetValue": {{50.0}},
           "PredefinedMetricSpecification": {
               "PredefinedMetricType": "ECSServiceAverageCPUUtilizationHighResolution"
           }
       }' \
       --region {{us-east-1}}
   ```

1. Verify the policy was created:

   ```
   aws application-autoscaling describe-scaling-policies \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --region {{us-east-1}}
   ```

## Validate faster service auto scaling
<a name="faster-auto-scaling-validate"></a>

**Part 1: Verify high-resolution metrics are publishing**  


1. Navigate to the CloudWatch console.

1. In the navigation pane, choose **Metrics**, then choose **All metrics**.

1. Choose the **AWS/ECS** namespace.

1. Choose **ClusterName, ServiceName**.

1. Locate the `CPUUtilization` and `MemoryUtilization` metrics for your service.

1. Set the period to **20 seconds**. You should see data points at 20-second intervals, confirming that high-resolution metrics are active.

**Part 2: Verify scaling policy is using the high-resolution metric**  


1. On the service details page, choose the **Service auto scaling** tab.

1. View your existing scaling policies and confirm the metric is set to a high-resolution variant (`ECSServiceAverageCPUUtilizationHighResolution` or `ECSServiceAverageMemoryUtilizationHighResolution`).

1. Alternatively, verify using the CLI:

   ```
   aws application-autoscaling describe-scaling-policies \
       --service-namespace ecs \
       --resource-id service/{{my-cluster}}/{{my-service}} \
       --scalable-dimension ecs:service:DesiredCount \
       --region {{us-east-1}}
   ```

   Confirm the `PredefinedMetricType` in the response is set to a high-resolution metric.

## Considerations
<a name="faster-auto-scaling-considerations"></a>
+ Monitoring configuration changes create a new service revision and require a service deployment. The high-resolution scaling metric is not available until the deployment completes and all tasks are emitting at 20-second resolution.
+ High-resolution metrics are supported for services using Application Load Balancers and Network Load Balancers. Services using Classic Load Balancers without target groups are not supported.
+ High-resolution metrics are not supported for services using the `CODE_DEPLOY` or `EXTERNAL` deployment controller types.
+ You can view the monitoring configuration for your service using `DescribeServiceRevisions`. The monitoring configuration is not returned in `CreateService` or `UpdateService` responses.