# Scale an endpoint to zero

instances

When you set up auto scaling for an endpoint, you can allow the scale-in process to
reduce the number of in-service instances to zero. By doing so, you save costs during
periods when your endpoint isn't serving inference requests and therefore doesn't
require any active instances.

However, after scaling in to zero instances, your endpoint can't respond to any
incoming inference requests until it provisions at least one instance. To automate the
provisioning process, you create a step scaling policy with Application Auto Scaling. Then, you assign
the policy to an Amazon CloudWatch alarm.

After you set up the step scaling policy and the alarm, your endpoint will
automatically provision an instance soon after it receives an inference request that it
can't respond to. Be aware that the provisioning process takes several minutes. During
that time, any attempts to invoke the endpoint will produce an error.

The following procedures explain how to set up auto scaling for an endpoint so that it
scales in to, and out from, zero instances. The procedures use commands with the
AWS CLI.

###### Before you begin

Before your endpoint can scale in to, and out from, zero instances, it must meet
the following requirements:

- It is in service.
- It hosts one or more inference components. An endpoint can scale to and from
  zero instances only if it hosts inference components.

For information about hosting inference components on SageMaker AI endpoints, see
[Deploy
models for real-time inference](realtime-endpoints-deploy-models.md "realtime-endpoints-deploy-models.md").

- In the endpoint configuration, for the production variant
  `ManagedInstanceScaling` object, you've set the
  `MinInstanceCount` parameter to `0`.

For reference information about this parameter, see [ProductionVariantManagedInstanceScaling](../APIReference/API_ProductionVariantManagedInstanceScaling.md "../APIReference/API_ProductionVariantManagedInstanceScaling.md").

###### To enable an endpoint to scale in to zero instances (AWS CLI)

For each inference component that the endpoint hosts, do the following:

1. Register the inference component as a scalable target. When you register it,
   set the minimum capacity to `0`, as shown by the following
   command:

```
aws application-autoscaling register-scalable-target \
  --service-namespace sagemaker \
  --resource-id inference-component/`inference-component-name` \
  --scalable-dimension sagemaker:inference-component:DesiredCopyCount \
  --min-capacity 0 \
  --max-capacity `n`
```

In this example, replace `inference-component-name`
with the name of your inference component. Replace `n`
with the maximum number of inference component copies to provision when scaling
out.

For more information about this command and each of its parameters, see [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") in the _AWS CLI Command Reference_. 2. Apply a target tracking policy to the inference component, as shown by the
following command:

```
aws application-autoscaling put-scaling-policy \
  --policy-name my-scaling-policy \
  --policy-type TargetTrackingScaling \
  --resource-id inference-component/`inference-component-name` \
  --service-namespace sagemaker \
  --scalable-dimension sagemaker:inference-component:DesiredCopyCount \
  --target-tracking-scaling-policy-configuration file://config.json
```

In this example, replace `inference-component-name`
with the name of your inference component.

In the example, the `config.json` file contains a target tracking
policy configuration, such as the following:

```
{
  "PredefinedMetricSpecification": {
      "PredefinedMetricType": "SageMakerInferenceComponentInvocationsPerCopy"
  },
  "TargetValue": 1,
  "ScaleInCooldown": 300,
  "ScaleOutCooldown": 300
}
```

For more example tracking policy configurations, see [Define a scaling policy](endpoint-auto-scaling-add-code-define.md "endpoint-auto-scaling-add-code-define.md").

For more information about this command and each of its parameters, see [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") in the _AWS CLI Command Reference_.

###### To enable an endpoint to scale out from zero instances (AWS CLI)

For each inference component that the endpoint hosts, do the following:

1. Apply a step scaling policy to the inference component, as shown by the
   following command:

```
aws application-autoscaling put-scaling-policy \
  --policy-name `my-scaling-policy` \
  --policy-type StepScaling \
  --resource-id inference-component/`inference-component-name` \
  --service-namespace sagemaker \
  --scalable-dimension sagemaker:inference-component:DesiredCopyCount \
  --step-scaling-policy-configuration file://config.json
```

In this example, replace `my-scaling-policy` with a
unique name for your policy. Replace
`inference-component-name` with the name of your
inference component.

In the example, the `config.json` file contains a step scaling
policy configuration, such as the following:

```
{
    "AdjustmentType": "ChangeInCapacity",
    "MetricAggregationType": "Maximum",
    "Cooldown": 60,
    "StepAdjustments":
      [
         {
           "MetricIntervalLowerBound": 0,
           "ScalingAdjustment": 1
         }
      ]
}
```

When this step scaling policy is triggered, SageMaker AI provisions the necessary
instances to support the inference component copies.

After you create the step scaling policy, take note of its Amazon Resource
Name (ARN). You need the ARN for the CloudWatch alarm in the next step.

For more information about step scaling polices, see [Step scaling policies](../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md "../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md") in the _Application Auto Scaling User Guide_. 2. Create a CloudWatch alarm and assign the step scaling policy to it, as shown by the
following example:

```
aws cloudwatch put-metric-alarm \
--alarm-actions `step-scaling-policy-arn` \
--alarm-description "Alarm when SM IC endpoint invoked that has 0 instances." \
--alarm-name `ic-step-scaling-alarm` \
--comparison-operator GreaterThanThreshold  \
--datapoints-to-alarm 1 \
--dimensions "Name=InferenceComponentName,Value=`inference-component-name`" \
--evaluation-periods 1 \
--metric-name NoCapacityInvocationFailures \
--namespace AWS/SageMaker \
--period 60 \
--statistic Sum \
--threshold 1
```

In this example, replace `step-scaling-policy-arn`
with the ARN of your step scaling policy. Replace
`ic-step-scaling-alarm` with a name of your choice.
Replace `inference-component-name` with the name of
your inference component.

This example sets the `--metric-name` parameter to
`NoCapacityInvocationFailures`. SageMaker AI emits this metric when an
endpoint receives an inference request, but the endpoint has no active instances
to serve the request. When that event occurs, the alarm initiates the step
scaling policy in the previous step.

For more information about this command and each of its parameters, see [put-metric-alarm](../../../cli/latest/reference/cloudwatch/put-metric-alarm.md "../../../cli/latest/reference/cloudwatch/put-metric-alarm.md") in the _AWS CLI Command Reference_.
